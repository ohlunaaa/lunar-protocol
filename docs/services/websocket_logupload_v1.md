# `lunarclient.websocket.logupload.v1`

## Service `LogUploadService`

Source: [`proto/extracted/lunarclient_websocket_logupload_v1_service.proto`](../../proto/extracted/lunarclient_websocket_logupload_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `StartLogUpload` | `lunarclient.websocket.logupload.v1.StartLogUploadRequest` | `lunarclient.websocket.logupload.v1.StartLogUploadResponse` |
| `CompleteLogUpload` | `lunarclient.websocket.logupload.v1.CompleteLogUploadRequest` | `lunarclient.websocket.logupload.v1.CompleteLogUploadResponse` |

## Messages

- **StartLogUploadRequest**
  - repeated `lunarclient.websocket.logupload.v1.StartLogUploadRequest.File` `files` = 1
  - `string` `sentry_crash_id` = 2
  - `string` `solution_id` = 3
  - **File**
    - `string` `name` = 1
- **StartLogUploadResponse**
  - repeated `lunarclient.websocket.logupload.v1.StartLogUploadResponse.File` `files` = 1
  - `string` `upload_id` = 2
  - `lunarclient.websocket.logupload.v1.StartLogUploadResponse.Status` `status` = 3
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_SUCCESS = 1`
    - `STATUS_NOT_ALLOWED = 2`
  - **File**
    - `string` `name` = 1
    - `string` `upload_url` = 2
- **CompleteLogUploadRequest**
  - `string` `upload_id` = 1
- **CompleteLogUploadResponse**
