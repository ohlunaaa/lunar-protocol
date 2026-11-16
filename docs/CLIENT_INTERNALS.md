# Client Internals — Decompiled Moonsworth Analysis

> Source: `lunar.jar` decompiled with CFR 0.152 (11,510 `.java` files).
> The `com.moonsworth.lunar` packages are name-obfuscated
> (`HCHORRIIC...`-style identifiers), but strings, constants, and
> structure survive intact. This document maps what the obfuscated
> client actually does.

## Decompilation setup

```text
JDK:   Temurin 17.0.21 (portable zip, no installer)
Tool:  CFR 0.152 (cfr.jar from github.com/leibnitz27/cfr)
Cmd:   java -Xmx6g -jar cfr.jar lunar.jar --outputdir out --silent true
```

Package layout after decompile:

| Package | Files | Content |
|---|---|---|
| `client.*` | 2,971 | Game client logic (mods, IPC, rendering, WS) |
| `client.util` | — | **Service config, constants** (readable!) |
| `lib.*` | 992 | Bundled libraries (adventure text, etc.) |
| root obfusc pkgs | ~670 | Launch pipeline, genesis, versioning |

## The service configuration class

`com.moonsworth.lunar.client.util.<obf>` (the "UrlConfig") — fully
recovered logic:

```java
// Dev-mode switch:
String dev = System.getenv("devServices");        // "yes" | "no"
// also: System.getProperty("devServices", "no").equals("yes")

// Per-service override hook (works in EVERY build):
String OOOHRCIORIOHRCHHCIIICCIOOORCIC(String name, String defaultUrl) {
    if (<forceProdFlag>) return defaultUrl;
    String env = System.getenv("serviceOverride" + name);
    if (env != null) return env;
    return System.getProperty("serviceOverride" + name, defaultUrl);
}
```

Production values (`devServices != yes`):

| Service name (override key) | URL |
|---|---|
| `serviceOverrideStyngr` | `https://api.styngr.com/api` |
| `serviceOverrideSkins` | `https://skins.mcstats.com` |
| `serviceOverrideThirdPartyCache` | `https://thirdpartycache.lunarclientprod.com` |
| `serviceOverrideAuthenticator` | `wss://authenticator.lunarclientprod.com` |
| `serviceOverrideAssetServer` | `wss://websocket.lunarclientprod.com` |
| `serviceOverrideApi` | `https://api.lunarclientprod.com` |

Dev values: same hosts on `lunarclientdev.com`, skins on
`mcstats.cloud`, Styngr staging at `stg.api.styngr.com/api`.

Plus constants: `https://textures.lunarclientcdn.com/file/` (cosmetic
assets), `https://store.lunarclient.com/`.

**Red-team note:** setting `-DserviceOverrideAssetServer=ws://localhost:9001`
on the game JVM redirects the entire game WebSocket — a clean
man-in-the-middle point for protocol research, no binary patching
required. The launcher similarly honors `DEV_SERVICES` in main.js.

## GameIPC client (game side) — full flow recovered

`client/<obf>/<obf>.java extends WebSocketClient` (java_websocket lib):

```java
// Connection:
super(URI.create("ws://127.0.0.1:" + PORT),   // PORT = 28190 (hardcoded
                                               // in client.util config)
      new Draft_6455(),
      Map.of("lc-handshake",
             Base64.getEncoder().encodeToString(handshake.toByteArray())),
      3000 /* connect timeout ms */);
```

