# Service Catalog — All 38 Services with RPCs

> Source: `proto/extracted/` (original descriptors pulled from
> lunar.jar). Full message definitions live in the respective
> `.proto` files.

## Game WebSocket services (`wss://websocket.lunarclientprod.com/game`)

### HeartbeatService — `lunarclient.websocket.heartbeat.v1`

| RPC | Request | Response |
|---|---|---|
| `LauncherHeartbeat` | `running_instances[]`, `open_renderers[]`, `badlion_connected` | `online_counts` |
| `GameHeartbeat` | `mods` map<string,bool> | empty |

The launcher heartbeat runs in the launcher context, the game
heartbeat in-game (roughly every 50s). The game heartbeat reports
active mods to the server.

### SubscriptionService — `lunarclient.websocket.subscription.v1`

| RPC | Request | Response |
|---|---|---|
| `SubscribeV2` | `target_uuids[]` | `cosmetic_pushes[]`, `radio_pushes[]` |
| `Unsubscribe` | `target_uuids[]` | empty |

Core detector: UUID present in `cosmetic_pushes` → Lunar user.

### CosmeticService — `lunarclient.websocket.cosmetic.v2`

| RPC | Purpose |
|---|---|
| `Login` | Session init; returns owned cosmetics, outfit tree, outfits, equipped |
| `CreateOutfit` | Create an outfit |
| `UpdateOutfit` | Edit an outfit |
| `DeleteOutfit` | Delete an outfit |
| `SelectOutfit` | Activate an outfit |
| `FavoriteCosmetic` / `UnfavoriteCosmetic` | Favorites |
| `LoadTabLogos` | Available tab logos |
| `SetCosmeticOwnershipVisibility` | Friends/Noone/Everyone |
| `UpdateLunarPlusColor` | Set the plus color |

**EquipCondition system** (in `common.proto`): outfits switch
conditionally — dimension, weather, biome temperature, passenger
state, movement state (swimming/creative fly/elytra), in-liquid
(water/lava), radio playing, on fire, server IP, time of day. An
outfit tree references a different outfit per condition.

`EquippedCosmetic` (v2, richer than the old docs): `cosmetic_id`
(int32!), `geckolib_metadata` (Struct), `cloth_cloak`, layer flags
(over skin/helmet/chestplate/leggings/boots), `hat_height_offset`,
`flip_arm`.

### FriendService — `lunarclient.websocket.friend.v1`

| RPC | Purpose |
|---|---|
| `Login` | Online/offline friends, requests, pins, visibilities, `user_created_at` |
| `BroadcastLocationChange` | Location + trigger (join/disconnect/hostedworld/richstatus) |
| `BroadcastStatusChange` | Online status |
| `BroadcastServerKick` | Kick reason to friends |
| `RemoveFriend` | by uuid |
| `ToggleFriendRequests` | allow flag |
| `SendFriendRequest` | by username; response with detailed status codes |
| `CancelFriendRequest` / `AcceptFriendRequest` / `DenyFriendRequest` | Request lifecycle |
| `AddFriendPin` / `RemoveFriendPin` | Pinned friends |
| `SetLastSeenVisibility` | |
| `SetCountryFlagVisibility` | |
| `SetGroupChatInvitePrivacy` | |

`SendFriendRequestResponse` directly includes the target's name, logo
color, plus color, rank, and badge ID.

### ConversationService — `lunarclient.websocket.conversation.v1`

The largest service (48 messages) — Lunar's built-in messenger:

| Group | Methods |
|---|---|
| Messaging | `SendConversationMessage`, `PreSendAction`, `LoadConversation` |
| Management | `Create/DeleteConversation`, `UpdateOwner/Name/Icon` |
| Participants | `Add/RemoveParticipant` |
| History | `DeleteMessage`, `DeleteHistory` |
| Pins | `LoadPinnedMessages`, `Add/RemovePinnedMessage` |
| Policies | `SetInvite/Name/Icon/MessagePinningPolicy` |
| UI | `SetConversationPinned`, `UnfocusConversations`, `GetConversations` |
| Uploads | `GetUploadUrls` (presigned uploads) |

### EmoteService — `lunarclient.websocket.emote.v1`

`Login`, `UseEmote`, `StopEmote`, `GetJamPlayback`, `UpdateEquippedEmotes`

### RadioService — `lunarclient.websocket.radio.v1`

`Login`, `BroadcastRadioInfoChange`, `SetRadioPlayingVisibility`

(Radio = the Styngr music integration in-game.)

### BadgeService — `lunarclient.websocket.badge.v1`

`Login`, `EquipBadge`

### ScreenshotService — `lunarclient.websocket.screenshot.v1`

`Login`, `RecordScreenshot`, `SetDefaultUploadPrivacy`

### NotificationService — `lunarclient.websocket.notification.v1`

`Login`, `OpenNotification`, `MarkAllNotificationsAsRead`, `OpenAlert`,
`DeleteNotification`

### ServerService — `lunarclient.websocket.server.v1`

`GetPlayerCounts`, `CheckServerRecommendations`,
`GetServerRecommendations`, `CheckAuthorizedFeatures` (Apollo features
per server)

### ServerDiscoveryService — `lunarclient.websocket.serverdiscovery.v1`

`Login`, `DiscoverServers`, `SearchServers`,
`LoadAutocompleteSuggestions`, `LoadServerModal`,
`TrackSectionNotInterested`, `TrackServerJoin`

