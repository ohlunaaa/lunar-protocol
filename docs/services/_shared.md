# Shared Types

Messages and enums without a service (common/push schemas).

## `lunarclient.apollo.beam.v1` ([source](../../proto/extracted/lunarclient_apollo_beam_v1_schema.proto))

- **DisplayBeaconBeamMessage**
  - `string` `id` = 1
  - `lunarclient.apollo.common.v1.Color` `color` = 2
  - `lunarclient.apollo.common.v1.BlockLocation` `location` = 3
- **RemoveBeaconBeamMessage**
  - `string` `id` = 1
- **ResetBeaconBeamsMessage**

## `lunarclient.apollo.border.v1` ([source](../../proto/extracted/lunarclient_apollo_border_v1_schema.proto))

- **DisplayBorderMessage**
  - `string` `id` = 1
  - `string` `world` = 2
  - `bool` `cancel_entry` = 3
  - `bool` `cancel_exit` = 4
  - `bool` `can_shrink_or_expand` = 5
  - `lunarclient.apollo.common.v1.Color` `color` = 6
  - `lunarclient.apollo.common.v1.Cuboid2D` `bounds` = 7
  - `int32` `duration_ticks` = 8
- **RemoveBorderMessage**
  - `string` `id` = 1
- **ResetBordersMessage**

## `lunarclient.apollo.button.v1` ([source](../../proto/extracted/lunarclient_apollo_button_v1_button.proto))

- **ButtonSize**
  - `float` `width` = 1
  - `float` `height` = 2
- **ButtonContentPart**
- **ButtonTooltip**
  - repeated `string` `adventure_json_lines` = 1
- **ButtonContent**
  - repeated `lunarclient.apollo.button.v1.ButtonContentPart` `parts` = 1
  - `float` `scale` = 2
- **Button**
- **ButtonUpdate**
  - `lunarclient.apollo.button.v1.ButtonContent` `content` = 1
  - `lunarclient.apollo.button.v1.ButtonTooltip` `tooltip` = 2

## `lunarclient.apollo.chat.v1` ([source](../../proto/extracted/lunarclient_apollo_chat_v1_schema.proto))

- **DisplayLiveChatMessageMessage**
  - `int32` `message_id` = 1
  - `string` `adventure_json_lines` = 2
- **RemoveLiveChatMessageMessage**
  - `int32` `message_id` = 1
- **ChatButton**
  - `lunarclient.apollo.button.v1.Button` `button` = 1
- **DisplayChatButtonsMessage**
  - repeated `lunarclient.apollo.chat.v1.ChatButton` `chat_buttons` = 1
- **RemoveChatButtonMessage**
  - `string` `id` = 1
- **ResetChatButtonsMessage**
- **UpdateChatButtonMessage**
  - `string` `id` = 1
  - `lunarclient.apollo.button.v1.ButtonUpdate` `update` = 2

## `lunarclient.apollo.coloredfire.v1` ([source](../../proto/extracted/lunarclient_apollo_coloredfire_v1_schema.proto))

- **OverrideColoredFireMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - `lunarclient.apollo.common.v1.Color` `color` = 2
- **ResetColoredFireMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
- **ResetColoredFiresMessage**

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_color.proto))

- **Color**
  - `int32` `color` = 1

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_component.proto))

- **Component**
  - `string` `content` = 1
  - `lunarclient.apollo.common.v1.Color` `color` = 2
  - repeated `lunarclient.apollo.common.v1.Component.TextDecorator` `decorators` = 3
  - repeated `lunarclient.apollo.common.v1.Component` `children` = 4
  - enum **TextDecorator**:
    - `TEXT_DECORATOR_UNSPECIFIED = 0`
    - `TEXT_DECORATOR_OBFUSCATED = 1`
    - `TEXT_DECORATOR_BOLD = 2`
    - `TEXT_DECORATOR_STRIKETHROUGH = 3`
    - `TEXT_DECORATOR_UNDERLINED = 4`
    - `TEXT_DECORATOR_ITALIC = 5`

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_cuboid.proto))

- **Cuboid2D**
  - `double` `min_x` = 1
  - `double` `min_z` = 2
  - `double` `max_x` = 3
  - `double` `max_z` = 4
- **Cuboid3D**
  - `double` `min_x` = 1
  - `double` `min_y` = 2
  - `double` `min_z` = 3
  - `double` `max_x` = 4
  - `double` `max_y` = 5
  - `double` `max_z` = 6

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_entityid.proto))

- **EntityId**
  - `int32` `entity_id` = 1
  - `lunarclient.apollo.common.v1.Uuid` `entity_uuid` = 2

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_icon.proto))

- **ItemStackIcon**
- **SimpleResourceLocationIcon**
  - `string` `resource_location` = 1
  - `int32` `size` = 2
- **AdvancedResourceLocationIcon**
  - `string` `resource_location` = 1
  - `float` `width` = 2
  - `float` `height` = 3
  - `float` `min_u` = 4
  - `float` `max_u` = 5
  - `float` `min_v` = 6
  - `float` `max_v` = 7
- **ResourceLocationIcon**
  - `string` `resource_location` = 1
- **Icon**

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_item.proto))

- **CustomModelData**
  - repeated `float` `floats` = 1
  - repeated `bool` `flags` = 2
  - repeated `string` `strings` = 3
  - repeated `int32` `colors` = 4

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_location.proto))

- **BlockLocation**
  - `string` `world` = 1
  - `sint32` `x` = 2
  - `sint32` `y` = 3
  - `sint32` `z` = 4
- **PlayerLocation**
  - `lunarclient.apollo.common.v1.Location` `location` = 1
  - `float` `yaw` = 2
  - `float` `pitch` = 3
- **Location**
  - `string` `world` = 1
  - `double` `x` = 2
  - `double` `y` = 3
  - `double` `z` = 4

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_profile.proto))

- **Profile**
  - `lunarclient.apollo.common.v1.Uuid` `id` = 1
  - `string` `texture` = 2
  - `string` `signature` = 3

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_sound.proto))

- **SimpleResourceLocationSound**
  - `string` `resource_location` = 1
- **Sound**

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_uuid.proto))

- **Uuid**
  - `fixed64` `high64` = 1
  - `fixed64` `low64` = 2

## `lunarclient.apollo.common.v1` ([source](../../proto/extracted/lunarclient_apollo_common_v1_version.proto))

- **MinecraftVersion**
  - `string` `enum` = 1
- **LunarClientVersion**
  - `string` `git_branch` = 1
  - `string` `git_commit` = 2
  - `string` `semver` = 3

## `lunarclient.apollo.configurable.v1` ([source](../../proto/extracted/lunarclient_apollo_configurable_v1_schema.proto))

- **ConfigurableSettings**
- **PropertiesEntry**
  - `string` `key` = 1
  - `google.protobuf.Value` `value` = 2
- **OverrideConfigurableSettingsMessage**
  - repeated `lunarclient.apollo.configurable.v1.ConfigurableSettings` `configurable_settings` = 1

## `lunarclient.apollo.cooldown.v1` ([source](../../proto/extracted/lunarclient_apollo_cooldown_v1_schema.proto))

- **DisplayCooldownMessage**
  - `string` `name` = 1
  - `google.protobuf.Duration` `duration` = 2
  - `lunarclient.apollo.common.v1.Icon` `icon` = 3
  - `lunarclient.apollo.cooldown.v1.CooldownStyle` `style` = 4
- **RemoveCooldownMessage**
  - `string` `name` = 1
- **ResetCooldownsMessage**
- **CooldownStyle**
  - `lunarclient.apollo.common.v1.Color` `circle_start_color` = 1
  - `lunarclient.apollo.common.v1.Color` `circle_end_color` = 2
  - `lunarclient.apollo.common.v1.Color` `circle_edge_color` = 3
  - `lunarclient.apollo.common.v1.Color` `text_color` = 4

## `lunarclient.apollo.cosmetic.v1` ([source](../../proto/extracted/lunarclient_apollo_cosmetic_v1_schema.proto))

- **EquipNpcCosmeticsMessage**
  - `lunarclient.apollo.common.v1.Uuid` `npc_uuid` = 1
  - repeated `lunarclient.apollo.cosmetic.v1.Cosmetic` `cosmetics` = 2
  - `bool` `copy_local_cosmetics` = 3
- **UnequipNpcCosmeticsMessage**
  - `lunarclient.apollo.common.v1.Uuid` `npc_uuid` = 1
  - repeated `int32` `cosmetic_ids` = 2
- **ResetNpcCosmeticsMessage**
  - `lunarclient.apollo.common.v1.Uuid` `npc_uuid` = 1
- **Cosmetic**
- **HatOptions**
  - `bool` `show_over_helmet` = 1
  - `bool` `show_over_skin_layer` = 2
  - `float` `height_offset` = 3
- **CloakOptions**
  - `bool` `use_cloth_physics` = 1
- **PetOptions**
  - `bool` `flip_shoulder` = 1
- **BodyOptions**
  - `bool` `show_over_chestplate` = 1
  - `bool` `show_over_leggings` = 2
  - `bool` `show_over_boots` = 3
- **StartNpcEmoteMessage**
  - `lunarclient.apollo.common.v1.Uuid` `npc_uuid` = 1
  - `lunarclient.apollo.cosmetic.v1.Emote` `emote` = 2
- **StopNpcEmoteMessage**
  - `lunarclient.apollo.common.v1.Uuid` `npc_uuid` = 1
- **ResetNpcEmotesMessage**
- **Emote**
  - `int32` `id` = 1
  - `int32` `metadata` = 2
- **DisplaySprayMessage**
  - `int32` `spray_id` = 1
  - `lunarclient.apollo.common.v1.BlockLocation` `location` = 2
  - `lunarclient.apollo.packetenrichment.v1.Direction` `facing` = 3
  - `float` `rotation` = 4
  - `google.protobuf.Duration` `duration` = 5
- **RemoveSprayMessage**
  - `int32` `spray_id` = 1
  - `lunarclient.apollo.common.v1.BlockLocation` `location` = 2
- **ResetSpraysMessage**

## `lunarclient.apollo.entity.v1` ([source](../../proto/extracted/lunarclient_apollo_entity_v1_schema.proto))

- **OverrideRainbowSheepMessage**
  - repeated `lunarclient.apollo.common.v1.EntityId` `entity_ids` = 1
- **ResetRainbowSheepMessage**
  - repeated `lunarclient.apollo.common.v1.EntityId` `entity_ids` = 1
- **FlipEntityMessage**
  - repeated `lunarclient.apollo.common.v1.EntityId` `entity_ids` = 1
- **ResetFlipedEntityMessage**
  - repeated `lunarclient.apollo.common.v1.EntityId` `entity_ids` = 1

## `lunarclient.apollo.evnt.v1` ([source](../../proto/extracted/lunarclient_apollo_evnt_v1_character.proto))

- **CharacterAbilityMessage**
  - `lunarclient.apollo.evnt.v1.CharacterType` `character_type` = 1
  - repeated `string` `abilities_adventure` = 2
- **OverrideCharacterCosmeticMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - `lunarclient.apollo.evnt.v1.CharacterType` `character_type` = 2
  - `string` `suit_name` = 3
- **OverrideCharacterAbilityMessage**
  - repeated `lunarclient.apollo.evnt.v1.CharacterAbilityMessage` `abilities` = 1
- **OverrideCharacterMessage**
  - `lunarclient.apollo.evnt.v1.CharacterType` `character_type` = 1
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 2
  - `lunarclient.apollo.common.v1.Color` `color` = 3
  - `bool` `equipped` = 4
  - `string` `suit_name` = 5

## `lunarclient.apollo.evnt.v1` ([source](../../proto/extracted/lunarclient_apollo_evnt_v1_cosmetics.proto))

- **OverrideCosmeticResourcesMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - `lunarclient.apollo.evnt.v1.CharacterType` `character_type` = 2
  - `string` `model_path` = 3
  - `string` `animation_path` = 4
  - `string` `texture_path` = 5
- **UpdateCosmeticsMessage**
  - repeated `string` `model_locations` = 1
  - repeated `string` `animation_locations` = 2
- **OverrideCharacterSuitResourcesMessage**
  - `lunarclient.apollo.evnt.v1.CharacterType` `character_type` = 1
  - repeated `string` `suit_names` = 2

## `lunarclient.apollo.evnt.v1` ([source](../../proto/extracted/lunarclient_apollo_evnt_v1_event.proto))

- **EventPlayerStatusMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - `float` `health` = 2
  - `float` `ultimate_percentage` = 3
  - `int64` `respawn_at` = 4
- **EventStatusOverviewMessage**
  - repeated `lunarclient.apollo.evnt.v1.EventPlayerStatusMessage` `team_one_status` = 1
  - repeated `lunarclient.apollo.evnt.v1.EventPlayerStatusMessage` `team_two_status` = 2
- **EventTeamStatusMessage**
  - `float` `top_wither_health` = 1
  - `float` `top_crystal_health` = 2
  - `float` `middle_wither_health` = 3
  - `float` `middle_crystal_health` = 4
  - `float` `bottom_wither_health` = 5
  - `float` `bottom_crystal_health` = 6
  - `float` `dragon_health` = 7
- **EventGameOverviewMessage**
  - `lunarclient.apollo.evnt.v1.EventTeamStatusMessage` `team_one_status` = 1
  - `lunarclient.apollo.evnt.v1.EventTeamStatusMessage` `team_two_status` = 2
  - `float` `tier_three_health` = 3
  - `int64` `game_start_time` = 4
  - `bool` `wither_shields` = 5
  - `bool` `lock_game_time` = 6
  - `int64` `mid_respawn_time` = 7
- **EventPlayerMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - `string` `player_name_adventure` = 2
  - `lunarclient.apollo.evnt.v1.CharacterType` `character_type` = 3
  - `bool` `team_one` = 4
- **EventOverviewMessage**
  - repeated `lunarclient.apollo.evnt.v1.EventPlayerMessage` `players` = 1

## `lunarclient.apollo.evnt.v1` ([source](../../proto/extracted/lunarclient_apollo_evnt_v1_gui.proto))

- **OpenGuiMessage**
  - `lunarclient.apollo.evnt.v1.GuiType` `gui_type` = 1
- **CloseGuiMessage**
  - `lunarclient.apollo.evnt.v1.GuiType` `gui_type` = 1

## `lunarclient.apollo.evnt.v1` ([source](../../proto/extracted/lunarclient_apollo_evnt_v1_hearttexture.proto))

