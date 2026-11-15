# Launcher Analysis — app.asar Reverse Engineering

> Source: `C:\Users\<user>\AppData\Local\Programs\Lunar Client\resources\app.asar`
> (26.3 MB, Electron launcher v3.7.36-ow, commit `7e0f4462`).
> Extracted with [tools/extract_asar.py](../tools/extract_asar.py).

## Launcher identity

From `package.json`:

| Key | Value |
|---|---|
| Name | `lunarclient` |
| Version | `3.7.36-ow` (Overwolf build) |
| Author | Moonsworth LLC |
| Repo | github.com/LunarClient/Launcher (private) |
| Electron | 44.9.0 |
| Branch / commit | `master` / `7e0f4462952a9744c86f76b2a2d71990f980f40f` |
| Node | >= 24.x, pnpm 12 |

Notable dependencies: `ws` (WebSocket), `jose` (JWT), `socket.io-client`
2.5.0 (legacy!), `better-sqlite3`, `minecraft-server-util`,
`prismarine-nbt`, `smart-buffer`, `bsdiff-node`, `7zip-bin`.

Overwolf integration (from `package.json.overwolf`):
packages `overlay` + `crn`, uid `jilehohlakeokncafogkgnicgndeecdiengddbcc`,
ads CMP at `content.overwolf.com/monsdk/electron/latest/cmp/partners/lunar/cmp.html`.

## Archive structure

```text
app.asar
├── package.json           # identity (above)
├── build/                 # icons, tray assets
├── dist/                  # renderer assets (html + bundled frontend)
├── dist-electron/
│   ├── electron/
│   │   ├── main.js        # 6 MB bundled main process (all backend logic)
│   │   ├── archive-worker.js
│   │   ├── consts.js
│   │   └── index.js
│   └── preload/           # auth, launcher, popup preload scripts
└── node_modules/          # bundled runtime deps
```

`main.js` is a rollup bundle (minified, single scope) — but **not
obfuscated**: all protobuf-generated code, endpoints, and protocol
logic are readable.

## Key discoveries in main.js

### 1. The launcher uses a SEPARATE WebSocket endpoint

```js
iNe = () => `wss://websocket.lunarclient${ov() ? `dev` : `prod`}.com/launcher-v3`
```

```text
wss://websocket.lunarclientprod.com/launcher-v3    (production)
wss://websocket.lunarclientdev.com/launcher-v3     (development)
```

This is distinct from the game endpoint (`/game`). The launcher
connects with `LauncherHandshake` (field 9 of the handshake proto) and
uses `LauncherHeartbeat` (default interval 30s, from
`metadata.refreshIntervals.heartbeat`).

All 38 remote services are also compiled into the launcher (the
protobuf client impls are bundled) — the launcher can call
friend/chat/store RPCs directly, without a running game.

### 2. GameIPC server (launcher <-> game)

Fully documented in [GAMEIPC.md](./GAMEIPC.md). Summary:

```js
port = 28190;                      // base port, +1 scan up to +29
server = new WebSocketServer({ host: "127.0.0.1", port: port + e });
// verifyClient: (info, cb) => cb(true)   <- accepts everything
```

### 3. Module architecture

The launcher is organized into modules with services:

```js
class Module { services = new Map() }   // each service registers by name
class GameIpcService extends ... { send(frame) { this.ws.send(frame) } }
```

- Services register via a service directory (`No default export found
  for service at ...` log line reveals the pattern).
- `getLaunchSession()` resolves the current or focused launch.
- Push queueing binds unsent pushes to the next game launch.

### 4. Telemetry / analytics flags

From `LauncherHandshake`: `optimized_ads`, `analytics`, `owahe`
(Overwolf ads enabled), `safe_storage` — all reported to the server
during the handshake. The launcher also embeds Sentry
(`%APPDATA%\lunarclient\sentry\`).

### 5. Legacy Discord RPC

The bundle contains a Discord IPC client (named pipe
`\\?\pipe\discord-ipc-0..9` on Windows, with HTTP fallback probing
`127.0.0.1:6463-6472`). Standard
[Discord Rich Presence](https://discord.com/developers/docs/topics/rpc)
framing: `int32LE op + int32LE len + JSON`, ops
HANDSHAKE=0/FRAME=1/CLOSE=2/PING=3/PING=4. Used for Discord presence
while in-game. (Initially easy to confuse with gameipc — different
protocol.)

## Launcher state on disk

| Path | Contents |
|---|---|
| `%APPDATA%\lunarclient\Local Storage\leveldb\` | Launcher UI state (Redux-persisted via electron-redux) |
| `%APPDATA%\lunarclient\Code Cache\js\` | Cached renderer JS |
| `%APPDATA%\lunarclient\Network\Cookies` | Electron cookie store (launcher web sessions) |
| `~/.lunarclient/settings/launcher.json` | User settings |
| `~/.lunarclient/launcher-cache/` | `installation-id`, UI zips, texture index |
| `%LOCALAPPDATA%\lunarclient-updater\` | `package.7z`, pending update exe, `update-info.json` |
| `%APPDATA%\lunarclient\Partitions\__owepm__\` | Overwolf ads partition |

## Renderer (dist/)

The UI is a bundled web app (React-style SPA) loaded from `dist/html`.
It communicates with the main process exclusively through the preload
bridge (`dist-electron/preload/{auth,launcher,popup}.js`) via
contextBridge IPC — the renderer never touches sockets directly.

## Reproducing the extraction

```bash
python tools/extract_asar.py \
  "C:\Users\<user>\AppData\Local\Programs\Lunar Client\resources\app.asar" \
  asar-out

# then grep the bundle:
grep -o "wss://[^\"\`]*" asar-out/dist-electron/electron/main.js
grep -o "launcher-v3"    asar-out/dist-electron/electron/main.js
grep -o "28190"          asar-out/dist-electron/electron/main.js
```

The ASAR format (Chromium pickle header):

```text
UInt32 LE  pickle payload size (4)
UInt32 LE  total header size
UInt32 LE  header string size field
UInt32 LE  JSON length
JSON       file tree (offsets relative to end of aligned header)
padding    to 4-byte alignment
file data
```
