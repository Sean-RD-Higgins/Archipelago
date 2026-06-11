from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import HoVWorld

    	
# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
ITEM_NAME_TO_ID = {

    "Launch Bomb": 0_000,
    "Backflip Caltrop": 0_001,
    "Climbing Axe": 0_002,
    "Dash Knife": 0_003,
    "Jump Wing": 0_004,
    "Pogo Cleats": 0_005,

    "Goo": 1_000,
    "Fiber": 1_001,
    "Protein": 1_002,
    "Rock": 1_003,
    "Tarsus": 1_004,
    "Wood": 1_005,
    "Freshwater": 1_006,
    "Herb": 1_007,
    "Metal": 1_008,
    "Oil": 1_009,
    "Flour": 1_010,
    "Yeast": 1_011,
    "Feather": 1_012,
    "Bone": 1_013,
    "Shell": 1_014,
    "Charcoal": 1_015,
    "Mutagen": 1_016,
    "Spicy Pepper": 1_017,
    "Viscous Tar": 1_018,
    "Novaculite": 1_019,
    "Vines": 1_020,
    "Femur": 1_021,
    "Shoe Buckle": 1_022,
    "Cloud Sponge": 1_023,
    "Tetrodotox": 1_024,
    "Capsule": 1_025,
    "Pinion": 1_026,
    "Pumpkin": 1_027,
    "Ladle": 1_028,

    "Beetroot": 2_000,
    "Eggplant": 2_001,
    "Bread": 2_002,
    "Biscuit": 2_003,
    "Cookie": 2_004,
    "Herbal Bread": 2_005,
    "Corn": 2_006,
    "Potato": 2_007,
    "Wheat Pasta": 2_008,
    "Pumpkin Soup": 2_009,
    "Barley Melt": 2_010,
    "Pan Plantain": 2_011,
    "Buckwheat Pasta": 2_012,
    "Quick Quinoa": 2_013,
    "Refried Lentils": 2_014,
    "Overnight Oats": 2_015,
    "Roast Zucchini": 2_016,
    "Sweet Yam": 2_017,
    "Squash Soup": 2_018,
    "Harvest Medley": 2_019,
    "Powder Protein": 2_020,
    "Liquid Protein": 2_021,
    "Powder Magnesium": 2_022,
    "Liquid Magnesium": 2_023,
    "Powder Potassium": 2_024,
    "Liquid Potassium": 2_025,
    "Solid Potassium": 2_026,
    "Pill Potassium": 2_027,
    "Powder Calcium": 2_028,
    "Liquid Calcium": 2_029,
    "Solid Calcium": 2_030,
    "Pill Calcium": 2_031,
    "Powder Iron": 2_032,
    "Liquid Iron": 2_033,
    "Solid Iron": 2_034,
    "Pill Iron": 2_035,
    "Arcade Credit": 2_036,

    "Empty Slot": 3_000,

    "Easy Mode Ribbon": 4_000,
    "Heart Brooch": 4_001,
    "Heart Anklet": 4_002,
    "Heart Ribbon": 4_003,
    "Heart Ring": 4_004,
    "Heart Bangle": 4_005,
    "Heart Chain": 4_006,
    "Heart Armband": 4_007,
    "Heart Choker": 4_008,
    "Whip Regrip Tape": 4_009,
    "Whip Grip Aerator": 4_010,
    "Spirit Chalk": 4_011,
    "Spirit Balm": 4_012,
    "Spirit Spray": 4_013,
    "Spirit Lotion": 4_014,
    "Spirit Soap": 4_015,
    "Spirit Shampoo": 4_016,
    "Spirit Condi-tioner": 4_017,
    "Spirit Body Wash": 4_018,
    "Spirit Oin'mnt": 4_019,
    "Spirit Lather": 4_020,
    "Axe Oil": 4_021,
    "Knife Oil": 4_022,
    "Caltrop Oil": 4_023,
    "Bomb Oil": 4_024,
    "Cleat Oil": 4_025,
    "Wings Oil": 4_026,
    "LOOT_GRAB_WHIP": 4_027,
    "Loot Sub Magnet": 4_028,
    "Loot Magnet": 4_029,
    "Loot Magnet Ex": 4_030,
    "Invinci-Go": 4_031,
    "Invinci-Bro": 4_032,
    "Whip Oil": 4_033,
    "Axe BOGO Tag": 4_034,
    "Knife BOGO Tag": 4_035,
    "Caltrop BOGO Tag": 4_036,
    "Bomb BOGO Tag": 4_037,
    "Cleat BOGO Tag": 4_038,
    "Wings BOGO Tag": 4_039,
    "Axe Pocket": 4_040,
    "Axe Belt": 4_041,
    "Axe Bag": 4_042,
    "Axe Pack": 4_043,
    "Knife Pocket": 4_044,
    "Knife Belt": 4_045,
    "Knife Bag": 4_046,
    "Knife Pack": 4_047,
    "Caltrop Pocket": 4_048,
    "Caltrop Belt": 4_049,
    "Caltrop Bag": 4_050,
    "Caltrop Pack": 4_051,
    "Bomb Pocket": 4_052,
    "Bomb Belt": 4_053,
    "Bomb Bag": 4_054,
    "Bomb Pack": 4_055,
    "Cleat Pocket": 4_056,
    "Cleat Belt": 4_057,
    "Cleat Bag": 4_058,
    "Cleat Pack": 4_059,
    "Wings Pocket": 4_060,
    "Wings Belt": 4_061,
    "Wings Bag": 4_062,
    "Wings Pack": 4_063,
    "10kg Ton": 4_064,
    "Sumo Bubble": 4_065,
    "Barb Rage": 4_066,
    "Thief Band": 4_067,
    "Thief Glove": 4_068,
    "Thief Boots": 4_069,
    "Thief Cape": 4_070,
    "Spike Shirt": 4_071,
    "Counter Bangle": 4_072,
    "Soloist Mark": 4_073,
    "Padded Armor": 4_074,
    "Padded Vam-brace": 4_075,
    "Padded Helm": 4_076,
    "Padded Greaves": 4_077,
    "Pretty Ribbon": 4_078,
    "Space Helmet": 4_079,
    "Axe Whet-stone": 4_080,
    "Knife Whet-stone": 4_081,
    "Caltrop Whet-stone": 4_082,
    "Bomb Whet-stone": 4_083,
    "Cleat Whet-stone": 4_084,
    "Wing Whet-stone": 4_085,
    "Nerd Glasses": 4_086,
    "Quake Heels": 4_087,
    "Quake Toes": 4_088,
    "Custom Command": 4_089,
    "Custom Jump": 4_090,
    "Custom Attacks": 4_091,
    "3kg Ton": 4_092,
    "Padded Full-plate": 4_093,
    "Whip Sling": 4_094,
    "Sword Red Flag": 4_095,
    "Shield Red Flag": 4_096,
    "Sub Whet-stone": 4_097,
    "Health Flag": 4_098,
    "Health Happy": 4_099,
    "Health Elated": 4_100,
    "Health Advance": 4_101,
    "Thief Thin Gloves": 4_102,
    "Loot WhipAir Magnet": 4_103,
    "Apart-ment Heart": 4_104,
    "Critical Heart": 4_105,
    "House Heart": 4_106,
    "Loot Foe Claw": 4_107,
    "Loot FoeShot Claw": 4_108,
    "Loot WindSub Whpclaw": 4_109,
    "Thief Mittens": 4_110,
    "Sub Prime": 4_111,
    "Break Chain": 4_112,
    "Break Link": 4_113,
    "Break Reaction": 4_114,
    "Break-fast Wrap": 4_115,
    "Lunch Bento": 4_116,
    "TV Dinner Box": 4_117,
    "Dessert TO-GO": 4_118,
    "Copper Maker": 4_119,
    "Iron Maker": 4_120,
    "Tun'stn Maker": 4_121,
    "Steel Maker": 4_122,
    "Roll Maker": 4_123,
    "Taco Maker": 4_124,
    "Wrap Maker": 4_125,
    "Wedge Maker": 4_126,
    "Sub Red Flag": 4_127,
    "Sub Max Flag": 4_128,
    "Sword Max Flag": 4_129,
    "Bandaid Map": 4_130,
    "Gauze Map": 4_131,
    "Patch Map": 4_132,
    "Cast Map": 4_133,
    "Grip Red Flag": 4_134,
    "Grip Max Flag": 4_135,
    "Grip Whet-stone": 4_136,
    "Hero's Heart": 4_137,
    "Tri-hit Shell": 4_138,
    "One Hit Wonder": 4_139,
    "Pain Quake": 4_140,
    "Sword Quake": 4_141,
    "Sub Quake": 4_142,
    "Whip Grip Brand": 4_143,
    "Hazard Shield": 4_144,
    "Bump Shield": 4_145,
    "Shot Shield": 4_146,
    "All Shield": 4_147,
    "Hazard+ Bump Shield": 4_148,
    "Hazard+ Shot Shield": 4_149,
    "Bump+ Shot Shield": 4_150,
    "Hurt Sub Power": 4_151,
    "Rolling Claw": 4_152,
    "Anti- Magnet Claw": 4_153,
    "Axe Crude Oil": 4_154,
    "Knife Crude Oil": 4_155,
    "Caltrop Crude Oil": 4_156,
    "Bomb Crude Oil": 4_157,
    "Cleat Crude Oil": 4_158,
    "Wings Crude Oil": 4_159,
    "Whip Wave": 4_160,
    "Cracked Whip Wave": 4_161,
    "Thin Whip Wave": 4_162,
    "Course Whip Wave": 4_163,
    "Sub Chain Break": 4_164,
    "Cracked Sub Break": 4_165,
    "Thin Sub Break": 4_166,
    "Course Sub Break": 4_167,
    "Cracked Loot Magnet": 4_168,
    "Thin Loot Magnet": 4_169,
    "Course Loot Magnet": 4_170,
    "Double Jump": 4_171,
    "Restart Stage Bow": 4_172,
    "Elastic Belt": 4_173,
    "Perma- loss Hairpin": 4_174,
    "Amnesia Med": 4_175,
    "Iron Rings": 4_176,
    "Iron Glove": 4_177,
    "Expired BusPass": 4_178,
    "Fiber Pills": 4_179,
    "Sub Full Flag": 4_180,
    "Sub Thin Flag": 4_181,
    "Rigid Armor": 4_182,
    "Sub Refill": 4_183,
    "Sub Free-fill": 4_184,
    "Food Refill": 4_185,
    "Food Free-fill": 4_186,
    "Whip Durable A": 4_187,
    "Whip Durable B": 4_188,
    "Chest Breaker": 4_189,
    "Full Whip Sling": 4_190,
}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
DEFAULT_ITEM_CLASSIFICATIONS = {

    "Launch Bomb": ItemClassification.progression | ItemClassification.useful,
    "Backflip Caltrop": ItemClassification.progression | ItemClassification.useful,
    "Climbing Axe": ItemClassification.progression | ItemClassification.useful,
    "Dash Knife": ItemClassification.progression | ItemClassification.useful,
    "Jump Wing": ItemClassification.progression | ItemClassification.useful,
    "Pogo Cleats": ItemClassification.progression | ItemClassification.useful,

    "Goo": ItemClassification.filler,
    "Fiber": ItemClassification.filler,
    "Protein": ItemClassification.filler,
    "Rock": ItemClassification.filler,
    "Tarsus": ItemClassification.filler,
    "Wood": ItemClassification.filler,
    "Freshwater": ItemClassification.filler,
    "Herb": ItemClassification.filler,
    "Metal": ItemClassification.filler,
    "Oil": ItemClassification.filler,
    "Flour": ItemClassification.filler,
    "Yeast": ItemClassification.filler,
    "Feather": ItemClassification.filler,
    "Bone": ItemClassification.filler,
    "Shell": ItemClassification.filler,
    "Charcoal": ItemClassification.filler,
    "Mutagen": ItemClassification.filler,
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
    "Arcade Credit": ItemClassification.filler,

    "Empty Slot": ItemClassification.trap,

    "Easy Mode Ribbon": ItemClassification.trap,
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
    "Spirit Chalk": ItemClassification.useful,
    "Spirit Balm": ItemClassification.useful,
    "Spirit Spray": ItemClassification.useful,
    "Spirit Lotion": ItemClassification.useful,
    "Spirit Soap": ItemClassification.useful,
    "Spirit Shampoo": ItemClassification.useful,
    "Spirit Condi-tioner": ItemClassification.useful,
    "Spirit Body Wash": ItemClassification.useful,
    "Spirit Oin'mnt": ItemClassification.useful,
    "Spirit Lather": ItemClassification.useful,
    "Axe Oil": ItemClassification.useful,
    "Knife Oil": ItemClassification.useful,
    "Caltrop Oil": ItemClassification.filler,
    "Bomb Oil": ItemClassification.useful,
    "Cleat Oil": ItemClassification.filler,
    "Wings Oil": ItemClassification.useful,
    "LOOT_GRAB_WHIP": ItemClassification.filler,
    "Loot Sub Magnet": ItemClassification.filler,
    "Loot Magnet": ItemClassification.filler,
    "Loot Magnet Ex": ItemClassification.filler,
    "Invinci-Go": ItemClassification.filler,
    "Invinci-Bro": ItemClassification.filler,
    "Whip Oil": ItemClassification.progression | ItemClassification.useful,
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
    "Nerd Glasses": ItemClassification.filler,
    "Quake Heels": ItemClassification.filler,
    "Quake Toes": ItemClassification.filler,
    "Custom Command": ItemClassification.useful,
    "Custom Jump": ItemClassification.useful,
    "Custom Attacks": ItemClassification.useful,
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
    "Cast Map": ItemClassification.useful,
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
    "Double Jump": ItemClassification.progression | ItemClassification.useful,
    "Restart Stage Bow": ItemClassification.trap,
    "Elastic Belt": ItemClassification.trap,
    "Perma- loss Hairpin": ItemClassification.trap,
    "Amnesia Med": ItemClassification.trap,
    "Iron Rings": ItemClassification.trap,
    "Iron Glove": ItemClassification.trap,
    "Expired BusPass": ItemClassification.trap,
    "Fiber Pills": ItemClassification.trap,
    "Sub Full Flag": ItemClassification.filler,
    "Sub Thin Flag": ItemClassification.trap,
    "Rigid Armor": ItemClassification.filler,
    "Sub Refill": ItemClassification.progression | ItemClassification.useful,
    "Sub Free-fill": ItemClassification.progression | ItemClassification.useful,
    "Food Refill": ItemClassification.filler,
    "Food Free-fill": ItemClassification.filler,
    "Whip Durable A": ItemClassification.progression | ItemClassification.useful,
    "Whip Durable B": ItemClassification.progression | ItemClassification.useful,
    "Chest Breaker": ItemClassification.progression | ItemClassification.useful,
    "Full Whip Sling": ItemClassification.useful,
}

