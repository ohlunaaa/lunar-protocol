# Proto Reference — Complete Field Reference

> All messages from `proto/` with field numbers, wire types, and semantics.
> Based on: this repo's `.proto` files + Moonlight reference source.

## Package Overview

| Package | File | Purpose |
|---|---|---|
| `lunarclient.common.v1` | `common.proto` | Shared types (Uuid, Color) |
| `lunarclient.authenticator.v1` | `authenticator.proto` | Auth WebSocket messages |
| `lunarclient.websocket.v1` | `websocket.proto` | Handshake + RPC framing |
| `lunarclient.websocket.subscription.v1` | `subscription.proto` | SubscribeV2 + cosmetics pushes |

> **Note:** The manually reconstructed schemas above are a subset. The
> complete original schemas (176 files) extracted from `lunar.jar` live in
> [`proto/extracted/`](../proto/extracted) — see
> [JAR_ANALYSIS.md](./JAR_ANALYSIS.md).

---

## lunarclient.common.v1

### Uuid

Minecraft UUID as two unsigned 64-bit integers.

| Field | # | Type | Wire | Meaning |
|---|---|---|---|---|
| `high` | 1 | `fixed64` | 1 (64-bit) | First 16 hex chars of the UUID without dashes |
| `low` | 2 | `fixed64` | 1 (64-bit) | Last 16 hex chars |

**Important:** `fixed64`, NOT `uint64`! `uint64` would be varint-encoded.
Anyone assuming varint during reverse engineering decodes garbage.
`fixed64` is always exactly 8 bytes little-endian on the wire.

Conversion (string → proto):

```text
"069a79f4-44e9-4726-a5be-fca90e38aaf5"
→ "069a79f444e94726a5befca90e38aaf5"     (strip dashes)
→ high = 0x069a79f444e94726              (first 16 hex)
→ low  = 0xa5befca90e38aaf5              (last 16 hex)
```

Reverse:

```text
high.toString(16).padStart(16, "0") + low.toString(16).padStart(16, "0")
→ all 32 hex chars → format with dashes
```

JavaScript caveat: use `BigInt`; `Number` loses precision above 2^53.

### Color

| Field | # | Type | Meaning |
|---|---|---|---|
| `color` | 1 | `int32` | Packed ARGB value |

Not four floats, not three bytes — ONE int32. Hex ↔ int conversion:

```text
"#ffffff" (RGB)    → 0x00FFFFFF or with alpha 0xFFFFFFFF
"#7fffffff" (ARGB) → 0x7FFFFFFF
```

**Varint trap:** `int32` is varint-encoded. Negative values (e.g.
alpha=FF → value above 2^31 or directly negative depending on
interpretation) encode as 10-byte varints (sign-bit extension).
Account for this when decoding manually.

---

## lunarclient.authenticator.v1

### UuidAndUsername

| Field | # | Type | Meaning |
|---|---|---|---|
| `uuid` | 1 | `lunarclient.common.v1.Uuid` | Player UUID |
| `username` | 2 | `string` | Player name |

### HelloMessage (Client → Server, first message)

| Field | # | Type | Meaning |
|---|---|---|---|
| `identity` | 1 | `UuidAndUsername` | UUID + username |
| `initiator` | 2 | `string` | `"assetServer"` for the game client |

`initiator` is the connection context. Observed: `"assetServer"`.

### EncryptionRequestMessage (Server → Client)

| Field | # | Type | Meaning |
|---|---|---|---|
| `public_key` | 1 | `bytes` | DER-encoded RSA public key (X.509 SPKI) |
| `random_bytes` | 2 | `bytes` | Server nonce/challenge |

The public key loads directly (e.g. Java `X509EncodedKeySpec`, Node
`crypto.createPublicKey({ key, format: 'der', type: 'spki' })`).

### EncryptionResponseMessage (Client → Server)

| Field | # | Type | Meaning |
|---|---|---|---|
| `secret_key` | 1 | `bytes` | RSA-PKCS1v15-encrypted AES-128 key |
| `public_key` | 2 | `bytes` | RSA-PKCS1v15-encrypted nonce |

