# Lunar Client Jar Analysis — Full Reverse Engineering

> Source: `~/.lunarclient/offline/multiver/lunar.jar` (69.9 MB build with
> protobuf codegen). Class files extracted + embedded FileDescriptor
> blobs pulled from the constant pools of the `*Proto.class` files.
>
> **Result: 176 `.proto` files, 38 services, 150+ RPC methods —
> the complete protocol, unobfuscated.**

## Table of Contents

- [Locations on Disk](#locations-on-disk)
- [Jar Structure](#jar-structure)
- [Extraction Method](#extraction-method)
- [What the Jar Reveals](#what-the-jar-reveals)
- [Architecture Overview](#architecture-overview)

## Locations on Disk

| Path | Contents |
|---|---|
| `~/.lunarclient/offline/multiver/lunar.jar` | The game client (70 MB) |
| `~/.lunarclient/offline/multiver/*.jar` | Modules (genesis, sodium, replay, optifine...) |
| `~/.lunarclient/offline/multiver/natives/` | LWJGL, Ultralight (UI), DLLs |
| `~/.lunarclient/jre/<hash>/zulu17...` | Bundled Zulu JREs (17 + 25) |
| `~/.lunarclient/launcher-cache/` | `installation-id`, UI zips, texture index |
| `~/.lunarclient/settings/launcher.json` | Launcher settings |
| `%APPDATA%\lunarclient\` | Electron profile (cookies, local storage, code cache) |
| `%APPDATA%\lunarclient\shared_proto_db\` | LevelDB, video clip metadata (NOT protos) |
| `%LOCALAPPDATA%\lunarclient-updater\` | Updater artifacts |

## Jar Structure

```text
lunar.jar
├── com/lunarclient/          # UNOBFUSCATED — the entire protocol
│   ├── authenticator/v1/     # Auth WS messages
│   ├── common/v1/            # Uuid, Color, Version, Location, Skin...
│   ├── websocket/            # 35 service packages (v1/v2)
│   │   ├── handshake/v1/     # The real handshake (richer than old docs!)
│   │   ├── protocol/v1/      # RPC envelope
│   │   ├── subscription/v1/  # SubscribeV2
│   │   ├── cosmetic/v2/      # 20 messages
│   │   ├── friend/v1/        # 30 messages
│   │   ├── conversation/v1/  # 48 messages (friend messenger)
│   │   └── ... (analytics through wrapped)
│   ├── gameipc/              # Launcher <-> Game RPC (LaunchService, Styngr...)
│   └── apollo/v1/            # Server-owner API (Beam, Waypoints...)
├── com/moonsworth/lunar/     # OBFUSCATED (HCOOH...-style class names)
│   └── client/               # Client logic, mixins
├── okhttp3/, okio/           # HTTP stack
├── io/netty/                 # Networking
├── google/protobuf/          # Protobuf runtime
└── native/                   # Native bridges
```

**Key insight:** Only `com.moonsworth.lunar` is obfuscated. ALL
protobuf-generated classes under `com.lunarclient` are in plain text —
including every message, every service, every field number.

## Extraction Method

The generated `*Proto.class` files contain serialized
`FileDescriptorProto` blobs as Utf8 constant-pool entries (modified
UTF-8, no longer Base64 since protobuf-java 3.x).

Extraction script: [../tools/extract_protos.py](../tools/extract_protos.py)

```text
1. Unpack lunar.jar (tar -xf, to bypass the Windows path-length limit)
2. Find all *Proto.class under com/lunarclient (176 files)
3. Parse the constant pool (tag 1 = Utf8)
4. Decode modified UTF-8 (0xC0 0x80 -> 0x00)
5. Detect blobs: starts with 0x0A, contains ".proto" in first 80 bytes
6. Parse FileDescriptorProto fields (name, package, messages, enums, services)
7. Re-emit as .proto text
```

Output: [`proto/extracted/`](../proto/extracted) — 176 files.

## What the Jar Reveals

### The REAL handshake (handshake/v1/common.proto)

Significantly richer than the old community reconstruction:

```protobuf
message Handshake {
  oneof client { }            // game or launcher
  MinecraftIdentity identity = 1;
  LauncherVersion launcher_version = 2;
  string installation_id = 3;          // ~/.lunarclient/launcher-cache/installation-id
  string operating_system = 5;         // "win32"
  string operating_system_release = 11;
  string cpu_architecture = 6;         // "x64"
  Language language = 7;
  string canary_token = 10;            // launcher canary token!
  string overwolf_muid = 12;           // Overwolf tracking ID!
  GameHandshake game_handshake = 8;
  LauncherHandshake launcher_handshake = 9;
}
```

**Sensitive:** `canary_token`, `overwolf_muid` — telemetry IDs. The
`installation_id` sits in plain text under `launcher-cache/installation-id`.

`MinecraftIdentity` contains more than UUID + name: skins, capes,
account privileges, ban scopes (`Attributes.BannedScope` with ban
reason and expiry!), name-change history, Bedrock ownership.

### GameHandshake

GPU info (Nvidia VRAM, Mesa), ichor modules, installed mods with type
(Fabric/Forge internal/external), GL extensions, launch_id, client
settings.

### LauncherHandshake

Environment, session_id, updater_stream, Electron binaries type
(Overwolf!), elevated, build_number, git hashes, radio info,
`optimized_ads`, `analytics`, `owahe`, `safe_storage` flags.

### AllowedSender (protocol/v1)

```protobuf
enum AllowedSender {
  ALLOWED_SENDER_AUTHENTICATED_GAME = 1;
  ALLOWED_SENDER_AUTHENTICATED_LAUNCHER = 2;
  ALLOWED_SENDER_AUTHENTICATED_GAME_OR_LAUNCHER = 3;
}
```

Every RPC method carries a sender-restriction descriptor extension —
the server validates whether game or launcher is allowed to call.

### The heartbeat is NOT empty

```protobuf
message GameHeartbeatRequest {
  message ModsEntry { string key = 1; bool value = 2; }
  // map<string,bool> field — active mods
}
```

The game heartbeat carries a map of active mods — telemetry on module
usage.

## Architecture Overview

```text
Launcher (Electron/Overwolf)
  │  gameipc (LaunchService, BrowserService, StyngrRadioService...)
  ▼
Game JVM (lunar.jar)
  │  Auth WS: authenticator.lunarclientprod.com  (RSA/AES + Mojang joinServer)
  │  Game WS: websocket.lunarclientprod.com      (handshake + RPC)
  ▼
38 services: analytics, apollo, badge, chat, conversation, cosmetic,
emote, friend, handshake, heartbeat, hostedworld, jam, language,
legacyapi, liveexperience, logupload, marker, notification, paynow,
performance, promotion, protocol, radio, screenshot, server,
serverdiscovery, setting, skyblock, socials, spray, store, subscription,
tebex, wrapped
```

Additionally `apollo/v1` — a parallel API set for SERVER OWNERS
(beams, borders, waypoints, holograms, staffmods...) running over the
same WS.

## Next Steps

- Derive per-service docs from `proto/extracted/`
- Reverse the launcher's (Electron) `app.asar` for the launcher side
- Capture the `gameipc` connection (launcher <-> game)