- **OverrideHeartTextureMessage**
  - `int32` `location_x` = 1
  - `bool` `hardcore` = 2
- **ResetHeartTextureMessage**

## `lunarclient.apollo.glow.v1` ([source](../../proto/extracted/lunarclient_apollo_glow_v1_schema.proto))

- **OverrideGlowEffectMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - `lunarclient.apollo.common.v1.Color` `color` = 2
- **ResetGlowEffectMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
- **ResetGlowEffectsMessage**

## `lunarclient.apollo.heightlimit.v1` ([source](../../proto/extracted/lunarclient_apollo_heightlimit_v1_schema.proto))

- **OverrideHeightLimitMessage**
  - `string` `world` = 1
  - `int32` `limit` = 2
  - `string` `display_name_adventure_json_lines` = 3
- **RemoveHeightLimitMessage**
  - `string` `world` = 1
- **ResetHeightLimitsMessage**

## `lunarclient.apollo.hologram.v1` ([source](../../proto/extracted/lunarclient_apollo_hologram_v1_schema.proto))

- **DisplayHologramMessage**
  - `string` `id` = 1
  - `lunarclient.apollo.common.v1.Location` `location` = 2
  - `bool` `show_through_walls` = 4
  - `bool` `show_shadow` = 5
  - `bool` `show_background` = 6
  - repeated `string` `adventure_json_lines` = 7
- **RemoveHologramMessage**
  - `string` `id` = 1
- **ResetHologramsMessage**

## `lunarclient.apollo.hud.v1` ([source](../../proto/extracted/lunarclient_apollo_hud_v1_position.proto))

- **HudPosition**
  - `float` `x` = 1
  - `float` `y` = 2

## `lunarclient.apollo.inventory.v1` ([source](../../proto/extracted/lunarclient_apollo_inventory_v1_schema.proto))

- **InventoryButton**
  - `lunarclient.apollo.button.v1.Button` `button` = 1
  - `lunarclient.apollo.inventory.v1.InventoryType` `inventory_type` = 2
  - `lunarclient.apollo.inventory.v1.InventoryButtonBox` `box` = 3
- **DisplayInventoryButtonsMessage**
  - repeated `lunarclient.apollo.inventory.v1.InventoryButton` `inventory_buttons` = 1
- **RemoveInventoryButtonMessage**
  - `string` `id` = 1
- **ResetInventoryButtonsMessage**
- **UpdateInventoryButtonMessage**
  - `string` `id` = 1
  - `lunarclient.apollo.button.v1.ButtonUpdate` `update` = 2

## `lunarclient.apollo.limb.v1` ([source](../../proto/extracted/lunarclient_apollo_limb_v1_schema.proto))

- **HideArmorPiecesMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - repeated `lunarclient.apollo.limb.v1.ArmorPiece` `armor_pieces` = 2
- **ResetArmorPiecesMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - repeated `lunarclient.apollo.limb.v1.ArmorPiece` `armor_pieces` = 2
- **HideBodyPartMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - repeated `lunarclient.apollo.limb.v1.BodyPart` `body_parts` = 2
- **ResetBodyPartMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - repeated `lunarclient.apollo.limb.v1.BodyPart` `body_parts` = 2

## `lunarclient.apollo.marker.v1` ([source](../../proto/extracted/lunarclient_apollo_marker_v1_schema.proto))

- **DisplayMarkerMessage**
  - `string` `id` = 1
  - `lunarclient.apollo.common.v1.Location` `location` = 2
  - `lunarclient.apollo.common.v1.Uuid` `owner_id` = 3
  - `string` `owner_name` = 4
  - `lunarclient.apollo.marker.v1.MarkerFlag` `flag` = 5
  - `lunarclient.apollo.marker.v1.MarkerTarget` `target` = 6
  - `google.protobuf.Duration` `duration` = 7
  - `bool` `in_game_notification` = 8
  - `bool` `chat_notify` = 9
  - `bool` `middle_click_remove` = 10
  - `lunarclient.apollo.marker.v1.MarkerStyle` `style` = 11
- **RemoveMarkerMessage**
  - `string` `id` = 1
- **ResetMarkersMessage**
- **MarkerFlag**
- **NormalMarker**
  - `lunarclient.apollo.common.v1.Color` `color` = 1
- **DangerMarker**
  - `lunarclient.apollo.common.v1.Color` `color` = 1
- **InfoMarker**
  - `lunarclient.apollo.common.v1.Color` `color` = 1
- **InterestMarker**
  - `lunarclient.apollo.common.v1.Color` `color` = 1
- **MarkerTarget**
- **ItemTarget**
  - `lunarclient.apollo.common.v1.ItemStackIcon` `item_stack` = 1
- **BlockTarget**
  - `lunarclient.apollo.common.v1.ItemStackIcon` `item_stack` = 1
- **EntityTarget**
  - `string` `entity_type` = 1
- **PlayerTarget**
  - `lunarclient.apollo.common.v1.Uuid` `uuid` = 1
  - `string` `name` = 2
- **MarkerStyle**
  - `float` `scale` = 1
  - `bool` `animate_marker_on_hover` = 2
  - `bool` `compact_mode` = 3
  - `bool` `text_shadow` = 4
  - `string` `owner_suffix` = 5
  - `lunarclient.apollo.marker.v1.MarkerOwnerDisplay` `owner_display` = 6
  - `lunarclient.apollo.marker.v1.MarkerDisplayCondition` `show_owner` = 7
  - `lunarclient.apollo.marker.v1.MarkerDisplayCondition` `show_coordinates` = 8
  - `lunarclient.apollo.marker.v1.MarkerDisplayCondition` `show_distance` = 9
  - `lunarclient.apollo.marker.v1.MarkerDisplayCondition` `show_description` = 10
  - `lunarclient.apollo.marker.v1.MarkerDescriptionDisplay` `description_display` = 11

## `lunarclient.apollo.modsetting.v1` ([source](../../proto/extracted/lunarclient_apollo_modsetting_v1_schema.proto))

- **InstalledModsRequest**
  - `bytes` `request_id` = 1
- **InstalledModsResponse**
  - `bytes` `request_id` = 1
  - `int32` `page` = 2
  - `int32` `total_pages` = 3
  - repeated `lunarclient.apollo.modsetting.v1.ModGroup` `mod_groups` = 4
- **ModStatusRequest**
  - `bytes` `request_id` = 1
- **ModStatusResponse**
  - `bytes` `request_id` = 1
  - `int32` `page` = 2
  - `int32` `total_pages` = 3
  - repeated `lunarclient.apollo.modsetting.v1.ModOptionStatus` `mod_options` = 4
- **ModOptionStatus**
  - `string` `key` = 1
  - `google.protobuf.Value` `value` = 2
- **ModGroup**
  - `lunarclient.apollo.modsetting.v1.ModGroup.Type` `type` = 1
  - repeated `lunarclient.apollo.modsetting.v1.Mod` `mods` = 2
  - enum **Type**:
    - `TYPE_UNSPECIFIED = 0`
    - `TYPE_FABRIC_INTERNAL = 1`
    - `TYPE_FABRIC_EXTERNAL = 2`
    - `TYPE_FORGE_INTERNAL = 3`
    - `TYPE_FORGE_EXTERNAL = 4`
- **Mod**
  - `string` `id` = 1
  - `string` `version` = 2

## `lunarclient.apollo.nametag.v1` ([source](../../proto/extracted/lunarclient_apollo_nametag_v1_schema.proto))

- **OverrideNametagMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - repeated `string` `adventure_json_lines` = 3
  - `lunarclient.apollo.nametag.v1.NametagVisibilityOverride` `visibility_override` = 4
- **ResetNametagMessage**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
- **ResetNametagsMessage**

## `lunarclient.apollo.nickhider.v1` ([source](../../proto/extracted/lunarclient_apollo_nickhider_v1_schema.proto))

- **OverrideNickHiderMessage**
  - `string` `nick` = 1
- **ResetNickHiderMessage**

## `lunarclient.apollo.notification.v1` ([source](../../proto/extracted/lunarclient_apollo_notification_v1_schema.proto))

- **DisplayNotificationMessage**
  - `google.protobuf.Duration` `display_time` = 4
  - `string` `title_adventure_json_lines` = 5
  - `string` `description_adventure_json_lines` = 6
  - `lunarclient.apollo.common.v1.Icon` `icon` = 7
- **ResetNotificationsMessage**

## `lunarclient.apollo.packetenrichment.v1` ([source](../../proto/extracted/lunarclient_apollo_packetenrichment_v1_chat.proto))

- **PlayerChatOpenMessage**
  - `lunarclient.apollo.packetenrichment.v1.PlayerInfo` `player_info` = 1
  - `lunarclient.apollo.packetenrichment.v1.PacketInfo` `packet_info` = 2
- **PlayerChatCloseMessage**
  - `lunarclient.apollo.packetenrichment.v1.PlayerInfo` `player_info` = 1
  - `lunarclient.apollo.packetenrichment.v1.PacketInfo` `packet_info` = 2

## `lunarclient.apollo.packetenrichment.v1` ([source](../../proto/extracted/lunarclient_apollo_packetenrichment_v1_inventory.proto))

- **PlayerInventoryOpenMessage**
  - `lunarclient.apollo.packetenrichment.v1.PlayerInfo` `player_info` = 1
  - `lunarclient.apollo.packetenrichment.v1.PacketInfo` `packet_info` = 2
- **PlayerInventoryCloseMessage**
  - `lunarclient.apollo.packetenrichment.v1.PlayerInfo` `player_info` = 1
  - `lunarclient.apollo.packetenrichment.v1.PacketInfo` `packet_info` = 2

## `lunarclient.apollo.packetenrichment.v1` ([source](../../proto/extracted/lunarclient_apollo_packetenrichment_v1_melee.proto))

- **PlayerAttackMessage**
  - `lunarclient.apollo.packetenrichment.v1.PacketInfo` `packet_info` = 1
  - `lunarclient.apollo.packetenrichment.v1.PlayerInfo` `target_info` = 2
  - `lunarclient.apollo.packetenrichment.v1.PlayerInfo` `attacker_info` = 3
  - `double` `distance` = 4

## `lunarclient.apollo.packetenrichment.v1` ([source](../../proto/extracted/lunarclient_apollo_packetenrichment_v1_packet.proto))

- **PacketInfo**
  - `google.protobuf.Timestamp` `instantiation_time` = 1

## `lunarclient.apollo.packetenrichment.v1` ([source](../../proto/extracted/lunarclient_apollo_packetenrichment_v1_player.proto))

- **PlayerInfo**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - `lunarclient.apollo.common.v1.PlayerLocation` `location` = 2
  - `bool` `sneaking` = 3
  - `bool` `sprinting` = 4
  - `bool` `jumping` = 5
  - `float` `forward_speed` = 6
  - `float` `strafe_speed` = 7

## `lunarclient.apollo.packetenrichment.v1` ([source](../../proto/extracted/lunarclient_apollo_packetenrichment_v1_raytrace.proto))

- **RayTraceResult**
- **BlockHit**
  - `lunarclient.apollo.common.v1.Location` `hit_location` = 1
  - `lunarclient.apollo.common.v1.BlockLocation` `block_location` = 2
  - `lunarclient.apollo.packetenrichment.v1.Direction` `direction` = 3
- **EntityHit**
  - `lunarclient.apollo.common.v1.Location` `hit_location` = 1
  - `lunarclient.apollo.common.v1.EntityId` `entity_id` = 2
- **Miss**

## `lunarclient.apollo.packetenrichment.v1` ([source](../../proto/extracted/lunarclient_apollo_packetenrichment_v1_world.proto))

- **PlayerUseItemMessage**
  - `lunarclient.apollo.packetenrichment.v1.PacketInfo` `packet_info` = 1
  - `lunarclient.apollo.packetenrichment.v1.PlayerInfo` `player_info` = 2
  - `bool` `main_hand` = 3
- **PlayerUseItemBucketMessage**
  - `lunarclient.apollo.packetenrichment.v1.PacketInfo` `packet_info` = 1
  - `lunarclient.apollo.packetenrichment.v1.PlayerInfo` `player_info` = 2
  - `lunarclient.apollo.packetenrichment.v1.RayTraceResult` `ray_trace_result` = 3

## `lunarclient.apollo.paynow.v1` ([source](../../proto/extracted/lunarclient_apollo_paynow_v1_schema.proto))

- **OpenPayNowEmbeddedCheckoutMessage**
  - `string` `checkout_token` = 1

## `lunarclient.apollo.pingmarker.v1` ([source](../../proto/extracted/lunarclient_apollo_pingmarker_v1_schema.proto))

- **SetPingMarkerTypeMessage**
  - `string` `id` = 1
  - `lunarclient.apollo.common.v1.Icon` `icon` = 2
- **SetPingMarkerTypesMessage**
  - repeated `lunarclient.apollo.pingmarker.v1.SetPingMarkerTypeMessage` `types` = 1
- **RemovePingMarkerTypeMessage**
  - `string` `id` = 1
- **ResetPingMarkerTypesMessage**
- **RequestPlayerPingMessage**
  - `lunarclient.apollo.common.v1.Uuid` `id` = 1
  - `string` `type` = 2
  - `lunarclient.apollo.common.v1.Location` `source_location` = 3
  - `lunarclient.apollo.common.v1.Location` `target_location` = 4
- **DisplayPlayerPingMessage**
  - `lunarclient.apollo.common.v1.Uuid` `id` = 1
  - `string` `type` = 2
  - `lunarclient.apollo.common.v1.Location` `location` = 3
  - `lunarclient.apollo.common.v1.Color` `color` = 4
  - `lunarclient.apollo.common.v1.Icon` `icon` = 5
  - `lunarclient.apollo.common.v1.Sound` `sound` = 6
  - `google.protobuf.Duration` `duration` = 7
  - `bool` `focus` = 8
- **RemovePlayerPingMessage**
  - `lunarclient.apollo.common.v1.Uuid` `id` = 1
- **ResetPlayerPingMessage**

## `lunarclient.apollo.player.v1` ([source](../../proto/extracted/lunarclient_apollo_player_v1_handshake.proto))

- **ModMessage**
  - `string` `id` = 1
  - `string` `name` = 2
  - `string` `version` = 3
  - `lunarclient.apollo.player.v1.ModMessage.Type` `type` = 4
  - enum **Type**:
    - `TYPE_UNSPECIFIED = 0`
    - `TYPE_FABRIC_INTERNAL = 1`
    - `TYPE_FABRIC_EXTERNAL = 2`
    - `TYPE_FORGE_INTERNAL = 3`
    - `TYPE_FORGE_EXTERNAL = 4`
