# `lunarclient.gameipc.chat.v1`

## Service `ChatService`

Source: [`proto/extracted/lunarclient_gameipc_chat_v1_service.proto`](../../proto/extracted/lunarclient_gameipc_chat_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `ReceiveMessage` | `lunarclient.gameipc.chat.v1.ReceiveMessageRequest` | `lunarclient.gameipc.chat.v1.ReceiveMessageResponse` |

## Messages

- **ReceiveMessageRequest**
  - `lunarclient.common.v1.UuidAndUsername` `sender` = 1
  - `string` `content` = 2
- **ReceiveMessageResponse**
