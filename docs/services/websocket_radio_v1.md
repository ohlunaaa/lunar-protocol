# `lunarclient.websocket.radio.v1`

## Service `RadioService`

Source: [`proto/extracted/lunarclient_websocket_radio_v1_service.proto`](../../proto/extracted/lunarclient_websocket_radio_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.radio.v1.LoginRequest` | `lunarclient.websocket.radio.v1.LoginResponse` |
| `BroadcastRadioInfoChange` | `lunarclient.websocket.radio.v1.BroadcastRadioInfoChangeRequest` | `lunarclient.websocket.radio.v1.BroadcastRadioInfoChangeResponse` |
| `SetRadioPlayingVisibility` | `lunarclient.websocket.radio.v1.SetRadioPlayingVisibilityRequest` | `lunarclient.websocket.radio.v1.SetRadioPlayingVisibilityResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - `bool` `is_premium` = 1
  - `lunarclient.websocket.radio.v1.RadioPlayingVisibility` `radio_playing_visibility` = 2
- **SetRadioPlayingVisibilityRequest**
  - `lunarclient.websocket.radio.v1.RadioPlayingVisibility` `visibility` = 1
- **SetRadioPlayingVisibilityResponse**
- **BroadcastRadioInfoChangeRequest**
  - `lunarclient.websocket.radio.v1.InboundRadioInfo` `new_radio_info` = 1
  - `lunarclient.websocket.radio.v1.BroadcastRadioInfoChangeRequest.InfoChangeInitiator` `initiator` = 2
  - `lunarclient.websocket.radio.v1.BroadcastRadioInfoChangeRequest.InfoChangeInitiatorSource` `initiator_source` = 3
  - enum **InfoChangeInitiator**:
    - `INFO_CHANGE_INITIATOR_UNSPECIFIED = 0`
    - `INFO_CHANGE_INITIATOR_STOP = 1`
    - `INFO_CHANGE_INITIATOR_SKIP = 2`
    - `INFO_CHANGE_INITIATOR_NEXT_TRACK = 3`
    - `INFO_CHANGE_INITIATOR_START_STATION = 4`
    - `INFO_CHANGE_INITIATOR_STATION_COMPLETE = 5`
    - `INFO_CHANGE_INITIATOR_TRACK_PLAY_PAUSE = 6`
    - `INFO_CHANGE_INITIATOR_TRACK_LIKE_TOGGLE = 7`
    - `INFO_CHANGE_INITIATOR_STATION_LIKE_TOGGLE = 8`
    - `INFO_CHANGE_INITIATOR_STATION_LOOP = 9`
    - `INFO_CHANGE_INITIATOR_STATION_AUTO_START = 10`
    - `INFO_CHANGE_INITIATOR_STATION_AUTO_START_RANDOM = 11`
    - `INFO_CHANGE_INITIATOR_START_STATION_RANDOM = 12`
    - `INFO_CHANGE_INITIATOR_INACTIVE = 13`
  - enum **InfoChangeInitiatorSource**:
    - `INFO_CHANGE_INITIATOR_SOURCE_UNSPECIFIED = 0`
    - `INFO_CHANGE_INITIATOR_SOURCE_GAME = 1`
    - `INFO_CHANGE_INITIATOR_SOURCE_LAUNCHER = 2`
- **BroadcastRadioInfoChangeResponse**
  - `lunarclient.common.v1.RadioInfo` `new_radio_info` = 1
