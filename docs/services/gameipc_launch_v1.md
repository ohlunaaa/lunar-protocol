# `lunarclient.gameipc.launch.v1`

## Service `LaunchService`

Source: [`proto/extracted/lunarclient_gameipc_launch_v1_service.proto`](../../proto/extracted/lunarclient_gameipc_launch_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `LaunchGame` | `lunarclient.gameipc.launch.v1.LaunchGameRequest` | `lunarclient.gameipc.launch.v1.LaunchGameResponse` |

## Messages

- **LaunchGameRequest**
  - `string` `version` = 1
  - `string` `module` = 2
  - `string` `auto_join_server_ip` = 3
  - `lunarclient.gameipc.launch.v1.LaunchGameRequest.LaunchSource` `launch_source` = 4
  - `lunarclient.common.v1.PlayerModpack` `modpack` = 5
  - enum **LaunchSource**:
    - `LAUNCH_SOURCE_UNSPECIFIED = 0`
    - `LAUNCH_SOURCE_MAIN_MENU_SWITCHER = 1`
    - `LAUNCH_SOURCE_SERVER_KICK_PROMPT = 2`
    - `LAUNCH_SOURCE_SERVER_MODPACK_RECOMMENDATION = 3`
- **LaunchGameResponse**
