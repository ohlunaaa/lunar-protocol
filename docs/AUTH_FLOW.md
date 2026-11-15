# Auth Flow — The Authenticator WebSocket in Detail

> The complete path from connection to JWT, with crypto details,
> failure states, and implementation pitfalls.

## Overview

```text
┌────────┐  1. WS connect    ┌──────────────┐
│ Client │ ────────────────► │ Authenticator │
│        │  2. hello         │   WebSocket   │
│        │ ────────────────► │               │
│        │  3. encryptionRequest (pubkey, nonce)
│        │ ◄──────────────── │               │
│        │                   └───────┬───────┘
│        │  4. joinServer           │ Mojang session
│        │ ────────────────► ┌──────┴───────┐
│        │                   │ sessionserver│
│        │  5. encryptionResponse   │.mojang.com │
│        │ ────────────────► │ Authenticator │
│        │  6. authSuccess (jwt)    │               │
│        │ ◄──────────────── │               │
└────────┘                   └───────────────┘
```

## 1 — Connecting

```text
URL:        wss://authenticator.lunarclientprod.com/game
User-Agent: Lunar Client 1.8.9-2.16.0
Protocol:   binary WebSocket, every frame = 1 protobuf envelope
```

## 2 — Sending HelloMessage

```json
{
  "hello": {
    "identity": {
      "uuid": { "high": "...", "low": "..." },
      "username": "ExamplePlayer"
    },
    "initiator": "assetServer"
  }
}
```

- UUID as `lunarclient.common.v1.Uuid` (fixed64 high/low).
- `initiator` observed: `"assetServer"` (game client context).

## 3 — Receiving EncryptionRequestMessage

The server sends:

```text
public_key:   DER SPKI RSA public key (2048-bit observed)
random_bytes: nonce (challenge)
```

The key loads directly:

**Node.js:**
```js
const { createPublicKey } = require("crypto");
const key = createPublicKey({
  key: publicKeyDer,
  format: "der",
  type: "spki",
});
```

**Java:**
```java
X509EncodedKeySpec spec = new X509EncodedKeySpec(publicKey);
PublicKey key = KeyFactory.getInstance("RSA").generatePublic(spec);
```

## 4 — Mojang joinServer

The trick: Lunar uses Mojang's session system as proof of identity. The
client proves it controls the account by depositing the AES key with the
Mojang session server.

### 4.1 Generate the AES key

16 random bytes = AES-128 key. Generate securely (`crypto.randomBytes`,
`SecureRandom`) — never `Math.random`.

### 4.2 Compute the session hash

```text
SHA-1(aesKeyBytes || serverPublicKeyDerBytes)
→ interpret as signed Java BigInteger hex
→ strip leading zeros
→ prepend minus sign if negative
```

This is Mojang's classic `serverId` format from the vanilla protocol —
the same logic used when joining a regular Minecraft server.

Reference implementation of the Mojang `serverId`:

```js
const { createHash } = require("crypto");

function computeServerId(aesKey, publicKeyDer) {
  const digest = createHash("sha1")
    .update(aesKey)
    .update(publicKeyDer)
    .digest();
  return sha1DigestToServerId(digest);
}

function sha1DigestToServerId(digest) {
  let hex = Buffer.from(digest).toString("hex");
  // two's complement: if the highest bit is set → negative
  if (parseInt(hex.slice(0, 1), 16) >= 8) {
    // negative: invert + 1, prepend minus
    let carry = 1n;
    let out = "";
    for (let i = hex.length - 1; i >= 0; i--) {
      let v = 15n - BigInt("0x" + hex[i]) + carry;
      carry = v >> 4n;
      out = (v & 0xfn).toString(16) + out;
    }
    hex = "-" + out.replace(/^0+/, "");
  } else {
    hex = hex.replace(/^0+/, "");
  }
  return hex;
}
```

### 4.3 POST to Mojang

```text
POST https://sessionserver.mojang.com/session/minecraft/join
Content-Type: application/json

{
  "accessToken": "<minecraft access token>",
  "selectedProfile": "<uuid without dashes>",
  "serverId": "<serverId hex>"
}
```

Success: HTTP `204 No Content`.

**Note:** Don't let too much time pass between joinServer and the
actual connection — Mojang doesn't invalidate immediately, but the
flow expects a fresh join state.

## 5 — Sending EncryptionResponseMessage

```text
secret_key = RSA_PKCS1v15_encrypt(aesKey, serverPublicKey)
public_key = RSA_PKCS1v15_encrypt(nonce, serverPublicKey)
```

- Padding: PKCS#1 v1.5 (NOT OAEP!).
- Field 2 is named `public_key` but contains the encrypted NONCE.

**Node.js:**
```js
const { publicEncrypt, constants } = require("crypto");
const encKey = publicEncrypt(
  { key, padding: constants.RSA_PKCS1_PADDING },
  aesKey
);
const encNonce = publicEncrypt(
  { key, padding: constants.RSA_PKCS1_PADDING },
  nonce
);
```

## 6 — AuthSuccessMessage

The server responds (on success):

```text
jwt: <string>
```

This JWT is the entry ticket for the game WebSocket. It can be decoded
(Base64URL parts) to inspect expiry/payload:

```js
const [h, p, s] = jwt.split(".");
const payload = JSON.parse(Buffer.from(p, "base64url").toString());
```

## Failure States

| State | Detection | Action |
|---|---|---|
| Mojang rejects joinServer | HTTP 4xx | Abort, refresh token |
| encryption_fail from server | `ClientboundAuthMessage` without `auth_success` | Inspect `reason` |
| WS closes after encryptionResponse | Check close code | Usually wrong key format (DER vs PEM) |
| JWT invalid at game WS | Close code `4011` | Retry auth |

## Common Mistakes

1. **Varint UUID:** Declaring Uuid as `uint64` decodes garbage. Use `fixed64`.
2. **OAEP instead of PKCS1v15:** The server can't parse the response.
3. **Wrong serverId formatting:** Leading zeros must be stripped, sign
   handling must follow Java BigInteger semantics. Otherwise Mojang
   returns 403.
4. **Delaying between joinServer and encryptionResponse:** The longer
   the gap, the more likely a timeout. Send immediately.
5. **Missing User-Agent:** The server may reject without a UA.
6. **Wrong User-Agent:** The UA must match the Lunar format.

## JWT Usage

The JWT goes into the game WebSocket handshake (field
`identity.authenticator_jwt`) unchanged. Don't sign it, don't modify
it, don't build your own — just pass it through.