- **PlayerHandshakeMessage**
  - `lunarclient.apollo.common.v1.MinecraftVersion` `minecraft_version` = 1
  - `lunarclient.apollo.common.v1.LunarClientVersion` `lunar_client_version` = 2
  - `lunarclient.apollo.player.v1.EmbeddedCheckoutSupport` `embedded_checkout_support` = 4
  - **ModStatusEntry**
    - `string` `key` = 1
    - `google.protobuf.Value` `value` = 2

## `lunarclient.apollo.player.v1` ([source](../../proto/extracted/lunarclient_apollo_player_v1_world.proto))

- **UpdatePlayerWorldMessage**
  - `string` `world` = 1

## `lunarclient.apollo.richpresence.v1` ([source](../../proto/extracted/lunarclient_apollo_richpresence_v1_schema.proto))

- **OverrideServerRichPresenceMessage**
  - `string` `game_name` = 1
  - `string` `game_variant_name` = 2
  - `string` `game_state` = 3
  - `string` `player_state` = 4
  - `string` `map_name` = 5
  - `string` `sub_server` = 6
  - `int32` `team_current_size` = 7
  - `int32` `team_max_size` = 8
- **ResetServerRichPresenceMessage**

## `lunarclient.apollo.serverlink.v1` ([source](../../proto/extracted/lunarclient_apollo_serverlink_v1_serverlink.proto))

- **OverrideServerLinkResourceMessage**
  - `lunarclient.apollo.common.v1.ResourceLocationIcon` `icon` = 1
- **ResetServerLinkResourceMessage**
- **AddServerLinkMessage**
  - repeated `lunarclient.apollo.serverlink.v1.ServerLink` `server_links` = 1
- **RemoveServerLinkMessage**
  - repeated `string` `server_link_ids` = 1
- **ResetServerLinksMessage**
- **ServerLink**
  - `string` `id` = 1
  - `string` `display_name_adventure_json_lines` = 2
  - `string` `url` = 3

## `lunarclient.apollo.staffmod.v1` ([source](../../proto/extracted/lunarclient_apollo_staffmod_v1_schema.proto))

- **EnableStaffModsMessage**
  - repeated `lunarclient.apollo.staffmod.v1.StaffMod` `staff_mods` = 1
  - `bool` `enabled_by_default` = 2
- **DisableStaffModsMessage**
  - repeated `lunarclient.apollo.staffmod.v1.StaffMod` `staff_mods` = 1

## `lunarclient.apollo.stopwatch.v1` ([source](../../proto/extracted/lunarclient_apollo_stopwatch_v1_schema.proto))

- **AddStopwatchMessage**
  - `string` `id` = 1
  - `string` `name` = 2
  - `bool` `reset_on_start` = 3
  - `bool` `prevent_modification` = 4
  - `bool` `hide_when_stopped` = 5
  - `string` `display_format` = 6
  - `lunarclient.apollo.common.v1.Color` `text_color` = 7
  - `lunarclient.apollo.hud.v1.HudPosition` `hud_position` = 8
- **RemoveStopwatchMessage**
  - `string` `id` = 1
- **StartStopwatchMessage**
  - `string` `id` = 1
- **StopStopwatchMessage**
  - `string` `id` = 1
- **ResetStopwatchMessage**
  - `string` `id` = 1
- **ResetStopwatchesMessage**
- **AddTimerMessage**
  - `string` `id` = 1
  - `string` `name` = 2
  - `google.protobuf.Duration` `duration` = 3
  - `bool` `loop` = 4
  - `bool` `prevent_modification` = 5
  - `bool` `in_game_notification` = 6
  - `bool` `hide_when_stopped` = 7
  - `string` `display_format` = 8
  - `string` `title_text_adventure_json_lines` = 9
  - `lunarclient.apollo.common.v1.Color` `text_color` = 10
  - `lunarclient.apollo.hud.v1.HudPosition` `hud_position` = 11
- **RemoveTimerMessage**
  - `string` `id` = 1
- **StartTimerMessage**
  - `string` `id` = 1
- **StopTimerMessage**
  - `string` `id` = 1
- **ResetTimerMessage**
  - `string` `id` = 1
- **ResetTimersMessage**

## `lunarclient.apollo.team.v1` ([source](../../proto/extracted/lunarclient_apollo_team_v1_schema.proto))

- **TeamMember**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - `lunarclient.apollo.common.v1.Location` `location` = 3
  - `lunarclient.apollo.common.v1.Color` `marker_color` = 4
  - `string` `adventure_json_player_name` = 5
- **UpdateTeamMembersMessage**
  - repeated `lunarclient.apollo.team.v1.TeamMember` `members` = 1
- **ResetTeamMembersMessage**

## `lunarclient.apollo.tebex.v1` ([source](../../proto/extracted/lunarclient_apollo_tebex_v1_schema.proto))

- **OpenTebexEmbeddedCheckoutMessage**
  - `string` `basket_ident` = 1
  - `string` `locale` = 2

## `lunarclient.apollo.title.v1` ([source](../../proto/extracted/lunarclient_apollo_title_v1_schema.proto))

- **DisplayTitleMessage**
  - `lunarclient.apollo.title.v1.TitleType` `title_type` = 1
  - `float` `scale` = 3
  - `google.protobuf.Duration` `fade_in_time` = 4
  - `google.protobuf.Duration` `display_time` = 5
  - `google.protobuf.Duration` `fade_out_time` = 6
  - `string` `adventure_json_message` = 7
  - `float` `interpolation_scale` = 8
  - `float` `interpolation_rate` = 9
- **ResetTitlesMessage**

## `lunarclient.apollo.tntcountdown.v1` ([source](../../proto/extracted/lunarclient_apollo_tntcountdown_v1_schema.proto))

- **SetTntCountdownMessage**
  - `lunarclient.apollo.common.v1.EntityId` `entity_id` = 1
  - `int32` `duration_ticks` = 2

## `lunarclient.apollo.totemcounter.v1` ([source](../../proto/extracted/lunarclient_apollo_totemcounter_v1_schema.proto))

- **TotemCounter**
  - `lunarclient.apollo.common.v1.Uuid` `player_uuid` = 1
  - `int32` `pops` = 2
- **OverrideTotemCountersMessage**
  - repeated `lunarclient.apollo.totemcounter.v1.TotemCounter` `totem_counters` = 1
- **ResetTotemCounterMessage**
  - repeated `lunarclient.apollo.common.v1.Uuid` `player_uuids` = 1
- **ResetTotemCountersMessage**

## `lunarclient.apollo.transfer.v1` ([source](../../proto/extracted/lunarclient_apollo_transfer_v1_schema.proto))

- **PingData**
  - `string` `server_ip` = 1
  - `lunarclient.apollo.transfer.v1.PingData.Status` `status` = 2
  - `int32` `ping` = 3
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_SUCCESS = 1`
    - `STATUS_TIMED_OUT = 2`
- **PingRequest**
  - `bytes` `request_id` = 1
  - repeated `string` `server_ips` = 2
- **PingResponse**
  - `bytes` `request_id` = 1
  - repeated `lunarclient.apollo.transfer.v1.PingData` `ping_data` = 2
- **TransferRequest**
  - `bytes` `request_id` = 1
  - `string` `server_ip` = 2
- **TransferResponse**
  - `bytes` `request_id` = 1
  - `lunarclient.apollo.transfer.v1.TransferResponse.Status` `status` = 2
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_ACCEPTED = 1`
    - `STATUS_REJECTED = 2`

## `lunarclient.apollo.vignette.v1` ([source](../../proto/extracted/lunarclient_apollo_vignette_v1_schema.proto))

- **DisplayVignetteMessage**
  - `string` `resource_location` = 1
  - `float` `opacity` = 2
- **ResetVignetteMessage**

## `lunarclient.apollo.waypoint.v1` ([source](../../proto/extracted/lunarclient_apollo_waypoint_v1_schema.proto))

- **DisplayWaypointMessage**
  - `string` `name` = 1
  - `lunarclient.apollo.common.v1.BlockLocation` `location` = 2
  - `lunarclient.apollo.common.v1.Color` `color` = 3
  - `bool` `prevent_removal` = 4
  - `bool` `hidden` = 5
  - `bool` `show_beam` = 6
  - `bool` `highlight_block` = 7
  - `float` `highlight_block_line_width` = 8
  - `lunarclient.apollo.waypoint.v1.WaypointTextStyle` `style` = 9
- **ShowWaypointMessage**
  - `string` `name` = 1
- **HideWaypointMessage**
  - `string` `name` = 1
- **RemoveWaypointMessage**
  - `string` `name` = 1
- **ResetWaypointsMessage**
- **WaypointTextStyle**
  - `bool` `show_text` = 1
  - `bool` `only_show_text_when_looking_near` = 2
  - `bool` `show_icons` = 3
  - `float` `text_icon_scale` = 4
  - `float` `label_scale` = 5
  - `float` `box_padding` = 6
  - `bool` `box_borders` = 7
  - `bool` `text_shadow` = 8
  - `bool` `show_distance` = 9

## `lunarclient.authenticator.v1` ([source](../../proto/extracted/lunarclient_authenticator_v1_message.proto))

- **HelloMessage**
  - `lunarclient.common.v1.UuidAndUsername` `identity` = 1
  - `string` `initiator` = 2
- **EncryptionRequestMessage**
  - `bytes` `public_key` = 1
  - `bytes` `random_bytes` = 2
- **EncryptionFailMessage**
  - `string` `reason` = 1
- **EncryptionResponseMessage**
  - `bytes` `secret_key` = 1
  - `bytes` `public_key` = 2
- **AuthSuccessMessage**
  - `string` `jwt` = 1
  - `bytes` `encrypted_jwt` = 2

## `lunarclient.authenticator.v1` ([source](../../proto/extracted/lunarclient_authenticator_v1_protocol.proto))

- **ServerboundWebSocketMessage**
- **ClientboundWebSocketMessage**

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_color.proto))

- **Color**
  - `int32` `color` = 1

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_gift.proto))

- **GiftInfo**

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_inbound_location.proto))

- **InboundServer**
  - `string` `server_ip` = 1
  - `lunarclient.common.v1.ServerRichStatus` `rich_status` = 2
- **InboundSinglePlayer**
- **InboundMinecraftRealms**
- **InboundInMenus**
- **InboundInLauncher**
- **InboundHostedWorld**
  - `lunarclient.common.v1.Uuid` `world_host` = 1
- **InboundReplayWorld**
- **InboundRewindWorld**
  - `lunarclient.common.v1.InboundRewindWorld.RewindWorldType` `type` = 1
  - enum **RewindWorldType**:
    - `REWIND_WORLD_TYPE_UNSPECIFIED = 0`
    - `REWIND_WORLD_TYPE_PROJECT = 1`
    - `REWIND_WORLD_TYPE_PREVIEW = 2`
- **InboundInGame**
  - `lunarclient.common.v1.MinecraftVersion` `minecraft_version` = 1
  - `bool` `is_launch` = 2
  - `lunarclient.common.v1.PlayerModpack` `modpack` = 3
  - `bool` `is_badlion` = 4
- **InboundLocation**

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_location.proto))

- **ServerRichStatus**
  - `lunarclient.common.v1.ServerRichStatus.Source` `source` = 8
  - `string` `game_name` = 1
  - `string` `game_variant_name` = 9
  - `string` `game_state` = 2
  - `string` `player_state` = 3
  - `string` `map_name` = 4
  - `string` `sub_server` = 5
  - `int32` `team_current_size` = 6
  - `int32` `team_max_size` = 7
  - enum **Source**:
    - `SOURCE_UNSPECIFIED = 0`
    - `SOURCE_APOLLO = 1`
    - `SOURCE_LUNAR_CLIENT_PARSED = 2`
- **PublicServerColors**
  - `lunarclient.common.v1.Color` `primary` = 1
  - `lunarclient.common.v1.Color` `secondary` = 2
- **PublicServerVersions**
  - repeated `lunarclient.common.v1.MinecraftVersion` `supported` = 1
  - `lunarclient.common.v1.MinecraftVersion` `recommended` = 2
- **PublicServer**
  - `string` `server_mappings_id` = 1
  - `string` `name` = 2
  - `string` `logo_url` = 8
  - `string` `primary_address` = 3
  - `lunarclient.common.v1.PublicServerColors` `colors` = 4
  - `lunarclient.common.v1.PublicServerVersions` `versions` = 5
  - `lunarclient.common.v1.ServerRichStatus` `rich_status` = 7
- **PrivateServer**
- **LocalServer**
  - `lunarclient.common.v1.ServerRichStatus` `rich_status` = 1
- **SinglePlayer**
- **MinecraftRealms**
- **InMenus**
- **InLauncher**
- **HostedWorld**
  - `lunarclient.common.v1.UuidAndUsername` `world_host` = 1
- **ReplayWorld**
- **RewindWorld**
- **InGame**
  - `lunarclient.common.v1.MinecraftVersion` `minecraft_version` = 1
  - `lunarclient.common.v1.PlayerModpack` `modpack` = 2
  - `bool` `is_badlion` = 3
- **Location**

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_modpack.proto))

- **PlayerModpack**
  - `string` `modrinth_id` = 1
  - `string` `name` = 2
  - `string` `icon_url` = 3
  - `string` `modrinth_version_id` = 4
  - `string` `curseforge_id` = 5
  - `string` `curseforge_file_id` = 6

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_position.proto))

- **GlobalPos**
  - `string` `dimension` = 1
  - `int32` `x` = 2
  - `int32` `y` = 3
  - `int32` `z` = 4
- **Vector3i**
  - `int32` `x` = 1
  - `int32` `y` = 2
  - `int32` `z` = 3
- **Vector2i**
  - `int32` `x` = 1
  - `int32` `z` = 3
- **Vector3f**
  - `float` `x` = 1
  - `float` `y` = 2
  - `float` `z` = 3

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_radio.proto))

- **RadioTrack**
  - `string` `title` = 1
  - repeated `string` `artist_names` = 2
  - `int32` `duration` = 3
  - `int32` `progress` = 4
  - `bool` `paused` = 5
  - `string` `image_url` = 6
- **RadioStation**
  - `string` `name` = 1
  - `string` `description` = 2
  - `string` `station_id` = 3
  - `string` `image_url` = 4