**Key discovery — the handshake is NOT the first frame:** the game
sends the `gameipc.handshake.v1.Handshake` protobuf **Base64-encoded in
the `lc-handshake` WebSocket subprotocol header** during the HTTP
upgrade. The launcher server must list `lc-handshake` as supported
subprotocol. (Correction to GAMEIPC.md's "first frame" description.)

On open, the client:

1. Registers push consumers: `PlayServerPush`, `ExitGamePush`,
   `FocusGamePush`, `PendingPromotionUpdatePush`,
   `StartStorePreviewSessionPush`, `TebexJsCheckoutClosed`.
2. Immediately calls `LocationService.UpdateFocus` with the current
   window-focus state.
3. Calls `TebexService.CheckTebexCapabilities` and
   `PayNowService.CheckPayNowCapabilities` — the responses
   (`EMBEDDED_CHECKOUT_OVERWOLF_OVERLAY` vs
   `EMBEDDED_CHECKOUT_ELECTRON_WINDOW`) select overlay vs window
   checkout UI.

Stubs held by the client: `AuthService`, `LaunchService`,
`LocationService`, `TebexService`, `PayNowService`, `BrowserService`,
`PromotionService`, `StyngrRadioService` — confirming the gameipc
service list from the protos.

## Client-side constants (harvested from all decompiled sources)

### URLs

| URL | Purpose |
|---|---|
| `https://analytics.lunarclientprod.com` (+dev) | Client analytics |
| `https://49c0ccff7276e28e55e9e82de4addd1d@o923049.ingest.sentry.io/6029559` | Sentry (game client, release) |
| `https://49db0029d2304d69bd80986185f7fafd@o923049.ingest.sentry.io/6029559` | Sentry (game client, alternate env) |
| `https://api.klipy.com/api/v1/RpEJNT11YK7VjO07Z75cV8iEybS1DXSnhbsIeGP84Azp7xMsAY9oxcS7ZuVhMISv/gifs` | GIF search (same key as launcher) |
| `https://api.mojang.com/users/profiles/minecraft/` | Name → UUID |
| `https://sessionserver.mojang.com/blockedservers` | Blocked-server list check |
| `https://api.minecraftservices.com/minecraft/profile/skins` | Skin upload |
| `https://i.imgur.com/`, `https://imgur.com/` | Image upload |
| `https://lunr.pics/`, `https://lunr.pics/i/` | Screenshot host |
| `https://medal.tv/lunar` | Clip recording |
| `https://resourcepacks.gg` | Resource packs |
| `https://s-optifine.net` | OptiFine downloads |
| `https://store.lunarclient.com/checkout/instant?package=` | Instant checkout |

### System properties (game JVM)

| Property | Effect |
|---|---|
| `lunar.dataDir` | Override data directory |
| `lunar.generateModClasses` | Dev: dump generated mod classes |
| `lunar.jit.preserveLocalAssets` | Keep local assets during JIT update |
| `lunar.legacyStyledText` | Old text rendering |
| `lunar.sentryDebug` / `lunar.sentrySendErrors` | Sentry control |
| `lunar.webosr.bundlePath` / `.renderer` / `.url` | Ultralight/WebOSR UI engine config |
| `devServices` | Env + property: switch to dev endpoints |
| `serviceOverride<Service>` | Env + property: per-service URL override |

### Env vars

`APPDATA`, `PATH`, `PROCESSOR_ARCHITECTURE`, `WINDIR`, `WAYLAND_DISPLAY`,
`XDG_SESSION_TYPE`, `devServices`.

## What is NOT in the game client

- **No anticheat client module** — no cheat-detection strings beyond
  vanilla `FEATURE_FLAG_DEBUG` and library internals. Lunar's
  anticheat (if server-side via Apollo) is not a client component;
  the client only reports mods via heartbeat/launch metadata.
- **No license/validation logic** beyond the JWT handshake — the game
  trusts the WS handshake for identity; cosmetics/entitlements come
  from `CosmeticService.Login` responses.

## Reproducing

```bash
# portable JDK + CFR
curl -L -o jdk17.zip "https://api.adoptium.net/v3/binary/latest/17/ga/windows/x64/jdk/hotspot/normal/eclipse?project=jdk"
curl -L -o cfr.jar "https://github.com/leibnitz27/cfr/releases/download/0.152/cfr-0.152.jar"
unzip jdk17.zip
jdk*/bin/java -Xmx6g -jar cfr.jar lunar.jar --outputdir out --silent true
# then grep for the service config:
grep -rl "lunarclientprod.com" out/com/moonsworth/lunar/client/util/
```

Note: deeply nested obfuscated package names can exceed Windows'
260-char path limit — use `tar`/long-path-aware tools or search via
grep/Python rather than Explorer.
