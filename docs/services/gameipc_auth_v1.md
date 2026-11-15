# `lunarclient.gameipc.auth.v1`

## Service `AuthService`

Source: [`proto/extracted/lunarclient_gameipc_auth_v1_service.proto`](../../proto/extracted/lunarclient_gameipc_auth_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `RefreshAccount` | `lunarclient.gameipc.auth.v1.RefreshAccountRequest` | `lunarclient.gameipc.auth.v1.RefreshAccountResponse` |
| `AddAccount` | `lunarclient.gameipc.auth.v1.AddAccountRequest` | `lunarclient.gameipc.auth.v1.AddAccountResponse` |

## Messages

- **OpenMicrosoftPopupRequest**
- **OpenMicrosoftPopupResponse**
  - `lunarclient.gameipc.auth.v1.OpenMicrosoftPopupResponse.Status` `status` = 1
  - `string` `url` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_MATCHED_TARGET_URL = 1`
    - `STATUS_CLOSED_WITH_NO_URL = 2`
- **RefreshAccountRequest**
  - `lunarclient.common.v1.Uuid` `uuid` = 1
- **RefreshAccountResponse**
  - `bool` `success` = 1
  - `lunarclient.gameipc.auth.v1.RefreshAccountResponse.AccountError` `error` = 2
  - enum **AccountError**:
    - `ACCOUNT_ERROR_UNSPECIFIED = 0`
    - `ACCOUNT_ERROR_ACCOUNTS_FILE_EMPTY = 1`
    - `ACCOUNT_ERROR_NOT_PURCHASED_MINECRAFT = 2`
    - `ACCOUNT_ERROR_MISSING_REFRESH_TOKEN = 3`
    - `ACCOUNT_ERROR_ALREADY_REFRESHING = 4`
- **AddAccountRequest**
- **AddAccountResponse**
  - `bool` `success` = 1
  - `lunarclient.gameipc.auth.v1.AddAccountResponse.AccountError` `error` = 2
  - enum **AccountError**:
    - `ACCOUNT_ERROR_UNSPECIFIED = 0`
    - `ACCOUNT_ERROR_NOT_PURCHASED_MINECRAFT = 1`
- **NotifySwitchAccountRequest**
  - `lunarclient.common.v1.Uuid` `uuid` = 1
- **NotifySwitchAccountResponse**
