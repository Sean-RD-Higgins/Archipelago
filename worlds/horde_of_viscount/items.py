from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import HoVWorld

class EQUIP():
    WHIP_PIERCE = "Whip Oil"
    SUB_REFILL = "Sub Refill"
    SUB_REFILL_FREE = "Sub Free-fill"
    WINGS_ONE_FREE = "Double Jump"
    WHIP_DURABLE_A = "Whip Durable A"
    WHIP_DURABLE_B = "Whip Durable B"
    CHEST_BREAKER = "Chest Breaker"
    SHOW_DAMAGE = "Nerd Glasses"
    CUSTOM_COMMANDS = "Custom Command"
    CUSTOM_JUMP = "Custom Jump"
    CUSTOM_ATTACKS = "Custom Attacks"
    MAP_HEAL_MAX = "Cast Map"
    EASYMODE = "Easy Mode Ribbon"
    MAX_SATIATION_UP = "Elastic Belt"
    MAX_SATIATION_DOWN = "Fiber Pills"
    RESTART_STAGE = "Restart Stage Bow"
    PERMALOSS = "Perma- loss Hairpin"
    DEBUFF_ON_FALL = "Amnesia Med"
    LESS_EP = "Iron Rings"
    NO_EP = "Iron Glove"
    NO_MAP_WARP = "Expired BusPass"
    EP1 = "Spirit Chalk"
    EP2 = "Spirit Balm"
    EP3 = "Spirit Spray"
    EP4 = "Spirit Lotion"
    EP5 = "Spirit Soap"
    EP6 = "Spirit Shampoo"
    EP7 = "Spirit Condi-tioner"
    EP8 = "Spirit Body Wash"
    EP9 = "Spirit Oin'mnt"
    EP10 = "Spirit Lather"


class SUBWEAPON():
    BOMB = "Launch Bomb"
    CALTROP = "Backflip Caltrop"
    AXE = "Climbing Axe"
    KNIFE = "Dash Knife"
    WINGS = "Jump Wing"
    CLEATS = "Pogo Cleats"

SUBWEAPON_NAMES = [
    "Launch Bomb",
    "Backflip Caltrop",
    "Climbing Axe",
    "Dash Knife",
    "Jump Wing",
    "Pogo Cleats",
]

class ITEM():
    EYE = "Goo"
    FIBER = "Fiber"
    PROTEIN = "Protein"
    ROCK = "Rock"
    TARSUS = "Tarsus"
    WOOD = "Wood"
    FRESHWATER = "Freshwater"
    HERB = "Herb"
    METAL = "Metal"
    OIL = "Oil"
    FLOUR = "Flour"
    YEAST = "Yeast"
    FEATHER = "Feather"
    BONE = "Bone"
    SHELL = "Shell"
    CHARCOAL = "Charcoal"
    MUTAGEN = "Mutagen"

ITEM_RANK_LIST = [
    ITEM.TARSUS,
    ITEM.HERB,
    ITEM.WOOD,
    ITEM.EYE,
    ITEM.FLOUR,
    ITEM.YEAST,
    ITEM.OIL,
    ITEM.ROCK,
    ITEM.METAL,
    ITEM.FIBER,
    ITEM.PROTEIN,
    ITEM.BONE,
    ITEM.FEATHER,
    ITEM.FRESHWATER,
    ITEM.SHELL,
    ITEM.CHARCOAL,
]

