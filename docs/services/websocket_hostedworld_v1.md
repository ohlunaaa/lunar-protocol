# `lunarclient.websocket.hostedworld.v1`

## Service `HostedWorldService`

Source: [`proto/extracted/lunarclient_websocket_hostedworld_v1_service.proto`](../../proto/extracted/lunarclient_websocket_hostedworld_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.hostedworld.v1.LoginRequest` | `lunarclient.websocket.hostedworld.v1.LoginResponse` |
| `StartHostingWorld` | `lunarclient.websocket.hostedworld.v1.StartHostingWorldRequest` | `lunarclient.websocket.hostedworld.v1.StartHostingWorldResponse` |
| `StopHostingWorld` | `lunarclient.websocket.hostedworld.v1.StopHostingWorldRequest` | `lunarclient.websocket.hostedworld.v1.StopHostingWorldResponse` |
| `HostedWorldHeartbeat` | `lunarclient.websocket.hostedworld.v1.HostedWorldHeartbeatRequest` | `lunarclient.websocket.hostedworld.v1.HostedWorldHeartbeatResponse` |
| `ListHostedWorlds` | `lunarclient.websocket.hostedworld.v1.ListHostedWorldsRequest` | `lunarclient.websocket.hostedworld.v1.ListHostedWorldsResponse` |
| `PreJoinHostedWorld` | `lunarclient.websocket.hostedworld.v1.PreJoinHostedWorldRequest` | `lunarclient.websocket.hostedworld.v1.PreJoinHostedWorldResponse` |
| `JoinHostedWorld` | `lunarclient.websocket.hostedworld.v1.JoinHostedWorldRequest` | `lunarclient.websocket.hostedworld.v1.JoinHostedWorldResponse` |
| `ConfirmHostedWorldJoin` | `lunarclient.websocket.hostedworld.v1.ConfirmHostedWorldJoinRequest` | `lunarclient.websocket.hostedworld.v1.ConfirmHostedWorldJoinResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - `bool` `hosting_enabled` = 1
  - `bool` `joining_enabled` = 2
  - `int32` `max_world_player_count` = 3
  - repeated `lunarclient.websocket.hostedworld.v1.AddressAndPort` `ping_requests` = 4
  - `int32` `multiplayer_refresh_interval_seconds` = 5
- **StartHostingWorldRequest**
  - `lunarclient.websocket.hostedworld.v1.Heartbeat` `heartbeat` = 1
- **StartHostingWorldResponse**
  - `lunarclient.websocket.hostedworld.v1.StartHostingWorldResponse.Status` `status` = 1
  - `string` `join_ip` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_ALREADY_HOSTING_WORLD = 2`
    - `STATUS_HOSTING_DISABLED = 3`
- **StopHostingWorldRequest**
- **StopHostingWorldResponse**
  - `lunarclient.websocket.hostedworld.v1.StopHostingWorldResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_HOSTING_WORLD = 2`
- **HostedWorldHeartbeatRequest**
  - `lunarclient.websocket.hostedworld.v1.Heartbeat` `heartbeat` = 1
- **HostedWorldHeartbeatResponse**
  - `lunarclient.websocket.hostedworld.v1.HostedWorldHeartbeatResponse.Status` `status` = 1
  - repeated `lunarclient.websocket.hostedworld.v1.AddressAndPort` `relays_to_ping` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_HOSTING_WORLD = 2`
- **ListHostedWorldsRequest**
- **ListHostedWorldsResponse**
  - repeated `lunarclient.websocket.hostedworld.v1.ListHostedWorldsResponse.HostedWorld` `hosted_worlds` = 1
  - **HostedWorld**
    - `lunarclient.common.v1.UuidAndUsername` `host` = 1
    - `lunarclient.common.v1.MinecraftVersion` `minecraft_version` = 2
    - `lunarclient.websocket.hostedworld.v1.Joinability` `joinability` = 3
    - `int32` `online_players` = 4
    - `int32` `max_players` = 5
    - repeated `lunarclient.common.v1.UuidAndUsername` `sample_players` = 6
    - `bool` `lunar_plus_boost` = 7
    - `lunarclient.common.v1.Color` `logo_color` = 8
    - `lunarclient.common.v1.Color` `plus_color` = 9
- **JoinHostedWorldRequest**
  - `lunarclient.common.v1.Uuid` `world_host_uuid` = 1
  - repeated `lunarclient.websocket.hostedworld.v1.PingResponse` `ping_responses` = 2
  - `lunarclient.websocket.hostedworld.v1.JoinHostedWorldRequest.Source` `source` = 3
  - enum **Source**:
    - `SOURCE_UNSPECIFIED = 0`
    - `SOURCE_FRIEND_CHAT_BOX = 1`
    - `SOURCE_FRIEND_LIST_INLINE = 2`
    - `SOURCE_FRIEND_LIST_RIGHT_CLICK = 3`
    - `SOURCE_MULTIPLAYER_SERVER = 4`
- **PreJoinHostedWorldRequest**
- **PreJoinHostedWorldResponse**
  - repeated `lunarclient.websocket.hostedworld.v1.AddressAndPort` `relays_to_ping` = 1
- **JoinHostedWorldResponse**
  - `lunarclient.websocket.hostedworld.v1.JoinHostedWorldResponse.Status` `status` = 1
  - `lunarclient.websocket.hostedworld.v1.AddressAndPort` `relay` = 2
  - `lunarclient.websocket.hostedworld.v1.Joinability` `joinability` = 3
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NO_ACCESS = 2`
    - `STATUS_NOT_JOINABLE = 3`
    - `STATUS_JOINING_DISABLED = 4`
    - `STATUS_NO_RELAY = 5`
- **ConfirmHostedWorldJoinRequest**
  - `lunarclient.common.v1.Uuid` `world_host_uuid` = 1
- **ConfirmHostedWorldJoinResponse**