**Field name is misleading:** field 2 contains the encrypted NONCE,
not a public key. Verified in the observed flow.

### AuthSuccessMessage (Server → Client)

| Field | # | Type | Meaning |
|---|---|---|---|
| `jwt` | 1 | `string` | JWT for the game WebSocket handshake |

### EncryptionFailMessage (Client → Server)

| Field | # | Type | Meaning |
|---|---|---|---|
| `reason` | 1 | `string` | Failure reason |

### Envelopes

```protobuf
// Client -> Server
message ServerboundAuthMessage {
  oneof contents {
    HelloMessage              hello               = 1;
    EncryptionResponseMessage encryption_response = 2;
    EncryptionFailMessage     encryption_fail     = 3;
  }
}

// Server -> Client
message ClientboundAuthMessage {
  oneof contents {
    EncryptionRequestMessage encryption_request = 1;
    AuthSuccessMessage       auth_success       = 2;
  }
}
```

Each direction has exactly ONE envelope. One frame = one
`ServerboundAuthMessage` or `ClientboundAuthMessage`, never naked
messages.

---

## lunarclient.websocket.v1

> The extracted original splits this into `websocket/handshake/v1`,
> `websocket/protocol/v1` and more — see
> [GAME_WEBSOCKET.md](./GAME_WEBSOCKET.md) for the real handshake.

### UuidAndUsername (duplicate!)

Identical to `authenticator.v1.UuidAndUsername` — Lunar duplicates the
type per package instead of keeping it in `common`. Generate both
during codegen; don't merge them.

### VersionInfo

| Field | # | Type | Meaning |
|---|---|---|---|
| `version` | 1 | `string` | e.g. `"2.16.0"` |

Just ONE string field. No int32, no semantic-versioning triple.

### Language

| Field | # | Type | Meaning |
|---|---|---|---|
| `language` | 1 | `string` | `"eng"` (ISO 639-2) |
| `locale` | 2 | `string` | `"en_US"` |

### MinecraftVersion

| Field | # | Type | Meaning |
|---|---|---|---|
| `version` | 1 | `string` | `"V1_8"` for 1.8.9 |

**Again a STRING, not an enum int.** The enum values are encoded as
strings: `V1_8`, `V1_12`, `V1_16`, `V1_17`, `V1_18_1`, `V1_19`, ...
— full list in the game WebSocket doc.

### LunarClientVersion

| Field | # | Type | Meaning |
|---|---|---|---|
| `branch` | 1 | `string` | `"dev"`, `"master"` |
| `git_commit` | 2 | `string` | Short hash, e.g. `"a1b2c3d"` |
| `version` | 3 | `string` | `"2.16.0"` |

Field order matters: branch=1, commit=2, semver=3.

### GameBlock

| Field | # | Type | Meaning |
|---|---|---|---|
| `minecraft_version` | 1 | `MinecraftVersion` | MC version |
| `lunar_client_version` | 2 | `LunarClientVersion` | Lunar version |

### MinecraftIdentity

| Field | # | Type | Meaning |
|---|---|---|---|
| `player` | 1 | `UuidAndUsername` | Player |
| `type` | 2 | `int32` | Account type; observed: `1` = Microsoft |
| `authenticator_jwt` | 3 | `string` | JWT from the auth flow |

### Handshake (first frame, NOT wrapped)

| Field | # | Type | Meaning |
|---|---|---|---|
| `identity` | 1 | `MinecraftIdentity` | Player + JWT |
| `version_info` | 2 | `VersionInfo` | Lunar version |
| *(unknown)* | 3 | — | Always left empty |
| *(unknown)* | 4 | — | Always left empty |
| `os` | 5 | `string` | `"win32"`, `"darwin"`, `"linux"` |
| `arch` | 6 | `string` | `"x64"`, `"arm64"` |
| `language` | 7 | `Language` | Language/locale |
| `game_block` | 8 | `GameBlock` | MC + Lunar version |

Fields 3 and 4 appear in community proto descriptions but are
unidentified in content. Leave empty. The numbering gaps (3, 4) are
intentional reservations by Lunar.

### ServerboundWebSocketMessage (RPC request envelope)

