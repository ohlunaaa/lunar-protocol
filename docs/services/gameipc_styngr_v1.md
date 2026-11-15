# `lunarclient.gameipc.styngr.v1`

## Service `StyngrRadioService`

Source: [`proto/extracted/lunarclient_gameipc_styngr_v1_service.proto`](../../proto/extracted/lunarclient_gameipc_styngr_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `FetchState` | `lunarclient.gameipc.styngr.v1.FetchStateRequest` | `lunarclient.gameipc.styngr.v1.FetchStateResponse` |
| `FetchPlaylists` | `lunarclient.gameipc.styngr.v1.FetchPlaylistsRequest` | `lunarclient.gameipc.styngr.v1.FetchPlaylistsResponse` |
| `StartPlaylist` | `lunarclient.gameipc.styngr.v1.StartPlaylistRequest` | `lunarclient.gameipc.styngr.v1.StartPlaylistResponse` |
| `NextTrack` | `lunarclient.gameipc.styngr.v1.NextTrackRequest` | `lunarclient.gameipc.styngr.v1.NextTrackResponse` |
| `SetPlaying` | `lunarclient.gameipc.styngr.v1.SetPlayingRequest` | `lunarclient.gameipc.styngr.v1.SetPlayingResponse` |
| `SetMuted` | `lunarclient.gameipc.styngr.v1.SetMutedRequest` | `lunarclient.gameipc.styngr.v1.SetMutedResponse` |
| `SetVolume` | `lunarclient.gameipc.styngr.v1.SetVolumeRequest` | `lunarclient.gameipc.styngr.v1.SetVolumeResponse` |
| `ToggleLiked` | `lunarclient.gameipc.styngr.v1.ToggleLikedRequest` | `lunarclient.gameipc.styngr.v1.ToggleLikedResponse` |
| `OpenSelector` | `lunarclient.gameipc.styngr.v1.OpenSelectorRequest` | `lunarclient.gameipc.styngr.v1.OpenSelectorResponse` |

## Messages

- **FetchStateRequest**
- **FetchStateResponse**
  - `lunarclient.gameipc.styngr.v1.StyngrTrackState` `track` = 1
  - `lunarclient.gameipc.styngr.v1.StyngrControlsState` `controls` = 2
  - `lunarclient.gameipc.styngr.v1.StyngrProgressState` `progress` = 3
- **FetchPlaylistsRequest**
- **FetchPlaylistsResponse**
  - repeated `lunarclient.gameipc.styngr.v1.FetchPlaylistsResponse.Playlist` `playlists` = 1
  - `bool` `premium` = 2
  - `string` `id` = 1
  - `string` `name` = 2
  - `string` `description` = 3
  - `int32` `track_count` = 4
  - `google.protobuf.Duration` `duration` = 5
  - `lunarclient.gameipc.styngr.v1.PlaylistLicense` `license` = 6
  - `lunarclient.gameipc.styngr.v1.PlaylistMonetization` `monetization` = 7
  - **Playlist**
- **StartPlaylistRequest**
  - `lunarclient.gameipc.styngr.v1.PlaylistLicense` `playlist_type` = 1
  - `string` `playlist_id` = 2
- **StartPlaylistResponse**
- **NextTrackRequest**
- **NextTrackResponse**
- **SetPlayingRequest**
  - `bool` `playing` = 1
- **SetPlayingResponse**
- **SetMutedRequest**
  - `bool` `muted` = 1
- **SetMutedResponse**
- **SetVolumeRequest**
  - `float` `volume` = 1
- **SetVolumeResponse**
- **ToggleLikedRequest**
- **ToggleLikedResponse**
- **OpenSelectorRequest**
- **OpenSelectorResponse**
