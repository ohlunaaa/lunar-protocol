# Lunar Client WebSocket Protocol Documentation

> Unofficial technical notes on Lunar Client's authenticator and game WebSocket protocol.

This document explains the authentication flow, game WebSocket handshake, protobuf RPC envelope, heartbeat, and player cosmetic subscription flow used by Lunar Client.

## Table Of Contents

- [Overview](#overview)
- [Protocol Files](#protocol-files)
- [UUID Encoding](#uuid-encoding)
- [Authenticator WebSocket](#authenticator-websocket)
- [Mojang Join Server](#mojang-join-server)
- [Auth Success](#auth-success)
- [Game WebSocket](#game-websocket)
- [Game Handshake](#game-handshake)
- [RPC Envelope](#rpc-envelope)
- [Heartbeat](#heartbeat)
- [Cosmetic Service Login](#cosmetic-service-login)
- [Detecting Lunar Players](#detecting-lunar-players)
- [Cosmetic Push Data](#cosmetic-push-data)
- [End-To-End Flow](#end-to-end-flow)
- [Implementation Notes](#implementation-notes)
- [Extended Documentation](#extended-documentation)

## Overview

Lunar uses two binary WebSocket connections:

| Purpose | Endpoint | Format |
|---|---|---|
| Authentication | `wss://authenticator.lunarclientprod.com/game` | protobuf messages |
| Game services | `wss://websocket.lunarclientprod.com/game` | protobuf handshake + protobuf RPC |

High-level flow:

```text
Minecraft session
  -> connect authenticator WebSocket
  -> send HelloMessage
  -> receive EncryptionRequestMessage
  -> call Mojang joinServer
  -> send EncryptionResponseMessage
  -> receive AuthSuccessMessage with JWT
  -> close authenticator WebSocket
  -> connect game WebSocket
  -> send Handshake with JWT
  -> send CosmeticService.Login
  -> keep GameHeartbeat running
  -> call SubscriptionService.SubscribeV2 with UUIDs
  -> decode cosmeticPushes
```

## Protocol Files

A reference implementation typically loads these protobuf files:

```text
proto/common.proto
proto/authenticator.proto
proto/websocket.proto
proto/subscription.proto
```

Important protobuf types:

```text
lunarclient.authenticator.v1.ServerboundAuthMessage
lunarclient.authenticator.v1.ClientboundAuthMessage
lunarclient.websocket.v1.Handshake
lunarclient.websocket.v1.ServerboundWebSocketMessage
lunarclient.websocket.v1.ClientboundWebSocketMessage
lunarclient.websocket.subscription.v1.SubscribeV2Request
lunarclient.websocket.subscription.v1.SubscribeV2Response
```

## UUID Encoding

Lunar's protobuf UUID type stores a Minecraft UUID as two unsigned 64-bit integers:

```text
Uuid {
  high: uint64
  low:  uint64
}
```

Conversion:

```text
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
-> remove dashes
-> first 16 hex chars  = high
-> second 16 hex chars = low
```

When decoding, `high` and `low` are padded to 16 hex characters each and joined back into the normal Minecraft UUID string.

## Authenticator WebSocket

Endpoint:

```text
wss://authenticator.lunarclientprod.com/game
```

Header:

```text
User-Agent: Lunar Client 1.8.9-2.16.0
```

The first client message is `ServerboundAuthMessage.hello`.

Example structure:

```json
{
  "hello": {
    "identity": {
      "uuid": "<protobuf Uuid>",
      "username": "ExamplePlayer"
    },
    "initiator": "assetServer"
  }
}
```

## Mojang Join Server

The server replies with `ClientboundAuthMessage.encryptionRequest`.

It contains:

```text
publicKey: DER-encoded RSA public key
randomBytes: nonce
```

The client generates a random 16-byte AES key and computes the Minecraft session hash:

```text
SHA-1(aesKey || serverPublicKeyDer)
```

The SHA-1 digest is formatted as Minecraft's signed Java `BigInteger` server-id hex string.

Then the client calls Mojang:

```text
POST https://sessionserver.mojang.com/session/minecraft/join
```

Body:

```json
{
  "accessToken": "<minecraft access token>",
  "selectedProfile": "<minecraft uuid without dashes>",
  "serverId": "<signed sha1 hex>"
}
```

A successful response is usually HTTP `204 No Content`.

## Auth Success

After Mojang accepts the join request, the client sends `ServerboundAuthMessage.encryptionResponse`.

Payload:

```text
secretKey: RSA_PKCS1_encrypt(aesKey, serverPublicKey)
publicKey: RSA_PKCS1_encrypt(nonce, serverPublicKey)
```

Despite the field name, the second value is the encrypted nonce in the observed flow.

The server then sends:

```text
ClientboundAuthMessage.authSuccess
```

The important value is:

```text
jwt
```

The authenticator WebSocket can then be closed normally.

## Game WebSocket

Endpoint:

```text
wss://websocket.lunarclientprod.com/game
```

Header:

```text
User-Agent: Lunar Client 1.8.9-2.16.0
```

The first frame is a raw `lunarclient.websocket.v1.Handshake`, not an RPC wrapper.

After the handshake, messages use:

```text
ServerboundWebSocketMessage
ClientboundWebSocketMessage
```

## Game Handshake

Observed handshake structure:

```json
{
  "identity": {
    "player": {
      "uuid": "<protobuf Uuid>",
      "username": "ExamplePlayer"
    },
    "type": 1,
    "authenticatorJwt": "<jwt from authenticator>"
  },
  "versionInfo": {
    "version": "2.16.0"
  },
  "os": "win32",
  "arch": "x64",
  "language": {
    "language": "eng",
    "locale": "en_US"
  },
  "gameBlock": {
    "minecraftVersion": {
      "version": "V1_8"
    },
    "lunarClientVersion": {
      "branch": "dev",
      "gitCommit": "0000000",
      "version": "2.16.0"
    }
  }
}
```

Useful close codes:

| Code | Meaning |
|---|---|
| `4011` | JWT validation failed |
| `4012` | Handshake timeout |

## RPC Envelope

After the handshake, client RPC calls are encoded as:

```text
lunarclient.websocket.v1.ServerboundWebSocketMessage
```

Observed fields:

```json
{
  "requestId": "<ascii bytes, e.g. '1'>",
  "service": "fully.qualified.ServiceName",
  "method": "MethodName",
  "input": "<protobuf-encoded request bytes>"
}
```

Responses arrive as `ClientboundWebSocketMessage.rpcResponse`.

The response `requestId` matches the request ID bytes. The `output` field contains protobuf-encoded response bytes for the specific RPC method.

## Heartbeat

The game WebSocket expects a heartbeat roughly every 60 seconds.

The reference implementation sends one every 50 seconds.

RPC:

```text
service: lunarclient.websocket.heartbeat.v1.HeartbeatService
method:  GameHeartbeat
input:   empty bytes
```

## Cosmetic Service Login

After the game handshake, the client sends:

```text
service: lunarclient.websocket.cosmetic.v2.CosmeticService
method:  Login
input:   empty bytes
```

The response can be ignored for basic player detection.

## Detecting Lunar Players

Player detection uses `SubscriptionService.SubscribeV2`.

Request type:

```text
lunarclient.websocket.subscription.v1.SubscribeV2Request
```

RPC:

```text
service: lunarclient.websocket.subscription.v1.SubscriptionService
method:  SubscribeV2
input:   SubscribeV2Request
```

Request shape:

```json
{
  "targetUuids": [
    "<protobuf Uuid>",
    "<protobuf Uuid>"
  ]
}
```

Response type:

```text
lunarclient.websocket.subscription.v1.SubscribeV2Response
```

The key field is:

```text
cosmeticPushes
```

If a UUID appears in `cosmeticPushes`, it can be treated as a Lunar Client user.

## Cosmetic Push Data

Each cosmetic push can contain data such as:

```text
playerUuid
logoColor
logoAlwaysShow
plusColor
badgeId
defaultCosmetics
conditionalCosmetics
```

Useful output shape:

```json
{
  "uuid": "00000000-0000-4000-8000-000000000000",
  "logoColor": "#ffffff",
  "logoAlwaysShow": true,
  "plusColor": null,
  "badgeId": 0,
  "badgeUrl": null,
  "cosmetics": [
    {
      "id": "123"
    }
  ]
}
```

Badge icons can be derived with:

```text
https://cosmetics.lunarclientcdn.com/badge/{badgeId}/icon.png
```

## End-To-End Flow

```text
Load protobuf schemas
  -> connect authenticator WebSocket
  -> send HelloMessage
  -> receive EncryptionRequestMessage
  -> generate AES key
  -> compute Minecraft session hash
  -> POST Mojang joinServer
  -> send EncryptionResponseMessage
  -> receive AuthSuccessMessage.jwt
  -> connect game WebSocket
  -> send raw Handshake with JWT
  -> send CosmeticService.Login
  -> start GameHeartbeat loop
  -> encode SubscribeV2Request with UUIDs
  -> send RPC SubscriptionService.SubscribeV2
  -> decode SubscribeV2Response
  -> map cosmeticPushes by playerUuid
```

## Implementation Notes

- The authenticator and game sockets are both binary WebSockets.
- Messages are protobuf-encoded, not JSON.
- The first game WebSocket frame is a raw `Handshake`.
- Later game WebSocket calls use the RPC wrapper.
- `requestId` is ASCII bytes such as `"1"`, `"2"`, `"3"`.
- Heartbeats should be sent before the 60-second timeout.
- `SubscribeV2` can be used with UUIDs from the Minecraft tab list.
- UUIDs must be encoded as unsigned `high` / `low` 64-bit values.
- A returned `cosmeticPush` is the practical Lunar user signal.

## Extended Documentation

The documents above describe the minimal detection flow. Deeper analysis lives in the companion documents:

- [PROTO_REFERENCE.md](./PROTO_REFERENCE.md) — every field, wire type, and trap
- [AUTH_FLOW.md](./AUTH_FLOW.md) — the auth flow with crypto details and pitfalls
- [GAME_WEBSOCKET.md](./GAME_WEBSOCKET.md) — the real handshake from the jar descriptors
- [SERVICE_CATALOG.md](./SERVICE_CATALOG.md) — all 38 services with their RPCs
- [JAR_ANALYSIS.md](./JAR_ANALYSIS.md) — how the full protocol was extracted from lunar.jar
- [`proto/extracted/`](../proto/extracted) — the 176 original `.proto` files
