# `lunarclient.websocket.legacyapi.v1`

## Service `LegacyApiService`

Source: [`proto/extracted/lunarclient_websocket_legacyapi_v1_service.proto`](../../proto/extracted/lunarclient_websocket_legacyapi_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `RecordDeprecatedApiUsage` | `lunarclient.websocket.legacyapi.v1.RecordDeprecatedApiUsageRequest` | `lunarclient.websocket.legacyapi.v1.RecordDeprecatedApiUsageResponse` |

## Messages

- **RecordDeprecatedApiUsageRequest**
  - `lunarclient.websocket.legacyapi.v1.RecordDeprecatedApiUsageRequest.Feature` `feature` = 1
  - enum **Feature**:
    - `FEATURE_UNSPECIFIED = 0`
    - `FEATURE_TRANSFER_PACKET = 1`
    - `FEATURE_BOSS_BAR = 2`
    - `FEATURE_VOICE = 3`
    - `FEATURE_COOLDOWN = 4`
    - `FEATURE_GHOST = 5`
    - `FEATURE_HOLOGRAM = 6`
    - `FEATURE_MOD_SETTINGS = 7`
    - `FEATURE_NAMETAGS = 8`
    - `FEATURE_NOTIFICATION = 9`
    - `FEATURE_SERVER_RULE = 10`
    - `FEATURE_SERVER_UPDATE = 11`
    - `FEATURE_STAFF_MOD = 12`
    - `FEATURE_TEAMMATES = 13`
    - `FEATURE_TITLE = 14`
    - `FEATURE_WORLD = 15`
    - `FEATURE_WORLD_BORDER = 16`
    - `FEATURE_WAYPOINT = 17`
    - `FEATURE_EMOTE = 18`
- **RecordDeprecatedApiUsageResponse**
