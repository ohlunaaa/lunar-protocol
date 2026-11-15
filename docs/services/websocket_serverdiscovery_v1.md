# `lunarclient.websocket.serverdiscovery.v1`

## Service `ServerDiscoveryService`

Source: [`proto/extracted/lunarclient_websocket_serverdiscovery_v1_service.proto`](../../proto/extracted/lunarclient_websocket_serverdiscovery_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.serverdiscovery.v1.LoginRequest` | `lunarclient.websocket.serverdiscovery.v1.LoginResponse` |
| `DiscoverServers` | `lunarclient.websocket.serverdiscovery.v1.DiscoverServersRequest` | `lunarclient.websocket.serverdiscovery.v1.DiscoverServersResponse` |
| `SearchServers` | `lunarclient.websocket.serverdiscovery.v1.SearchServersRequest` | `lunarclient.websocket.serverdiscovery.v1.SearchServersResponse` |
| `LoadAutocompleteSuggestions` | `lunarclient.websocket.serverdiscovery.v1.LoadAutocompleteSuggestionsRequest` | `lunarclient.websocket.serverdiscovery.v1.LoadAutocompleteSuggestionsResponse` |
| `LoadServerModal` | `lunarclient.websocket.serverdiscovery.v1.LoadServerModalRequest` | `lunarclient.websocket.serverdiscovery.v1.LoadServerModalResponse` |
| `TrackSectionNotInterested` | `lunarclient.websocket.serverdiscovery.v1.TrackSectionNotInterestedRequest` | `lunarclient.websocket.serverdiscovery.v1.TrackSectionNotInterestedResponse` |
| `TrackServerJoin` | `lunarclient.websocket.serverdiscovery.v1.TrackServerJoinRequest` | `lunarclient.websocket.serverdiscovery.v1.TrackServerJoinResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - `int32` `total_servers` = 1
  - `lunarclient.websocket.serverdiscovery.v1.GlobalAnnouncement` `announcement` = 2
  - repeated `lunarclient.websocket.serverdiscovery.v1.ServerGameType` `game_types` = 3
- **DiscoverServersRequest**
- **DiscoverServersResponse**
  - repeated `lunarclient.websocket.serverdiscovery.v1.ServerSection` `sections` = 1
- **SearchServersRequest**
  - `string` `query` = 1
- **SearchServersResponse**
  - repeated `lunarclient.websocket.serverdiscovery.v1.ServerCard` `servers` = 1
- **LoadAutocompleteSuggestionsRequest**
- **LoadAutocompleteSuggestionsResponse**
  - repeated `lunarclient.websocket.serverdiscovery.v1.AutocompleteSuggestion` `suggestions` = 1
- **AutocompleteSuggestion**
  - `string` `name` = 1
  - `string` `primary_address` = 2
  - repeated `string` `addresses` = 3
- **LoadServerModalRequest**
  - `string` `server_mappings_id` = 1
- **LoadServerModalResponse**
  - `lunarclient.websocket.serverdiscovery.v1.ServerModalDetails` `details` = 1
- **TrackSectionNotInterestedRequest**
  - `string` `id` = 1
- **TrackSectionNotInterestedResponse**
- **TrackServerJoinRequest**
  - `string` `section_id` = 1
  - `string` `card_server_mappings_id` = 2
  - `string` `card_recommendation_id` = 3
- **TrackServerJoinResponse**
