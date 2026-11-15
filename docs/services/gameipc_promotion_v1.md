# `lunarclient.gameipc.promotion.v1`

## Service `PromotionService`

Source: [`proto/extracted/lunarclient_gameipc_promotion_v1_service.proto`](../../proto/extracted/lunarclient_gameipc_promotion_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `CheckPendingPromotion` | `lunarclient.gameipc.promotion.v1.CheckPendingPromotionRequest` | `lunarclient.gameipc.promotion.v1.CheckPendingPromotionResponse` |
| `PlayPromotion` | `lunarclient.gameipc.promotion.v1.PlayPromotionRequest` | `lunarclient.gameipc.promotion.v1.PlayPromotionResponse` |

## Messages

- **CheckPendingPromotionRequest**
- **CheckPendingPromotionResponse**
  - repeated `lunarclient.gameipc.promotion.v1.PromotionType` `pending_promotions` = 2
- **PlayPromotionRequest**
  - `lunarclient.gameipc.promotion.v1.PromotionType` `type` = 1
- **PlayPromotionResponse**
