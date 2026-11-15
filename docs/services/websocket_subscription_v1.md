# `lunarclient.websocket.subscription.v1`

## Service `SubscriptionService`

Source: [`proto/extracted/lunarclient_websocket_subscription_v1_service.proto`](../../proto/extracted/lunarclient_websocket_subscription_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `SubscribeV2` | `lunarclient.websocket.subscription.v1.SubscribeV2Request` | `lunarclient.websocket.subscription.v1.SubscribeV2Response` |
| `Unsubscribe` | `lunarclient.websocket.subscription.v1.UnsubscribeRequest` | `lunarclient.websocket.subscription.v1.UnsubscribeResponse` |

## Messages

- **SubscribeV2Request**
  - repeated `lunarclient.common.v1.Uuid` `target_uuids` = 1
- **SubscribeV2Response**
  - repeated `lunarclient.websocket.cosmetic.v2.PlayerCosmeticsPushV2` `cosmetic_pushes` = 1
  - repeated `lunarclient.websocket.radio.v1.PlayerRadioPush` `radio_pushes` = 2
- **UnsubscribeRequest**
  - repeated `lunarclient.common.v1.Uuid` `target_uuids` = 1
- **UnsubscribeResponse**
