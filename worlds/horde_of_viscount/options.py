from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  APQuest doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md


# The first type of Option we'll discuss is the Toggle.
# A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# The default for a toggle is "off".
# If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.
class HardMode(Toggle):
    """
    In hard mode, you will NOT have Sub Refill; only Sub FreeFill.
    """

    # The docstring of an option is used as the description on the website and in the template yaml.

    # You'll also want to set a display name, which will determine what the option is called on the website.
    display_name = "Hard Mode"


class SubweaponSpawn(Toggle):
    """
    A handful of a subweapon type can spawn randomly in chests.
    This will make the map run generally much easier.
    """

    display_name = "Subweapon Spawn"


class HealHub(Toggle):
    """
    Arrival to the main hub room will fully heal you.
    """

    display_name = "Hub Heal"


class HubSubFill(Toggle):
    """
    Arrival to the main hub room will free refill your held subweapons
    """

    display_name = "Hub Sub Fill"


class HubFoodFill(Toggle):
    """
    Arrival to the main hub room will free refill your held food
    """

    display_name = "Hub Food Fill"

class WhipRank2(Toggle):
    """
    Start a run with a Rank 2 weapon
    """

    display_name = "Whip Rank 2"

class WhipRank3(Toggle):
    """
    Start a run with a Rank 3 weapon
    """

    display_name = "Whip Rank 3"

class DropsPlus(Toggle):
    """
    Increases the amount of drops you get when you pick up a bundle from chests.
    """

    display_name = "Drops +"


# A Range is a numeric option with a min and max value. This will be represented by a slider on the website.
class ChestChoice(Range):
    """
    Increases the amount of item options you get when opening a chest.
    """

    display_name = "Chest Choice +"

    range_start = 1
    range_end = 3

    # Range options must define an explicit default value.
    default = 1

class BadEquipChance(Range):
    """
    Percentage chance that any given filler item will end up as a detrimental Equip.
    """

    display_name = "Bad Equip Chance"

    range_start = 0
    range_end = 100
    default = 0



# A Range is a numeric option with a min and max value. This will be represented by a slider on the website.
class ArcadeTokenFill(Range):
    """
    How much confetti each use of a confetti cannon will fire.
    """

    display_name = "Arcade Token Fill"

    range_start = 0
    range_end = 99

    # Range options must define an explicit default value.
    default = 0


# A Choice is an option with multiple discrete choices. This will be represented by a dropdown on the website.
class PlayerSprite(Choice):
    """
    The sprite that the player will have.
    """

    display_name = "Player Sprite"

    option_whipp = 0
    option_whipp_light = 1
    option_whipp_dark = 2
    option_whipp_classic = 3

    # Choice options must define an explicit default value.
    default = option_whipp

# A Choice is an option with multiple discrete choices. This will be represented by a dropdown on the website.
class ChestsRequired(Choice):
    """
    Sets the amount of chests per room required to complete it.
    """

    display_name = "Chests Required"

    option_all = 0
    option_1 = 1
    option_2 = 2
    option_3 = 3

    # Choice options must define an explicit default value.
    default = option_2

class MapSize(Range):
    """
    The amount of room tiles horizontally of the map. The same number will be used for how many tiles vertically there will be on the map.
    """

    display_name = "Bad Equip Chance"

    range_start = 0
    range_end = 100
    default = 0


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class APQuestOptions(PerGameCommonOptions):
    hard_mode: HardMode
    subweapon_spawn: SubweaponSpawn
    heal_hub: HealHub
    hub_sub_fill: HubSubFill
    hub_food_fill: HubFoodFill
    whip_rank2: WhipRank2
    whip_rank3: WhipRank3
    drops_plus: DropsPlus
    chest_choice: ChestChoice
    bad_equip_chance: BadEquipChance
    arcade_token_fill: ArcadeTokenFill
    player_sprite: PlayerSprite
    chests_required: ChestsRequired
    map_size: MapSize


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay",
        [HardMode, MapSize, SubweaponSpawn, ChestsRequired],
    ),
    OptionGroup(
        "Boons",
        [HealHub, HubSubFill, HubFoodFill, WhipRank2, WhipRank3, DropsPlus, ChestChoice, BadEquipChance, ArcadeTokenFill],
    ),
    OptionGroup(
        "Vanity",
        [PlayerSprite],
    ),
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "easy": {
        "hard_mode": False,
        "subweapon_spawn": True,
        "heal_hub": True,
        "hub_sub_fill": True,
        "hub_food_fill": True,
        "whip_rank2": True,
        "whip_rank3": True,
        "drops_plus": True,
        "chest_choice": 3,
        "bad_equip_chance": 0,
        "arcade_token_fill": ArcadeTokenFill.range_end,
        "player_sprite": PlayerSprite.option_whipp,
        "chests_required": 1,
        "map_size": 6,
    },
    "normal": {
        "hard_mode": False,
        "subweapon_spawn": False,
        "heal_hub": False,
        "hub_sub_fill": False,
        "hub_food_fill": False,
        "whip_rank2": False,
        "whip_rank3": False,
        "drops_plus": False,
        "chest_choice": 2,
        "bad_equip_chance": 10,
        "arcade_token_fill": ArcadeTokenFill.range_end,
        "player_sprite": PlayerSprite.option_whipp,
        "chests_required": 3,
        "map_size": 9,
    },
    "hard": {
        "hard_mode": True,
        "subweapon_spawn": False,
        "heal_hub": False,
        "hub_sub_fill": False,
        "hub_food_fill": False,
        "whip_rank2": False,
        "whip_rank3": False,
        "drops_plus": False,
        "chest_choice": 1,
        "bad_equip_chance": 50,
        "arcade_token_fill": ArcadeTokenFill.range_start,
        "player_sprite": PlayerSprite.option_whipp,
        "chests_required": 0,
        "map_size": 16,
    },
}