class FOOD():
    ROOM_REDO = "Arcade Credit"

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
# WE CANNOT START THE ITEM IDs AS 0, AS 0 IS RESERVED FOR "NO ITEM" IN AP. START AT 1.
ITEM_NAME_TO_ID = {

    SUBWEAPON.BOMB: 1,
    SUBWEAPON.CALTROP: 2,
    SUBWEAPON.AXE: 3,
    SUBWEAPON.KNIFE: 4,
    SUBWEAPON.WINGS: 5,
    SUBWEAPON.CLEATS: 6,

    ITEM.EYE: 1000,
    ITEM.FIBER: 1001,
    ITEM.PROTEIN: 1002,
    ITEM.ROCK: 1003,
    ITEM.TARSUS: 1004,
    ITEM.WOOD: 1005,
    ITEM.FRESHWATER: 1006,
    ITEM.HERB: 1007,
    ITEM.METAL: 1008,
    ITEM.OIL: 1009,
    ITEM.FLOUR: 1010,
    ITEM.YEAST: 1011,
    ITEM.FEATHER: 1012,
    ITEM.BONE: 1013,
    ITEM.SHELL: 1014,
    ITEM.CHARCOAL: 1015,
    ITEM.MUTAGEN: 1016,
    "Spicy Pepper": 1017,
    "Viscous Tar": 1018,
    "Novaculite": 1019,
    "Vines": 1020,
    "Femur": 1021,
    "Shoe Buckle": 1022,
    "Cloud Sponge": 1023,
    "Tetrodotox": 1024,
    "Capsule": 1025,
    "Pinion": 1026,
    "Pumpkin": 1027,
    "Ladle": 1028,

    "Beetroot": 2000,
    "Eggplant": 2001,
    "Bread": 2002,
    "Biscuit": 2003,
    "Cookie": 2004,
    "Herbal Bread": 2005,
    "Corn": 2006,
    "Potato": 2007,
    "Wheat Pasta": 2008,
    "Pumpkin Soup": 2009,
    "Barley Melt": 2010,
    "Pan Plantain": 2011,
    "Buckwheat Pasta": 2012,
    "Quick Quinoa": 2013,
    "Refried Lentils": 2014,
    "Overnight Oats": 2015,
    "Roast Zucchini": 2016,
    "Sweet Yam": 2017,
    "Squash Soup": 2018,
    "Harvest Medley": 2019,
    "Powder Protein": 2020,
    "Liquid Protein": 2021,
    "Powder Magnesium": 2022,
    "Liquid Magnesium": 2023,
    "Powder Potassium": 2024,
    "Liquid Potassium": 2025,
    "Solid Potassium": 2026,
    "Pill Potassium": 2027,
    "Powder Calcium": 2028,
    "Liquid Calcium": 2029,
    "Solid Calcium": 2030,
    "Pill Calcium": 2031,
    "Powder Iron": 2032,
    "Liquid Iron": 2033,
    "Solid Iron": 2034,
    "Pill Iron": 2035,
    FOOD.ROOM_REDO: 2036,

    # Keep this Item ID free since it maps to ItemType.
    #"Empty Slot": 3000,

    EQUIP.EASYMODE: 4000,
    "Heart Brooch": 4001,
    "Heart Anklet": 4002,
    "Heart Ribbon": 4003,
    "Heart Ring": 4004,
    "Heart Bangle": 4005,
    "Heart Chain": 4006,
    "Heart Armband": 4007,
    "Heart Choker": 4008,
    "Whip Regrip Tape": 4009,
    "Whip Grip Aerator": 4010,
    EQUIP.EP1: 4011,
    EQUIP.EP2: 4012,
    EQUIP.EP3: 4013,
    EQUIP.EP4: 4014,
    EQUIP.EP5: 4015,
    EQUIP.EP6: 4016,
    EQUIP.EP7: 4017,
    EQUIP.EP8: 4018,
    EQUIP.EP9: 4019,
    EQUIP.EP10: 4020,
    "Axe Oil": 4021,
    "Knife Oil": 4022,
    "Caltrop Oil": 4023,
    "Bomb Oil": 4024,
    "Cleat Oil": 4025,
    "Wings Oil": 4026,
    "Loot Whip Magnet": 4027,
    "Loot Sub Magnet": 4028,
    "Loot Magnet": 4029,
    "Loot Magnet Ex": 4030,
    "Invinci-Go": 4031,
    "Invinci-Bro": 4032,
    EQUIP.WHIP_PIERCE: 4033,
    "Axe BOGO Tag": 4034,
    "Knife BOGO Tag": 4035,
    "Caltrop BOGO Tag": 4036,
    "Bomb BOGO Tag": 4037,
    "Cleat BOGO Tag": 4038,
    "Wings BOGO Tag": 4039,
    "Axe Pocket": 4040,
    "Axe Belt": 4041,
    "Axe Bag": 4042,
    "Axe Pack": 4043,
    "Knife Pocket": 4044,
    "Knife Belt": 4045,
    "Knife Bag": 4046,
    "Knife Pack": 4047,
    "Caltrop Pocket": 4048,
    "Caltrop Belt": 4049,
    "Caltrop Bag": 4050,
    "Caltrop Pack": 4051,
    "Bomb Pocket": 4052,
    "Bomb Belt": 4053,
    "Bomb Bag": 4054,
    "Bomb Pack": 4055,
    "Cleat Pocket": 4056,
    "Cleat Belt": 4057,
    "Cleat Bag": 4058,
    "Cleat Pack": 4059,
    "Wings Pocket": 4060,
    "Wings Belt": 4061,
    "Wings Bag": 4062,
    "Wings Pack": 4063,
    "10kg Ton": 4064,
    "Sumo Bubble": 4065,
    "Barb Rage": 4066,
    "Thief Band": 4067,
    "Thief Glove": 4068,
    "Thief Boots": 4069,
    "Thief Cape": 4070,
    "Spike Shirt": 4071,
    "Counter Bangle": 4072,
    "Soloist Mark": 4073,
    "Padded Armor": 4074,
    "Padded Vam-brace": 4075,
    "Padded Helm": 4076,
    "Padded Greaves": 4077,
    "Pretty Ribbon": 4078,
    "Space Helmet": 4079,
    "Axe Whet-stone": 4080,
    "Knife Whet-stone": 4081,
    "Caltrop Whet-stone": 4082,
    "Bomb Whet-stone": 4083,
    "Cleat Whet-stone": 4084,
    "Wing Whet-stone": 4085,
    EQUIP.SHOW_DAMAGE: 4086,
    "Quake Heels": 4087,
    "Quake Toes": 4088,
    EQUIP.CUSTOM_COMMANDS: 4089,
    EQUIP.CUSTOM_JUMP: 4090,
    EQUIP.CUSTOM_ATTACKS: 4091,
    "3kg Ton": 4092,
    "Padded Full-plate": 4093,
    "Whip Sling": 4094,
    "Sword Red Flag": 4095,
    "Shield Red Flag": 4096,
    "Sub Whet-stone": 4097,
    "Health Flag": 4098,
    "Health Happy": 4099,
    "Health Elated": 4100,
    "Health Advance": 4101,
    "Thief Thin Gloves": 4102,
    "Loot WhipAir Magnet": 4103,
    "Apart-ment Heart": 4104,
    "Critical Heart": 4105,
    "House Heart": 4106,
    "Loot Foe Claw": 4107,
    "Loot FoeShot Claw": 4108,
    "Loot WindSub Whpclaw": 4109,
    "Thief Mittens": 4110,
    "Sub Prime": 4111,
    "Break Chain": 4112,
    "Break Link": 4113,
    "Break Reaction": 4114,
    "Break-fast Wrap": 4115,
    "Lunch Bento": 4116,
    "TV Dinner Box": 4117,
    "Dessert TO-GO": 4118,
    "Copper Maker": 4119,
    "Iron Maker": 4120,
    "Tun'stn Maker": 4121,
    "Steel Maker": 4122,
    "Roll Maker": 4123,
    "Taco Maker": 4124,
    "Wrap Maker": 4125,
    "Wedge Maker": 4126,
    "Sub Red Flag": 4127,
    "Sub Max Flag": 4128,
    "Sword Max Flag": 4129,
    "Bandaid Map": 4130,
    "Gauze Map": 4131,
    "Patch Map": 4132,
    EQUIP.MAP_HEAL_MAX: 4133,
    "Grip Red Flag": 4134,
    "Grip Max Flag": 4135,
    "Grip Whet-stone": 4136,
    "Hero's Heart": 4137,
    "Tri-hit Shell": 4138,
    "One Hit Wonder": 4139,
    "Pain Quake": 4140,
    "Sword Quake": 4141,
    "Sub Quake": 4142,
    "Whip Grip Brand": 4143,
    "Hazard Shield": 4144,
    "Bump Shield": 4145,
    "Shot Shield": 4146,
    "All Shield": 4147,
    "Hazard+ Bump Shield": 4148,
    "Hazard+ Shot Shield": 4149,
    "Bump+ Shot Shield": 4150,
    "Hurt Sub Power": 4151,
    "Rolling Claw": 4152,
    "Anti- Magnet Claw": 4153,
    "Axe Crude Oil": 4154,
    "Knife Crude Oil": 4155,
    "Caltrop Crude Oil": 4156,
    "Bomb Crude Oil": 4157,
    "Cleat Crude Oil": 4158,
    "Wings Crude Oil": 4159,
    "Whip Wave": 4160,
    "Cracked Whip Wave": 4161,
    "Thin Whip Wave": 4162,
    "Course Whip Wave": 4163,
    "Sub Chain Break": 4164,
    "Cracked Sub Break": 4165,
    "Thin Sub Break": 4166,
    "Course Sub Break": 4167,
    "Cracked Loot Magnet": 4168,
    "Thin Loot Magnet": 4169,
    "Course Loot Magnet": 4170,
    EQUIP.WINGS_ONE_FREE: 4171,
    EQUIP.RESTART_STAGE: 4172,
    EQUIP.MAX_SATIATION_UP: 4173,
    EQUIP.PERMALOSS: 4174,
    EQUIP.DEBUFF_ON_FALL: 4175,
    EQUIP.LESS_EP: 4176,
    EQUIP.NO_EP: 4177,
    EQUIP.NO_MAP_WARP: 4178,
    EQUIP.MAX_SATIATION_DOWN: 4179,
    "Sub Full Flag": 4180,
    "Sub Thin Flag": 4181,
    "Rigid Armor": 4182,
    EQUIP.SUB_REFILL: 4183,
    EQUIP.SUB_REFILL_FREE: 4184,
    "Food Refill": 4185,
    "Food Free-fill": 4186,
    EQUIP.WHIP_DURABLE_A: 4187,
    EQUIP.WHIP_DURABLE_B: 4188,
    EQUIP.CHEST_BREAKER: 4189,
    "Full Whip Sling": 4190,

    # "Ending A Victory": 1000001,
    # "Ending B Victory": 1000002,
    # "Ending C Victory": 1000003,
    # "Ending D Victory": 1000004,
}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
DEFAULT_ITEM_CLASSIFICATIONS = {

    SUBWEAPON.BOMB: ItemClassification.progression | ItemClassification.useful,
    SUBWEAPON.CALTROP: ItemClassification.progression | ItemClassification.useful,
    SUBWEAPON.AXE: ItemClassification.progression | ItemClassification.useful,
    SUBWEAPON.KNIFE: ItemClassification.progression | ItemClassification.useful,
    SUBWEAPON.WINGS: ItemClassification.progression | ItemClassification.useful,
    SUBWEAPON.CLEATS: ItemClassification.progression | ItemClassification.useful,

    ITEM.EYE: ItemClassification.progression | ItemClassification.useful,
    ITEM.FIBER: ItemClassification.progression | ItemClassification.useful,
    ITEM.PROTEIN: ItemClassification.progression | ItemClassification.useful,
    ITEM.ROCK: ItemClassification.progression | ItemClassification.useful,
    ITEM.TARSUS: ItemClassification.progression | ItemClassification.useful,
    ITEM.WOOD: ItemClassification.progression | ItemClassification.useful,
    ITEM.FRESHWATER: ItemClassification.progression | ItemClassification.useful,
    ITEM.HERB: ItemClassification.progression | ItemClassification.useful,
    ITEM.METAL: ItemClassification.progression | ItemClassification.useful,
    ITEM.OIL: ItemClassification.progression | ItemClassification.useful,
    ITEM.FLOUR: ItemClassification.progression | ItemClassification.useful,
    ITEM.YEAST: ItemClassification.progression | ItemClassification.useful,
    ITEM.FEATHER: ItemClassification.progression | ItemClassification.useful,
    ITEM.BONE: ItemClassification.progression | ItemClassification.useful,
    ITEM.SHELL: ItemClassification.progression | ItemClassification.useful,
    ITEM.CHARCOAL: ItemClassification.progression | ItemClassification.useful,
    ITEM.MUTAGEN: ItemClassification.progression | ItemClassification.useful,
    "Spicy Pepper": ItemClassification.trap,
    "Viscous Tar": ItemClassification.trap,
    "Novaculite": ItemClassification.trap,
    "Vines": ItemClassification.trap,
    "Femur": ItemClassification.trap,
    "Shoe Buckle": ItemClassification.trap,
    "Cloud Sponge": ItemClassification.trap,
    "Tetrodotox": ItemClassification.trap,
    "Capsule": ItemClassification.trap,
    "Pinion": ItemClassification.trap,
    "Pumpkin": ItemClassification.trap,
    "Ladle": ItemClassification.trap,

    "Beetroot": ItemClassification.filler,
    "Eggplant": ItemClassification.filler,
    "Bread": ItemClassification.filler,
    "Biscuit": ItemClassification.filler,
    "Cookie": ItemClassification.filler,
    "Herbal Bread": ItemClassification.filler,
    "Corn": ItemClassification.filler,
    "Potato": ItemClassification.filler,
    "Wheat Pasta": ItemClassification.filler,
    "Pumpkin Soup": ItemClassification.filler,
    "Barley Melt": ItemClassification.filler,
    "Pan Plantain": ItemClassification.filler,
    "Buckwheat Pasta": ItemClassification.filler,
    "Quick Quinoa": ItemClassification.filler,
    "Refried Lentils": ItemClassification.filler,
    "Overnight Oats": ItemClassification.filler,
    "Roast Zucchini": ItemClassification.filler,
    "Sweet Yam": ItemClassification.filler,
    "Squash Soup": ItemClassification.filler,
    "Harvest Medley": ItemClassification.filler,
    "Powder Protein": ItemClassification.filler,
    "Liquid Protein": ItemClassification.filler,
    "Powder Magnesium": ItemClassification.filler,
    "Liquid Magnesium": ItemClassification.filler,
    "Powder Potassium": ItemClassification.filler,
    "Liquid Potassium": ItemClassification.filler,
    "Solid Potassium": ItemClassification.filler,
    "Pill Potassium": ItemClassification.filler,
    "Powder Calcium": ItemClassification.filler,
    "Liquid Calcium": ItemClassification.filler,
    "Solid Calcium": ItemClassification.filler,
    "Pill Calcium": ItemClassification.filler,
    "Powder Iron": ItemClassification.filler,
    "Liquid Iron": ItemClassification.filler,
    "Solid Iron": ItemClassification.filler,
    "Pill Iron": ItemClassification.filler,
    FOOD.ROOM_REDO: ItemClassification.filler,

    #"Empty Slot": ItemClassification.trap,

    EQUIP.EASYMODE: ItemClassification.trap,
    "Heart Brooch": ItemClassification.useful,
    "Heart Anklet": ItemClassification.useful,
    "Heart Ribbon": ItemClassification.useful,
    "Heart Ring": ItemClassification.useful,
    "Heart Bangle": ItemClassification.useful,
    "Heart Chain": ItemClassification.useful,
    "Heart Armband": ItemClassification.useful,
    "Heart Choker": ItemClassification.useful,
    "Whip Regrip Tape": ItemClassification.useful,
    "Whip Grip Aerator": ItemClassification.useful,
    EQUIP.EP1: ItemClassification.useful,
    EQUIP.EP2: ItemClassification.useful,
    EQUIP.EP3: ItemClassification.useful,
    EQUIP.EP4: ItemClassification.useful,
    EQUIP.EP5: ItemClassification.useful,
    EQUIP.EP6: ItemClassification.useful,
    EQUIP.EP7: ItemClassification.useful,
    EQUIP.EP8: ItemClassification.useful,
    EQUIP.EP9: ItemClassification.useful,
    EQUIP.EP10: ItemClassification.useful,
    "Axe Oil": ItemClassification.useful,
    "Knife Oil": ItemClassification.useful,
    "Caltrop Oil": ItemClassification.filler,
    "Bomb Oil": ItemClassification.useful,
    "Cleat Oil": ItemClassification.filler,
    "Wings Oil": ItemClassification.useful,
    "Loot Whip Magnet": ItemClassification.filler,
    "Loot Sub Magnet": ItemClassification.filler,
    "Loot Magnet": ItemClassification.filler,
    "Loot Magnet Ex": ItemClassification.filler,
    "Invinci-Go": ItemClassification.filler,
    "Invinci-Bro": ItemClassification.filler,
    EQUIP.WHIP_PIERCE: ItemClassification.progression | ItemClassification.useful,
    "Axe BOGO Tag": ItemClassification.useful,
    "Knife BOGO Tag": ItemClassification.useful,
    "Caltrop BOGO Tag": ItemClassification.useful,
    "Bomb BOGO Tag": ItemClassification.useful,
    "Cleat BOGO Tag": ItemClassification.useful,
    "Wings BOGO Tag": ItemClassification.useful,
    "Axe Pocket": ItemClassification.useful,
    "Axe Belt": ItemClassification.useful,
    "Axe Bag": ItemClassification.useful,
    "Axe Pack": ItemClassification.useful,
    "Knife Pocket": ItemClassification.useful,
    "Knife Belt": ItemClassification.useful,
    "Knife Bag": ItemClassification.useful,
    "Knife Pack": ItemClassification.useful,
    "Caltrop Pocket": ItemClassification.useful,
    "Caltrop Belt": ItemClassification.useful,
    "Caltrop Bag": ItemClassification.useful,
    "Caltrop Pack": ItemClassification.useful,
    "Bomb Pocket": ItemClassification.useful,
    "Bomb Belt": ItemClassification.useful,
    "Bomb Bag": ItemClassification.useful,
    "Bomb Pack": ItemClassification.useful,
    "Cleat Pocket": ItemClassification.useful,
    "Cleat Belt": ItemClassification.useful,
    "Cleat Bag": ItemClassification.useful,
    "Cleat Pack": ItemClassification.useful,
    "Wings Pocket": ItemClassification.useful,
    "Wings Belt": ItemClassification.useful,
    "Wings Bag": ItemClassification.useful,
    "Wings Pack": ItemClassification.useful,
    "10kg Ton": ItemClassification.useful,
    "Sumo Bubble": ItemClassification.useful,
    "Barb Rage": ItemClassification.trap,
    "Thief Band": ItemClassification.filler,
    "Thief Glove": ItemClassification.filler,
    "Thief Boots": ItemClassification.filler,
    "Thief Cape": ItemClassification.filler,
    "Spike Shirt": ItemClassification.filler,
    "Counter Bangle": ItemClassification.filler,
    "Soloist Mark": ItemClassification.filler,
    "Padded Armor": ItemClassification.filler,
    "Padded Vam-brace": ItemClassification.filler,
    "Padded Helm": ItemClassification.filler,
    "Padded Greaves": ItemClassification.filler,
    "Pretty Ribbon": ItemClassification.trap,
    "Space Helmet": ItemClassification.trap,
    "Axe Whet-stone": ItemClassification.useful,
    "Knife Whet-stone": ItemClassification.useful,
    "Caltrop Whet-stone": ItemClassification.useful,
    "Bomb Whet-stone": ItemClassification.useful,
    "Cleat Whet-stone": ItemClassification.useful,
    "Wing Whet-stone": ItemClassification.useful,
    EQUIP.SHOW_DAMAGE: ItemClassification.filler,
    "Quake Heels": ItemClassification.filler,
    "Quake Toes": ItemClassification.filler,
    EQUIP.CUSTOM_COMMANDS: ItemClassification.useful,
    EQUIP.CUSTOM_JUMP: ItemClassification.useful,
    EQUIP.CUSTOM_ATTACKS: ItemClassification.useful,
    "3kg Ton": ItemClassification.useful,
    "Padded Full-plate": ItemClassification.filler,
    "Whip Sling": ItemClassification.useful,
    "Sword Red Flag": ItemClassification.filler,
    "Shield Red Flag": ItemClassification.filler,
    "Sub Whet-stone": ItemClassification.filler,
    "Health Flag": ItemClassification.filler,
    "Health Happy": ItemClassification.filler,
    "Health Elated": ItemClassification.filler,
    "Health Advance": ItemClassification.filler,
    "Thief Thin Gloves": ItemClassification.filler,
    "Loot WhipAir Magnet": ItemClassification.filler,
    "Apart-ment Heart": ItemClassification.useful,
    "Critical Heart": ItemClassification.useful,
    "House Heart": ItemClassification.useful,
    "Loot Foe Claw": ItemClassification.filler,
    "Loot FoeShot Claw": ItemClassification.filler,
    "Loot WindSub Whpclaw": ItemClassification.filler,
    "Thief Mittens": ItemClassification.filler,
    "Sub Prime": ItemClassification.filler,
    "Break Chain": ItemClassification.filler,
    "Break Link": ItemClassification.filler,
    "Break Reaction": ItemClassification.filler,
    "Break-fast Wrap": ItemClassification.filler,
    "Lunch Bento": ItemClassification.filler,
    "TV Dinner Box": ItemClassification.filler,
    "Dessert TO-GO": ItemClassification.filler,
    "Copper Maker": ItemClassification.useful,
    "Iron Maker": ItemClassification.useful,
    "Tun'stn Maker": ItemClassification.useful,
    "Steel Maker": ItemClassification.useful,
    "Roll Maker": ItemClassification.filler,
    "Taco Maker": ItemClassification.filler,
    "Wrap Maker": ItemClassification.filler,
    "Wedge Maker": ItemClassification.filler,
    "Sub Red Flag": ItemClassification.filler,
    "Sub Max Flag": ItemClassification.filler,
    "Sword Max Flag": ItemClassification.filler,
    "Bandaid Map": ItemClassification.useful,
    "Gauze Map": ItemClassification.useful,
    "Patch Map": ItemClassification.useful,
    EQUIP.MAP_HEAL_MAX: ItemClassification.useful,
    "Grip Red Flag": ItemClassification.filler,
    "Grip Max Flag": ItemClassification.filler,
    "Grip Whet-stone": ItemClassification.filler,
    "Hero's Heart": ItemClassification.trap,
    "Tri-hit Shell": ItemClassification.trap,
    "One Hit Wonder": ItemClassification.trap,
    "Pain Quake": ItemClassification.filler,
    "Sword Quake": ItemClassification.filler,
    "Sub Quake": ItemClassification.filler,
    "Whip Grip Brand": ItemClassification.filler,
    "Hazard Shield": ItemClassification.useful,
    "Bump Shield": ItemClassification.useful,
    "Shot Shield": ItemClassification.useful,
    "All Shield": ItemClassification.useful,
    "Hazard+ Bump Shield": ItemClassification.useful,
    "Hazard+ Shot Shield": ItemClassification.useful,
    "Bump+ Shot Shield": ItemClassification.useful,
    "Hurt Sub Power": ItemClassification.filler,
    "Rolling Claw": ItemClassification.trap,
    "Anti- Magnet Claw": ItemClassification.trap,
    "Axe Crude Oil": ItemClassification.trap,
    "Knife Crude Oil": ItemClassification.trap,
    "Caltrop Crude Oil": ItemClassification.trap,
    "Bomb Crude Oil": ItemClassification.trap,
    "Cleat Crude Oil": ItemClassification.trap,
    "Wings Crude Oil": ItemClassification.trap,
    "Whip Wave": ItemClassification.useful,
    "Cracked Whip Wave": ItemClassification.trap,
    "Thin Whip Wave": ItemClassification.trap,
    "Course Whip Wave": ItemClassification.trap,
    "Sub Chain Break": ItemClassification.filler,
    "Cracked Sub Break": ItemClassification.trap,
    "Thin Sub Break": ItemClassification.trap,
    "Course Sub Break": ItemClassification.trap,
    "Cracked Loot Magnet": ItemClassification.trap,
    "Thin Loot Magnet": ItemClassification.trap,
    "Course Loot Magnet": ItemClassification.trap,
    EQUIP.WINGS_ONE_FREE: ItemClassification.progression | ItemClassification.useful,
    EQUIP.RESTART_STAGE: ItemClassification.trap,
    EQUIP.MAX_SATIATION_UP: ItemClassification.trap,
    EQUIP.PERMALOSS: ItemClassification.trap,
    EQUIP.DEBUFF_ON_FALL: ItemClassification.trap,
    EQUIP.LESS_EP: ItemClassification.trap,
    EQUIP.NO_EP: ItemClassification.trap,
    EQUIP.NO_MAP_WARP: ItemClassification.trap,
    EQUIP.MAX_SATIATION_DOWN: ItemClassification.trap,
    "Sub Full Flag": ItemClassification.filler,
    "Sub Thin Flag": ItemClassification.trap,
    "Rigid Armor": ItemClassification.filler,
    EQUIP.SUB_REFILL: ItemClassification.progression | ItemClassification.useful,
    EQUIP.SUB_REFILL_FREE: ItemClassification.progression | ItemClassification.useful,
    "Food Refill": ItemClassification.filler,
    "Food Free-fill": ItemClassification.filler,
    EQUIP.WHIP_DURABLE_A: ItemClassification.progression | ItemClassification.useful,
    EQUIP.WHIP_DURABLE_B: ItemClassification.progression | ItemClassification.useful,
    EQUIP.CHEST_BREAKER: ItemClassification.progression | ItemClassification.useful,
    "Full Whip Sling": ItemClassification.useful,
}

