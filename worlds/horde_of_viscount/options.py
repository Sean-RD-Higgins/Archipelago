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



# A Choice is an option with multiple discrete choices. This will be represented by a dropdown on the website.
class Ending(Choice):
    """
    Which Ending is required to complete the game. 
    Ending A is the hardest, requiring no assistance from Lasha nor Merchants.
    Ending B is the easiest. 
    Ending C is the default. 
    Ending D is the best ending, requiring the most work. 
    """

    display_name = "Ending Required"

    option_A = 0
    option_B = 1
    option_C = 2
    option_D = 3

    # Choice options must define an explicit default value.
    default = option_B

class EasyModeRibbon(Toggle): 
    """
    Start with Easy Mode Ribbon. A pretty ribbon making hunting much easier. More hearts for less drops.
    """
    
    display_name = "Easy Mode Ribbon"
    # EQUIP.EASYMODE
    default = False

class FiberPills(Toggle): 
    """
    Start with Fiber Pills. Decrease max Satiation. More EP for more difficulty.
    """
    
    display_name = "Fiber Pills"
    # EQUIP.MAX_SATIATION_DOWN
    default = False

class RestartStageBow(Toggle): 
    """
    Start with Restart Stage Bow. When defeated, you will restart the stage. More EP for more difficulty.
    """
    
    display_name = "Restart Stage Bow"
    # EQUIP.RESTART_STAGE
    default = True

class PermaLossHairpin(Toggle): 
    """
    Start with Perma-loss Hairpin. When defeated, you lose all progress. More EP for more difficulty
    """
    
    display_name = "Perma-loss Hairpin"
    # EQUIP.PERMALOSS
    default = False

class AmnesiaMed(Toggle): 
    """
    Start with Amnesia Med. When defeated, you lose all of your buffs. More EP for more difficulty.
    """
    
    display_name = "Amnesia Med"
    # EQUIP.DEBUFF_ON_FALL
    default = False

class IronRings(Toggle): 
    """
    Start with Iron Rings. You just have less EQUIP POINTS to work with, that's it.  No benefit besides bragging.
    """
    
    display_name = "Iron Rings"
    # EQUIP.LESS_EP
    default = False

class IronGlove(Toggle): 
    """
    Start with Iron Glove. You just have NO EQUIP POINTS.  No benefit besides bragging.
    """
    
    display_name = "Iron Glove"
    # EQUIP.NO_EP
    default = False

class ExpiredBusPass(Toggle): 
    """
    Start with Expired BusPass. You cannot warp to any other map. More EP for more difficulty.
    """
    
    display_name = "Expired BusPass"
    # EQUIP.NO_MAP_WARP
    default = False


class LevelUpProgression(Range):
    """
    Smaller number means materials required for leveling up is easier to find. Larger number means the materials required will not be as easily obtainable.
    """

    display_name = "Level Up Progression"

    range_start = 0
    range_end = 100
    default = 50

class CustomCommandEquips(Toggle):
    """
    Start with all custom command equips so you can map your buttons to directions + Jump, Attack, or Subweapon.
    """

    # The docstring of an option is used as the description on the website and in the template yaml.

    # You'll also want to set a display name, which will determine what the option is called on the website.
    display_name = "Custom Command Equips"
    default = True
class NerdGlasses(Toggle):
    """
    Start with Nerd Glasses, allowing you to see damage numbers.
    """

    # The docstring of an option is used as the description on the website and in the template yaml.

    # You'll also want to set a display name, which will determine what the option is called on the website.
    display_name = "Nerd Glasses"
    default = True
class WhipOil(Toggle):
    """
    Start with Whip Oil, allowing you to pierce through Hordemen with your Whip.
    """

    # The docstring of an option is used as the description on the website and in the template yaml.

    # You'll also want to set a display name, which will determine what the option is called on the website.
    display_name = "Whip Oil"
    default = True

