# REST & External APIs — Complete Surface

> Mined from the launcher's `app.asar` (`dist-electron/electron/main.js`)
> plus live-fetched OpenAPI specs. Every base URL, route, auth mechanism,
> and third-party integration.

## Base URLs

| Helper | Production URL | Purpose |
|---|---|---|
| `Ov()` | `https://api.lunarclientprod.com` | Lunar API root |
| `Av()` | `https://api.lunarclientprod.com/launcher` | Launcher REST API |
| `S_e()` | `https://api.lunarclientprod.com/styngr` | Styngr radio proxy |
| `kv()` | `https://thirdpartycache.lunarclientprod.com` | Third-party cache |
| `Zxe()` | `https://analytics.lunarclientprod.com` | Analytics |
| `lv()` | `https://skins.mcstats.com` | Player skins/faces |
| `Ttt()` | (dev-gated) | — |
| — | `https://launcher-releases.lunarclientprod.com/master/<sha>` | Launcher updates |
| — | `https://translations.lunarclientcdn.com/launcher/<lang>.json` | i18n |

All dev variants swap `prod` → `dev` (`lunarclientdev.com`), gated by
`DEV_SERVICES` global.

---

## Launcher API (`api.lunarclientprod.com/launcher`)

All calls go through a wrapper `Zb({url, requestMethod, additionalData,
headers, useLocalCache})` — the auth layer injects the session token.
`jv = "Lunar Client Launcher v<version>"` is the User-Agent.

### Launch

| Method | Route | Body/Query | Purpose |
|---|---|---|---|
| POST | `/launch` | `{version, branch, args, module, canary_preference, profile:{id,name,modrinth?}}` | Fetch launch artifacts for a Lunar version |
| POST | `/launch/vanilla` | `{version, loaderVersion, loaders[], use_combined_data}` | Launch data for vanilla/modloader profiles |
| GET | `/launch/licenses` | — | License file list (`licenses[].file`) |

### Metadata

| Method | Route | Purpose |
|---|---|---|
| GET | `/metadata/layout` | Home layout: alerts, blog posts, servers CTA, nav items, video promotion, ads, carousel, announcements |
| GET | `/metadata/misc` | `?launcher_update_stream=` — modpack list, terms (id+hash), etc. |
| GET | `/metadata/radio` | Radio stations + premium packages |
| GET | `/metadata/crash-classifications` | Crash pattern classifications |
| GET | `/metadata/versions/lunar` | `?branch=` — versions, subversion assets, branchReset, recommendedLibraries |
| GET | `/metadata/versions/vanilla` | Vanilla version list |
| GET | `/metadata/versions/vanilla/{id}` | `?include_snapshots=` — vanilla versions for loader |
| GET | `/metadata/versions/badlion` | Badlion-compatible versions (behind `badlion-services` flag) |
| GET | `/metadata/mod-incompatibilities` | (on api root `/launcher` prefix via `dLe`) known Fabric mod conflicts, 64 KB cache, 5 s timeout, bundled fallback |

### Servers

| Method | Route | Purpose |
|---|---|---|
| GET | `/servers` | `?language=` + filters — featured/shelf servers |
| GET | `/server/{serverId}` | `?language=` — resolve a server for deep links |

### Moderation & Uploads

| Method | Route | Body | Purpose |
|---|---|---|---|
| POST | `/moderation/profanity` | `{text}` → `{allowed}` | Profanity check (locally cached) |
| POST | `/log-upload/start` | — | Begin log upload (presigned URL flow) |
| POST | `/log-upload/complete` | — | Finish log upload |

(`/log-upload/start` + `/log-upload/complete` constants `c0e`/`l0e` with
300 s timeout; uploads also serve JFR perf recordings + crash dumps with
window screenshots as attachments.)

---

## Loader metadata proxies (api root, `Ov()`)

| Method | Route | Purpose |
|---|---|---|
| GET | `/fabric/v2/versions/loader/{mcVersion}` | Fabric loader versions |
| GET | `/forge/v2/versions/loader/{mcVersion}` | Forge loader versions |
| GET | `/neoforge/v2/versions/loader/{mcVersion}` | NeoForge loader versions |
| GET | `/quilt/v2/versions/loader/{mcVersion}` | Quilt loader versions |
| GET | `/optifine/v2/versions/loader/{mcVersion}` | OptiFine loader versions |

## Styngr proxy (`api.lunarclientprod.com/styngr`)

