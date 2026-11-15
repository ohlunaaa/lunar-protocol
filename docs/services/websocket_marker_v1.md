# `lunarclient.websocket.marker.v1`

## Service `MarkerService`

Source: [`proto/extracted/lunarclient_websocket_marker_v1_service.proto`](../../proto/extracted/lunarclient_websocket_marker_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `BroadcastNewMarker` | `lunarclient.websocket.marker.v1.BroadcastNewMarkerRequest` | `lunarclient.websocket.marker.v1.BroadcastNewMarkerResponse` |

## Messages

- **BroadcastNewMarkerRequest**
  - `lunarclient.websocket.marker.v1.Marker` `marker` = 1
  - repeated `lunarclient.common.v1.Uuid` `receiver_uuids` = 2
- **BroadcastNewMarkerResponse**