class DashKnife(Toggle):
    """
    Start with Dash Knife, to traverse horizontally.
    """

    # The docstring of an option is used as the description on the website and in the template yaml.

    # You'll also want to set a display name, which will determine what the option is called on the website.
    display_name = "Dash Knife"
    default = True

class SubRefill(Toggle):
    """
    Start with Sub Refill, which will give you some subweapons from storage when going to a new room. Logic requires this, disable at your own risk.
    """
    display_name = "Sub Refill"
    default = True

class SubFreefill(Toggle):
    """
    Start with Sub Freefill, which will give you some subweapons when going to a new room. Logic requires this, disable at your own risk.
    """
    display_name = "Sub Freefill"
    default = True

class DoubleJump(Toggle):
    """
    Start with the Double Jump Equip
    """
    display_name = "Double Jump"
    default = False

class HardMode(Toggle):
    """
    In hard mode, you will NOT have Sub Refill; only Sub FreeFill, and less powerful EQUIPs. Might be impossible.
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
    default = True

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
class ArcadeCreditFill(Range):
    """
    How many arcade credits you will start with. These are used to restart a room with no cost.
    """

    display_name = "Arcade Credit Fill"

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

    display_name = "Map Size"

    range_start = 5
    range_end = 19
    default = 15


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class HoVOptions(PerGameCommonOptions):

    ending: Ending
    
    custom_command_equips: CustomCommandEquips
    nerd_glasses: NerdGlasses
    whip_oil: WhipOil
    arcade_credit_fill: ArcadeCreditFill
    level_up_progression: LevelUpProgression

    easyModeRibbon: EasyModeRibbon
    fiberPills: FiberPills
    restartStageBow: RestartStageBow
    permaLossHairpin: PermaLossHairpin
    amnesiaMed: AmnesiaMed
    ironRings: IronRings
    ironGlove: IronGlove
    expiredBusPass: ExpiredBusPass

    heal_hub: HealHub
    whip_rank2: WhipRank2
    whip_rank3: WhipRank3
    double_jump: DoubleJump
    dash_knife: DashKnife

    bad_equip_chance: BadEquipChance
    hard_mode: HardMode
    sub_refill: SubRefill
    sub_freefill: SubFreefill

    # subweapon_spawn: SubweaponSpawn
    # hub_sub_fill: HubSubFill
    # hub_food_fill: HubFoodFill
    # drops_plus: DropsPlus
    # chest_choice: ChestChoice
    # player_sprite: PlayerSprite
    # chests_required: ChestsRequired
    # map_size: MapSize


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Goal",
        [Ending],
    ),
    OptionGroup(
        "Quality of Life",
        [CustomCommandEquips, NerdGlasses, WhipOil, ArcadeCreditFill, LevelUpProgression],
    ),
    OptionGroup(
        "Much Easier Mode",
        [HealHub, DoubleJump, WhipRank2, WhipRank3, DashKnife, FiberPills, EasyModeRibbon],
    ),
    OptionGroup(
        "Much Harder Mode",
        [RestartStageBow, AmnesiaMed, IronRings, IronGlove, ExpiredBusPass, BadEquipChance],
    ),
    OptionGroup(
        "Customize",
        [HardMode, SubRefill, SubFreefill, PermaLossHairpin],
    ),
    # OptionGroup(
    #     "Roguelite Mode",
    #     [MapSize, SubweaponSpawn, ChestsRequired, PlayerSprite, HubSubFill, HubFoodFill, 
    #         DropsPlus, ChestChoice],
    # ),
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "easy": {
        "ending": Ending.option_B,

        "custom_command_equips": True,
        "nerd_glasses": True,
        "whip_oil": True,
        "arcade_credit_fill": ArcadeCreditFill.range_end,
        "level_up_progression": LevelUpProgression.range_start,

        "whip_rank2": True,
        "whip_rank3": True,
        "heal_hub": True,
        "double_jump": True,
        "dash_knife": True,
        "easyModeRibbon": True,
        "fiberPills": True,

        "sub_refill": True,
        "sub_freefill": True,
        "restartStageBow": False,
        "permaLossHairpin": False,
        "amnesiaMed": False,
        "ironRings": False,
        "ironGlove": False,
        "expiredBusPass": False,

        "hard_mode": False,
        # "subweapon_spawn": True,
        # "heal_hub": True,
        # "hub_sub_fill": True,
        # "hub_food_fill": True,
        # "drops_plus": True,
        # "chest_choice": 3,
        # "bad_equip_chance": 0,
        # "player_sprite": PlayerSprite.option_whipp,
        # "chests_required": 1,
        # "map_size": 9,
    },
    "normal": {
        "ending": Ending.option_C,

        "custom_command_equips": True,
        "nerd_glasses": True,
        "whip_oil": True,
        "arcade_credit_fill": ArcadeCreditFill.range_end,
        "level_up_progression": LevelUpProgression.range_end // 2,

        "heal_hub": True,
        "double_jump": False,
        "whip_rank2": False,
        "whip_rank3": False,
        "dash_knife": True,
        "easyModeRibbon": False,
        "fiberPills": False,

        "sub_refill": True,
        "sub_freefill": True,
        "restartStageBow": True,
        "permaLossHairpin": False,
        "amnesiaMed": False,
        "ironRings": False,
        "ironGlove": False,
        "expiredBusPass": False,
        
        "hard_mode": False,
        # "subweapon_spawn": False,
        # "heal_hub": False,
        # "hub_sub_fill": False,
        # "hub_food_fill": False,
        # "drops_plus": False,
        # "chest_choice": 2,
        # "bad_equip_chance": 10,
        # "player_sprite": PlayerSprite.option_whipp,
        # "chests_required": 3,
        # "map_size": 15,
    },
    "hard": {
        "ending": Ending.option_D,

        "custom_command_equips": True,
        "nerd_glasses": False,
        "whip_oil": False,
        "arcade_credit_fill": ArcadeCreditFill.range_start,
        "level_up_progression": LevelUpProgression.range_end * 0.75,

        "heal_hub": True,
        "double_jump": True,
        "whip_rank2": False,
        "whip_rank3": False,
        "dash_knife": False,
        "easyModeRibbon": False,
        "fiberPills": False,

        "sub_refill": True,
        "sub_freefill": True,
        "restartStageBow": True,
        "permaLossHairpin": False,
        "amnesiaMed": True,
        "ironRings": False,
        "ironGlove": False,
        "expiredBusPass": False,

        "hard_mode": True,
        # "subweapon_spawn": False,
        # "heal_hub": False,
        # "hub_sub_fill": False,
        # "hub_food_fill": False,
        # "drops_plus": False,
        # "chest_choice": 1,
        # "bad_equip_chance": 50,
        # "player_sprite": PlayerSprite.option_whipp,
        # "chests_required": 0,
        # "map_size": 19,
    },
    "unfair": {
        "ending": Ending.option_A,

        "custom_command_equips": True,
        "nerd_glasses": False,
        "whip_oil": False,
        "arcade_credit_fill": ArcadeCreditFill.range_start,
        "level_up_progression": LevelUpProgression.range_end,

        "heal_hub": False,
        "double_jump": False,
        "whip_rank2": False,
        "whip_rank3": False,
        "dash_knife": False,
        "easyModeRibbon": False,
        "fiberPills": False,

        "sub_refill": False,
        "sub_freefill": False,
        "restartStageBow": True,
        "permaLossHairpin": True,
        "amnesiaMed": True,
        "ironRings": True,
        "ironGlove": True,
        "expiredBusPass": True,
        
        "hard_mode": True,
        # "subweapon_spawn": False,
        # "hub_sub_fill": False,
        # "hub_food_fill": False,
        # "drops_plus": False,
        # "chest_choice": 1,
        # "bad_equip_chance": 100,
        # "player_sprite": PlayerSprite.option_whipp,
        # "chests_required": 0,
        # "map_size": 19,
    },
}