- **RadioInfo**
  - `lunarclient.common.v1.RadioTrack` `track` = 1
  - `lunarclient.common.v1.RadioStation` `station` = 2

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_skin.proto))

- **MinecraftSkin**
  - `string` `texture_id` = 1
  - `lunarclient.common.v1.MinecraftSkinModel` `model` = 2

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_social.proto))

- **UserSocial**
  - `lunarclient.common.v1.UserSocialPlatform` `platform` = 1
  - `string` `username` = 2
  - `string` `avatar` = 3

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_uuid.proto))

- **Uuid**
  - `fixed64` `high64` = 1
  - `fixed64` `low64` = 2
- **UuidAndUsername**
  - `lunarclient.common.v1.Uuid` `uuid` = 1
  - `string` `username` = 2

## `lunarclient.common.v1` ([source](../../proto/extracted/lunarclient_common_v1_version.proto))

- **MinecraftVersion**
  - `string` `enum` = 1
  - `lunarclient.common.v1.MinecraftVersion.MinecraftVersionType` `type` = 2
  - `string` `id` = 3
  - enum **MinecraftVersionType**:
    - `MINECRAFT_VERSION_TYPE_UNSPECIFIED = 0`
    - `MINECRAFT_VERSION_TYPE_RELEASE = 1`
    - `MINECRAFT_VERSION_TYPE_SNAPSHOT = 2`
    - `MINECRAFT_VERSION_TYPE_OLD_BETA = 3`
    - `MINECRAFT_VERSION_TYPE_OLD_ALPHA = 4`
- **LauncherVersion**
  - `string` `semver` = 1
- **LunarClientVersion**
  - `string` `git_branch` = 1
  - `string` `git_commit` = 2
  - `string` `semver` = 3
- **LunarClientUiVersion**
  - `string` `git_branch` = 1
  - `string` `git_commit` = 2

## `lunarclient.gameipc.chat.v1` ([source](../../proto/extracted/lunarclient_gameipc_chat_v1_push.proto))

- **SendChatPush**
  - `string` `message` = 1

## `lunarclient.gameipc.handshake.v1` ([source](../../proto/extracted/lunarclient_gameipc_handshake_v1_common.proto))

- **Handshake**
  - `string` `launch_id` = 1
  - `string` `process_id` = 2
  - `string` `installation_id` = 3

## `lunarclient.gameipc.launch.v1` ([source](../../proto/extracted/lunarclient_gameipc_launch_v1_push.proto))

- **PlayServerPush**
  - `string` `auto_join_server_ip` = 1
- **ExitGamePush**

## `lunarclient.gameipc.location.v1` ([source](../../proto/extracted/lunarclient_gameipc_location_v1_push.proto))

- **FocusGamePush**

## `lunarclient.gameipc.paynow.v1` ([source](../../proto/extracted/lunarclient_gameipc_paynow_v1_push.proto))

- **PayNowJsCheckoutClosed**

## `lunarclient.gameipc.promotion.v1` ([source](../../proto/extracted/lunarclient_gameipc_promotion_v1_push.proto))

- **PendingPromotionUpdatePush**
  - repeated `lunarclient.gameipc.promotion.v1.PromotionType` `pending_promotions` = 2

## `lunarclient.gameipc.protocol.v1` ([source](../../proto/extracted/lunarclient_gameipc_protocol_v1_common.proto))

- **LauncherboundIPCMessage**
  - `bytes` `request_id` = 1
  - `string` `service` = 2
  - `string` `method` = 3
  - `bytes` `input` = 4
  - `string` `full_method` = 6
  - `string` `input_name` = 7
  - `string` `input_full_name` = 8
- **GameboundIPCMessage**
- **IPCRpcResponse**
  - `bytes` `request_id` = 1
  - `bytes` `output` = 2

## `lunarclient.gameipc.store.v1` ([source](../../proto/extracted/lunarclient_gameipc_store_v1_push.proto))

- **StartStorePreviewSessionPush**

## `lunarclient.gameipc.styngr.v1` ([source](../../proto/extracted/lunarclient_gameipc_styngr_v1_common.proto))

- **StyngrTrackState**
  - `string` `image_url` = 1
  - `string` `title` = 2
  - repeated `string` `artist_names` = 3
  - `bool` `liked` = 4
  - `int32` `remaining_skips` = 5
  - `string` `playlist_id` = 6
  - `string` `playlist_name` = 7
- **StyngrControlsState**
  - `bool` `playing` = 1
  - `bool` `muted` = 2
  - `float` `volume` = 3
- **StyngrProgressState**
  - `float` `duration` = 1
  - `float` `position` = 2

## `lunarclient.gameipc.styngr.v1` ([source](../../proto/extracted/lunarclient_gameipc_styngr_v1_push.proto))

- **StyngrTrackControlsUpdate**
  - `bool` `playing` = 1
  - `bool` `muted` = 2
  - `float` `volume` = 3
- **StyngrTrackProgressUpdate**
  - `float` `duration` = 1
  - `float` `position` = 2
- **StyngrTrackUpdate**

## `lunarclient.gameipc.tebex.v1` ([source](../../proto/extracted/lunarclient_gameipc_tebex_v1_push.proto))

- **TebexJsCheckoutClosed**

## `lunarclient.websocket.analytics.v1` ([source](../../proto/extracted/lunarclient_websocket_analytics_v1_common.proto))

- **CounterUpdate**
  - `string` `counter` = 1
  - `int32` `delta` = 2

## `lunarclient.websocket.badge.v1` ([source](../../proto/extracted/lunarclient_websocket_badge_v1_common.proto))

- **OwnedBadge**
  - `int32` `badge_id` = 1
  - `google.protobuf.Timestamp` `granted_at` = 2
  - `google.protobuf.Timestamp` `expires_at` = 3
  - `lunarclient.websocket.badge.v1.OwnedBadge.ExpirationReason` `expiration_reason` = 4
  - `bool` `is_lunar_plus` = 6
  - enum **ExpirationReason**:
    - `EXPIRATION_REASON_UNSPECIFIED = 0`
    - `EXPIRATION_REASON_TIME_LAPSED = 1`
    - `EXPIRATION_REASON_LEFT_LC_DISCORD = 2`

## `lunarclient.websocket.badge.v1` ([source](../../proto/extracted/lunarclient_websocket_badge_v1_push.proto))

- **RefreshBadgesPush**

## `lunarclient.websocket.chat.v1` ([source](../../proto/extracted/lunarclient_websocket_chat_v1_push.proto))

- **ReceiveChatPush**
  - `lunarclient.common.v1.Uuid` `sender_uuid` = 1
  - `string` `chat_message` = 2

## `lunarclient.websocket.conversation.v1` ([source](../../proto/extracted/lunarclient_websocket_conversation_v1_common.proto))

- **Conversation**
- **UserConversationState**
  - `google.protobuf.Timestamp` `last_seen_time` = 1
  - `int32` `unread_count` = 2
  - `bool` `pinned` = 3
- **ConversationParticipant**
  - `lunarclient.common.v1.UuidAndUsername` `player` = 1
  - `lunarclient.common.v1.Color` `logo_color` = 2
  - `lunarclient.common.v1.Color` `plus_color` = 3
  - `string` `rank_name` = 4
  - `bool` `is_radio_premium` = 5
  - `int32` `badge_id` = 6
- **ConversationReference**
- **ConversationSender**
- **ConversationMessageContents**
- **ConversationMessage**
- **SystemMessage**
- **SystemPinnedMessageEvent**
  - `lunarclient.common.v1.Uuid` `pinned_message_id` = 1
- **SystemInviteEvent**
  - repeated `lunarclient.common.v1.UuidAndUsername` `invitees` = 1
- **SystemLeaveEvent**
  - `lunarclient.common.v1.UuidAndUsername` `player` = 1
- **SystemNameChangeEvent**
  - `string` `new_name` = 1
- **SystemIconChangeEvent**
  - `string` `new_icon_url` = 1
- **ConversationMessageEmbed**
- **ImageEmbed**
- **LinkPreviewEmbed**
  - `string` `raw_url` = 1
  - `string` `normalized_url` = 2
  - `string` `proxied_url` = 3
  - `string` `site_name` = 4
  - `string` `title` = 5
  - `string` `description` = 6
  - `lunarclient.websocket.conversation.v1.OgImage` `image` = 7
  - `string` `og_type` = 8
  - `string` `content_type` = 9
- **OgImage**
- **ConversationImage**
  - `string` `url` = 1
- **LunarSticker**
  - `string` `id` = 1
  - `string` `url` = 2
  - `string` `name` = 3
- **LunarStickerPack**
  - `string` `id` = 1
  - `string` `name` = 2
  - `string` `icon_url` = 3
  - repeated `lunarclient.websocket.conversation.v1.LunarSticker` `stickers` = 4
- **LunarEmoji**
  - `string` `id` = 1
  - `string` `url` = 2
  - `string` `name` = 3
- **LunarEmojiCategory**
  - `string` `id` = 1
  - `string` `name` = 2
  - `string` `icon_url` = 3
  - repeated `lunarclient.websocket.conversation.v1.LunarEmoji` `emojis` = 4
- **UploadRequestItem**
  - `string` `content_type` = 1
  - `uint64` `expected_size_bytes` = 2
- **PresignedUpload**
  - `string` `upload_url` = 1
  - repeated `lunarclient.websocket.conversation.v1.PresignedUpload.RequiredHeadersEntry` `required_headers` = 2
  - `uint64` `max_bytes` = 3
  - `string` `accepted_content_type` = 4
  - `google.protobuf.Timestamp` `expires_at` = 5
  - `string` `finished_url` = 6
  - **RequiredHeadersEntry**
    - `string` `key` = 1
    - `string` `value` = 2
- **ConversationStub**

## `lunarclient.websocket.conversation.v1` ([source](../../proto/extracted/lunarclient_websocket_conversation_v1_push.proto))

- **ConversationMessagePush**
- **ConversationPreSendActionPush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.PreSendAction` `action` = 2
  - `lunarclient.websocket.conversation.v1.ConversationSender` `sender` = 3
- **ConversationOwnerUpdatePush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.UuidAndUsername` `invoker` = 2
  - `lunarclient.common.v1.Uuid` `previous_owner_uuid` = 3
  - `lunarclient.common.v1.Uuid` `owner_uuid` = 4
- **ConversationAddParticipantsPush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.UuidAndUsername` `invoker` = 2
  - repeated `lunarclient.websocket.conversation.v1.ConversationParticipant` `participants` = 3
- **ConversationRemoveParticipantPush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.UuidAndUsername` `invoker` = 2
  - `lunarclient.common.v1.UuidAndUsername` `participant` = 3
- **ConversationUpdateNamePush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.UuidAndUsername` `invoker` = 2
  - `string` `name` = 3
- **ConversationUpdateIconPush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.UuidAndUsername` `invoker` = 2
  - `string` `image_url` = 3
- **ConversationAddPinnedMessagePush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.UuidAndUsername` `invoker` = 2
  - `lunarclient.common.v1.Uuid` `message_id` = 3
- **ConversationRemovePinnedMessagePush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.UuidAndUsername` `invoker` = 2
  - `lunarclient.common.v1.Uuid` `message_id` = 3
- **ConversationUpdateInvitePolicyPush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.InvitePolicy` `policy` = 2
- **ConversationUpdateNamePolicyPush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.NamePolicy` `policy` = 2
- **ConversationUpdateIconPolicyPush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.IconPolicy` `policy` = 2
- **ConversationUpdateMessagePinningPolicyPush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.websocket.conversation.v1.MessagePinningPolicy` `policy` = 2
- **ConversationAddedPush**
  - `lunarclient.websocket.conversation.v1.Conversation` `conversation` = 1
  - `lunarclient.common.v1.UuidAndUsername` `sender` = 2
  - `google.protobuf.Timestamp` `added_at` = 3
- **ConversationRemovedPush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
- **ConversationRemoveMessagePush**
  - `lunarclient.websocket.conversation.v1.ConversationReference` `conversation_reference` = 1
  - `lunarclient.common.v1.Uuid` `id` = 2
- **ConversationMessageHistoryDeletedPush**
- **RefreshConversationsPush**

## `lunarclient.websocket.cosmetic.v1` ([source](../../proto/extracted/lunarclient_websocket_cosmetic_v1_common.proto))

- **OwnedCosmetic**
  - `int32` `cosmetic_id` = 1
  - `google.protobuf.Timestamp` `granted_at` = 2
  - `google.protobuf.Timestamp` `expires_at` = 3
  - `lunarclient.websocket.cosmetic.v1.OwnedCosmetic.ExpirationReason` `expiration_reason` = 4
  - `lunarclient.common.v1.GiftInfo` `gift_info` = 5
  - enum **ExpirationReason**:
    - `EXPIRATION_REASON_UNSPECIFIED = 0`
    - `EXPIRATION_REASON_TIME_LAPSED = 1`
    - `EXPIRATION_REASON_LEFT_LC_DISCORD = 2`

## `lunarclient.websocket.cosmetic.v2` ([source](../../proto/extracted/lunarclient_websocket_cosmetic_v2_common.proto))

- **EquippedCosmetic**
  - `int32` `cosmetic_id` = 1
  - `google.protobuf.Struct` `geckolib_metadata` = 2
  - `bool` `cloth_cloak` = 3
  - `bool` `show_over_skin_layer` = 4
  - `bool` `show_over_helmet` = 5
  - `bool` `show_over_chestplate` = 6
  - `bool` `show_over_leggings` = 7
  - `bool` `show_over_boots` = 8
  - `float` `hat_height_offset` = 9
  - `bool` `flip_arm` = 10
- **OwnedCosmetic**
  - `int32` `cosmetic_id` = 1
  - `google.protobuf.Timestamp` `granted_at` = 2
  - `google.protobuf.Timestamp` `expires_at` = 3
  - `lunarclient.websocket.cosmetic.v2.OwnedCosmetic.ExpirationReason` `expiration_reason` = 4
  - `lunarclient.common.v1.GiftInfo` `gift_info` = 5
  - enum **ExpirationReason**:
    - `EXPIRATION_REASON_UNSPECIFIED = 0`
    - `EXPIRATION_REASON_TIME_LAPSED = 1`
    - `EXPIRATION_REASON_LEFT_LC_DISCORD = 2`
- **Outfit**
- **ServerCondition**
  - `string` `server_ip` = 1
- **DimensionCondition**
  - `string` `dimension_id` = 1
