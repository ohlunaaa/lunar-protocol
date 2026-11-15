# `lunarclient.websocket.badge.v1`

## Service `BadgeService`

Source: [`proto/extracted/lunarclient_websocket_badge_v1_service.proto`](../../proto/extracted/lunarclient_websocket_badge_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.badge.v1.LoginRequest` | `lunarclient.websocket.badge.v1.LoginResponse` |
| `EquipBadge` | `lunarclient.websocket.badge.v1.EquipBadgeRequest` | `lunarclient.websocket.badge.v1.EquipBadgeResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - repeated `lunarclient.websocket.badge.v1.OwnedBadge` `owned_badges` = 1
  - `int32` `equipped_badge_id` = 2
  - `bool` `has_all_badges_flag` = 3
- **EquipBadgeRequest**
  - `int32` `badge_id` = 1
- **EquipBadgeResponse**