| Method | Route | Auth | Purpose |
|---|---|---|---|
| POST | `/jwt` | `Authorization: <Lunar JWT>` body `{platform: "LAUNCHER"}` | Exchange Lunar JWT → Styngr JWT |

The launcher obtains the Lunar JWT via
`auth.getAccountAuthenticatorJwt("LAUNCHER_STYNGR_JWT", playerId)` —
same JWT machinery as the game, scoped audience.

### Styngr SDK (direct, api.styngr.com — from live OpenAPI)

Full spec: 236 KB, 27 endpoints. Highlights:

| Method | Route |
|---|---|
| GET | `/api/v1/sdk/integration/playlists` |
| POST | `/api/v1/sdk/integration/playlists/{id}/start` |
| POST | `/api/v1/sdk/integration/playlists/{id}/next` / `resume` / `skip` |
| POST | `/api/v1/sdk/integration/playlists/{playlistId}/likes` |
| GET | `/api/v1/sdk/apps/radio/availability/countries` |
| GET | `/api/v1/sdk/nfts`, `/nfts/my`, `/nfts/previewAvailable` |
| POST | `/api/v1/sdk/nfts/{collectionId}/buy` / `preview`, `/nfts/{id}/bind` / `claim`, `/nfts/payment/confirm` |
| GET | `/api/v1/sdk/events`, `/events/nfts/my`, `/events/styngs/my` |
| POST | `/api/v1/sdk/events/{eventId}/unbind` |

(Yes — Styngr ships an NFT marketplace API. The launcher only uses the
playlist routes via gameipc.)

---

## CurseForge (proxied via api root, helper `dG()`)

| Method | Route |
|---|---|
| GET | `/mods/{modId}` |
| POST | `/mods` body `{modIds[]}` |
| GET | `/mods/{modId}/files`, `/mods/{modId}/files/{fileId}`, `/mods/{modId}/description` |
| POST | `/mods/files` body `{fileIds[]}` |
| POST | `/fingerprints` and `/fingerprints/432` body `{fingerprints[]}` |
| GET | `/mods/search?<filters>` |

## Modrinth (direct or proxied, helper `bF()` — v2, `bF("v3")` for v3)

| Method | Route |
|---|---|
| GET | `/search` |
| GET | `/projects?ids=[..]`, `/project/{id}`, `/project/{id}/check`, `/project/{id}/dependencies` |
| GET | `/versions?ids=[..]`, `/version/{id}` |
| POST | `/version_files` body `{hashes[], algorithm}`, `/version_files/update` |
| GET | `/version_file/{hash}?algorithm=` |
| GET | `/teams?ids=[..]`, `/user/{id}`, `/user/{id}/projects` |
| GET | `v3 /organizations?ids=`, `v3 /organization/{id}/projects` |

CDN: `https://edge.forgecdn.net/files/` (CurseForge),
`https://resources.download.minecraft.net` (Mojang assets),
`https://s3-{region}.amazonaws.com/` fallback.

---

## Microsoft / Xbox / Mojang auth chain

Two independent implementations in the bundle:

### Classic MSA (OAuth2 code flow)

```text
authorize:  https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize
token:      https://login.microsoftonline.com/consumers/oauth2/v2.0/token
redirect:   https://login.microsoftonline.com/common/oauth2/nativeclient
scopes:     "XboxLive.signin offline_access"
live-token: https://login.live.com/oauth20_token.srf
live-desk:  https://login.live.com/oauth20_desktop.srf
```

### XAL (Xbox Auth Library, Win32)

| Constant | Value |
|---|---|
| Device token | `https://device.auth.xboxlive.com/device/authenticate` |
| Sisu | `https://sisu.xboxlive.com/authenticate` + `/authorize` |
| User token | `https://user.auth.xboxlive.com/user/authenticate` |
| XSTS | `https://xsts.auth.xboxlive.com/xsts/authorize` |
| Client id | `00000000402b5328` |
| Relying party | `rp://api.minecraftservices.com/` |
| Service | `service::user.auth.xboxlive.com::MBI_SSL` |
| XAL version string | `XAL Win32 2021.11.20220411.002` |
| Title id | `1794566092` |
| Device-code grant | `urn:ietf:params:oauth:grant-type:device_code` |

XAL requests are **signature-authenticated** (SmartBuffer-built
signature blobs with keypair + Windows FILETIME timestamps) — that's
the `tB({url, authorizationToken, payload, keyPair, date})` builder.

