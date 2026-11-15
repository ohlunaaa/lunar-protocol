# `lunarclient.websocket.chat.v1`

## Service `ChatService`

Source: [`proto/extracted/lunarclient_websocket_chat_v1_service.proto`](../../proto/extracted/lunarclient_websocket_chat_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `SendChat` | `lunarclient.websocket.chat.v1.SendChatRequest` | `lunarclient.websocket.chat.v1.SendChatResponse` |

## Messages

- **SendChatRequest**
  - `lunarclient.common.v1.Uuid` `target_uuid` = 1
  - `string` `chat_message` = 2
- **SendChatResponse**
