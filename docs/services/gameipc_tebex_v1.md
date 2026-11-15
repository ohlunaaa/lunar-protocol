# `lunarclient.gameipc.tebex.v1`

## Service `TebexService`

Source: [`proto/extracted/lunarclient_gameipc_tebex_v1_service.proto`](../../proto/extracted/lunarclient_gameipc_tebex_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `OpenTebexJsCheckout` | `lunarclient.gameipc.tebex.v1.OpenTebexJsCheckoutRequest` | `lunarclient.gameipc.tebex.v1.OpenTebexJsCheckoutResponse` |
| `CheckTebexCapabilities` | `lunarclient.gameipc.tebex.v1.CheckTebexCapabilitiesRequest` | `lunarclient.gameipc.tebex.v1.CheckTebexCapabilitiesResponse` |

## Messages

- **CheckTebexCapabilitiesRequest**
- **CheckTebexCapabilitiesResponse**
  - `lunarclient.gameipc.tebex.v1.CheckTebexCapabilitiesResponse.EmbeddedCheckout` `embedded_checkout` = 1
  - enum **EmbeddedCheckout**:
    - `EMBEDDED_CHECKOUT_UNSPECIFIED = 0`
    - `EMBEDDED_CHECKOUT_OVERWOLF_OVERLAY = 1`
    - `EMBEDDED_CHECKOUT_ELECTRON_WINDOW = 2`
- **OpenTebexJsCheckoutRequest**
  - `string` `basket_ident` = 1
  - `string` `locale` = 2
- **OpenTebexJsCheckoutResponse**
  - `lunarclient.gameipc.tebex.v1.OpenTebexJsCheckoutResponse.Status` `status` = 1
  - `bool` `open_minecraft_screen` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_INTERNAL_ERROR = 2`
    - `STATUS_SERVER_NOT_ALLOWED = 3`
