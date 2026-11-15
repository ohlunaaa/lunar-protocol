# `lunarclient.websocket.friend.v1`

## Service `FriendService`

Source: [`proto/extracted/lunarclient_websocket_friend_v1_service.proto`](../../proto/extracted/lunarclient_websocket_friend_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.friend.v1.LoginRequest` | `lunarclient.websocket.friend.v1.LoginResponse` |
| `BroadcastLocationChange` | `lunarclient.websocket.friend.v1.BroadcastLocationChangeRequest` | `lunarclient.websocket.friend.v1.BroadcastLocationChangeResponse` |
| `BroadcastStatusChange` | `lunarclient.websocket.friend.v1.BroadcastStatusChangeRequest` | `lunarclient.websocket.friend.v1.BroadcastStatusChangeResponse` |
| `BroadcastServerKick` | `lunarclient.websocket.friend.v1.BroadcastServerKickRequest` | `lunarclient.websocket.friend.v1.BroadcastServerKickResponse` |
| `RemoveFriend` | `lunarclient.websocket.friend.v1.RemoveFriendRequest` | `lunarclient.websocket.friend.v1.RemoveFriendResponse` |
| `ToggleFriendRequests` | `lunarclient.websocket.friend.v1.ToggleFriendRequestsRequest` | `lunarclient.websocket.friend.v1.ToggleFriendRequestsResponse` |
| `SendFriendRequest` | `lunarclient.websocket.friend.v1.SendFriendRequestRequest` | `lunarclient.websocket.friend.v1.SendFriendRequestResponse` |
| `CancelFriendRequest` | `lunarclient.websocket.friend.v1.CancelFriendRequestRequest` | `lunarclient.websocket.friend.v1.CancelFriendRequestResponse` |
| `AcceptFriendRequest` | `lunarclient.websocket.friend.v1.AcceptFriendRequestRequest` | `lunarclient.websocket.friend.v1.AcceptFriendRequestResponse` |
| `DenyFriendRequest` | `lunarclient.websocket.friend.v1.DenyFriendRequestRequest` | `lunarclient.websocket.friend.v1.DenyFriendRequestResponse` |
| `AddFriendPin` | `lunarclient.websocket.friend.v1.AddFriendPinRequest` | `lunarclient.websocket.friend.v1.AddFriendPinResponse` |
| `RemoveFriendPin` | `lunarclient.websocket.friend.v1.RemoveFriendPinRequest` | `lunarclient.websocket.friend.v1.RemoveFriendPinResponse` |
| `SetLastSeenVisibility` | `lunarclient.websocket.friend.v1.SetLastSeenVisibilityRequest` | `lunarclient.websocket.friend.v1.SetLastSeenVisibilityResponse` |
| `SetCountryFlagVisibility` | `lunarclient.websocket.friend.v1.SetCountryFlagVisibilityRequest` | `lunarclient.websocket.friend.v1.SetCountryFlagVisibilityResponse` |
| `SetGroupChatInvitePrivacy` | `lunarclient.websocket.friend.v1.SetGroupChatInvitePrivacyRequest` | `lunarclient.websocket.friend.v1.SetGroupChatInvitePrivacyResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - `lunarclient.websocket.friend.v1.OnlineFriendStatus` `current_status` = 1
  - repeated `lunarclient.websocket.friend.v1.OnlineFriend` `online_friends` = 11
  - repeated `lunarclient.websocket.friend.v1.OfflineFriend` `offline_friends` = 2
  - `bool` `allow_friend_requests` = 3
  - repeated `lunarclient.websocket.friend.v1.FriendRequest` `outbound_friend_add_requests` = 6
  - repeated `lunarclient.websocket.friend.v1.FriendRequest` `inbound_friend_add_requests` = 7
  - repeated `lunarclient.common.v1.Uuid` `pinned_friends` = 8
  - `lunarclient.websocket.friend.v1.LastSeenVisibility` `last_seen_visibility` = 9
  - `lunarclient.websocket.friend.v1.CountryFlagVisibility` `country_flag_visibility` = 10
  - `google.protobuf.Timestamp` `user_created_at` = 12
- **BroadcastLocationChangeRequest**
  - `lunarclient.common.v1.InboundLocation` `new_location` = 1
  - `lunarclient.websocket.friend.v1.BroadcastLocationChangeRequest.Trigger` `trigger` = 2
  - enum **Trigger**:
    - `TRIGGER_UNSPECIFIED = 0`
    - `TRIGGER_JOIN_EVENT = 1`
    - `TRIGGER_DISCONNECT_EVENT = 2`
    - `TRIGGER_HOSTED_WORLD_START = 3`
    - `TRIGGER_HOSTED_WORLD_STOP = 4`
    - `TRIGGER_SERVER_RICH_STATUS = 5`
- **BroadcastLocationChangeResponse**
  - `lunarclient.common.v1.Location` `new_location` = 1
- **BroadcastStatusChangeRequest**
  - `lunarclient.websocket.friend.v1.OnlineFriendStatus` `new_status` = 1
- **BroadcastStatusChangeResponse**
- **BroadcastServerKickRequest**
  - `string` `kick_reason` = 1
- **BroadcastServerKickResponse**
- **RemoveFriendRequest**
  - `lunarclient.common.v1.Uuid` `friend_uuid` = 1
- **RemoveFriendResponse**
- **ToggleFriendRequestsRequest**
  - `bool` `allow_friend_requests` = 1
- **ToggleFriendRequestsResponse**
- **SendFriendRequestRequest**
  - `string` `target_username` = 1
- **SendFriendRequestResponse**
  - `lunarclient.websocket.friend.v1.SendFriendRequestResponse.Status` `status` = 1
  - `lunarclient.common.v1.UuidAndUsername` `target` = 2
  - `lunarclient.common.v1.Color` `target_logo_color` = 3
  - `lunarclient.common.v1.Color` `target_plus_color` = 4
  - `string` `target_rank_name` = 5
  - `int32` `target_badge_id` = 6
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_TARGET_INVALID_USERNAME = 2`
    - `STATUS_TARGET_NOT_FOUND = 3`
    - `STATUS_TARGET_FRIEND_REQUESTS_DISABLED = 4`
    - `STATUS_TARGET_IS_SENDER = 5`
    - `STATUS_ALREADY_FRIENDS = 6`
    - `STATUS_ALREADY_HAVE_INBOUND_REQUEST = 7`
    - `STATUS_ALREADY_HAVE_OUTBOUND_REQUEST = 8`
- **CancelFriendRequestRequest**
  - `lunarclient.common.v1.Uuid` `target_uuid` = 1
- **CancelFriendRequestResponse**
- **AcceptFriendRequestRequest**
  - `lunarclient.common.v1.Uuid` `sender_uuid` = 1
- **AcceptFriendRequestResponse**
  - `lunarclient.websocket.friend.v1.AcceptFriendRequestResponse.Status` `status` = 1
  - `lunarclient.websocket.friend.v1.OfflineFriend` `offline_friend` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_YOUR_FRIEND_LIST_FULL = 2`
    - `STATUS_TARGET_FRIEND_LIST_FULL = 3`
    - `STATUS_ALREADY_FRIENDS = 4`
    - `STATUS_FRIEND_REQUEST_NOT_FOUND = 5`
- **DenyFriendRequestRequest**
  - `lunarclient.common.v1.Uuid` `sender_uuid` = 1
- **DenyFriendRequestResponse**
- **AddFriendPinRequest**
  - `lunarclient.common.v1.Uuid` `target_uuid` = 1
- **AddFriendPinResponse**
  - `lunarclient.websocket.friend.v1.AddFriendPinResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_FRIEND_ALREADY_PINNED = 2`
    - `STATUS_TARGET_IS_NOT_FRIEND = 3`
    - `STATUS_TARGET_NOT_FOUND = 4`
    - `STATUS_LIMIT_REACHED = 5`
- **RemoveFriendPinRequest**
  - `lunarclient.common.v1.Uuid` `target_uuid` = 1
- **RemoveFriendPinResponse**
  - `lunarclient.websocket.friend.v1.RemoveFriendPinResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_FRIEND_NOT_PINNED = 2`
    - `STATUS_TARGET_IS_NOT_FRIEND = 3`
    - `STATUS_TARGET_NOT_FOUND = 4`
- **SetLastSeenVisibilityRequest**
  - `lunarclient.websocket.friend.v1.LastSeenVisibility` `visibility` = 1
- **SetLastSeenVisibilityResponse**
- **SetCountryFlagVisibilityRequest**
  - `lunarclient.websocket.friend.v1.CountryFlagVisibility` `visibility` = 1
- **SetCountryFlagVisibilityResponse**
- **SetGroupChatInvitePrivacyRequest**
  - `lunarclient.websocket.friend.v1.GroupChatInvitePrivacy` `privacy` = 1
- **SetGroupChatInvitePrivacyResponse**
