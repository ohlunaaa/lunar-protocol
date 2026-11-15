# `lunarclient.websocket.server.v1`

## Service `ServerService`

Source: [`proto/extracted/lunarclient_websocket_server_v1_service.proto`](../../proto/extracted/lunarclient_websocket_server_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `GetPlayerCounts` | `lunarclient.websocket.server.v1.GetPlayerCountsRequest` | `lunarclient.websocket.server.v1.GetPlayerCountsResponse` |
| `CheckServerRecommendations` | `lunarclient.websocket.server.v1.CheckServerRecommendationsRequest` | `lunarclient.websocket.server.v1.CheckServerRecommendationsResponse` |
| `GetServerRecommendations` | `lunarclient.websocket.server.v1.GetServerRecommendationsRequest` | `lunarclient.websocket.server.v1.GetServerRecommendationsResponse` |
| `CheckAuthorizedFeatures` | `lunarclient.websocket.server.v1.CheckAuthorizedFeaturesRequest` | `lunarclient.websocket.server.v1.CheckAuthorizedFeaturesResponse` |

## Messages

- **GetPlayerCountsRequest**
  - repeated `string` `server_ids` = 1
- **GetPlayerCountsResponse**
  - repeated `lunarclient.websocket.server.v1.GetPlayerCountsResponse.Server` `servers` = 1
  - **Server**
    - `string` `server_id` = 1
    - `lunarclient.websocket.server.v1.GetPlayerCountsResponse.Server.Status` `status` = 2
    - `int32` `online_count` = 3
    - `int32` `max_count` = 4
    - enum **Status**:
      - `STATUS_UNSPECIFIED = 0`
      - `STATUS_ONLINE = 1`
      - `STATUS_OFFLINE = 2`
- **CheckServerRecommendationsRequest**
  - `string` `server_ip` = 1
- **CheckServerRecommendationsResponse**
  - `lunarclient.websocket.server.v1.ServerRecommendations` `recommendations` = 1
- **GetServerRecommendationsRequest**
- **GetServerRecommendationsResponse**
  - repeated `lunarclient.websocket.server.v1.ServerRecommendations` `recommendations` = 1
- **CheckAuthorizedFeaturesRequest**
  - `string` `server_ip` = 1
- **CheckAuthorizedFeaturesResponse**
  - repeated `string` `scopes` = 1
  - repeated `int32` `associated_cosmetic_ids` = 2
  - repeated `int32` `associated_emote_ids` = 3
  - repeated `int32` `associated_spray_ids` = 4