- **TimeCondition**
  - `lunarclient.websocket.cosmetic.v2.TimeCondition.Time` `time` = 1
  - enum **Time**:
    - `TIME_UNSPECIFIED = 0`
    - `TIME_DAY = 1`
    - `TIME_NIGHT = 2`
- **WeatherCondition**
  - `lunarclient.websocket.cosmetic.v2.WeatherCondition.Weather` `weather` = 1
  - enum **Weather**:
    - `WEATHER_UNSPECIFIED = 0`
    - `WEATHER_RAIN = 1`
    - `WEATHER_SNOW = 2`
    - `WEATHER_THUNDERSTORM = 3`
    - `WEATHER_CLEAR = 4`
- **BiomeTemperatureCondition**
  - `lunarclient.websocket.cosmetic.v2.BiomeTemperatureCondition.Temperature` `temperature` = 1
  - enum **Temperature**:
    - `TEMPERATURE_UNSPECIFIED = 0`
    - `TEMPERATURE_HOT = 1`
    - `TEMPERATURE_COLD = 2`
- **PassengerOfEntityCondition**
  - `string` `entity_id` = 1
- **MovementStateCondition**
  - `lunarclient.websocket.cosmetic.v2.MovementStateCondition.State` `state` = 1
  - enum **State**:
    - `STATE_UNSPECIFIED = 0`
    - `STATE_SWIMMING = 1`
    - `STATE_CREATIVE_FLYING = 2`
    - `STATE_ELYTRA_FLYING = 3`
- **InLiquidCondition**
  - `lunarclient.websocket.cosmetic.v2.InLiquidCondition.Liquid` `liquid` = 1
  - enum **Liquid**:
    - `LIQUID_UNSPECIFIED = 0`
    - `LIQUID_WATER = 1`
    - `LIQUID_LAVA = 2`
- **RadioPlayingCondition**
- **OnFireCondition**
- **EquipCondition**
- **OutfitTree**
  - repeated `lunarclient.websocket.cosmetic.v2.OutfitTree.ConditionalOutfit` `conditional_outfits` = 1
  - `lunarclient.common.v1.Uuid` `default_outfit_id` = 2
  - **ConditionalOutfit**
    - `lunarclient.websocket.cosmetic.v2.EquipCondition` `equip_condition` = 1
    - `lunarclient.common.v1.Uuid` `outfit_id` = 2

## `lunarclient.websocket.cosmetic.v2` ([source](../../proto/extracted/lunarclient_websocket_cosmetic_v2_push.proto))

- **PlayerCosmeticsPushV2**
  - `lunarclient.common.v1.Uuid` `player_uuid` = 1
  - `lunarclient.common.v1.Color` `logo_color` = 2
  - `bool` `logo_always_show` = 3
  - `lunarclient.common.v1.Color` `plus_color` = 4
  - repeated `lunarclient.websocket.cosmetic.v2.PlayerCosmeticsPushV2.ConditionalCosmetics` `conditional_cosmetics` = 5
  - repeated `lunarclient.websocket.cosmetic.v2.EquippedCosmetic` `default_cosmetics` = 6
  - `int32` `badge_id` = 7
  - `lunarclient.common.v1.Uuid` `outfit_uuid` = 8
  - **ConditionalCosmetics**
    - `lunarclient.websocket.cosmetic.v2.EquipCondition` `equip_condition` = 1
    - repeated `lunarclient.websocket.cosmetic.v2.EquippedCosmetic` `cosmetics` = 2
- **RefreshCosmeticsPush**

## `lunarclient.websocket.emote.v1` ([source](../../proto/extracted/lunarclient_websocket_emote_v1_common.proto))

- **RecommendedJam**
  - `int32` `jam_id` = 1
- **OwnedEmote**
  - `int32` `emote_id` = 1
  - `google.protobuf.Timestamp` `granted_at` = 2
  - `google.protobuf.Timestamp` `expires_at` = 3
  - repeated `lunarclient.websocket.emote.v1.RecommendedJam` `recommended_jams` = 4
  - `lunarclient.common.v1.GiftInfo` `gift_info` = 5
- **EquippedEmote**
  - `int32` `emote_id` = 1
  - `int32` `slot_number` = 2
  - `int32` `attached_jam_id` = 3

## `lunarclient.websocket.emote.v1` ([source](../../proto/extracted/lunarclient_websocket_emote_v1_push.proto))

- **UseEmotePush**
  - `lunarclient.common.v1.Uuid` `player_uuid` = 1
  - `int32` `emote_id` = 2
  - `int32` `emote_metadata` = 3
  - `string` `emote_soundtrack_url` = 4
  - `int32` `emote_jam_id` = 5
- **StopEmotePush**
  - `lunarclient.common.v1.Uuid` `player_uuid` = 1
- **RefreshEmotesPush**

## `lunarclient.websocket.friend.v1` ([source](../../proto/extracted/lunarclient_websocket_friend_v1_common.proto))

- **FriendSocials**
  - `bool` `hidden` = 1
  - repeated `lunarclient.common.v1.UserSocial` `linked` = 2
- **OnlineFriend**
  - `lunarclient.common.v1.UuidAndUsername` `player` = 1
  - `lunarclient.websocket.friend.v1.OnlineFriendStatus` `status` = 2
  - `lunarclient.common.v1.Location` `location` = 3
  - `lunarclient.common.v1.MinecraftVersion` `minecraft_version` = 4
  - `bool` `just_came_online` = 5
  - `lunarclient.websocket.hostedworld.v1.Joinability` `hosted_world_joinability` = 6
  - `lunarclient.common.v1.Color` `logo_color` = 7
  - `lunarclient.common.v1.PlayerModpack` `modpack` = 8
  - `lunarclient.common.v1.Color` `plus_color` = 9
  - `bool` `is_radio_premium` = 10
  - `google.protobuf.Timestamp` `friends_since` = 11
  - `lunarclient.websocket.friend.v1.FriendSocials` `socials` = 12
  - `string` `rank_name` = 13
  - `string` `country_code` = 14
  - `int32` `badge_id` = 15
- **OfflineFriend**
  - `lunarclient.common.v1.UuidAndUsername` `player` = 1
  - `google.protobuf.Timestamp` `last_visible_online` = 2
  - `lunarclient.common.v1.Color` `logo_color` = 3
  - `lunarclient.common.v1.Color` `plus_color` = 4
  - `bool` `is_radio_premium` = 5
  - `google.protobuf.Timestamp` `friends_since` = 6
  - `lunarclient.websocket.friend.v1.FriendSocials` `socials` = 7
  - `string` `rank_name` = 8
  - `string` `country_code` = 9
  - `int32` `badge_id` = 10
- **FriendRequest**
  - `lunarclient.common.v1.UuidAndUsername` `player` = 1
  - `google.protobuf.Timestamp` `sent_at` = 2
  - `lunarclient.common.v1.Color` `player_logo_color` = 3
  - `lunarclient.common.v1.Color` `player_plus_color` = 4
  - `string` `player_rank_name` = 5
  - `int32` `player_badge_id` = 6

## `lunarclient.websocket.friend.v1` ([source](../../proto/extracted/lunarclient_websocket_friend_v1_push.proto))

- **FriendStatusPush**
- **FriendRadioInfoPush**
  - `lunarclient.common.v1.Uuid` `friend_uuid` = 1
  - `lunarclient.common.v1.RadioInfo` `radio_info` = 2
- **FriendRemovedYouPush**
  - `lunarclient.common.v1.Uuid` `friend_uuid` = 1
- **FriendRequestReceivedPush**
  - `lunarclient.common.v1.UuidAndUsername` `sender` = 1
  - `lunarclient.common.v1.Color` `sender_logo_color` = 3
  - `lunarclient.common.v1.Color` `sender_plus_color` = 4
  - `string` `sender_rank_name` = 5
  - `int32` `sender_badge_id` = 6
- **FriendRequestAcceptedPush**
  - `lunarclient.common.v1.UuidAndUsername` `new_friend` = 2
- **FriendRequestDeniedPush**
  - `lunarclient.common.v1.Uuid` `denier_uuid` = 1
- **FriendRequestCanceledPush**
  - `lunarclient.common.v1.Uuid` `sender_uuid` = 1

## `lunarclient.websocket.handshake.v1` ([source](../../proto/extracted/lunarclient_websocket_handshake_v1_common.proto))

- **Handshake**
- **InstalledMod**
  - `string` `id` = 1
  - `string` `name` = 2
  - `string` `version` = 3
  - `lunarclient.websocket.handshake.v1.InstalledMod.Type` `type` = 4
  - enum **Type**:
    - `TYPE_UNSPECIFIED = 0`
    - `TYPE_FABRIC_INTERNAL = 1`
    - `TYPE_FABRIC_EXTERNAL = 2`
    - `TYPE_FORGE_INTERNAL = 3`
    - `TYPE_FORGE_EXTERNAL = 4`
- **MinecraftIdentity**
  - `lunarclient.common.v1.UuidAndUsername` `player` = 1
  - `lunarclient.websocket.handshake.v1.MinecraftIdentity.Type` `type` = 2
  - `string` `authenticator_jwt` = 3
  - repeated `lunarclient.websocket.handshake.v1.MinecraftIdentity.Skin` `skins` = 4
  - repeated `lunarclient.websocket.handshake.v1.MinecraftIdentity.Cape` `capes` = 5
  - `lunarclient.websocket.handshake.v1.MinecraftIdentity.Attributes` `attributes` = 6
  - `google.protobuf.Timestamp` `created_at` = 8
  - `lunarclient.websocket.handshake.v1.MinecraftIdentity.NameChange` `name_change` = 9
  - `bool` `owns_bedrock_edition` = 10
  - enum **Type**:
    - `TYPE_UNSPECIFIED = 0`
    - `TYPE_MOJANG = 1`
    - `TYPE_MICROSOFT = 2`
  - enum **TextureState**:
    - `TEXTURE_STATE_UNSPECIFIED = 0`
    - `TEXTURE_STATE_ACTIVE = 1`
    - `TEXTURE_STATE_INACTIVE = 2`
  - **NameChange**
    - `google.protobuf.Timestamp` `last_changed_at` = 1
    - `bool` `allowed` = 2
  - **Skin**
    - `string` `id` = 1
    - `lunarclient.websocket.handshake.v1.MinecraftIdentity.TextureState` `state` = 2
    - `lunarclient.common.v1.MinecraftSkin` `skin` = 3
  - **Cape**
    - `string` `id` = 1
    - `lunarclient.websocket.handshake.v1.MinecraftIdentity.TextureState` `state` = 2
    - `string` `texture_id` = 3
    - `string` `alias` = 4
  - **Attributes**
    - `bool` `priviledge_online_chat` = 1
    - `bool` `priviledge_multiplayer_server` = 2
    - `bool` `priviledge_multiplayer_realms` = 3
    - `bool` `priviledge_telemetry` = 4
    - `bool` `priviledge_optional_telemetry` = 5
    - `bool` `profanity_filter_realms` = 6
    - repeated `lunarclient.websocket.handshake.v1.MinecraftIdentity.Attributes.BannedScope` `banned_scopes` = 7
    - **BannedScope**
      - `lunarclient.websocket.handshake.v1.MinecraftIdentity.Attributes.BannedScope.Type` `type` = 1
      - `string` `ban_id` = 2
      - `google.protobuf.Timestamp` `expires` = 3
      - `string` `reason` = 4
      - `string` `reason_message` = 5
      - enum **Type**:
        - `TYPE_UNSPECIFIED = 0`
        - `TYPE_MULTIPLAYER = 1`
- **NvidiaGpuMemory**
  - `int32` `dedicated_vram_kb` = 1
  - `int32` `total_available_memory_kb` = 2
- **MesaGpuMemory**
  - `int32` `total_vram_mb` = 1
  - `bool` `unified_memory` = 2
- **GameHandshake**
- **LauncherHandshake**
  - `string` `environment` = 1
  - `string` `session_id` = 2
  - `string` `updater_stream` = 3
  - `lunarclient.websocket.handshake.v1.LauncherHandshake.ElectronBinariesType` `electron_binaries_type` = 4
  - `bool` `elevated` = 5
  - `bool` `silent_start` = 6
  - `int32` `uptime_since_start` = 7
  - `google.protobuf.Timestamp` `started_at` = 8
  - `int32` `build_number` = 9
  - `string` `git_commit_hash` = 10
  - `string` `git_short_commit_hash` = 11
  - `lunarclient.websocket.radio.v1.InboundRadioInfo` `radio_info` = 12
  - `bool` `optimized_ads` = 13
  - `bool` `analytics` = 14
  - `bool` `owahe` = 15
  - repeated `lunarclient.websocket.setting.v1.LauncherSetting` `settings` = 16
  - `bool` `safe_storage` = 17
  - enum **ElectronBinariesType**:
    - `ELECTRON_BINARIES_TYPE_UNSPECIFIED = 0`
    - `ELECTRON_BINARIES_TYPE_OVERWOLF_OW_ELECTRON = 1`
    - `ELECTRON_BINARIES_TYPE_ELECTRON = 2`

## `lunarclient.websocket.handshake.v1` ([source](../../proto/extracted/lunarclient_websocket_handshake_v1_push.proto))

- **SessionIdentifyPush**
  - `lunarclient.common.v1.Uuid` `session_id` = 1

## `lunarclient.websocket.heartbeat.v1` ([source](../../proto/extracted/lunarclient_websocket_heartbeat_v1_common.proto))

- **OnlineCounts**
  - `int32` `launcher` = 1
  - `int32` `game` = 2
- **RunningInstanceLoader**
  - `string` `loader` = 1
  - `string` `loader_version` = 2
  - `bool` `loader_version_recommended` = 3
- **RunningInstance**
  - `string` `launch_id` = 1
  - `lunarclient.common.v1.MinecraftVersion` `minecraft_version` = 2
  - `string` `module` = 3
  - `lunarclient.common.v1.PlayerModpack` `modpack` = 4
  - `lunarclient.common.v1.Location` `location` = 5
  - `lunarclient.websocket.heartbeat.v1.RunningInstanceLoader` `loader` = 6
- **RendererPosition**
  - `int32` `position_x` = 1
  - `int32` `position_y` = 2
  - `int32` `width` = 3
  - `int32` `height` = 4
  - `int32` `display_id` = 5
  - `bool` `primary_display` = 6
  - `int32` `display_width` = 7
  - `int32` `display_height` = 8
  - `lunarclient.websocket.heartbeat.v1.RendererPosition.DisplayType` `display_type` = 9
  - enum **DisplayType**:
    - `DISPLAY_TYPE_UNSPECIFIED = 0`
    - `DISPLAY_TYPE_NATIVE = 1`
    - `DISPLAY_TYPE_OSR = 2`
