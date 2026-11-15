# `lunarclient.websocket.tebex.v1`

## Service `TebexService`

Source: [`proto/extracted/lunarclient_websocket_tebex_v1_service.proto`](../../proto/extracted/lunarclient_websocket_tebex_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `TebexJsCheckoutOpened` | `lunarclient.websocket.tebex.v1.TebexJsCheckoutOpenedRequest` | `lunarclient.websocket.tebex.v1.TebexJsCheckoutOpenedResponse` |
| `TebexJsCheckoutClosed` | `lunarclient.websocket.tebex.v1.TebexJsCheckoutClosedRequest` | `lunarclient.websocket.tebex.v1.TebexJsCheckoutClosedResponse` |

## Messages

- **TebexJsCheckoutOpenedRequest**
  - `string` `basket_ident` = 1
  - `lunarclient.websocket.tebex.v1.TebexJsCheckoutOpenedRequest.Backend` `backend` = 2
  - `string` `locale` = 3
  - enum **Backend**:
    - `BACKEND_UNSPECIFIED = 0`
    - `BACKEND_OVERWOLF_OVERLAY = 1`
    - `BACKEND_ELECTRON_WINDOW = 2`
- **TebexJsCheckoutOpenedResponse**
- **TebexJsCheckoutClosedRequest**
- **TebexJsCheckoutClosedResponse**
