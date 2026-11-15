# lunar-protocol

Unofficial documentation and research notes for Lunar Client's authentication and game WebSocket protocol.

This repository documents how a Minecraft session authenticates with Lunar's authenticator WebSocket, connects to the game WebSocket, sends protobuf RPC messages, and subscribes to player cosmetic data. It also contains the **complete protocol extracted from `lunar.jar`**: 176 original `.proto` files covering all 38 services and 150+ RPC methods.

## Documentation

- [Protocol Documentation](./docs/PROTOCOL.md)
- [Proto Reference](./docs/PROTO_REFERENCE.md)
- [Auth Flow](./docs/AUTH_FLOW.md)
- [Game WebSocket](./docs/GAME_WEBSOCKET.md)
- [Service Catalog](./docs/SERVICE_CATALOG.md)
- [Jar Analysis (full reverse engineering)](./docs/JAR_ANALYSIS.md)
- [Protobuf Schemas](./proto) — manual reconstruction
- [Extracted original protos](./proto/extracted) — 176 files from lunar.jar

## Covered Topics

- Authenticator WebSocket flow
- RSA/AES challenge-response authentication
- Mojang `joinServer` integration
- Game WebSocket handshake (original descriptors)
- Protobuf message structure (176 .proto files)
- All 38 WebSocket services with 150+ RPC methods
- GameIPC (launcher <-> game) protocol
- Apollo server-owner API
- `SubscribeV2` player detection
- UUID conversion between Minecraft strings and protobuf `Uuid`

## Architecture

```text
Minecraft session
  -> Lunar Authenticator WebSocket
  -> Mojang joinServer challenge
  -> AuthSuccess JWT
  -> Lunar Game WebSocket
  -> Handshake with JWT
  -> RPC calls for heartbeat and subscriptions
```

| Layer | Endpoint | Protocol |
|---|---|---|
| Authenticator | `wss://authenticator.lunarclientprod.com/game` | Binary WebSocket + protobuf |
| Game WebSocket | `wss://websocket.lunarclientprod.com/game` | Binary WebSocket + protobuf RPC |
| Mojang Session | `https://sessionserver.mojang.com/session/minecraft/join` | HTTPS + JSON |

## Tools

- [`tools/extract_protos.py`](./tools/extract_protos.py) — pulls the embedded
  FileDescriptor blobs out of the generated `*Proto.class` files of an
  unpacked `lunar.jar` and re-emits them as `.proto` text.

## Status

These notes are based on protocol research, a reference implementation, and static analysis of the installed client. They are intended as technical research notes, not official documentation.

## Disclaimer

This project is not affiliated with Lunar Client. Use these notes responsibly and respect all applicable terms of service.