TRAP_ITEM_NAME_LIST = [
    "Spicy Pepper"
    "Viscous Tar"
    "Novaculite"
    "Vines"
    "Femur"
    "Shoe Buckle"
    "Cloud Sponge"
    "Tetrodotox"
    "Capsule"
    "Pinion"
    "Pumpkin"
    "Ladle"
    "Empty Slot"
    "Easy Mode Ribbon"
    "Barb Rage"
    "Pretty Ribbon"
    "Space Helmet"
    "Hero's Heart"
    "Tri-hit Shell"
    "One Hit Wonder"
    "Rolling Claw"
    "Anti- Magnet Claw"
    "Axe Crude Oil"
    "Knife Crude Oil"
    "Caltrop Crude Oil"
    "Bomb Crude Oil"
    "Cleat Crude Oil"
    "Wings Crude Oil"
    "Cracked Whip Wave"
    "Thin Whip Wave"
    "Course Whip Wave"
    "Cracked Sub Break"
    "Thin Sub Break"
    "Course Sub Break"
    "Cracked Loot Magnet"
    "Thin Loot Magnet"
    "Course Loot Magnet"
    "Restart Stage Bow"
    "Elastic Belt"
    "Perma- loss Hairpin"
    "Amnesia Med"
    "Iron Rings"
    "Iron Glove"
    "Expired BusPass"
    "Fiber Pills"
    "Sub Thin Flag"
]

