# `lunarclient.websocket.socials.v1`

## Service `SocialsService`

Source: [`proto/extracted/lunarclient_websocket_socials_v1_service.proto`](../../proto/extracted/lunarclient_websocket_socials_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `Login` | `lunarclient.websocket.socials.v1.LoginRequest` | `lunarclient.websocket.socials.v1.LoginResponse` |
| `UnlinkSocial` | `lunarclient.websocket.socials.v1.UnlinkSocialRequest` | `lunarclient.websocket.socials.v1.UnlinkSocialResponse` |
| `SetSocialsVisibility` | `lunarclient.websocket.socials.v1.SetSocialsVisibilityRequest` | `lunarclient.websocket.socials.v1.SetSocialsVisibilityResponse` |

## Messages

- **LoginRequest**
- **LoginResponse**
  - repeated `lunarclient.websocket.socials.v1.LinkedSocial` `linked_socials` = 1
  - `lunarclient.websocket.socials.v1.SocialsVisibility` `socials_visibility` = 2
- **SetSocialsVisibilityRequest**
  - `lunarclient.websocket.socials.v1.SocialsVisibility` `visibility` = 1
- **SetSocialsVisibilityResponse**
- **UnlinkSocialRequest**
  - `lunarclient.common.v1.UserSocialPlatform` `platform` = 1
- **UnlinkSocialResponse**
  - `lunarclient.websocket.socials.v1.UnlinkSocialResponse.Status` `status` = 1
  - `lunarclient.common.v1.UserSocialPlatform` `platform` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_OK = 1`
    - `STATUS_TARGET_NOT_LINKED = 2`