- **OpenRenderer**
  - `string` `id` = 1
  - `string` `route` = 2
  - `string` `title` = 3
  - `bool` `focused` = 4
  - `bool` `visible` = 5
  - `bool` `fullscreened` = 6
  - `bool` `minimized` = 7
  - `lunarclient.websocket.heartbeat.v1.RendererPosition` `position` = 8
  - `lunarclient.websocket.heartbeat.v1.OpenRenderer.ContentType` `content_type` = 9
  - enum **ContentType**:
    - `CONTENT_TYPE_UNSPECIFIED = 0`
    - `CONTENT_TYPE_MAIN = 1`
    - `CONTENT_TYPE_MISSION_CONTROL = 2`
    - `CONTENT_TYPE_CHAT = 3`
    - `CONTENT_TYPE_FRIENDS = 4`
    - `CONTENT_TYPE_SATELLITE = 5`
    - `CONTENT_TYPE_EMBEDDED_BROWSER = 6`
    - `CONTENT_TYPE_UPDATER = 7`
    - `CONTENT_TYPE_VISUALISE_RESOLUTION = 8`
    - `CONTENT_TYPE_CHECKOUT = 9`

## `lunarclient.websocket.heartbeat.v1` ([source](../../proto/extracted/lunarclient_websocket_heartbeat_v1_push.proto))

- **RefreshMetadataPush**
- **CheckForUpdatesPush**
  - `bool` `force_install` = 1

## `lunarclient.websocket.hostedworld.v1` ([source](../../proto/extracted/lunarclient_websocket_hostedworld_v1_common.proto))

- **AddressAndPort**
  - `string` `address` = 1
  - `int32` `port` = 2
- **PingResponse**
  - `lunarclient.websocket.hostedworld.v1.AddressAndPort` `target` = 1
  - `bool` `success` = 2
  - `google.protobuf.Duration` `latency` = 3
- **Heartbeat**
  - repeated `lunarclient.websocket.hostedworld.v1.JoinSource` `allowed_join_sources` = 1
  - `int32` `max_players` = 2
  - repeated `lunarclient.common.v1.Uuid` `whitelisted_uuids` = 3
  - repeated `lunarclient.websocket.hostedworld.v1.Heartbeat.OnlinePlayer` `online_players` = 4
  - repeated `lunarclient.websocket.hostedworld.v1.Heartbeat.OfflinePlayer` `offline_players` = 5
  - repeated `lunarclient.websocket.hostedworld.v1.PingResponse` `ping_responses` = 6
  - **OnlinePlayer**
    - `lunarclient.common.v1.UuidAndUsername` `player` = 1
  - **OfflinePlayer**
    - `lunarclient.common.v1.UuidAndUsername` `player` = 1
    - `google.protobuf.Timestamp` `last_online` = 2

## `lunarclient.websocket.hostedworld.v1` ([source](../../proto/extracted/lunarclient_websocket_hostedworld_v1_push.proto))

- **JoinHostedWorldPush**
  - `lunarclient.websocket.hostedworld.v1.AddressAndPort` `relay` = 1
  - `string` `relay_session_id` = 2
  - `lunarclient.common.v1.Uuid` `joiner_uuid` = 3
  - `lunarclient.websocket.hostedworld.v1.AddressAndPort` `simple_voice_chat_endpoint` = 4
- **HostedWorldAvailablePush**
  - `lunarclient.common.v1.UuidAndUsername` `world_host` = 1
- **HostedWorldWhitelistedPush**
  - `lunarclient.common.v1.UuidAndUsername` `world_host` = 1
- **HostedWorldStatusPush**
  - repeated `lunarclient.websocket.hostedworld.v1.HostedWorldStatusPush.OnlinePlayer` `online_players` = 1
  - repeated `lunarclient.websocket.hostedworld.v1.HostedWorldStatusPush.OfflinePlayer` `offline_players` = 2
  - repeated `lunarclient.websocket.hostedworld.v1.JoinSource` `allowed_join_sources` = 3
  - `int32` `max_players` = 4
  - **OnlinePlayer**
    - `lunarclient.common.v1.UuidAndUsername` `player` = 1
    - `lunarclient.websocket.hostedworld.v1.Role` `role` = 2
    - `lunarclient.common.v1.Color` `logo_color` = 3
    - `lunarclient.common.v1.Color` `plus_color` = 4
  - **OfflinePlayer**
    - `lunarclient.common.v1.UuidAndUsername` `player` = 1
    - `google.protobuf.Timestamp` `last_online` = 2

## `lunarclient.websocket.jam.v1` ([source](../../proto/extracted/lunarclient_websocket_jam_v1_common.proto))

- **OwnedJam**
  - `int32` `jam_id` = 1
  - `google.protobuf.Timestamp` `granted_at` = 2
  - `google.protobuf.Timestamp` `expires_at` = 3
  - `lunarclient.common.v1.GiftInfo` `gift_info` = 4

## `lunarclient.websocket.jam.v1` ([source](../../proto/extracted/lunarclient_websocket_jam_v1_push.proto))

- **RefreshJamsPush**

## `lunarclient.websocket.language.v1` ([source](../../proto/extracted/lunarclient_websocket_language_v1_common.proto))

- **Language**

## `lunarclient.websocket.liveexperience.v1` ([source](../../proto/extracted/lunarclient_websocket_liveexperience_v1_common.proto))

- **LiveExperience**
  - `string` `id` = 1
  - `string` `name` = 2
  - `string` `background_image` = 3
  - `string` `foreground_image` = 4
- **AddressAndPort**
  - `string` `address` = 1
  - `int32` `port` = 2

## `lunarclient.websocket.marker.v1` ([source](../../proto/extracted/lunarclient_websocket_marker_v1_common.proto))

- **Marker**
  - `lunarclient.common.v1.Vector3f` `position` = 1
  - repeated `string` `description` = 2
  - `string` `source` = 3

## `lunarclient.websocket.marker.v1` ([source](../../proto/extracted/lunarclient_websocket_marker_v1_push.proto))

- **NewMarkerPush**
  - `lunarclient.common.v1.Uuid` `sender_uuid` = 1
  - `lunarclient.websocket.marker.v1.Marker` `marker` = 2

## `lunarclient.websocket.notification.v1` ([source](../../proto/extracted/lunarclient_websocket_notification_v1_common.proto))

- **Notification**
  - `lunarclient.common.v1.Uuid` `id` = 1
  - `string` `title` = 2
  - `lunarclient.websocket.notification.v1.Notification.NotificationType` `type` = 3
  - `google.protobuf.Timestamp` `sent_at` = 4
  - `google.protobuf.Timestamp` `read_at` = 5
  - `string` `metadata` = 6
  - enum **NotificationType**:
    - `NOTIFICATION_TYPE_UNSPECIFIED = 0`
    - `NOTIFICATION_TYPE_ANNOUNCEMENT = 1`
    - `NOTIFICATION_TYPE_FRIEND_REQUEST = 2`
    - `NOTIFICATION_TYPE_PURCHASE = 3`
    - `NOTIFICATION_TYPE_GIFT = 4`
    - `NOTIFICATION_TYPE_GENERAL = 5`
    - `NOTIFICATION_TYPE_NOW_FRIENDS = 6`
    - `NOTIFICATION_TYPE_PROMOTION = 7`

## `lunarclient.websocket.notification.v1` ([source](../../proto/extracted/lunarclient_websocket_notification_v1_push.proto))

- **DisplayNotificationPush**
  - `string` `notification_title` = 1
  - `string` `notification_message` = 2
- **DisplayChatMessagePush**
  - `string` `chat_message` = 1
- **NewNotificationPush**
  - `lunarclient.websocket.notification.v1.Notification` `notification` = 1
- **RemoveNotificationPush**
  - `lunarclient.common.v1.Uuid` `id` = 1

## `lunarclient.websocket.paynow.v1` ([source](../../proto/extracted/lunarclient_websocket_paynow_v1_push.proto))

- **OpenPayNowCheckoutPush**
  - `string` `checkout_token` = 1

## `lunarclient.websocket.performance.v1` ([source](../../proto/extracted/lunarclient_websocket_performance_v1_push.proto))

- **StartJfrProfilePush**
  - `google.protobuf.Duration` `duration` = 1
- **StopJfrProfilePush**

## `lunarclient.websocket.promotion.v1` ([source](../../proto/extracted/lunarclient_websocket_promotion_v1_common.proto))

- **CosmeticPromotionReward**
  - `int32` `cosmetic_id` = 1
- **EmotePromotionReward**
  - `int32` `emote_id` = 1
- **SprayPromotionReward**
  - `int32` `spray_id` = 1
- **BadgePromotionReward**
  - `int32` `badge_id` = 1
- **PromotionReward**
- **PendingReward**
  - `lunarclient.websocket.promotion.v1.PendingRewardType` `type` = 1
  - repeated `lunarclient.websocket.promotion.v1.PromotionReward` `rewards` = 2

## `lunarclient.websocket.protocol.v1` ([source](../../proto/extracted/lunarclient_websocket_protocol_v1_common.proto))

- **ServerboundWebSocketMessage**
  - `bytes` `request_id` = 1
  - `string` `service` = 2
  - `string` `method` = 3
  - `bytes` `input` = 4
- **ClientboundWebSocketMessage**
- **WebSocketRpcResponse**
  - `bytes` `request_id` = 1
  - `bytes` `output` = 2

## `lunarclient.websocket.protocol.v1` ([source](../../proto/extracted/lunarclient_websocket_protocol_v1_push.proto))

- **WebSocketRichClosePush**
  - `lunarclient.websocket.protocol.v1.WebSocketRichClosePush.ReconnectDelay` `reconnect_delay` = 1
  - `string` `reason` = 2
  - `string` `reconnect_authenticator_jwt` = 3
  - enum **ReconnectDelay**:
    - `RECONNECT_DELAY_UNSPECIFIED = 0`
    - `RECONNECT_DELAY_IMMEDIATE = 1`
    - `RECONNECT_DELAY_NORMAL = 2`

## `lunarclient.websocket.radio.v1` ([source](../../proto/extracted/lunarclient_websocket_radio_v1_common.proto))

- **InboundRadioTrack**
  - `string` `title` = 1
  - `int32` `track_id` = 2
  - `int32` `asset_id` = 3
  - `bool` `liked` = 4
  - repeated `string` `artist_names` = 5
  - `int32` `duration` = 7
  - `int32` `progress` = 8
  - `int32` `position` = 9
  - `bool` `paused` = 10
  - `string` `image_url` = 11
  - repeated `lunarclient.websocket.radio.v1.InboundRadioTrack.CustomMetadataEntry` `custom_metadata` = 12
  - `string` `album_name` = 13
  - `string` `royalty_free_usage_report_id` = 14
  - **CustomMetadataEntry**
    - `string` `key` = 1
    - `string` `value` = 2
- **InboundRadioStation**
  - `string` `name` = 1
  - `string` `description` = 2
  - `string` `station_id` = 3
  - `int32` `track_count` = 4
  - `lunarclient.websocket.radio.v1.InboundRadioStation.StationType` `station_type` = 5
  - `lunarclient.websocket.radio.v1.InboundRadioStation.MonetizationType` `monetization_type` = 6
  - `int32` `duration` = 7
  - `string` `licensed_session_id` = 8
  - `string` `image_url` = 9
  - enum **StationType**:
    - `STATION_TYPE_UNSPECIFIED = 0`
    - `STATION_TYPE_LICENSED = 1`
    - `STATION_TYPE_ROYALTY_FREE = 2`
  - enum **MonetizationType**:
    - `MONETIZATION_TYPE_UNSPECIFIED = 0`
    - `MONETIZATION_TYPE_INTERNAL_AD_FUNDED = 1`
    - `MONETIZATION_TYPE_EXTERNAL_AD_FUNDED = 2`
    - `MONETIZATION_TYPE_PREMIUM = 3`
- **InboundRadioInfo**
  - `lunarclient.websocket.radio.v1.InboundRadioTrack` `track` = 1
  - `lunarclient.websocket.radio.v1.InboundRadioStation` `station` = 2

## `lunarclient.websocket.radio.v1` ([source](../../proto/extracted/lunarclient_websocket_radio_v1_push.proto))

- **PlayerRadioPush**
  - `lunarclient.common.v1.Uuid` `player_uuid` = 1
  - `bool` `radio_playing` = 2
- **RefreshRadioPush**

## `lunarclient.websocket.screenshot.v1` ([source](../../proto/extracted/lunarclient_websocket_screenshot_v1_common.proto))

- **ScreenshotMessage**
  - `lunarclient.common.v1.UuidAndUsername` `author` = 1
  - repeated `lunarclient.websocket.screenshot.v1.PlayerState` `states` = 2
  - repeated `lunarclient.websocket.screenshot.v1.ScreenshotPlayer` `players` = 3
  - `string` `dimension` = 4
  - `string` `biome` = 5
  - `float` `yaw` = 6
  - `float` `pitch` = 7
  - `lunarclient.common.v1.Vector3f` `pos` = 8
  - `lunarclient.websocket.screenshot.v1.Dimensions` `size` = 9
  - `lunarclient.websocket.screenshot.v1.Perspective` `perspective` = 10
  - `bool` `has_hud` = 11
  - `int64` `day_time` = 12
  - `lunarclient.websocket.screenshot.v1.Weather` `weather` = 13
  - `float` `health` = 14
  - `float` `max_health` = 15
  - `float` `food_level` = 16
  - `float` `saturation_level` = 17
  - `lunarclient.common.v1.Uuid` `local_id` = 18
- **ScreenshotPlayer**
  - `lunarclient.common.v1.UuidAndUsername` `player` = 1
  - repeated `lunarclient.websocket.screenshot.v1.PlayerState` `states` = 2
  - repeated `int32` `cosmetics` = 3
  - `int32` `emote` = 4
  - `int32` `emote_jam` = 5
  - `lunarclient.common.v1.MinecraftSkin` `skin` = 6
  - `string` `cape` = 7
- **ExtraScreenshotData**
  - `lunarclient.common.v1.MinecraftVersion` `mc_version` = 1
  - `lunarclient.common.v1.LunarClientVersion` `lunar_version` = 2
  - `lunarclient.common.v1.Location` `location` = 3
- **Dimensions**
  - `int64` `width` = 1
  - `int64` `height` = 2

