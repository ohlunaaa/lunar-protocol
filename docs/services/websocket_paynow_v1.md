# `lunarclient.websocket.paynow.v1`

## Service `PayNowService`

Source: [`proto/extracted/lunarclient_websocket_paynow_v1_service.proto`](../../proto/extracted/lunarclient_websocket_paynow_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `PayNowCheckoutOpened` | `lunarclient.websocket.paynow.v1.PayNowCheckoutOpenedRequest` | `lunarclient.websocket.paynow.v1.PayNowCheckoutOpenedResponse` |
| `PayNowCheckoutClosed` | `lunarclient.websocket.paynow.v1.PayNowCheckoutClosedRequest` | `lunarclient.websocket.paynow.v1.PayNowCheckoutClosedResponse` |

## Messages

- **PayNowCheckoutOpenedRequest**
  - `string` `checkout_token` = 1
  - `lunarclient.websocket.paynow.v1.PayNowCheckoutOpenedRequest.Backend` `backend` = 2
  - enum **Backend**:
    - `BACKEND_UNSPECIFIED = 0`
    - `BACKEND_OVERWOLF_OVERLAY = 1`
    - `BACKEND_ELECTRON_WINDOW = 2`
- **PayNowCheckoutOpenedResponse**
- **PayNowCheckoutClosedRequest**
- **PayNowCheckoutClosedResponse**