TRAP_ITEM_NAME_LIST = [
    "Spicy Pepper",
    "Viscous Tar",
    "Novaculite",
    "Vines",
    "Femur",
    "Shoe Buckle",
    "Cloud Sponge",
    "Tetrodotox",
    "Capsule",
    "Pinion",
    "Pumpkin",
    "Ladle",
    #"Empty Slot",
    EQUIP.EASYMODE,
    "Barb Rage",
    "Pretty Ribbon",
    "Space Helmet",
    "Hero's Heart",
    "Tri-hit Shell",
    "One Hit Wonder",
    "Rolling Claw",
    "Anti- Magnet Claw",
    "Axe Crude Oil",
    "Knife Crude Oil",
    "Caltrop Crude Oil",
    "Bomb Crude Oil",
    "Cleat Crude Oil",
    "Wings Crude Oil",
    "Cracked Whip Wave",
    "Thin Whip Wave",
    "Course Whip Wave",
    "Cracked Sub Break",
    "Thin Sub Break",
    "Course Sub Break",
    "Cracked Loot Magnet",
    "Thin Loot Magnet",
    "Course Loot Magnet",
    EQUIP.RESTART_STAGE,
    EQUIP.MAX_SATIATION_UP,
    EQUIP.PERMALOSS,
    EQUIP.DEBUFF_ON_FALL,
    EQUIP.LESS_EP,
    EQUIP.NO_EP,
    EQUIP.NO_MAP_WARP,
    EQUIP.MAX_SATIATION_DOWN,
    "Sub Thin Flag"
]