## `lunarclient.websocket.screenshot.v1` ([source](../../proto/extracted/lunarclient_websocket_screenshot_v1_push.proto))

- **RefreshScreenshotsPush**

## `lunarclient.websocket.server.v1` ([source](../../proto/extracted/lunarclient_websocket_server_v1_common.proto))

- **ServerRecommendations**
  - `lunarclient.common.v1.PlayerModpack` `modpack` = 1
  - repeated `string` `ip_addresses` = 2
  - repeated `lunarclient.common.v1.MinecraftVersion` `versions` = 3

## `lunarclient.websocket.serverdiscovery.v1` ([source](../../proto/extracted/lunarclient_websocket_serverdiscovery_v1_common.proto))

- **ServerSection**
  - `string` `id` = 1
  - `string` `name` = 2
  - `string` `emoji` = 3
  - `bool` `show_not_interested` = 4
  - `lunarclient.websocket.serverdiscovery.v1.ServerSection.CardSize` `card_size` = 5
  - repeated `lunarclient.websocket.serverdiscovery.v1.ServerCard` `cards` = 6
  - `string` `description` = 7
  - enum **CardSize**:
    - `CARD_SIZE_UNSPECIFIED = 0`
    - `CARD_SIZE_SMALL = 1`
    - `CARD_SIZE_MEDIUM = 2`
    - `CARD_SIZE_LARGE = 3`
- **ServerCard**
  - `string` `recommendation_id` = 1
  - `string` `server_mappings_id` = 11
  - `string` `name` = 2
  - `string` `logo_url` = 4
  - `string` `background_url` = 5
  - `lunarclient.common.v1.Color` `primary_color` = 6
  - `string` `primary_address` = 7
  - `lunarclient.websocket.serverdiscovery.v1.ServerCard.Badge` `badge` = 8
  - `google.protobuf.Timestamp` `last_joined` = 9
  - `lunarclient.websocket.serverdiscovery.v1.Announcement` `announcement` = 12
  - repeated `string` `region_codes` = 13
  - repeated `lunarclient.websocket.serverdiscovery.v1.ServerGameType` `game_types` = 14
  - enum **Badge**:
    - `BADGE_UNSPECIFIED = 0`
    - `BADGE_LUNAR_CLIENT_PARTNER = 1`
    - `BADGE_FEATURED = 2`
    - `BADGE_OFFICIAL = 3`
- **Announcement**
- **GlobalAnnouncement**
  - `lunarclient.websocket.serverdiscovery.v1.Announcement` `announcement` = 1
  - `lunarclient.websocket.serverdiscovery.v1.ServerCard` `server` = 2
- **ServerModalDetails**
  - `string` `description` = 1
  - `string` `twitter` = 2
  - `string` `discord` = 3
  - `string` `youtube` = 4
  - `string` `instagram` = 5
  - `string` `twitch` = 6
  - `string` `telegram` = 7
  - `string` `reddit` = 8
  - `string` `tiktok` = 9
  - `string` `facebook` = 10
  - `lunarclient.common.v1.PlayerModpack` `modpack` = 11
- **ServerGameType**
  - `string` `name` = 1
  - `string` `emoji` = 2

## `lunarclient.websocket.serverdiscovery.v1` ([source](../../proto/extracted/lunarclient_websocket_serverdiscovery_v1_push.proto))

- **ServerSectionCardsPush**
  - `string` `section_id` = 1
  - repeated `lunarclient.websocket.serverdiscovery.v1.ServerCard` `cards` = 2

## `lunarclient.websocket.setting.v1` ([source](../../proto/extracted/lunarclient_websocket_setting_v1_common.proto))

- **LauncherSetting**
  - `string` `id` = 1
  - `google.protobuf.Any` `value` = 2
  - `bool` `changed_value` = 3
  - `bool` `default_value` = 4
- **ClientSetting**
  - `string` `id` = 1
  - `google.protobuf.Any` `value` = 2
  - `bool` `changed_value` = 3
  - `bool` `default_value` = 4

## `lunarclient.websocket.skyblock.v1` ([source](../../proto/extracted/lunarclient_websocket_skyblock_v1_common.proto))

- **EarlyInDoor**
  - `lunarclient.websocket.skyblock.v1.DungeonRoomType` `type` = 1
  - `lunarclient.common.v1.Vector2i` `position_1` = 2
  - `lunarclient.common.v1.Vector2i` `position_2` = 3
- **EarlyInRoom**
  - repeated `lunarclient.common.v1.Vector2i` `components` = 1
  - `lunarclient.websocket.skyblock.v1.DungeonRoomType` `type` = 2
- **EarlyInUnknown**
  - `lunarclient.common.v1.Vector2i` `position` = 1
- **RoomDetection**
  - `lunarclient.common.v1.Vector2i` `position` = 1
  - `string` `hash` = 2
  - `lunarclient.common.v1.Vector3i` `origin` = 3
  - `lunarclient.websocket.skyblock.v1.DungeonRoomRotation` `rotation` = 4
- **RoomSecrets**
  - `lunarclient.common.v1.Vector2i` `position` = 1
  - `int32` `current` = 2
  - `int32` `max` = 3
- **DungeonUpdate**

## `lunarclient.websocket.skyblock.v1` ([source](../../proto/extracted/lunarclient_websocket_skyblock_v1_push.proto))

- **DungeonUpdatePush**
  - `lunarclient.common.v1.Uuid` `sender_uuid` = 1
  - `lunarclient.websocket.skyblock.v1.DungeonUpdate` `update` = 2

## `lunarclient.websocket.socials.v1` ([source](../../proto/extracted/lunarclient_websocket_socials_v1_common.proto))

- **LinkedSocialCommunity**
  - `bool` `is_member` = 1
  - `google.protobuf.Timestamp` `joined_at` = 2
  - `google.protobuf.Timestamp` `left_at` = 3
  - `bool` `has_flair` = 4
- **LinkedSocial**
  - `lunarclient.common.v1.UserSocial` `social` = 1
  - `google.protobuf.Timestamp` `linked_at` = 2
  - `lunarclient.websocket.socials.v1.LinkedSocialCommunity` `community` = 3

## `lunarclient.websocket.socials.v1` ([source](../../proto/extracted/lunarclient_websocket_socials_v1_push.proto))

- **RefreshSocialsPush**

## `lunarclient.websocket.spray.v1` ([source](../../proto/extracted/lunarclient_websocket_spray_v1_common.proto))

- **OwnedSpray**
  - `int32` `spray_id` = 1
  - `google.protobuf.Timestamp` `granted_at` = 2
  - `google.protobuf.Timestamp` `expires_at` = 3
  - `lunarclient.common.v1.GiftInfo` `gift_info` = 4
- **EquippedSpray**
  - `int32` `spray_id` = 1
  - `int32` `slot_number` = 2

## `lunarclient.websocket.spray.v1` ([source](../../proto/extracted/lunarclient_websocket_spray_v1_push.proto))

- **UseSprayPush**
  - `lunarclient.common.v1.Uuid` `player_uuid` = 1
  - `int32` `spray_id` = 2
  - `lunarclient.common.v1.Vector3f` `pos` = 3
  - `lunarclient.common.v1.Direction` `facing` = 4
  - `float` `rotation` = 5
  - `int32` `max_active_sprays` = 6
- **RemoveSprayPush**
  - `lunarclient.common.v1.Uuid` `player_uuid` = 1
  - `lunarclient.common.v1.Vector3f` `pos` = 2
- **RefreshSpraysPush**

## `lunarclient.websocket.store.v1` ([source](../../proto/extracted/lunarclient_websocket_store_v1_push.proto))

- **RefreshStorePush**

## `lunarclient.websocket.tebex.v1` ([source](../../proto/extracted/lunarclient_websocket_tebex_v1_push.proto))

- **OpenTebexJsCheckoutPush**
  - `string` `basket_ident` = 1
  - `string` `locale` = 2

## `lunarclient.websocket.wrapped.v1` ([source](../../proto/extracted/lunarclient_websocket_wrapped_v1_common.proto))

- **CounterUpdate**
  - `string` `counter` = 1
  - `int32` `delta` = 2

## `lunarclient.apollo.button.v1` enums ([source](../../proto/extracted/lunarclient_apollo_button_v1_button.proto))

- enum **ButtonShape**:
  - `BUTTON_SHAPE_UNSPECIFIED = 0`
  - `BUTTON_SHAPE_ROUNDED_SQUARE = 1`
  - `BUTTON_SHAPE_CIRCLE = 2`
- enum **ButtonClientAction**:
  - `BUTTON_CLIENT_ACTION_UNSPECIFIED = 0`
  - `BUTTON_CLIENT_ACTION_OPEN_MINIMAP_VIEW = 1`
  - `BUTTON_CLIENT_ACTION_OPEN_WAYPOINTS_MENU = 2`

## `lunarclient.apollo.evnt.v1` enums ([source](../../proto/extracted/lunarclient_apollo_evnt_v1_character.proto))

- enum **CharacterType**:
  - `CHARACTER_TYPE_UNSPECIFIED = 0`
  - `CHARACTER_TYPE_ANGEL = 1`
  - `CHARACTER_TYPE_AXEL = 2`
  - `CHARACTER_TYPE_BANJAX = 3`
  - `CHARACTER_TYPE_DAEDRA = 4`
  - `CHARACTER_TYPE_FROSKA = 5`
  - `CHARACTER_TYPE_GRANNY = 6`
  - `CHARACTER_TYPE_GREAT_MAGE = 7`
  - `CHARACTER_TYPE_IGNUS = 8`
  - `CHARACTER_TYPE_TULABOT = 9`
  - `CHARACTER_TYPE_SIR_BLOCK = 10`
  - `CHARACTER_TYPE_HARMONY = 11`

## `lunarclient.apollo.evnt.v1` enums ([source](../../proto/extracted/lunarclient_apollo_evnt_v1_gui.proto))

- enum **GuiType**:
  - `GUI_TYPE_UNSPECIFIED = 0`
  - `GUI_TYPE_SUIT = 1`
  - `GUI_TYPE_CHARACTER_SELECTION = 2`
  - `GUI_TYPE_OBSERVER_UI = 3`
  - `GUI_TYPE_WELCOME_UI = 4`
  - `GUI_TYPE_ESC = 5`
  - `GUI_TYPE_PLAYER_INVENTORY = 6`

## `lunarclient.apollo.inventory.v1` enums ([source](../../proto/extracted/lunarclient_apollo_inventory_v1_schema.proto))

- enum **InventoryButtonBox**:
  - `INVENTORY_BUTTON_BOX_UNSPECIFIED = 0`
  - `INVENTORY_BUTTON_BOX_LEFT = 1`
  - `INVENTORY_BUTTON_BOX_RIGHT = 2`
- enum **InventoryType**:
  - `INVENTORY_TYPE_UNSPECIFIED = 0`
  - `INVENTORY_TYPE_PLAYER = 1`

## `lunarclient.apollo.limb.v1` enums ([source](../../proto/extracted/lunarclient_apollo_limb_v1_schema.proto))

- enum **ArmorPiece**:
  - `ARMOR_PIECE_UNSPECIFIED = 0`
  - `ARMOR_PIECE_HELMET = 1`
  - `ARMOR_PIECE_CHESTPLATE = 2`
  - `ARMOR_PIECE_LEGGINGS = 3`
  - `ARMOR_PIECE_BOOTS = 4`
- enum **BodyPart**:
  - `BODY_PART_UNSPECIFIED = 0`
  - `BODY_PART_HEAD = 1`
  - `BODY_PART_TORSO = 2`
  - `BODY_PART_LEFT_ARM = 3`
  - `BODY_PART_RIGHT_ARM = 4`
  - `BODY_PART_LEFT_LEG = 5`
  - `BODY_PART_RIGHT_LEG = 6`

## `lunarclient.apollo.marker.v1` enums ([source](../../proto/extracted/lunarclient_apollo_marker_v1_schema.proto))

- enum **MarkerDisplayCondition**:
  - `MARKER_DISPLAY_CONDITION_UNSPECIFIED = 0`
  - `MARKER_DISPLAY_CONDITION_NEVER = 1`
  - `MARKER_DISPLAY_CONDITION_HOVER = 2`
  - `MARKER_DISPLAY_CONDITION_ALWAYS = 3`
- enum **MarkerOwnerDisplay**:
  - `MARKER_OWNER_DISPLAY_UNSPECIFIED = 0`
  - `MARKER_OWNER_DISPLAY_HEAD = 1`
  - `MARKER_OWNER_DISPLAY_NAME = 2`
- enum **MarkerDescriptionDisplay**:
  - `MARKER_DESCRIPTION_DISPLAY_UNSPECIFIED = 0`
  - `MARKER_DESCRIPTION_DISPLAY_ICON = 1`
  - `MARKER_DESCRIPTION_DISPLAY_TEXT = 2`

## `lunarclient.apollo.nametag.v1` enums ([source](../../proto/extracted/lunarclient_apollo_nametag_v1_schema.proto))

- enum **NametagVisibilityOverride**:
  - `NAMETAG_VISIBILITY_OVERRIDE_UNSPECIFIED = 0`
  - `NAMETAG_VISIBILITY_OVERRIDE_NONE = 1`
  - `NAMETAG_VISIBILITY_OVERRIDE_SHOWN = 2`
  - `NAMETAG_VISIBILITY_OVERRIDE_HIDDEN = 3`

## `lunarclient.apollo.packetenrichment.v1` enums ([source](../../proto/extracted/lunarclient_apollo_packetenrichment_v1_raytrace.proto))

- enum **Direction**:
  - `DIRECTION_UNSPECIFIED = 0`
  - `DIRECTION_DOWN = 1`
  - `DIRECTION_UP = 2`
  - `DIRECTION_NORTH = 3`
  - `DIRECTION_SOUTH = 4`
  - `DIRECTION_WEST = 5`
  - `DIRECTION_EAST = 6`

## `lunarclient.apollo.player.v1` enums ([source](../../proto/extracted/lunarclient_apollo_player_v1_handshake.proto))

- enum **EmbeddedCheckoutSupport**:
  - `EMBEDDED_CHECKOUT_SUPPORT_UNSPECIFIED = 0`
  - `EMBEDDED_CHECKOUT_SUPPORT_OVERLAY = 1`
  - `EMBEDDED_CHECKOUT_SUPPORT_WINDOW = 2`

## `lunarclient.apollo.staffmod.v1` enums ([source](../../proto/extracted/lunarclient_apollo_staffmod_v1_schema.proto))

