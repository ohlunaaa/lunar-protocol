# `lunarclient.gameipc.location.v1`

## Service `LocationService`

Source: [`proto/extracted/lunarclient_gameipc_location_v1_service.proto`](../../proto/extracted/lunarclient_gameipc_location_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `UpdateFocus` | `lunarclient.gameipc.location.v1.UpdateFocusRequest` | `lunarclient.gameipc.location.v1.UpdateFocusResponse` |
| `UpdateLocation` | `lunarclient.gameipc.location.v1.UpdateLocationRequest` | `lunarclient.gameipc.location.v1.UpdateLocationResponse` |

## Messages

- **UpdateLocationRequest**
  - `lunarclient.common.v1.Location` `location` = 1
  - `lunarclient.common.v1.InboundLocation` `inbound_location` = 2
- **UpdateLocationResponse**
- **UpdateFocusRequest**
  - `bool` `focused` = 1
- **UpdateFocusResponse**