FILLER_ITEM_NAME_LIST = [
    ITEM.EYE,
    ITEM.FIBER,
    ITEM.PROTEIN,
    ITEM.ROCK,
    ITEM.TARSUS,
    ITEM.WOOD,
    ITEM.FRESHWATER,
    ITEM.HERB,
    ITEM.METAL,
    ITEM.OIL,
    ITEM.FLOUR,
    ITEM.YEAST,
    ITEM.FEATHER,
    ITEM.BONE,
    ITEM.SHELL,
    ITEM.CHARCOAL,
    ITEM.MUTAGEN,
    "Beetroot",
    "Eggplant",
    "Bread",
    "Biscuit",
    "Cookie",
    "Herbal Bread",
    "Corn",
    "Potato",
    "Wheat Pasta",
    "Pumpkin Soup",
    "Barley Melt",
    "Pan Plantain",
    "Buckwheat Pasta",
    "Quick Quinoa",
    "Refried Lentils",
    "Overnight Oats",
    "Roast Zucchini",
    "Sweet Yam",
    "Squash Soup",
    "Harvest Medley",
    "Powder Protein",
    "Liquid Protein",
    "Powder Magnesium",
    "Liquid Magnesium",
    "Powder Potassium",
    "Liquid Potassium",
    "Solid Potassium",
    "Pill Potassium",
    "Powder Calcium",
    "Liquid Calcium",
    "Solid Calcium",
    "Pill Calcium",
    "Powder Iron",
    "Liquid Iron",
    "Solid Iron",
    "Pill Iron",
    FOOD.ROOM_REDO,
    "Caltrop Oil",
    "Cleat Oil",
    "Loot Whip Magnet",
    "Loot Sub Magnet",
    "Loot Magnet",
    "Loot Magnet Ex",
    "Invinci-Go",
    "Invinci-Bro",
    "Thief Band",
    "Thief Glove",
    "Thief Boots",
    "Thief Cape",
    "Spike Shirt",
    "Counter Bangle",
    "Soloist Mark",
    "Padded Armor",
    "Padded Vam-brace",
    "Padded Helm",
    "Padded Greaves",
    EQUIP.SHOW_DAMAGE,
    "Quake Heels",
    "Quake Toes",
    "Padded Full-plate",
    "Sword Red Flag",
    "Shield Red Flag",
    "Sub Whet-stone",
    "Health Flag",
    "Health Happy",
    "Health Elated",
    "Health Advance",
    "Thief Thin Gloves",
    "Loot WhipAir Magnet",
    "Loot Foe Claw",
    "Loot FoeShot Claw",
    "Loot WindSub Whpclaw",
    "Thief Mittens",
    "Sub Prime",
    "Break Chain",
    "Break Link",
    "Break Reaction",
    "Break-fast Wrap",
    "Lunch Bento",
    "TV Dinner Box",
    "Dessert TO-GO",
    "Roll Maker",
    "Taco Maker",
    "Wrap Maker",
    "Wedge Maker",
    "Sub Red Flag",
    "Sub Max Flag",
    "Sword Max Flag",
    "Grip Red Flag",
    "Grip Max Flag",
    "Grip Whet-stone",
    "Pain Quake",
    "Sword Quake",
    "Sub Quake",
    "Whip Grip Brand",
    "Hurt Sub Power",
    "Sub Chain Break",
    "Sub Full Flag",
    "Rigid Armor",
    "Food Refill",
    "Food Free-fill",
]

