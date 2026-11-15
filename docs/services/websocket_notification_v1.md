# `lunarclient.websocket.notification.v1`

## Service `NotificationService`

Source: [`proto/extracted/lunarclient_websocket_notification_v1_service.proto`](../../proto/extracted/lunarclient_websocket_notification_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.notification.v1.LoginRequest` | `lunarclient.websocket.notification.v1.LoginResponse` |
| `OpenNotification` | `lunarclient.websocket.notification.v1.OpenNotificationRequest` | `lunarclient.websocket.notification.v1.OpenNotificationResponse` |
| `MarkAllNotificationsAsRead` | `lunarclient.websocket.notification.v1.MarkAllNotificationsAsReadRequest` | `lunarclient.websocket.notification.v1.MarkAllNotificationsAsReadResponse` |
| `OpenAlert` | `lunarclient.websocket.notification.v1.OpenAlertRequest` | `lunarclient.websocket.notification.v1.OpenAlertResponse` |
| `DeleteNotification` | `lunarclient.websocket.notification.v1.DeleteNotificationRequest` | `lunarclient.websocket.notification.v1.DeleteNotificationResponse` |

## Messages

- **OpenNotificationRequest**
  - `lunarclient.common.v1.Uuid` `notification_id` = 1
- **OpenNotificationResponse**
- **OpenAlertRequest**
  - `int32` `alert_id` = 1
- **OpenAlertResponse**
- **LoginRequest**
- **LoginResponse**
  - repeated `lunarclient.websocket.notification.v1.Notification` `notifications` = 1
- **DeleteNotificationRequest**
  - `lunarclient.common.v1.Uuid` `notification_id` = 1
- **DeleteNotificationResponse**
- **MarkAllNotificationsAsReadRequest**
- **MarkAllNotificationsAsReadResponse**