### HostedWorldService — `lunarclient.websocket.hostedworld.v1`

`Login`, `StartHostingWorld`, `StopHostingWorld`,
`HostedWorldHeartbeat`, `ListHostedWorlds`, `PreJoinHostedWorld`,
`JoinHostedWorld`, `ConfirmHostedWorldJoin` — Lunar's "host your own
server" feature.

### Analytics / telemetry

| Service | RPCs |
|---|---|
| `AnalyticsService` | `RecordCounters`, `RecordPinnedServerInteraction`, `RecordEnabledMods` |
| `ApolloService` | `TrackFeatureAdoption` |
| `PerformanceService` | `RecordPerfSnapshot`, `StartJfrUpload`, `CompleteJfrUpload` |
| `LegacyApiService` | `RecordDeprecatedApiUsage` |
| `WrappedService` | `Login`, `RecordCounters`, `SetLeaderboardVisibility` |

### Store / checkout

| Service | RPCs |
|---|---|
| `StoreService` | `Login`, `SetIncomingGiftPrivacy` |
| `PayNowService` | `PayNowCheckoutOpened/Closed` |
| `TebexService` | `TebexJsCheckoutOpened/Closed` |

### Misc

| Service | RPCs |
|---|---|
| `LanguageService` | `UpdateLanguage` |
| `SocialsService` | `Login`, `UnlinkSocial`, `SetSocialsVisibility` |
| `SprayService` | `Login`, `UseSpray`, `RemoveSpray`, `UpdateEquippedSprays` |
| `MarkerService` | `BroadcastNewMarker` |
| `SkyblockService` | `BroadcastDungeonUpdate` |
| `JamService` | `Login` |
| `LiveExperienceService` | `LoadLiveExperience`, `JoinLiveExperience` |
| `LogUploadService` | `StartLogUpload`, `CompleteLogUpload` |
| `PromotionService` | `Login`, `Start/EndPromotionView`, `ClaimOutplayedReward`, `ClaimRewindPuzzleReward`, `ClaimPendingReward` |
| `ChatService` | `SendChat` |
| `SettingService` | `UpdateLauncherSetting`, `UpdateClientSetting` |

## Location model (common/v1)

The friend system and presence run on this oneof:

```text
Location (outbound):
  public_server(1) | private_server(2) | local_server(3) | single_player(4)
  | minecraft_realms(5) | in_menus(6) | in_launcher(7) | hosted_world(8)
  | replay_world(9) | in_game(10) | rewind_world(11)

InboundLocation (client -> server):
  server(1) | single_player(2) | minecraft_realms(3) | in_menus(4)
  | in_launcher(5) | hosted_world(6) | replay_world(7) | in_game(8)
  | rewind_world(9)
```

`PublicServer` contains `server_mappings_id`, name, logo URL, colors,
versions, and `ServerRichStatus` (game_name, game_state, player_state,
map, sub_server, team sizes — source Apollo or client-parsed).

`InGame` has an `is_badlion` flag — Lunar detects Badlion players.

## GameIPC services (launcher <-> game, local)

| Service | RPCs |
|---|---|
| `AuthService` | `RefreshAccount`, `AddAccount` |
| `LaunchService` | `LaunchGame` |
| `BrowserService` | `OpenUrl` |
| `ChatService` | `ReceiveMessage` (in-game chat -> game) |
| `LocationService` | `UpdateFocus`, `UpdateLocation` |
| `PayNowService` | `OpenPayNowJsCheckout`, `CheckPayNowCapabilities` |
| `PromotionService` | `CheckPendingPromotion`, `PlayPromotion` |
| `TeBexService` | `OpenTebexJsCheckout`, `CheckTebexCapabilities` |
| `StyngrRadioService` | `FetchState`, `FetchPlaylists`, `StartPlaylist`, `NextTrack`, `SetPlaying`, `SetMuted`, `SetVolume`, `ToggleLiked`, `OpenSelector` |

## Apollo (server-owner API, parallel on the same WS)

For server integration (not client → server RPC, but server → clients
over the Apollo channel): beam, border, button, chat, coloredfire,
configurable, cooldown, cosmetic, entity, glow, heightlimit, hologram,
hud, inventory, limb, marker, modsetting, nametag, nickhider,
notification, packetenrichment (chat/inventory/melee/player/raytrace/
world), pingmarker, richpresence, serverlink, staffmod, stopwatch,
team, tebex, title, tntcountdown, totemcounter, transfer, vignette,
waypoint.

Details in `proto/extracted/lunarclient_apollo_*`.

## Push channels (server → client)

Every service with a `push.proto` sends unsolicited updates:

| Package | Push |
|---|---|
| cosmetic.v2 | `PlayerCosmeticsPushV2` |
| radio.v1 | `PlayerRadioPush` |
| friend.v1 | 7 push types (status, location, requests...) |
| conversation.v1 | 18 push types |
| badge.v1 | badge updates |
| emote.v1 | emote playbacks |
| notification.v1 | 4 push types |
| hostedworld.v1 | 4 push types |
| spray.v1 | 3 push types |
| skyblock.v1 | dungeon updates |
| protocol.v1 | generic push |
| performance.v1 | perf snapshots |
| marker.v1, jam.v1, store.v1, socials.v1, serverdiscovery.v1, paynow.v1, tebex.v1, chat.v1, launch (gameipc) | 1+ each |
