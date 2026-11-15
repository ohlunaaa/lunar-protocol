# Game WebSocket — Handshake, RPC Framing, Services

> Connection, handshake, heartbeat, the RPC system, and all services.
>
> **Update:** The handshake data below comes from the original
> descriptors extracted out of `lunar.jar`
> (`handshake/v1/common.proto`) — it is MORE COMPLETE than the old
> community reconstruction.

## Connection

```text
URL:        wss://websocket.lunarclientprod.com/game
User-Agent: Lunar Client 1.8.9-2.16.0
Subprotocols: none
Binary:     all frames protobuf
```

## Handshake (first frame)

The first frame is a RAW
`lunarclient.websocket.handshake.v1.Handshake` — no envelope, no RPC
wrapper. Everything after switches to RPC framing.

### The real handshake (from the jar descriptor)

```protobuf
message Handshake {
  MinecraftIdentity identity            = 1;
  LauncherVersion launcher_version      = 2;  // { semver }
  string installation_id                = 3;  // from launcher-cache/installation-id
  string operating_system               = 5;  // "win32"
  string cpu_architecture               = 6;  // "x64"
  Language language                     = 7;
  GameHandshake game_handshake          = 8;  // only for the game client
  LauncherHandshake launcher_handshake  = 9;  // only for the launcher
  string canary_token                   = 10; // launcher telemetry token
  string operating_system_release       = 11;
  string overwolf_muid                  = 12; // Overwolf machine ID
}
```

Field 9 distinguishes game vs launcher connections on the SAME
endpoint — the server infers the context, no separate URLs needed.

### MinecraftIdentity (excerpt)

```protobuf
message MinecraftIdentity {
  enum Type { TYPE_UNSPECIFIED=0; TYPE_MOJANG=1; TYPE_MICROSOFT=2; }
  UuidAndUsername player      = 1;
  Type type                   = 2;
  string authenticator_jwt    = 3;
  repeated Skin skins         = 4;
  repeated Cape capes         = 5;
  Attributes attributes       = 6;  // includes BannedScopes with reason!
  Timestamp created_at        = 8;
  NameChange name_change      = 9;
  bool owns_bedrock_edition   = 10;
}
```

**Correction to the old docs:** `Type` is a REAL proto enum:
`1 = MOJANG`, `2 = MICROSOFT`.

### GameHandshake (field 8)

`minecraft_version`, `lunar_client_version`, `location`
(InboundLocation), `ichor_modules[]`, `installed_mods[]` (with type
Fabric/Forge internal/external), `modpack`, `gl_extensions[]`,
`launch_id`, `nvidia_memory` (dedicated/total VRAM), `mesa_memory`,
`settings[]` (ClientSetting), `lunar_client_ui_version`.

### LauncherHandshake (field 9)

`environment`, `session_id`, `updater_stream`,
`electron_binaries_type` (OVERWOLF_OW_ELECTRON/ELECTRON), `elevated`,
`silent_start`, `uptime_since_start`, `started_at`, `build_number`,
`git_commit_hash`, `git_short_commit_hash`, `radio_info`,
`optimized_ads`, `analytics`, `owahe`, `settings[]`, `safe_storage`.

### Sensitive fields

| Field | Source | Purpose |
|---|---|---|
| `installation_id` | `~/.lunarclient/launcher-cache/installation-id` | Device tracking |
| `canary_token` | Launcher config | Canary/alpha telemetry |
| `overwolf_muid` | Overwolf SDK | Overwolf machine ID |
| `nvidia_memory` | NVML | GPU fingerprinting |
| `gl_extensions[]` | GL context | GPU/driver fingerprinting |
| `installed_mods[]` | Launcher install | Mod inventory |

### MinecraftVersion (common/v1 — correct shape)

```protobuf
message MinecraftVersion {
  enum MinecraftVersionType {
    MINECRAFT_VERSION_TYPE_UNSPECIFIED=0; RELEASE=1; SNAPSHOT=2;
    OLD_BETA=3; OLD_ALPHA=4;
  }
  string enum = 1;   // "V1_8" etc.
  MinecraftVersionType type = 2;
  string id = 3;     // "1.8.9"
}
```

Three fields, not just the enum string!

### Close codes

| Code | Meaning |
|---|---|
| `4011` | JWT validation failed |
| `4012` | Handshake timeout |

## RPC framing (protocol/v1)

Request (client → server):

```protobuf
message ServerboundWebSocketMessage {
  bytes  request_id = 1;  // ASCII counter "0", "1", "2", ...
  string service    = 2;  // FQSN
  string method     = 3;
  bytes  input      = 4;  // protobuf params
}
```

Response (server → client):

```protobuf
message ClientboundWebSocketMessage {
  WebSocketRpcResponse rpc_response     = 1;
  google.protobuf.Any push_notification = 2;
}

message WebSocketRpcResponse {
  bytes request_id = 1;
  bytes output     = 2;
}
```

Push (server → client, unsolicited): `push_notification` as
`google.protobuf.Any` — the type URL identifies the push message.

### AllowedSender (server-side restriction)

```protobuf
enum AllowedSender {
  ALLOWED_SENDER_AUTHENTICATED_GAME             = 1;
  ALLOWED_SENDER_AUTHENTICATED_LAUNCHER         = 2;
  ALLOWED_SENDER_AUTHENTICATED_GAME_OR_LAUNCHER = 3;
}
```

Every method is bound to a sender type via a descriptor extension —
the server validates game vs launcher.

## Heartbeat

```text
service: lunarclient.websocket.heartbeat.v1.HeartbeatService
method:  GameHeartbeat
input:   GameHeartbeatRequest { map<string,bool> mods }
```

Send roughly every 50s (server timeout 60s). The game heartbeat
carries the map of active mods — telemetry.

Launcher equivalent: `LauncherHeartbeat` with `running_instances[]`,
`open_renderers[]`, `badlion_connected` — response contains
`online_counts`.

## Service catalog

Full list: [SERVICE_CATALOG.md](./SERVICE_CATALOG.md)

| Service | Methods (excerpt) |
|---|---|
| `HeartbeatService` | LauncherHeartbeat, GameHeartbeat |
| `SubscriptionService` | SubscribeV2, Unsubscribe |
| `CosmeticService` (v2) | Login, CreateOutfit, SelectOutfit, LoadTabLogos, ... |
| `FriendService` | Login, SendFriendRequest, BroadcastLocationChange, ... |
| `ConversationService` | 26 methods (messenger) |
| `EmoteService` | UseEmote, GetJamPlayback, UpdateEquippedEmotes |
| `ServerDiscoveryService` | DiscoverServers, SearchServers, TrackServerJoin |
| `HostedWorldService` | StartHostingWorld, JoinHostedWorld, ... |
| `WrappedService` | Login, RecordCounters, SetLeaderboardVisibility |
| ... | 38 services total, 150+ RPCs |

## Detector / stalking flow

```text
handshake
  → CosmeticService.Login
  → start heartbeat loop
  → SubscribeV2(uuids)
  → evaluate cosmetic_pushes
  → (optional) Unsubscribe(uuids)
```

## Push handling

Pushes arrive as `push_notification` (google.protobuf.Any). Known
sources: cosmetic.v2, radio.v1, friend.v1 (7 types), conversation.v1
(18 types), badge.v1, emote.v1, notification.v1, hostedworld.v1,
spray.v1, skyblock.v1. Unknown ones: `protoc --decode_raw` on the
`payload` field.
