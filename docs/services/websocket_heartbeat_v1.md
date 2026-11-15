# `lunarclient.websocket.heartbeat.v1`

## Service `HeartbeatService`

Source: [`proto/extracted/lunarclient_websocket_heartbeat_v1_service.proto`](../../proto/extracted/lunarclient_websocket_heartbeat_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `LauncherHeartbeat` | `lunarclient.websocket.heartbeat.v1.LauncherHeartbeatRequest` | `lunarclient.websocket.heartbeat.v1.LauncherHeartbeatResponse` |
| `GameHeartbeat` | `lunarclient.websocket.heartbeat.v1.GameHeartbeatRequest` | `lunarclient.websocket.heartbeat.v1.GameHeartbeatResponse` |

## Messages

- **LauncherHeartbeatRequest**
  - repeated `lunarclient.websocket.heartbeat.v1.RunningInstance` `running_instances` = 3
  - repeated `lunarclient.websocket.heartbeat.v1.OpenRenderer` `open_renderers` = 4
  - `bool` `badlion_connected` = 5
- **LauncherHeartbeatResponse**
  - `lunarclient.websocket.heartbeat.v1.OnlineCounts` `online_counts` = 1
- **GameHeartbeatRequest**
  - **ModsEntry**
    - `string` `key` = 1
    - `bool` `value` = 2
- **GameHeartbeatResponse**
