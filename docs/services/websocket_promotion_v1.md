# `lunarclient.websocket.promotion.v1`

## Service `PromotionService`

Source: [`proto/extracted/lunarclient_websocket_promotion_v1_service.proto`](../../proto/extracted/lunarclient_websocket_promotion_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.promotion.v1.LoginRequest` | `lunarclient.websocket.promotion.v1.LoginResponse` |
| `StartPromotionView` | `lunarclient.websocket.promotion.v1.StartPromotionViewRequest` | `lunarclient.websocket.promotion.v1.StartPromotionViewResponse` |
| `EndPromotionView` | `lunarclient.websocket.promotion.v1.EndPromotionViewRequest` | `lunarclient.websocket.promotion.v1.EndPromotionViewResponse` |
| `ClaimOutplayedReward` | `lunarclient.websocket.promotion.v1.ClaimOutplayedRewardRequest` | `lunarclient.websocket.promotion.v1.ClaimOutplayedRewardResponse` |
| `ClaimRewindPuzzleReward` | `lunarclient.websocket.promotion.v1.ClaimRewindPuzzleRewardRequest` | `lunarclient.websocket.promotion.v1.ClaimRewindPuzzleRewardResponse` |
| `ClaimPendingReward` | `lunarclient.websocket.promotion.v1.ClaimPendingRewardRequest` | `lunarclient.websocket.promotion.v1.ClaimPendingRewardResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - `bool` `show_ads` = 2
  - `lunarclient.websocket.promotion.v1.LoginResponse.OutplayedPromotionState` `outplayed_promotion_state` = 3
  - repeated `lunarclient.websocket.promotion.v1.PendingReward` `pending_rewards` = 4
  - `lunarclient.websocket.promotion.v1.LoginResponse.MedalPromotionState` `medal_promotion_state` = 5
  - enum **OutplayedPromotionState**:
    - `OUTPLAYED_PROMOTION_STATE_UNSPECIFIED = 0`
    - `OUTPLAYED_PROMOTION_STATE_UNAVAILABLE = 1`
    - `OUTPLAYED_PROMOTION_STATE_AVAILABLE = 2`
    - `OUTPLAYED_PROMOTION_STATE_CLAIMED = 3`
  - enum **MedalPromotionState**:
    - `MEDAL_PROMOTION_STATE_UNSPECIFIED = 0`
    - `MEDAL_PROMOTION_STATE_UNAVAILABLE = 1`
    - `MEDAL_PROMOTION_STATE_AVAILABLE = 2`
    - `MEDAL_PROMOTION_STATE_CLAIMED = 3`
- **StartPromotionViewRequest**
  - `string` `promotion_id` = 1
- **StartPromotionViewResponse**
- **EndPromotionViewRequest**
  - `string` `promotion_id` = 1
  - `bool` `completed` = 2
- **EndPromotionViewResponse**
  - repeated `lunarclient.websocket.promotion.v1.PromotionReward` `rewards` = 1
- **ClaimOutplayedRewardRequest**
  - `lunarclient.websocket.promotion.v1.ClaimOutplayedRewardRequest.Initiator` `initiator` = 1
  - enum **Initiator**:
    - `INITIATOR_UNSPECIFIED = 0`
    - `INITIATOR_TOPBAR = 1`
    - `INITIATOR_SIDEBAR = 2`
    - `INITIATOR_HOME_BLOG_POST = 3`
    - `INITIATOR_ANNOUNCEMENT = 4`
    - `INITIATOR_HOME_CAROUSEL_CTA = 5`
    - `INITIATOR_GAME_HOME_CTA = 6`
- **ClaimOutplayedRewardResponse**
  - `lunarclient.websocket.promotion.v1.ClaimOutplayedRewardResponse.Result` `result` = 1
  - enum **Result**:
    - `RESULT_UNSPECIFIED = 0`
    - `RESULT_SUCCESS = 1`
    - `RESULT_PLAYER_ALREADY_CLAIMED = 2`
    - `RESULT_OUTPLAYED_INSTALL_ALREADY_CLAIMED = 3`
    - `RESULT_NOT_WINDOWS = 4`
    - `RESULT_OUTPLAYED_NOT_INSTALLED = 5`
- **ClaimRewindPuzzleRewardRequest**
  - `string` `solution` = 1
- **ClaimRewindPuzzleRewardResponse**
  - `lunarclient.websocket.promotion.v1.ClaimRewindPuzzleRewardResponse.Result` `result` = 1
  - enum **Result**:
    - `RESULT_UNSPECIFIED = 0`
    - `RESULT_SUCCESS = 1`
    - `RESULT_INCORRECT_SOLUTION = 2`
    - `RESULT_PLAYER_ALREADY_CLAIMED = 3`
    - `RESULT_MAX_REWARDS_EXCEEDED = 4`
- **ClaimPendingRewardRequest**
  - `lunarclient.websocket.promotion.v1.ClaimPendingRewardRequest.Initiator` `initiator` = 1
  - `lunarclient.websocket.promotion.v1.PendingRewardType` `type` = 2
  - `lunarclient.websocket.promotion.v1.PromotionReward` `reward` = 3
  - enum **Initiator**:
    - `INITIATOR_UNSPECIFIED = 0`
    - `INITIATOR_GAME_HOME = 1`
- **ClaimPendingRewardResponse**
  - `lunarclient.websocket.promotion.v1.ClaimPendingRewardResponse.Result` `result` = 1
  - enum **Result**:
    - `RESULT_UNSPECIFIED = 0`
    - `RESULT_SUCCESS = 1`
    - `RESULT_PLAYER_ALREADY_OWNED = 2`
    - `RESULT_PLAYER_ALREADY_CLAIMED = 3`
