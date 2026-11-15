# `lunarclient.websocket.wrapped.v1`

## Service `WrappedService`

Source: [`proto/extracted/lunarclient_websocket_wrapped_v1_service.proto`](../../proto/extracted/lunarclient_websocket_wrapped_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.wrapped.v1.LoginRequest` | `lunarclient.websocket.wrapped.v1.LoginResponse` |
| `RecordCounters` | `lunarclient.websocket.wrapped.v1.RecordCountersRequest` | `lunarclient.websocket.wrapped.v1.RecordCountersResponse` |
| `SetLeaderboardVisibility` | `lunarclient.websocket.wrapped.v1.SetLeaderboardVisibilityRequest` | `lunarclient.websocket.wrapped.v1.SetLeaderboardVisibilityResponse` |

## Messages

- **RecordCountersRequest**
  - repeated `lunarclient.websocket.wrapped.v1.CounterUpdate` `updates` = 1
- **RecordCountersResponse**
- **LoginRequest**
- **LoginResponse**
  - `lunarclient.websocket.wrapped.v1.WrappedLeaderboardVisibility` `leaderboard_visibility` = 1
- **SetLeaderboardVisibilityRequest**
  - `lunarclient.websocket.wrapped.v1.WrappedLeaderboardVisibility` `leaderboard_visibility` = 1
- **SetLeaderboardVisibilityResponse**
