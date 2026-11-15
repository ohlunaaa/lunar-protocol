# `lunarclient.websocket.liveexperience.v1`

## Service `LiveExperienceService`

Source: [`proto/extracted/lunarclient_websocket_liveexperience_v1_service.proto`](../../proto/extracted/lunarclient_websocket_liveexperience_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `LoadLiveExperience` | `lunarclient.websocket.liveexperience.v1.LoadLiveExperienceRequest` | `lunarclient.websocket.liveexperience.v1.LoadLiveExperienceResponse` |
| `JoinLiveExperience` | `lunarclient.websocket.liveexperience.v1.JoinLiveExperienceRequest` | `lunarclient.websocket.liveexperience.v1.JoinLiveExperienceResponse` |

## Messages

- **LoadLiveExperienceRequest**
- **LoadLiveExperienceResponse**
  - `lunarclient.websocket.liveexperience.v1.LiveExperience` `experience` = 1
- **JoinLiveExperienceRequest**
  - `string` `experience_id` = 1
- **JoinLiveExperienceResponse**
