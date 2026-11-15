# `lunarclient.websocket.analytics.v1`

## Service `AnalyticsService`

Source: [`proto/extracted/lunarclient_websocket_analytics_v1_service.proto`](../../proto/extracted/lunarclient_websocket_analytics_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `RecordCounters` | `lunarclient.websocket.analytics.v1.RecordCountersRequest` | `lunarclient.websocket.analytics.v1.RecordCountersResponse` |
| `RecordPinnedServerInteraction` | `lunarclient.websocket.analytics.v1.RecordPinnedServerInteractionRequest` | `lunarclient.websocket.analytics.v1.RecordPinnedServerInteractionResponse` |
| `RecordEnabledMods` | `lunarclient.websocket.analytics.v1.RecordEnabledModsRequest` | `lunarclient.websocket.analytics.v1.RecordEnabledModsResponse` |

## Messages

- **RecordCountersRequest**
  - repeated `lunarclient.websocket.analytics.v1.CounterUpdate` `updates` = 1
- **RecordCountersResponse**
- **RecordPinnedServerInteractionRequest**
  - `string` `server_ip` = 1
  - `lunarclient.websocket.analytics.v1.RecordPinnedServerInteractionRequest.InteractionType` `interaction_type` = 2
  - enum **InteractionType**:
    - `INTERACTION_TYPE_UNSPECIFIED = 0`
    - `INTERACTION_TYPE_HOVER = 1`
    - `INTERACTION_TYPE_PLAY = 2`
- **RecordPinnedServerInteractionResponse**
- **RecordEnabledModsRequest**
  - repeated `lunarclient.websocket.analytics.v1.RecordEnabledModsRequest.ModsEntry` `mods` = 1
  - **ModsEntry**
    - `string` `key` = 1
    - `bool` `value` = 2
- **RecordEnabledModsResponse**
