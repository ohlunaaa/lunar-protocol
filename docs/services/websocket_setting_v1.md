# `lunarclient.websocket.setting.v1`

## Service `SettingService`

Source: [`proto/extracted/lunarclient_websocket_setting_v1_service.proto`](../../proto/extracted/lunarclient_websocket_setting_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `UpdateLauncherSetting` | `lunarclient.websocket.setting.v1.UpdateLauncherSettingRequest` | `lunarclient.websocket.setting.v1.UpdateLauncherSettingResponse` |
| `UpdateClientSetting` | `lunarclient.websocket.setting.v1.UpdateClientSettingRequest` | `lunarclient.websocket.setting.v1.UpdateClientSettingResponse` |

## Messages

- **UpdateLauncherSettingRequest**
  - `lunarclient.websocket.setting.v1.LauncherSetting` `setting` = 1
  - `lunarclient.websocket.setting.v1.UpdateLauncherSettingRequest.Initiator` `initiator` = 2
  - enum **Initiator**:
    - `INITIATOR_UNSPECIFIED = 0`
    - `INITIATOR_RESET = 1`
    - `INITIATOR_SET = 2`
- **UpdateLauncherSettingResponse**
- **UpdateClientSettingRequest**
  - `lunarclient.websocket.setting.v1.ClientSetting` `setting` = 1
  - `lunarclient.websocket.setting.v1.UpdateClientSettingRequest.Initiator` `initiator` = 2
  - enum **Initiator**:
    - `INITIATOR_UNSPECIFIED = 0`
    - `INITIATOR_RESET = 1`
    - `INITIATOR_SET = 2`
- **UpdateClientSettingResponse**
