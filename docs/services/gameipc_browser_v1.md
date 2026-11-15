# `lunarclient.gameipc.browser.v1`

## Service `BrowserService`

Source: [`proto/extracted/lunarclient_gameipc_browser_v1_service.proto`](../../proto/extracted/lunarclient_gameipc_browser_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `OpenUrl` | `lunarclient.gameipc.browser.v1.OpenUrlRequest` | `lunarclient.gameipc.browser.v1.OpenUrlResponse` |

## Messages

- **OpenUrlRequest**
  - `string` `url` = 1
  - `lunarclient.gameipc.browser.v1.OpenUrlRequest.Initiator` `initiator` = 2
  - `lunarclient.gameipc.browser.v1.OpenUrlRequest.OpenType` `open_type` = 3
  - enum **Initiator**:
    - `INITIATOR_UNSPECIFIED = 0`
    - `INITIATOR_COSMETICS = 1`
    - `INITIATOR_ALERT = 2`
    - `INITIATOR_AUTH = 3`
    - `INITIATOR_BLOG = 4`
    - `INITIATOR_SOCIAL_LINK = 5`
    - `INITIATOR_HOME_BUTTON = 6`
    - `INITIATOR_LINK_CONFIRM = 7`
    - `INITIATOR_SCREENSHOT_UPLOAD = 8`
    - `INITIATOR_HOME_CTA = 9`
    - `INITIATOR_STORE_PREVIEW = 10`
  - enum **OpenType**:
    - `OPEN_TYPE_UNSPECIFIED = 0`
    - `OPEN_TYPE_FORCE_EMBEDDED = 1`
    - `OPEN_TYPE_FORCE_EXTERNAL = 2`
- **OpenUrlResponse**
