# `lunarclient.gameipc.paynow.v1`

## Service `PayNowService`

Source: [`proto/extracted/lunarclient_gameipc_paynow_v1_service.proto`](../../proto/extracted/lunarclient_gameipc_paynow_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `OpenPayNowJsCheckout` | `lunarclient.gameipc.paynow.v1.OpenPayNowJsCheckoutRequest` | `lunarclient.gameipc.paynow.v1.OpenPayNowJsCheckoutResponse` |
| `CheckPayNowCapabilities` | `lunarclient.gameipc.paynow.v1.CheckPayNowCapabilitiesRequest` | `lunarclient.gameipc.paynow.v1.CheckPayNowCapabilitiesResponse` |

## Messages

- **CheckPayNowCapabilitiesRequest**
- **CheckPayNowCapabilitiesResponse**
  - `lunarclient.gameipc.paynow.v1.CheckPayNowCapabilitiesResponse.EmbeddedCheckout` `embedded_checkout` = 1
  - enum **EmbeddedCheckout**:
    - `EMBEDDED_CHECKOUT_UNSPECIFIED = 0`
    - `EMBEDDED_CHECKOUT_OVERWOLF_OVERLAY = 1`
    - `EMBEDDED_CHECKOUT_ELECTRON_WINDOW = 2`
- **OpenPayNowJsCheckoutRequest**
  - `string` `checkout_token` = 1
- **OpenPayNowJsCheckoutResponse**
  - `lunarclient.gameipc.paynow.v1.OpenPayNowJsCheckoutResponse.Status` `status` = 1
  - `bool` `open_minecraft_screen` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_INTERNAL_ERROR = 2`
    - `STATUS_SERVER_NOT_ALLOWED = 3`
