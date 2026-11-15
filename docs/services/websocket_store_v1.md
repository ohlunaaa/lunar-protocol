# `lunarclient.websocket.store.v1`

## Service `StoreService`

Source: [`proto/extracted/lunarclient_websocket_store_v1_service.proto`](../../proto/extracted/lunarclient_websocket_store_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.store.v1.LoginRequest` | `lunarclient.websocket.store.v1.LoginResponse` |
| `SetIncomingGiftPrivacy` | `lunarclient.websocket.store.v1.SetIncomingGiftPrivacyRequest` | `lunarclient.websocket.store.v1.SetIncomingGiftPrivacyResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - `lunarclient.websocket.store.v1.IncomingGiftPrivacy` `incoming_gift_privacy` = 1
  - `int64` `coins` = 2
- **SetIncomingGiftPrivacyRequest**
  - `lunarclient.websocket.store.v1.IncomingGiftPrivacy` `incoming_gift_privacy` = 1
- **SetIncomingGiftPrivacyResponse**
