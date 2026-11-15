# `lunarclient.websocket.emote.v1`

## Service `EmoteService`

Source: [`proto/extracted/lunarclient_websocket_emote_v1_service.proto`](../../proto/extracted/lunarclient_websocket_emote_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.emote.v1.LoginRequest` | `lunarclient.websocket.emote.v1.LoginResponse` |
| `UseEmote` | `lunarclient.websocket.emote.v1.UseEmoteRequest` | `lunarclient.websocket.emote.v1.UseEmoteResponse` |
| `GetJamPlayback` | `lunarclient.websocket.emote.v1.GetJamPlaybackRequest` | `lunarclient.websocket.emote.v1.GetJamPlaybackResponse` |
| `StopEmote` | `lunarclient.websocket.emote.v1.StopEmoteRequest` | `lunarclient.websocket.emote.v1.StopEmoteResponse` |
| `UpdateEquippedEmotes` | `lunarclient.websocket.emote.v1.UpdateEquippedEmotesRequest` | `lunarclient.websocket.emote.v1.UpdateEquippedEmotesResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - repeated `lunarclient.websocket.emote.v1.OwnedEmote` `owned_emotes` = 7
  - `bool` `has_all_emotes_flag` = 5
  - repeated `lunarclient.websocket.emote.v1.EquippedEmote` `equipped_emotes` = 8
  - repeated `int32` `lunar_plus_free_emote_ids` = 9
- **UseEmoteRequest**
  - `int32` `emote_id` = 1
  - `int32` `emote_metadata` = 2
  - `string` `emote_soundtrack_url` = 3
  - `int32` `emote_jam_id` = 4
- **UseEmoteResponse**
  - `lunarclient.websocket.emote.v1.UseEmoteResponse.Status` `status` = 1
  - `int32` `emote_id` = 2
  - `int32` `emote_metadata` = 3
  - `string` `emote_soundtrack_url` = 4
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_EMOTE_NOT_OWNED = 2`
    - `STATUS_ILLEGAL_SOUNDTRACK = 3`
    - `STATUS_RATE_LIMITED = 4`
- **GetJamPlaybackRequest**
  - `int32` `jam_id` = 1
- **GetJamPlaybackResponse**
  - `string` `url` = 1
  - `google.protobuf.Timestamp` `expires_at` = 2
- **StopEmoteRequest**
- **StopEmoteResponse**
- **UpdateEquippedEmotesRequest**
  - repeated `lunarclient.websocket.emote.v1.EquippedEmote` `equipped_emotes` = 2
- **UpdateEquippedEmotesResponse**