| Field | # | Type | Meaning |
|---|---|---|---|
| `request_id` | 1 | `bytes` | ASCII counter: `b"0"`, `b"1"`, `b"2"`, ... |
| `service` | 2 | `string` | Fully qualified service name |
| `method` | 3 | `string` | Method name |
| `input` | 4 | `bytes` | Protobuf-encoded request params |

`request_id` is NOT a varint counter but the ASCII representation of
the counter as bytes. `"1"` = `[0x31]`.

### RpcResponse

| Field | # | Type | Meaning |
|---|---|---|---|
| `request_id` | 1 | `bytes` | Matches the request ID |
| `output` | 2 | `bytes` | Protobuf-encoded response |

### PushNotification (Server → Client, unsolicited)

| Field | # | Type | Meaning |
|---|---|---|---|
| `service` | 1 | `string` | Push source |
| `push` | 2 | `string` | Push name/type |
| `payload` | 3 | `bytes` | Protobuf-encoded push data |

### ClientboundWebSocketMessage (server envelope)

```protobuf
message ClientboundWebSocketMessage {
  RpcResponse      rpc_response      = 1;
  PushNotification push_notification = 2;
}
```

---

## lunarclient.websocket.subscription.v1

### SubscribeV2Request

| Field | # | Type | Meaning |
|---|---|---|---|
| `target_uuids` | 1 | `repeated Uuid` | UUIDs to subscribe to |

### EquippedCosmetic

| Field | # | Type | Meaning |
|---|---|---|---|
| `id` | 1 | `int64` | Cosmetic ID |

`int64` = varint. More fields presumably exist (unknown); protobuf
skips unknowns cleanly.

### ConditionalCosmetics

| Field | # | Type | Meaning |
|---|---|---|---|
| `cosmetics` | 1 | `repeated EquippedCosmetic` | Items with context condition |

Conditions (e.g. "only on Hypixel") are encoded in unknown extra
fields — not yet reverse-engineered with certainty.

### PlayerCosmeticsPushV2

| Field | # | Type | Meaning |
|---|---|---|---|
| `player_uuid` | 1 | `Uuid` | Player UUID |
| `logo_color` | 2 | `Color` | Tab-list logo color |
| `logo_always_show` | 3 | `bool` | Lunar+ feature |
| `plus_color` | 4 | `Color` | Lunar+ color (subscribers only) |
| `conditional_cosmetics` | 5 | `repeated ConditionalCosmetics` | Context-bound items |
| `default_cosmetics` | 6 | `repeated EquippedCosmetic` | Always-active items |
| `badge_id` | 7 | `int32` | 0 = no badge |
| `outfit_uuid` | 8 | `Uuid` | Outfit UUID if set |

### PlayerRadioPush

| Field | # | Type | Meaning |
|---|---|---|---|
| `player_uuid` | 1 | `Uuid` | Player UUID |

Nearly empty in content — radio pushes appear to only signal presence.

### SubscribeV2Response

| Field | # | Type | Meaning |
|---|---|---|---|
| `cosmetic_pushes` | 1 | `repeated PlayerCosmeticsPushV2` | Lunar players + cosmetics |
| `radio_pushes` | 2 | `repeated PlayerRadioPush` | Radio-active players |

**Core signal:** UUID in `cosmetic_pushes` → Lunar Client user.

### UnsubscribeRequest / UnsubscribeResponse

| Message | Fields |
|---|---|
| `UnsubscribeRequest` | `target_uuids = 1 (repeated Uuid)` |
| `UnsubscribeResponse` | empty |

---

## Wire Format Cheat Sheet

| Type | Wire type | Encoding |
|---|---|---|
| `int32`, `int64` | 0 | varint |
| `fixed64` | 1 | 8 bytes little-endian |
| `string`, `bytes` | 2 | length prefix (varint) + raw bytes |
| `fixed32` | 5 | 4 bytes little-endian |

Tooling for raw dumping:

```bash
# Dump a WS frame to a file, then:
protoc --decode_raw < frame.bin
protoc --decode=lunarclient.websocket.v1.ClientboundWebSocketMessage \
  websocket.proto < frame.bin
```