HARDMODE_FILLER_LIST = [
    EQUIP.WHIP_DURABLE_B,
    EQUIP.SUB_REFILL,
]

PROGRESSION_ITEM_NAME_LIST = [
    ITEM.EYE,
    ITEM.FIBER,
    ITEM.PROTEIN,
    ITEM.ROCK,
    ITEM.TARSUS,
    ITEM.WOOD,
    ITEM.FRESHWATER,
    ITEM.HERB,
    ITEM.METAL,
    ITEM.OIL,
    ITEM.FLOUR,
    ITEM.YEAST,
    ITEM.FEATHER,
    ITEM.BONE,
    ITEM.SHELL,
    ITEM.CHARCOAL,
    ITEM.MUTAGEN,
    SUBWEAPON.BOMB,
    SUBWEAPON.CALTROP,
    SUBWEAPON.AXE,
    SUBWEAPON.KNIFE,
    SUBWEAPON.WINGS,
    SUBWEAPON.CLEATS,
    EQUIP.WHIP_PIERCE,
    EQUIP.WINGS_ONE_FREE,
    EQUIP.SUB_REFILL,
    EQUIP.SUB_REFILL_FREE,
    EQUIP.WHIP_DURABLE_A,
    EQUIP.WHIP_DURABLE_B,
    EQUIP.CHEST_BREAKER,
    EQUIP.EP1,
    EQUIP.EP2,
    EQUIP.EP3,
    EQUIP.EP4,
    EQUIP.EP5,
    EQUIP.EP6,
    EQUIP.EP7,
    EQUIP.EP8,
    EQUIP.EP9,
    EQUIP.EP10,
    EQUIP.SUB_REFILL,
    EQUIP.SUB_REFILL_FREE,
    "Health Flag",
    "Heart Brooch",
    "Heart Anklet",
    "Heart Ribbon",
    "Heart Ring",
    "Heart Bangle",
    "Heart Chain",
    "Heart Armband",
    "Heart Choker",
]

# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class HoVItem(Item):
    game = "Horde of Viscount"

# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: HoVWorld) -> str:
    # APQuest has an option called "trap_chance".
    # This is the percentage chance that each filler item is a Math Trap instead of a Confetti Cannon.
    # For this purpose, we need to use a random generator.

    # IMPORTANT: Whenever you need to use a random generator, you must use world.random.
    # This ensures that generating with the same generator seed twice yields the same output.
    # DO NOT use a bare random object from Python's built-in random module.
    if world.random.randint(0, 99) < world.options.bad_equip_chance:
        maxTrapIndex = len(TRAP_ITEM_NAME_LIST)
        trapIndex = world.random.randint(0, maxTrapIndex)
        return TRAP_ITEM_NAME_LIST[trapIndex]
    
    maxFillerIndex = len(FILLER_ITEM_NAME_LIST)
    fillerIndex = world.random.randint(0, maxFillerIndex - 1)
    return FILLER_ITEM_NAME_LIST[fillerIndex]


def create_item_with_correct_classification(world: HoVWorld, name: str) -> HoVItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # In our case, bonus progression equips just make the game easier (and thus labeled as "filler") in hard mode.
    if  name in HARDMODE_FILLER_LIST and world.options.hard_mode:
        classification = ItemClassification.filler

    return HoVItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: HoVWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.
    itempool: list[Item] = []
    
    for itemName in DEFAULT_ITEM_CLASSIFICATIONS.keys():
        itempool += world.create_item(itemName),


    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # APQuest has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to APQuest's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().
    if world.options.arcade_credit_fill:
        # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
        arcade_credit = next(item for item in itempool if item.name == FOOD.ROOM_REDO)
        for _ in range(world.options.arcade_credit_fill.value // 6):
            world.push_precollected(arcade_credit)
    if world.options.whip_oil:
        whip_oil = next(item for item in itempool if item.name == EQUIP.WHIP_PIERCE)
        world.push_precollected(whip_oil)
    if world.options.dash_knife:
        dash_knife = next(item for item in itempool if item.name == SUBWEAPON.KNIFE)
        world.push_precollected(dash_knife)
    if world.options.sub_refill:
        sub_refill = next(item for item in itempool if item.name == EQUIP.SUB_REFILL)
        world.push_precollected(sub_refill)
    if world.options.sub_freefill:
        sub_freefill = next(item for item in itempool if item.name == EQUIP.SUB_REFILL_FREE)
        world.push_precollected(sub_freefill)
    if world.options.nerd_glasses:
        nerd_glasses = next(item for item in itempool if item.name == EQUIP.SHOW_DAMAGE)
        world.push_precollected(nerd_glasses)
    if world.options.custom_command_equips:
        custom_commands = next(item for item in itempool if item.name == EQUIP.CUSTOM_COMMANDS)
        world.push_precollected(custom_commands)
        custom_jump = next(item for item in itempool if item.name == EQUIP.CUSTOM_JUMP)
        world.push_precollected(custom_jump)
        custom_attacks = next(item for item in itempool if item.name == EQUIP.CUSTOM_ATTACKS)
        world.push_precollected(custom_attacks)
    if world.options.whip_rank2:
        whip_rank2 = next(item for item in itempool if item.name == EQUIP.WHIP_DURABLE_A)
        world.push_precollected(whip_rank2)
    if world.options.whip_rank3:
        whip_rank3 = next(item for item in itempool if item.name == EQUIP.WHIP_DURABLE_B)
        world.push_precollected(whip_rank3)
    if world.options.heal_hub:
        heal_hub = next(item for item in itempool if item.name == EQUIP.MAP_HEAL_MAX)
        world.push_precollected(heal_hub)
    if world.options.easyModeRibbon:
        easyModeRibbon = next(item for item in itempool if item.name == EQUIP.EASYMODE)
        world.push_precollected(easyModeRibbon)
    if world.options.fiberPills:
        fiberPills = next(item for item in itempool if item.name == EQUIP.FIBER_PILLS)
        world.push_precollected(fiberPills)
    if world.options.restartStageBow:
        restartStageBow = next(item for item in itempool if item.name == EQUIP.RESTART_STAGE)
        world.push_precollected(restartStageBow)
    if world.options.permaLossHairpin:
        permaLossHairpin = next(item for item in itempool if item.name == EQUIP.PERMALOSS)
        world.push_precollected(permaLossHairpin)
    if world.options.fiberPills:
        fiberPills = next(item for item in itempool if item.name == EQUIP.DEBUFF_ON_FALL)
        world.push_precollected(fiberPills)
    if world.options.ironRings:
        ironRings = next(item for item in itempool if item.name == EQUIP.LESS_EP)
        world.push_precollected(ironRings)
    if world.options.ironGlove:
        ironGlove = next(item for item in itempool if item.name == EQUIP.NO_EP)
        world.push_precollected(ironGlove)
    if world.options.expiredBusPass:
        expiredBusPass = next(item for item in itempool if item.name == EQUIP.NO_MAP_WARP)
        world.push_precollected(expiredBusPass)


