# `lunarclient.websocket.spray.v1`

## Service `SprayService`

Source: [`proto/extracted/lunarclient_websocket_spray_v1_service.proto`](../../proto/extracted/lunarclient_websocket_spray_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.spray.v1.LoginRequest` | `lunarclient.websocket.spray.v1.LoginResponse` |
| `UseSpray` | `lunarclient.websocket.spray.v1.UseSprayRequest` | `lunarclient.websocket.spray.v1.UseSprayResponse` |
| `RemoveSpray` | `lunarclient.websocket.spray.v1.RemoveSprayRequest` | `lunarclient.websocket.spray.v1.RemoveSprayResponse` |
| `UpdateEquippedSprays` | `lunarclient.websocket.spray.v1.UpdateEquippedSpraysRequest` | `lunarclient.websocket.spray.v1.UpdateEquippedSpraysResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - repeated `lunarclient.websocket.spray.v1.OwnedSpray` `owned_sprays` = 1
  - repeated `lunarclient.websocket.spray.v1.EquippedSpray` `equipped_sprays` = 2
  - `bool` `has_all_sprays_flag` = 4
  - `int32` `max_active_sprays` = 5
  - repeated `int32` `lunar_plus_free_spray_ids` = 6
- **UseSprayRequest**
  - `int32` `spray_id` = 1
  - `lunarclient.common.v1.Vector3f` `pos` = 2
  - `lunarclient.common.v1.Direction` `facing` = 3
  - `float` `rotation` = 4
- **UseSprayResponse**
  - `lunarclient.websocket.spray.v1.UseSprayResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_SPRAY_NOT_OWNED = 2`
- **RemoveSprayRequest**
  - `lunarclient.common.v1.Vector3f` `pos` = 1
- **RemoveSprayResponse**
- **UpdateEquippedSpraysRequest**
  - repeated `lunarclient.websocket.spray.v1.EquippedSpray` `equipped_sprays` = 1
- **UpdateEquippedSpraysResponse**