### Minecraft services

| Method | Route |
|---|---|
| POST | `https://api.minecraftservices.com/authentication/login_with_xbox` |
| POST | `https://api.minecraftservices.com/launcher/login` |
| GET | `https://api.minecraftservices.com/entitlements/license` |
| GET | `https://api.minecraftservices.com/minecraft/profile` |
| GET/PUT | `.../profile/skins`, `.../profile/capes/active` |
| GET | `.../profile/lookup/name`, `.../profile/namechange` |
| GET | `.../player/attributes` |
| POST | `https://sessionserver.mojang.com/session/minecraft/join` (game auth) |

---

## Analytics

| Method | Route | Purpose |
|---|---|---|
| POST | `https://analytics.lunarclientprod.com/launcher/event/batch` | Event batches (15 s flush, 5 s retry, offline cache at `launcher-cache/offline-analytics.cache`) |

Event names (excerpt): `alert.interaction`, `auth.error`,
`updater.error`, `blogpost.interaction`, `external.open`, ...

Sentry DSNs (bundled): `o923049.ingest.sentry.io/6029601` (prod:
`8b91851...`, dev: `2b19802...`, sample rates 1%/5% dev, 0.1%? prod).

## Badlion integration (owlmessenger)

| Item | Value |
|---|---|
| Prod WS | `wss://owlmessenger.badlion.net` |
| Dev WS | `wss://owlmessenger.thisiswherewedev.badlion.net` |
| Transport | socket.io 2.5 (websocket-only) |
| Update base | `https://client-updates.badlion.net/moonsworth` |
| Auth | `AuthClientImpl` over the same RPC layer (protobuf) |

Used for Lunar↔Badlion friend messaging when `badlion-services` is
enabled. Badlion versions come from `/launcher/metadata/versions/badlion`.

## mcstats

| Method | Route | Purpose |
|---|---|---|
| — | `https://serverpinger.mcstats.com/openapi` | Live OpenAPI (fetched) |
| GET | `/server/{serverId}/history/?start&end&step` | Player history |
| GET | `/servers/tracked/` | Tracked servers + last pings |
| — | `https://skins.mcstats.com/face/{...}` | Player face images |

## Klipy GIFs (chat messenger)

```text
https://api.klipy.com/api/v1/RpEJNT11YK7VjO07Z75cV8iEybS1DXSnhbsIeGP84Azp7xMsAY9oxcS7ZuVhMISv/gifs
```

API key embedded in the bundle; used for GIF search in conversations.

## Discord

- Rich Presence over named pipe `\\.\pipe\discord-ipc-0..9`
  (fallback HTTP probe `127.0.0.1:6463-6472`), classic framing.
- REST: `https://discord.com/api` (presence assets).

## Overwolf

| Item | Value |
|---|---|
| App UID | `jilehohlakeokncafogkgnicgndeecdiengddbcc` |
| Port | `8032` (local ow-electron) |
| Ads CMP | `content.overwolf.com/monsdk/electron/latest/cmp/partners/lunar/cmp.html` |
| Packages | `overlay`, `crn` |

## Security: DNS pinning

The launcher pins its critical domains by scanning the hosts file
(`eqe` list): `lunarclientprod.com`, `lunarclientcdn.com`,
`lunarclient.com`, `moonsworth.com`, `login.live.com`,
`login.microsoftonline.com`, `sisu.xboxlive.com`, `xsts.auth.xboxlive.com`,
`user.auth.xboxlive.com`, `api.minecraftservices.com`,
`sessionserver.mojang.com` — it warns/blocks if they resolve to
non-public IPs (anti DNS-spoof for the auth chain).

Trusted-domain allowlist for images/links additionally includes:
`mcstats.com`, `mcstats.cloud`, `moonsworth.store`,
`mymoonsworth.store`, `lunar.gg`, `lunargg.dev`.

## Wrapped

| Route | Purpose |
|---|---|
| `https://wrapped.lunarclient.com/access?assumeUuid=&overrideUrl=` | Wrapped year-review, deep-link opens with optional UUID assumption |

## Update system

| Item | Value |
|---|---|
| Feed | `https://launcher-releases.lunarclientprod.com/master/<commit-sha>` |
| Updater dir | `%LOCALAPPDATA%\lunarclient-updater` (`package.7z`, pending exe, `update-info.json`) |
| Channels | `latest-ow` default; canary preference passed to `/launch` |
