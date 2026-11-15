# `lunarclient.websocket.screenshot.v1`

## Service `ScreenshotService`

Source: [`proto/extracted/lunarclient_websocket_screenshot_v1_service.proto`](../../proto/extracted/lunarclient_websocket_screenshot_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.screenshot.v1.LoginRequest` | `lunarclient.websocket.screenshot.v1.LoginResponse` |
| `RecordScreenshot` | `lunarclient.websocket.screenshot.v1.RecordScreenshotRequest` | `lunarclient.websocket.screenshot.v1.RecordScreenshotResponse` |
| `SetDefaultUploadPrivacy` | `lunarclient.websocket.screenshot.v1.SetDefaultUploadPrivacyRequest` | `lunarclient.websocket.screenshot.v1.SetDefaultUploadPrivacyResponse` |

## Messages

- **RecordScreenshotRequest**
  - `lunarclient.websocket.screenshot.v1.ScreenshotMessage` `screenshot` = 1
- **RecordScreenshotResponse**
- **LoginRequest**
- **LoginResponse**
  - `lunarclient.websocket.screenshot.v1.ScreenshotPrivacy` `default_upload_privacy` = 1
- **SetDefaultUploadPrivacyRequest**
  - `lunarclient.websocket.screenshot.v1.ScreenshotPrivacy` `default_upload_privacy` = 1
- **SetDefaultUploadPrivacyResponse**