- enum **StaffMod**:
  - `STAFF_MOD_UNSPECIFIED = 0`
  - `STAFF_MOD_XRAY = 1`
  - `STAFF_MOD_BHOP = 2`
  - `STAFF_MOD_NAMETAGS = 3`

## `lunarclient.apollo.title.v1` enums ([source](../../proto/extracted/lunarclient_apollo_title_v1_schema.proto))

- enum **TitleType**:
  - `TITLE_TYPE_UNSPECIFIED = 0`
  - `TITLE_TYPE_TITLE = 1`
  - `TITLE_TYPE_SUBTITLE = 2`

## `lunarclient.common.v1` enums ([source](../../proto/extracted/lunarclient_common_v1_position.proto))

- enum **Direction**:
  - `DIRECTION_UNSPECIFIED = 0`
  - `DIRECTION_DOWN = 1`
  - `DIRECTION_UP = 2`
  - `DIRECTION_NORTH = 3`
  - `DIRECTION_SOUTH = 4`
  - `DIRECTION_WEST = 5`
  - `DIRECTION_EAST = 6`

## `lunarclient.common.v1` enums ([source](../../proto/extracted/lunarclient_common_v1_skin.proto))

- enum **MinecraftSkinModel**:
  - `MINECRAFT_SKIN_MODEL_UNSPECIFIED = 0`
  - `MINECRAFT_SKIN_MODEL_CLASSIC = 1`
  - `MINECRAFT_SKIN_MODEL_SLIM = 2`

## `lunarclient.common.v1` enums ([source](../../proto/extracted/lunarclient_common_v1_social.proto))

- enum **UserSocialPlatform**:
  - `USER_SOCIAL_PLATFORM_UNSPECIFIED = 0`
  - `USER_SOCIAL_PLATFORM_TWITTER = 1`
  - `USER_SOCIAL_PLATFORM_DISCORD = 2`
  - `USER_SOCIAL_PLATFORM_TWITCH = 3`
  - `USER_SOCIAL_PLATFORM_YOUTUBE = 4`
  - `USER_SOCIAL_PLATFORM_TIKTOK = 5`

## `lunarclient.gameipc.promotion.v1` enums ([source](../../proto/extracted/lunarclient_gameipc_promotion_v1_common.proto))

- enum **PromotionType**:
  - `PROMOTION_TYPE_UNSPECIFIED = 0`
  - `PROMOTION_TYPE_VIDEO = 1`
  - `PROMOTION_TYPE_OUTPLAYED = 2`
  - `PROMOTION_TYPE_MEDAL = 3`

## `lunarclient.gameipc.styngr.v1` enums ([source](../../proto/extracted/lunarclient_gameipc_styngr_v1_common.proto))

- enum **PlaylistLicense**:
  - `PLAYLIST_LICENSE_UNSPECIFIED = 0`
  - `PLAYLIST_LICENSE_LICENSED = 1`
  - `PLAYLIST_LICENSE_ROYALTY_FREE = 2`
- enum **PlaylistMonetization**:
  - `PLAYLIST_MONETIZATION_UNSPECIFIED = 0`
  - `PLAYLIST_MONETIZATION_INTERNAL_AD_FUNDED = 1`
  - `PLAYLIST_MONETIZATION_EXTERNAL_AD_FUNDED = 2`
  - `PLAYLIST_MONETIZATION_PREMIUM = 3`

## `lunarclient.websocket.conversation.v1` enums ([source](../../proto/extracted/lunarclient_websocket_conversation_v1_common.proto))

- enum **ConversationType**:
  - `CONVERSATION_TYPE_UNSPECIFIED = 0`
  - `CONVERSATION_TYPE_FRIEND = 1`
  - `CONVERSATION_TYPE_GROUP_CHAT = 2`
- enum **ConversationMessageKind**:
  - `CONVERSATION_MESSAGE_KIND_UNSPECIFIED = 0`
  - `CONVERSATION_MESSAGE_KIND_USER = 1`
  - `CONVERSATION_MESSAGE_KIND_SYSTEM = 2`
- enum **PreSendAction**:
  - `PRE_SEND_ACTION_UNSPECIFIED = 0`
  - `PRE_SEND_ACTION_NONE = 1`
  - `PRE_SEND_ACTION_TYPING = 2`
- enum **InvitePolicy**:
  - `INVITE_POLICY_UNSPECIFIED = 0`
  - `INVITE_POLICY_EVERYONE = 1`
  - `INVITE_POLICY_OWNER = 2`
- enum **NamePolicy**:
  - `NAME_POLICY_UNSPECIFIED = 0`
  - `NAME_POLICY_EVERYONE = 1`
  - `NAME_POLICY_OWNER = 2`
- enum **IconPolicy**:
  - `ICON_POLICY_UNSPECIFIED = 0`
  - `ICON_POLICY_EVERYONE = 1`
  - `ICON_POLICY_OWNER = 2`
- enum **MessagePinningPolicy**:
  - `MESSAGE_PINNING_POLICY_UNSPECIFIED = 0`
  - `MESSAGE_PINNING_POLICY_EVERYONE = 1`
  - `MESSAGE_PINNING_POLICY_OWNER = 2`
- enum **UploadUsage**:
  - `UPLOAD_USAGE_UNSPECIFIED = 0`
  - `UPLOAD_USAGE_CONVERSATION_ICON = 1`
  - `UPLOAD_USAGE_CHAT = 2`

## `lunarclient.websocket.cosmetic.v2` enums ([source](../../proto/extracted/lunarclient_websocket_cosmetic_v2_common.proto))

- enum **CosmeticOwnershipVisibility**:
  - `COSMETIC_OWNERSHIP_VISIBILITY_UNSPECIFIED = 0`
  - `COSMETIC_OWNERSHIP_VISIBILITY_FRIENDS = 1`
  - `COSMETIC_OWNERSHIP_VISIBILITY_NOONE = 2`
  - `COSMETIC_OWNERSHIP_VISIBILITY_EVERYONE = 3`

## `lunarclient.websocket.friend.v1` enums ([source](../../proto/extracted/lunarclient_websocket_friend_v1_common.proto))

- enum **OnlineFriendStatus**:
  - `ONLINE_FRIEND_STATUS_UNSPECIFIED = 0`
  - `ONLINE_FRIEND_STATUS_ONLINE = 1`
  - `ONLINE_FRIEND_STATUS_AWAY = 2`
  - `ONLINE_FRIEND_STATUS_BUSY = 3`
  - `ONLINE_FRIEND_STATUS_INVISIBLE = 4`
- enum **LastSeenVisibility**:
  - `LAST_SEEN_VISIBILITY_UNSPECIFIED = 0`
  - `LAST_SEEN_VISIBILITY_FRIENDS = 1`
  - `LAST_SEEN_VISIBILITY_NOONE = 2`
  - `LAST_SEEN_VISIBILITY_EVERYONE = 3`
- enum **CountryFlagVisibility**:
  - `COUNTRY_FLAG_VISIBILITY_UNSPECIFIED = 0`
  - `COUNTRY_FLAG_VISIBILITY_EVERYONE = 1`
  - `COUNTRY_FLAG_VISIBILITY_FRIENDS = 2`
  - `COUNTRY_FLAG_VISIBILITY_NOONE = 3`
- enum **GroupChatInvitePrivacy**:
  - `GROUP_CHAT_INVITE_PRIVACY_UNSPECIFIED = 0`
  - `GROUP_CHAT_INVITE_PRIVACY_FRIENDS = 1`
  - `GROUP_CHAT_INVITE_PRIVACY_NOONE = 2`

## `lunarclient.websocket.hostedworld.v1` enums ([source](../../proto/extracted/lunarclient_websocket_hostedworld_v1_common.proto))

- enum **JoinSource**:
  - `JOIN_SOURCE_UNSPECIFIED = 0`
  - `JOIN_SOURCE_LOCAL_AREA_NETWORK = 1`
  - `JOIN_SOURCE_HOSTED_WORLD_WHITELIST = 2`
  - `JOIN_SOURCE_LUNAR_CLIENT_FRIENDS = 3`
  - `JOIN_SOURCE_EVERYONE = 4`
- enum **Joinability**:
  - `JOINABILITY_UNSPECIFIED = 0`
  - `JOINABILITY_ALLOWED = 1`
  - `JOINABILITY_WORLD_FULL = 2`
  - `JOINABILITY_INCOMPATIBLE_MINECRAFT_VERSION = 3`
- enum **Role**:
  - `ROLE_UNSPECIFIED = 0`
  - `ROLE_NONE = 1`
  - `ROLE_HOST = 2`

## `lunarclient.websocket.promotion.v1` enums ([source](../../proto/extracted/lunarclient_websocket_promotion_v1_common.proto))

- enum **PendingRewardType**:
  - `PENDING_REWARD_TYPE_UNSPECIFIED = 0`
  - `PENDING_REWARD_TYPE_MEDAL = 1`

## `lunarclient.websocket.protocol.v1` enums ([source](../../proto/extracted/lunarclient_websocket_protocol_v1_common.proto))

- enum **AllowedSender**:
  - `ALLOWED_SENDER_UNSPECIFIED = 0`
  - `ALLOWED_SENDER_AUTHENTICATED_GAME = 1`
  - `ALLOWED_SENDER_AUTHENTICATED_LAUNCHER = 2`
  - `ALLOWED_SENDER_AUTHENTICATED_GAME_OR_LAUNCHER = 3`

## `lunarclient.websocket.radio.v1` enums ([source](../../proto/extracted/lunarclient_websocket_radio_v1_common.proto))

- enum **RadioPlayingVisibility**:
  - `RADIO_PLAYING_VISIBILITY_UNSPECIFIED = 0`
  - `RADIO_PLAYING_VISIBILITY_FRIENDS = 1`
  - `RADIO_PLAYING_VISIBILITY_NOONE = 2`
  - `RADIO_PLAYING_VISIBILITY_EVERYONE = 3`

## `lunarclient.websocket.screenshot.v1` enums ([source](../../proto/extracted/lunarclient_websocket_screenshot_v1_common.proto))

- enum **Perspective**:
  - `PERSPECTIVE_UNSPECIFIED = 0`
  - `PERSPECTIVE_FIRST = 1`
  - `PERSPECTIVE_BACK = 2`
  - `PERSPECTIVE_FRONT = 3`
- enum **PlayerState**:
  - `PLAYER_STATE_UNSPECIFIED = 0`
  - `PLAYER_STATE_SLEEPING = 1`
  - `PLAYER_STATE_ELYTRA_FLYING = 2`
  - `PLAYER_STATE_FLYING = 3`
  - `PLAYER_STATE_SPRINTING = 4`
  - `PLAYER_STATE_SNEAKING = 5`
  - `PLAYER_STATE_SWIMMING = 6`
  - `PLAYER_STATE_RIDING = 7`
  - `PLAYER_STATE_JUMPING = 8`
  - `PLAYER_STATE_FALLING = 9`
  - `PLAYER_STATE_WALKING = 10`
  - `PLAYER_STATE_STANDING = 11`
- enum **Weather**:
  - `WEATHER_UNSPECIFIED = 0`
  - `WEATHER_CLEAR = 1`
  - `WEATHER_RAIN = 2`
  - `WEATHER_SNOW = 3`
  - `WEATHER_THUNDER = 4`
- enum **ScreenshotPrivacy**:
  - `SCREENSHOT_PRIVACY_UNSPECIFIED = 0`
  - `SCREENSHOT_PRIVACY_PUBLIC = 1`
  - `SCREENSHOT_PRIVACY_UNLISTED = 2`
  - `SCREENSHOT_PRIVACY_PRIVATE = 3`

## `lunarclient.websocket.skyblock.v1` enums ([source](../../proto/extracted/lunarclient_websocket_skyblock_v1_common.proto))

- enum **DungeonRoomType**:
  - `DUNGEON_ROOM_TYPE_UNSPECIFIED = 0`
  - `DUNGEON_ROOM_TYPE_SPAWN = 1`
  - `DUNGEON_ROOM_TYPE_CLEAR = 2`
  - `DUNGEON_ROOM_TYPE_MINIBOSS = 3`
  - `DUNGEON_ROOM_TYPE_PUZZLE = 4`
  - `DUNGEON_ROOM_TYPE_TRAP = 5`
  - `DUNGEON_ROOM_TYPE_FAIRY = 6`
  - `DUNGEON_ROOM_TYPE_BLOOD = 7`
  - `DUNGEON_ROOM_TYPE_BOSS = 8`
  - `DUNGEON_ROOM_TYPE_UNKNOWN = 9`
  - `DUNGEON_ROOM_TYPE_WITHER_DOOR = 10`
- enum **DungeonRoomRotation**:
  - `DUNGEON_ROOM_ROTATION_UNSPECIFIED = 0`
  - `DUNGEON_ROOM_ROTATION_EAST = 1`
  - `DUNGEON_ROOM_ROTATION_SOUTH = 2`
  - `DUNGEON_ROOM_ROTATION_WEST = 3`
  - `DUNGEON_ROOM_ROTATION_NORTH = 4`

## `lunarclient.websocket.socials.v1` enums ([source](../../proto/extracted/lunarclient_websocket_socials_v1_common.proto))

- enum **SocialsVisibility**:
  - `SOCIALS_VISIBILITY_UNSPECIFIED = 0`
  - `SOCIALS_VISIBILITY_FRIENDS = 1`
  - `SOCIALS_VISIBILITY_NOONE = 2`
  - `SOCIALS_VISIBILITY_EVERYONE = 3`

## `lunarclient.websocket.store.v1` enums ([source](../../proto/extracted/lunarclient_websocket_store_v1_common.proto))

- enum **IncomingGiftPrivacy**:
  - `INCOMING_GIFT_PRIVACY_UNSPECIFIED = 0`
  - `INCOMING_GIFT_PRIVACY_EVERYONE = 1`
  - `INCOMING_GIFT_PRIVACY_FRIENDS = 2`
  - `INCOMING_GIFT_PRIVACY_NOONE = 3`

## `lunarclient.websocket.wrapped.v1` enums ([source](../../proto/extracted/lunarclient_websocket_wrapped_v1_common.proto))

- enum **WrappedLeaderboardVisibility**:
  - `WRAPPED_LEADERBOARD_VISIBILITY_UNSPECIFIED = 0`
  - `WRAPPED_LEADERBOARD_VISIBILITY_EVERYONE = 1`
  - `WRAPPED_LEADERBOARD_VISIBILITY_NOONE = 2`
