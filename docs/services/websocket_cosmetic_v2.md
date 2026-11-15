# `lunarclient.websocket.cosmetic.v2`

## Service `CosmeticService`

Source: [`proto/extracted/lunarclient_websocket_cosmetic_v2_service.proto`](../../proto/extracted/lunarclient_websocket_cosmetic_v2_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.cosmetic.v2.LoginRequest` | `lunarclient.websocket.cosmetic.v2.LoginResponse` |
| `CreateOutfit` | `lunarclient.websocket.cosmetic.v2.CreateOutfitRequest` | `lunarclient.websocket.cosmetic.v2.CreateOutfitResponse` |
| `UpdateOutfit` | `lunarclient.websocket.cosmetic.v2.UpdateOutfitRequest` | `lunarclient.websocket.cosmetic.v2.UpdateOutfitResponse` |
| `DeleteOutfit` | `lunarclient.websocket.cosmetic.v2.DeleteOutfitRequest` | `lunarclient.websocket.cosmetic.v2.DeleteOutfitResponse` |
| `SelectOutfit` | `lunarclient.websocket.cosmetic.v2.SelectOutfitRequest` | `lunarclient.websocket.cosmetic.v2.SelectOutfitResponse` |
| `FavoriteCosmetic` | `lunarclient.websocket.cosmetic.v2.FavoriteCosmeticRequest` | `lunarclient.websocket.cosmetic.v2.FavoriteCosmeticResponse` |
| `UnfavoriteCosmetic` | `lunarclient.websocket.cosmetic.v2.UnfavoriteCosmeticRequest` | `lunarclient.websocket.cosmetic.v2.UnfavoriteCosmeticResponse` |
| `LoadTabLogos` | `lunarclient.websocket.cosmetic.v2.LoadTabLogosRequest` | `lunarclient.websocket.cosmetic.v2.LoadTabLogosResponse` |
| `SetCosmeticOwnershipVisibility` | `lunarclient.websocket.cosmetic.v2.SetCosmeticOwnershipVisibilityRequest` | `lunarclient.websocket.cosmetic.v2.SetCosmeticOwnershipVisibilityResponse` |
| `UpdateLunarPlusColor` | `lunarclient.websocket.cosmetic.v2.UpdateLunarPlusColorRequest` | `lunarclient.websocket.cosmetic.v2.UpdateLunarPlusColorResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - `lunarclient.common.v1.Color` `logo_color` = 1
  - `bool` `logo_always_show` = 2
  - `lunarclient.common.v1.Color` `plus_color` = 3
  - repeated `lunarclient.common.v1.Color` `available_lunar_plus_colors` = 4
  - repeated `int32` `lunar_plus_free_cosmetic_ids` = 5
  - repeated `lunarclient.websocket.cosmetic.v2.OwnedCosmetic` `owned_cosmetics` = 6
  - `bool` `has_all_cosmetics_flag` = 7
  - `string` `rank_name` = 8
  - repeated `int32` `favorite_cosmetic_ids` = 9
  - repeated `lunarclient.websocket.cosmetic.v2.Outfit` `outfits` = 10
  - `lunarclient.websocket.cosmetic.v2.OutfitTree` `outfit_tree` = 11
  - `bool` `artist_tools` = 12
  - `lunarclient.websocket.cosmetic.v2.CosmeticOwnershipVisibility` `cosmetic_ownership_visibility` = 13
  - `bool` `tester_tools` = 14
  - repeated `int32` `discord_rewards` = 15
  - repeated `int32` `discord_tag_rewards` = 16
- **CreateOutfitRequest**
  - `string` `name` = 1
- **CreateOutfitResponse**
  - `lunarclient.websocket.cosmetic.v2.CreateOutfitResponse.Status` `status` = 1
  - `lunarclient.websocket.cosmetic.v2.Outfit` `outfit` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_OUTFIT_LIMIT_REACHED = 2`
- **UpdateOutfitRequest**
  - `lunarclient.websocket.cosmetic.v2.Outfit` `outfit` = 1
- **UpdateOutfitResponse**
  - `lunarclient.websocket.cosmetic.v2.UpdateOutfitResponse.Status` `status` = 1
  - `lunarclient.websocket.cosmetic.v2.Outfit` `outfit` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
- **SelectOutfitRequest**
  - `lunarclient.websocket.cosmetic.v2.OutfitTree` `outfit_tree` = 1
- **SelectOutfitResponse**
  - `lunarclient.websocket.cosmetic.v2.SelectOutfitResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
- **DeleteOutfitRequest**
  - `lunarclient.common.v1.Uuid` `outfit_id` = 1
- **DeleteOutfitResponse**
  - `lunarclient.websocket.cosmetic.v2.DeleteOutfitResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
- **FavoriteCosmeticRequest**
  - `int32` `cosmetic_id` = 1
- **FavoriteCosmeticResponse**
- **UnfavoriteCosmeticRequest**
  - `int32` `cosmetic_id` = 1
- **UnfavoriteCosmeticResponse**
- **LoadTabLogosRequest**
  - repeated `lunarclient.common.v1.Uuid` `player_uuids` = 1
- **LoadTabLogosResponse**
  - repeated `lunarclient.websocket.cosmetic.v2.LoadTabLogosResponse.TabLogo` `tab_logos` = 1
  - **TabLogo**
    - `lunarclient.common.v1.Uuid` `player_uuid` = 1
    - `lunarclient.common.v1.Color` `logo_color` = 2
    - `lunarclient.common.v1.Color` `plus_color` = 3
    - `int32` `badge_id` = 4
- **SetCosmeticOwnershipVisibilityRequest**
  - `lunarclient.websocket.cosmetic.v2.CosmeticOwnershipVisibility` `visibility` = 1
- **SetCosmeticOwnershipVisibilityResponse**
- **UpdateLunarPlusColorRequest**
  - `lunarclient.common.v1.Color` `plus_color` = 3
- **UpdateLunarPlusColorResponse**
