# `lunarclient.websocket.conversation.v1`

## Service `ConversationService`

Source: [`proto/extracted/lunarclient_websocket_conversation_v1_service.proto`](../../proto/extracted/lunarclient_websocket_conversation_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.conversation.v1.LoginRequest` | `lunarclient.websocket.conversation.v1.LoginResponse` |
| `SendConversationMessage` | `lunarclient.websocket.conversation.v1.SendConversationMessageRequest` | `lunarclient.websocket.conversation.v1.SendConversationMessageResponse` |
| `PreSendAction` | `lunarclient.websocket.conversation.v1.PreSendActionRequest` | `lunarclient.websocket.conversation.v1.PreSendActionResponse` |
| `LoadConversation` | `lunarclient.websocket.conversation.v1.LoadConversationRequest` | `lunarclient.websocket.conversation.v1.LoadConversationResponse` |
| `CreateConversation` | `lunarclient.websocket.conversation.v1.CreateConversationRequest` | `lunarclient.websocket.conversation.v1.CreateConversationResponse` |
| `DeleteConversation` | `lunarclient.websocket.conversation.v1.DeleteConversationRequest` | `lunarclient.websocket.conversation.v1.DeleteConversationResponse` |
| `DeleteConversationMessage` | `lunarclient.websocket.conversation.v1.DeleteConversationMessageRequest` | `lunarclient.websocket.conversation.v1.DeleteConversationMessageResponse` |
| `DeleteConversationMessageHistory` | `lunarclient.websocket.conversation.v1.DeleteConversationMessageHistoryRequest` | `lunarclient.websocket.conversation.v1.DeleteConversationMessageHistoryResponse` |
| `UpdateConversationOwner` | `lunarclient.websocket.conversation.v1.UpdateConversationOwnerRequest` | `lunarclient.websocket.conversation.v1.UpdateConversationOwnerResponse` |
| `AddConversationParticipants` | `lunarclient.websocket.conversation.v1.AddConversationParticipantsRequest` | `lunarclient.websocket.conversation.v1.AddConversationParticipantsResponse` |
| `RemoveConversationParticipant` | `lunarclient.websocket.conversation.v1.RemoveConversationParticipantRequest` | `lunarclient.websocket.conversation.v1.RemoveConversationParticipantResponse` |
| `UpdateConversationName` | `lunarclient.websocket.conversation.v1.UpdateConversationNameRequest` | `lunarclient.websocket.conversation.v1.UpdateConversationNameResponse` |
| `UpdateConversationIcon` | `lunarclient.websocket.conversation.v1.UpdateConversationIconRequest` | `lunarclient.websocket.conversation.v1.UpdateConversationIconResponse` |
| `LoadPinnedMessages` | `lunarclient.websocket.conversation.v1.LoadPinnedMessagesRequest` | `lunarclient.websocket.conversation.v1.LoadPinnedMessagesResponse` |
| `AddPinnedMessage` | `lunarclient.websocket.conversation.v1.AddPinnedMessageRequest` | `lunarclient.websocket.conversation.v1.AddPinnedMessageResponse` |
| `RemovePinnedMessage` | `lunarclient.websocket.conversation.v1.RemovePinnedMessageRequest` | `lunarclient.websocket.conversation.v1.RemovePinnedMessageResponse` |
| `SetInvitePolicy` | `lunarclient.websocket.conversation.v1.SetInvitePolicyRequest` | `lunarclient.websocket.conversation.v1.SetInvitePolicyResponse` |
| `SetNamePolicy` | `lunarclient.websocket.conversation.v1.SetNamePolicyRequest` | `lunarclient.websocket.conversation.v1.SetNamePolicyResponse` |
| `SetIconPolicy` | `lunarclient.websocket.conversation.v1.SetIconPolicyRequest` | `lunarclient.websocket.conversation.v1.SetIconPolicyResponse` |
| `SetMessagePinningPolicy` | `lunarclient.websocket.conversation.v1.SetMessagePinningPolicyRequest` | `lunarclient.websocket.conversation.v1.SetMessagePinningPolicyResponse` |
| `SetConversationPinned` | `lunarclient.websocket.conversation.v1.SetConversationPinnedRequest` | `lunarclient.websocket.conversation.v1.SetConversationPinnedResponse` |
| `GetUploadUrls` | `lunarclient.websocket.conversation.v1.GetUploadUrlsRequest` | `lunarclient.websocket.conversation.v1.GetUploadUrlsResponse` |
| `UnfocusConversations` | `lunarclient.websocket.conversation.v1.UnfocusConversationsRequest` | `lunarclient.websocket.conversation.v1.UnfocusConversationsResponse` |
| `GetConversations` | `lunarclient.websocket.conversation.v1.GetConversationsRequest` | `lunarclient.websocket.conversation.v1.GetConversationsResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - repeated `lunarclient.websocket.conversation.v1.ConversationStub` `conversations` = 1
  - `int32` `participant_limit` = 2
  - repeated `lunarclient.websocket.conversation.v1.LunarStickerPack` `sticker_packs` = 3
  - repeated `lunarclient.websocket.conversation.v1.LunarEmojiCategory` `emoji_categories` = 4
  - `int32` `total_conversations` = 5
  - `int32` `max_message_length` = 6
  - `int32` `pinned_conversation_limit` = 7
- **SendConversationMessageRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.ConversationMessageContents` `message_contents` = 2
- **SendConversationMessageResponse**
  - `lunarclient.websocket.conversation.v1.SendConversationMessageResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_UNKNOWN_CONVERSATION = 2`
    - `STATUS_INNAPPROPRIATE = 3`
    - `STATUS_EXCEEDS_LIMIT = 4`
- **PreSendActionRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.PreSendAction` `action` = 2
- **PreSendActionResponse**
  - `lunarclient.websocket.conversation.v1.PreSendActionResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_UNKNOWN_CONVERSATION = 2`
- **LoadConversationRequest**
- **LoadConversationResponse**
  - repeated `lunarclient.websocket.conversation.v1.ConversationMessage` `messages` = 1
- **CreateConversationRequest**
  - `lunarclient.websocket.conversation.v1.ConversationType` `type` = 1
  - repeated `lunarclient.common.v1.Uuid` `participant_uuids` = 2
- **CreateConversationResponse**
  - `lunarclient.websocket.conversation.v1.CreateConversationResponse.Status` `status` = 1
  - `lunarclient.websocket.conversation.v1.Conversation` `conversation` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_LIMIT_REACHED = 2`
    - `STATUS_INVALID_PARTICIPANTS = 3`
    - `STATUS_CONVERSATION_ALREADY_EXISTS = 4`
- **DeleteConversationRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
- **DeleteConversationResponse**
  - `lunarclient.websocket.conversation.v1.DeleteConversationResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_NOT_OWNER = 3`
    - `STATUS_ALREADY_DELETED = 4`
- **DeleteConversationMessageRequest**
  - `lunarclient.common.v1.Uuid` `message_id` = 1
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 2
- **DeleteConversationMessageResponse**
  - `lunarclient.websocket.conversation.v1.DeleteConversationMessageResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_USERS_MESSAGE = 2`
    - `STATUS_ALREADY_DELETED = 3`
- **DeleteConversationMessageHistoryRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
- **DeleteConversationMessageHistoryResponse**
  - `lunarclient.websocket.conversation.v1.DeleteConversationMessageHistoryResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_UNKNOWN_CONVERSATION = 2`
    - `STATUS_NOT_IN_CONVERSATION = 3`
- **UpdateConversationOwnerRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.Uuid` `target_uuid` = 2
- **UpdateConversationOwnerResponse**
  - `lunarclient.websocket.conversation.v1.UpdateConversationOwnerResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_NOT_OWNER = 3`
    - `STATUS_TARGET_ALREADY_OWNER = 4`
    - `STATUS_TARGET_NOT_FOUND = 5`
- **AddConversationParticipantsRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - repeated `lunarclient.common.v1.UuidAndUsername` `targets` = 2
- **AddConversationParticipantsResponse**
  - `lunarclient.websocket.conversation.v1.AddConversationParticipantsResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_TARGET_ALREADY_IN_CONVERSATION = 3`
    - `STATUS_TARGET_NOT_FOUND = 4`
    - `STATUS_TARGET_INVITES_DISABLED = 5`
    - `STATUS_TARGET_NOT_FRIEND = 6`
    - `STATUS_LIMIT_REACHED = 7`
- **RemoveConversationParticipantRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.UuidAndUsername` `target` = 2
- **RemoveConversationParticipantResponse**
  - `lunarclient.websocket.conversation.v1.RemoveConversationParticipantResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_TARGET_NOT_IN_CONVERSATION = 3`
    - `STATUS_TARGET_NOT_FOUND = 4`
    - `STATUS_TARGET_IS_OWNER = 5`
    - `STATUS_NOT_OWNER = 6`
- **UpdateConversationNameRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `string` `name` = 2
- **UpdateConversationNameResponse**
  - `lunarclient.websocket.conversation.v1.UpdateConversationNameResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_INVALID_INPUT = 3`
    - `STATUS_NAME_POLICY_DISABLED = 4`
    - `STATUS_INNAPPROPRIATE = 5`
- **UpdateConversationIconRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.ConversationImage` `image` = 2
- **UpdateConversationIconResponse**
  - `lunarclient.websocket.conversation.v1.UpdateConversationIconResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_ICON_POLICY_DISABLED = 3`
    - `STATUS_INNAPPROPRIATE = 4`
- **LoadPinnedMessagesRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
- **LoadPinnedMessagesResponse**
  - `lunarclient.websocket.conversation.v1.LoadPinnedMessagesResponse.Status` `status` = 1
  - repeated `lunarclient.websocket.conversation.v1.ConversationMessage` `messages` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
- **AddPinnedMessageRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.Uuid` `message_id` = 2
- **AddPinnedMessageResponse**
  - `lunarclient.websocket.conversation.v1.AddPinnedMessageResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_MESSAGE_PINNING_POLICY_DISABLED = 3`
    - `STATUS_MESSAGE_NOT_FOUND = 4`
- **RemovePinnedMessageRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.Uuid` `message_id` = 2
- **RemovePinnedMessageResponse**
  - `lunarclient.websocket.conversation.v1.RemovePinnedMessageResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_MESSAGE_PINNING_POLICY_DISABLED = 3`
    - `STATUS_MESSAGE_NOT_FOUND = 4`
- **SetInvitePolicyRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.InvitePolicy` `policy` = 2
- **SetInvitePolicyResponse**
  - `lunarclient.websocket.conversation.v1.SetInvitePolicyResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_NOT_OWNER = 3`
- **SetNamePolicyRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.NamePolicy` `policy` = 2
- **SetNamePolicyResponse**
  - `lunarclient.websocket.conversation.v1.SetNamePolicyResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_NOT_OWNER = 3`
- **SetIconPolicyRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.IconPolicy` `policy` = 2
- **SetIconPolicyResponse**
  - `lunarclient.websocket.conversation.v1.SetIconPolicyResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_NOT_OWNER = 3`
- **SetMessagePinningPolicyRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.MessagePinningPolicy` `policy` = 2
- **SetMessagePinningPolicyResponse**
  - `lunarclient.websocket.conversation.v1.SetMessagePinningPolicyResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_NOT_OWNER = 3`
- **SetConversationPinnedRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `bool` `pinned` = 2
- **SetConversationPinnedResponse**
  - `lunarclient.websocket.conversation.v1.SetConversationPinnedResponse.Status` `status` = 1
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_LIMIT_REACHED = 3`
- **GetUploadUrlsRequest**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.UploadUsage` `usage` = 2
  - repeated `lunarclient.websocket.conversation.v1.UploadRequestItem` `items` = 3
- **GetUploadUrlsResponse**
  - `lunarclient.websocket.conversation.v1.GetUploadUrlsResponse.Status` `status` = 1
  - repeated `lunarclient.websocket.conversation.v1.PresignedUpload` `uploads` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_NOT_IN_CONVERSATION = 2`
    - `STATUS_ICON_POLICY_DISABLED = 3`
- **UnfocusConversationsRequest**
- **UnfocusConversationsResponse**
- **GetConversationsRequest**
- **GetConversationsResponse**
  - `lunarclient.websocket.conversation.v1.GetConversationsResponse.Status` `status` = 1
  - repeated `lunarclient.websocket.conversation.v1.Conversation` `conversations` = 2
  - `int32` `total_conversations` = 3
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_CONVERSATION_NOT_FOUND = 2`
    - `STATUS_NOT_IN_CONVERSATION = 3`
