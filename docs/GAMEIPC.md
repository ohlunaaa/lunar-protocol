# GameIPC — Launcher <-> Game Protocol

> The local RPC channel between the Electron launcher and running game
> instances. Reconstructed from the launcher's `app.asar`
> (`dist-electron/electron/main.js`) and cross-checked against the
> game-side protos in `proto/extracted/lunarclient_gameipc_*`.

## Transport

The launcher runs a **WebSocket server on localhost** and the game
connects to it as a client:

```text
ws://127.0.0.1:28190   (base port, from launcher source: port = 28190)
```

Port selection logic (from `main.js`):

- Start at port `28190`.
- On `EADDRINUSE`: retry the same port up to 5 times (1s apart), then
  move to `port + 1` and repeat — up to 30 ports total
  (`28190`–`28219`).
- `verifyClient` accepts everything — **no authentication on this
  socket**. Any local process can connect.

## Message flow

```text
Game (client)                          Launcher (server)
    │  1. connect ws://127.0.0.1:28190      │
    │ ─────────────────────────────────────► │
    │  2. Handshake (gameipc.handshake.v1)   │
    │ ─────────────────────────────────────► │  binds launchId
    │                                        │
    │  3. LauncherboundIPCMessage (RPC)      │
    │ ─────────────────────────────────────► │
    │  4. GameboundIPCMessage.rpc_response   │
    │ ◄───────────────────────────────────── │
    │                                        │
    │  5. GameboundIPCMessage.push (Any)     │  unsolicited
    │ ◄───────────────────────────────────── │
```

## Handshake (during WebSocket upgrade)

`lunarclient.gameipc.handshake.v1.Handshake` — **sent as the
`lc-handshake` WebSocket subprotocol header** (Base64 of the protobuf),
NOT as a first frame (corrected from launcher-side analysis; the
decompiled game client passes
`Map.of("lc-handshake", base64(handshake.toByteArray()))` to the
WebSocketClient constructor):

| Field | # | Type | Meaning |
|---|---|---|---|
| `launch_id` | 1 | `string` | Identifies the launch session |
| `process_id` | 2 | `string` | Game process PID |
| `installation_id` | 3 | `string` | Same device ID as the WS handshake |

The game connects with a 3,000 ms connect timeout and port `28190`
hardcoded (`client.util` config class). After the handshake the
launcher binds the connection to the `launch_id` and flushes pushes
that were queued while the game was starting.

## Envelopes

### Game → Launcher: `LauncherboundIPCMessage`

```protobuf
message LauncherboundIPCMessage {
  bytes  request_id      = 1;
  string service         = 2;
  string method          = 3;
  bytes  input           = 4;
  string full_method     = 6;  // "/package.Service/Method"
  string input_name      = 7;  // "MethodRequest"
  string input_full_name = 8;  // "lunarclient.gameipc...MethodRequest"
}
```

Same request/response pattern as the remote game WebSocket (ASCII
counter request IDs), plus fields 6–8 that carry gRPC-style full
method names (used for routing/registry).

### Launcher → Game: `GameboundIPCMessage`

```protobuf
message GameboundIPCMessage {
  IPCRpcResponse    rpc_response     = 1;
  google.protobuf.Any push_notification = 2;
}

message IPCRpcResponse {
  bytes request_id = 1;
  bytes output     = 2;
}
```

Pushes are wrapped in `google.protobuf.Any` with type URLs of the
form `type.googleapis.com/lunarclient.gameipc.<pkg>.<Message>`.

## Push routing

From the launcher source (`sendPush`, `queuePush`,
`bindPendingPushes`):

- Pushes can target a specific `launch_id` or broadcast to all
  connected games.
- Pushes sent while a game is still launching are **queued** and
  bound to the next launch (`pendingPushes`).
- The launcher tracks a `lastFocusedLaunchId` and only one game is
  "focused" at a time — some pushes (e.g. chat) go to the focused
  instance.

## Services callable by the game (game → launcher)

From `proto/extracted/lunarclient_gameipc_*_service.proto`:

| Service | RPCs |
|---|---|
| `AuthService` | `RefreshAccount`, `AddAccount` |
| `LaunchService` | `LaunchGame` |
| `BrowserService` | `OpenUrl` (initiator: cosmetics/alert/auth/blog/social link/home/screenshot/store, open type: embedded/external) |
| `ChatService` | `ReceiveMessage` (launcher -> game is a push; game -> launcher: `ReceiveMessage`) |
| `LocationService` | `UpdateFocus`, `UpdateLocation` |
| `PayNowService` | `OpenPayNowJsCheckout`, `CheckPayNowCapabilities` |
| `PromotionService` | `CheckPendingPromotion`, `PlayPromotion` |
| `TeBexService` | `OpenTebexJsCheckout`, `CheckTebexCapabilities` |
| `StyngrRadioService` | `FetchState`, `FetchPlaylists`, `StartPlaylist`, `NextTrack`, `SetPlaying`, `SetMuted`, `SetVolume`, `ToggleLiked`, `OpenSelector` |

## Pushes (launcher → game)

| Package | Push | Payload |
|---|---|---|
| `launch.v1` | `PlayServerPush` | `auto_join_server_ip` |
| `launch.v1` | `ExitGamePush` | empty — tells the game to quit |
| `chat.v1` | `SendChatPush` | `message` |
| `location.v1` | (focus/location push) | |
| `paynow.v1` / `tebex.v1` | checkout push | |
| `promotion.v1` | promotion push | |
| `store.v1` | store push | |
| `styngr.v1` | radio pushes (3 types) | |

## Security notes

- **No auth on the local socket** — `verifyClient` always accepts.
  Any local process can connect to `127.0.0.1:28190+`, send a
  handshake with a known `launch_id`, and receive pushes or call
  launcher services (e.g. `LaunchGame`, `OpenUrl`).
- The `launch_id` is the only routing credential; it is not secret
  (it also appears in the remote handshake as `GameHandshake.launch_id`).
- The game port is discoverable by scanning `28190–28219`.

## Capturing traffic

Since the transport is plain `ws://` on localhost:

```js
// Proxy: listen on 28190, forward to the real launcher port,
// dump both directions, decode with the gameipc protos.
```

Or set an env hook / patch `main.js` in the extracted asar to log
`LauncherboundIPCMessage` / `GameboundIPCMessage` frames. Wireshark on
the loopback interface with a `ws` dissector works too — the frames
are unmasked server->client but the payload is raw protobuf either way.