FILLER_ITEM_NAME_LIST = [
    "Goo",
    "Fiber",
    "Protein",
    "Rock",
    "Tarsus",
    "Wood",
    "Freshwater",
    "Herb",
    "Metal",
    "Oil",
    "Flour",
    "Yeast",
    "Feather",
    "Bone",
    "Shell",
    "Charcoal",
    "Mutagen",
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
    "Arcade Credit",
    "Caltrop Oil",
    "Cleat Oil",
    "LOOT_GRAB_WHIP",
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
    "Nerd Glasses",
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
    "Whip Durable B",
    "Sub Refill", 
]

PROGRESSION_ITEM_NAME_LIST = [
    "Launch Bomb",
    "Backflip Caltrop",
    "Climbing Axe",
    "Dash Knife",
    "Jump Wing",
    "Pogo Cleats",
    "Whip Oil",
    "Double Jump",
    "Sub Refill",
    "Sub Free-fill",
    "Whip Durable A",
    "Whip Durable B",
    "Chest Breaker",
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
    fillerIndex = world.random.randint(0, maxFillerIndex)
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
    for itemName in PROGRESSION_ITEM_NAME_LIST:
        itempool += world.create_item(itemName),

    # TODO handle options


    # Some items may only exist if the player enables certain options.
    # In our case, If the hammer option is enabled, the sixth item is the Hammer.
    # Otherwise, we add a filler Confetti Cannon.
    if world.options.subweapon_spawn:
        # Once again, it is important to stress that even though the Hammer doesn't always exist,
        # it must be present in the worlds item_name_to_id.
        # Whether it is actually in the itempool is determined purely by whether we create and add the item here.
        itempool.append(world.create_item("Hammer"))

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
    if world.options.hub_sub_fill:
        # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
        starting_confetti_cannon = world.create_item("Confetti Cannon")
        world.push_precollected(starting_confetti_cannon)
