from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import HoVWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
	"Abandon Town - Center Proletariat Chest 1": 73_01,
	"Abandon Town - Center Proletariat Chest 2": 73_02,
	"Abandon Town - Center Proletariat Chest 3": 73_03,
	"Abandon Town - Center Bourgeoisie Chest 1": 76_01,
	"Abandon Town - Center Bourgeoisie Chest 2": 76_02,
	"Abandon Town - Center Bourgeoisie Chest 3": 76_03,
	"Abandon Town - East Proletariat Chest 1": 74_01,
	"Abandon Town - East Proletariat Chest 2": 74_02,
	"Abandon Town - East Proletariat Chest 3": 74_03,
	"Abandon Town - East Bourgeoisie Chest 1": 77_01,
	"Abandon Town - East Bourgeoisie Chest 2": 77_02,
	"Abandon Town - East Bourgeoisie Chest 3": 77_03,
	"Abandon Town - East Sky Chest 1": 80_01,
	"Abandon Town - East Sky Chest 2": 80_02,
	"Abandon Town - East Sky Chest 3": 80_03,
	"Abandon Town - Abandoned Town Chest 1": 71_01,
	"Abandon Town - Abandoned Town Chest 2": 71_02,
	"Abandon Town - Abandoned Town Chest 3": 71_03,
	"Abandon Town - East Entrance Chest 1": 79_01,
	"Abandon Town - East Entrance Chest 2": 79_02,
	"Abandon Town - East Entrance Chest 3": 79_03,
	"Abandon Town - Hidden Chest 1": 84_01,
	"Abandon Town - Hidden Chest 2": 84_02,
	"Abandon Town - Hidden Chest 3": 84_03,
	"Abandon Town - Cold Nest Chest 1": 86_01,
	"Abandon Town - Cold Nest Chest 2": 86_02,
	"Abandon Town - Cold Nest Chest 3": 86_03,
	"Abandon Town - Cold Nest Chest 4": 86_04,
	"Abandon Town - Cold Nest Chest 5": 86_05,
	"Abandon Town - Cold Nest Chest 6": 86_06,
	"Abandon Town - Cold Nest Chest 7": 86_07,
	"Abandon Town - Cold Nest Chest 8": 86_08,
	"Abandon Town - Cold Nest Chest 9": 86_09,
	"Abandon Town - Cold Nest Chest 10": 86_10,
	"Abandon Town - Cold Nest Chest 11": 86_11,
	"Abandon Town - Cold Nest Chest 12": 86_12,
	"Abandon Town - Aqueduct Chest 1": 85_01,
	"Abandon Town - Aqueduct Chest 2": 85_02,
	"Abandon Town - Aqueduct Chest 3": 85_03,
	"Abandon Town - Cold Tunnel Chest 1": 82_01,
	"Abandon Town - Cold Tunnel Chest 2": 82_02,
	"Abandon Town - Cold Tunnel Chest 3": 82_03,
	"Abandon Town - Drain Chest 1": 81_01,
	"Abandon Town - Drain Chest 2": 81_02,
	"Abandon Town - Drain Chest 3": 81_03,
	"Abandon Town - West Proletariat Chest 1": 72_01,
	"Abandon Town - West Proletariat Chest 2": 72_02,
	"Abandon Town - West Proletariat Chest 3": 72_03,
	"Abandon Town - West Bourgeoisie Chest 1": 75_01,
	"Abandon Town - West Bourgeoisie Chest 2": 75_02,
	"Abandon Town - West Bourgeoisie Chest 3": 75_03,
	"Abandon Town - West Sky Chest 1": 78_01,
	"Abandon Town - West Sky Chest 2": 78_02,
	"Abandon Town - West Sky Chest 3": 78_03,
    "Axe Challenge 3 Chest 1": 208_01,
	"Bomb Challenge 3 Chest 1": 214_01,
	"GrimeBone Fort Chest 1": 18_01,
	"GrimeBone Fort Chest 2": 18_02,
	"GrimeBone Fort Chest 3": 18_03,
	"Caltrop Challenge 3 Chest 1": 205_01,
	"Kingdom Castle - Battlements Chest 1": 37_01,
	"Kingdom Castle - Kingdom Castle Chest 1": 29_01,
	"Kingdom Castle - Kingdom Castle Chest 2": 29_02,
	"Kingdom Castle - Kingdom Castle Chest 3": 29_03,
    "Kingdom Castle - Columns Chest 1": 88_01,
	"Kingdom Castle - Columns Chest 2": 88_02,
	"Kingdom Castle - Columns Chest 3": 88_03,
	"Kingdom Castle - Overhang Chest 1": 89_01,
	"Kingdom Castle - Overhang Chest 2": 89_02,
	"Kingdom Castle - Great Hall Chest 1": 33_01,
	"Kingdom Castle - Barbican Chest 1": 30_01,
	"Kingdom Castle - Hidden Hidden Storage Chest 1": 87_01,
	"Kingdom Castle - Hidden Hidden Storage Chest 2": 87_02,
	"Kingdom Castle - Hidden Hidden Storage Chest 3": 87_03,
	"Kingdom Castle - Hidden Storage Chest 1": 46_01,
	"Kingdom Castle - Hidden Storage Chest 2": 46_02,
	"Kingdom Castle - Hidden Storage Chest 3": 46_03,
	"Kingdom Castle - Hidden Storage Chest 4": 46_04,
	"Kingdom Castle - Hidden Storage Chest 5": 46_05,
	"Kingdom Castle - Hidden Storage Chest 6": 46_06,
	"Kingdom Castle - Kitchen Chest 1": 44_01,
	"Kingdom Castle - Kitchen Chest 2": 44_02,
	"Kingdom Castle - Kitchen Chest 3": 44_03,
	"Kingdom Castle - Machicolations Chest 1": 36_01,
	"Kingdom Castle - Portcullis Room Chest 1": 32_01,
	"Kingdom Castle - Portcullis Room Chest 2": 32_02,
	"Kingdom Castle - Portcullis Room Chest 3": 32_03,
	"Kingdom Castle - Ramparts Chest 1": 35_01,
	"Kingdom Castle - Rear Tower Chest 1": 47_01,
	"Kingdom Castle - Rear Tower Chest 2": 47_02,
	"Kingdom Castle - Castle Break Room Chest 1": 45_01,
	"Kingdom Castle - Lone Tower Chest 1": 91_01,
	"Kingdom Castle - Lone Tower Chest 2": 91_02,
	"Kingdom Castle - Lone Tower Chest 3": 91_03,
	"Kingdom Castle - Lone Tower Chest 4": 91_04,
	"Kingdom Castle - Lone Tower Chest 5": 91_05,
	"Kingdom Castle - Lone Tower Chest 6": 91_06,
	"Kingdom Castle - Top Ramparts Chest 1": 90_01,
	"Kingdom Castle - Tower Chest 1": 34_01,
	"Kingdom Castle - Tower Chest 2": 34_02,
	"Kingdom Castle - Tower Chest 3": 34_03,
	"Cleat Challenge 3 Chest 1": 211_01,
	"Cliffside Climb - Elevator Chest 1": 132_01,
	"Cliffside Climb - Cliffside Climb Chest 1": 115_01,
	"Cliffside Climb - Hidden Chest 1": 133_01,
	"Cliffside Climb - Hidden Chest 2": 133_02,
	"Cliffside Climb - Hidden Chest 3": 133_03,
	"Cliffside Climb - Stealth Underneath Chest 1": 137_01,
	"Cliffside Climb - Shining Exit Chest 1": 140_01,
	"Cliffside Climb - Shining Exit Chest 2": 140_02,
	"Cliffside Climb - Shining Exit Chest 3": 140_03,
	"Cliffside Climb - Cliff Exit Chest 1": 141_01,
	"Cliffside Climb - Cliff Exit Chest 2": 141_02,
	"Cliffside Climb - Cliff Exit Chest 3": 141_03,
	"Cliffside Climb - Cliffside Campsite Chest 1": 131_01,
	"Cliffside Climb - Cliffside Entrance Chest 1": 117_01,
	"Cliffside Climb - Scalable Cliff Chest 1": 116_01,
	"Cliffside Climb - Curving Exit Chest 1": 122_01,
	"Cliffside Climb - Precipice Edge Chest 1": 118_01,
	"Cliffside Climb - Small Underpass Chest 1": 127_01,
	"Cliffside Climb - Spiked Underpass Chest 1": 128_01,
	"Cliffside Climb - Wide Respite Chest 1": 119_01,
	"Cliffside Climb - Topside Entrance Chest 1": 120_01,
	"Cliffside Climb - Clifftop Chest 1": 121_01,
	"Cliffside Climb - Entrance Underpass Chest 1": 126_01,
	"Cliffside Climb - Underpass Chest 1": 125_01,
	"Credits Peak Chest 1": 227_01,
	"Credits Peak Chest 2": 227_02,
	"Crimson Cove Chest 1": 41_01,
	"Crimson Cove 2 Chest 1": 42_01,
	"Crimson Cove 3 Chest 1": 43_01,
    "Deadland Road Chest 1": 6_01,
	"Deadland Road 2 Chest 1": 7_01,
	"Deadland Road 3 Chest 1": 8_01,
	"Dusty Beach Chest 1": 20_01,
	"Dusty Beach 2 Chest 1": 21_01,
	"Dusty Beach 3 Chest 1": 22_01,
	"Iron Rock Mt Chest 1": 15_01,
	"Iron Rock Mt 2 Chest 1": 16_01,
	"Iron Rock Mt 3 Chest 1": 17_01,
	"Knife Challenge 3 Chest 1": 201_01,
	"Credits Overlook Chest 1": 198_01,
	"Larval Forest Chest 1": 12_01,
	"Larval Forest 2 Chest 1": 13_01,
    "Larval Forest 3 Chest 1": 14_01,
	"Larval Forest 3 Chest 2": 14_02,
	"Larval Forest 3 Chest 3": 14_03,
	"Viscount Manor - Bottom Path to Attic Chest 1": 193_01,
	"Viscount Manor - Around Middle Chest 1": 194_01,
	"Viscount Manor - Around Middle Chest 2": 194_02,
	"Viscount Manor - Around Middle Chest 3": 194_03,
	"Viscount Manor - Path to Attic Chest 1": 163_01,
	"Viscount Manor - Attic Entrance Chest 1": 164_01,
	"Viscount Manor - Left Attic Chest 1": 165_01,
	"Viscount Manor - Middle Attic Chest 1": 166_01,
	"Viscount Manor - Right Attic Chest 1": 167_01,
	"Viscount Manor - Attic Exit Chest 1": 168_01,
	"Viscount Manor - Top Lab Entrance Chest 1": 155_01,
	"Viscount Manor - Right Barbed Hallway Chest 1": 183_01,
	"Viscount Manor - Right Barbed Hallway Chest 2": 183_02,
	"Viscount Manor - Left Barbed Hallway Chest 1": 181_01,
	"Viscount Manor - Barbed Hidden Room Chest 1": 160_01,
	"Viscount Manor - Barbed Hidden Room Chest 2": 160_02,
	"Viscount Manor - Barbed Hidden Room Chest 3": 160_03,
	"Viscount Manor - Manor Barricade Chest 1": 161_01,
	"Viscount Manor - Center Barricade Chest 1": 176_01,
	"Viscount Manor - Right Barricade Chest 1": 173_01,
	"Viscount Manor - Manor Containment Chest 1": 156_01,
	"Viscount Manor - Containment Chest 1": 185_01,
	"Viscount Manor - Lab Bottom Cache Chest 1": 179_01,
	"Viscount Manor - Lab Bottom Cache Chest 2": 179_02,
	"Viscount Manor - Lab Bottom Cache Chest 3": 179_03,
	"Viscount Manor - Center Barricade Stud Path Chest 1": 149_01,
	"Viscount Manor - Testing Room Entrance Chest 1": 157_01,
	"Viscount Manor - Testing Room Entrance Chest 2": 157_02,
	"Viscount Manor - Testing Room Entrance Chest 3": 157_03,
	"Viscount Manor - Manor Center Underbelly Chest 1": 170_01,
	"Viscount Manor - Manor Center Underbelly Chest 2": 170_02,
	"Viscount Manor - Manor Center Underbelly Chest 3": 170_03,
	"Viscount Manor - Manor Right Underbelly Chest 1": 184_01,
	"Viscount Manor - Manor Right Underbelly Chest 2": 184_02,
	"Viscount Manor - Manor Right Underbelly Chest 3": 184_03,
	"Viscount Manor - Manor Left Underbelly Chest 1": 169_01,
	"Viscount Manor - Manor Cache Chest 1": 152_01,
	"Viscount Manor - Manor Cache Chest 2": 152_02,
	"Viscount Manor - Crimson Cove Entrance Chest 1": 162_01,
	"Viscount Manor - Left Barricade Stud Path Chest 1": 180_01,
	"Viscount Manor - Lower Hallway to Lab Chest 1": 182_01,
	"Viscount Manor - Hallway to Lab Chest 1": 192_01,
	"Viscount Manor - Hallway to Lab Chest 2": 192_02,
	"Viscount Manor - Hallway to Lab Chest 3": 192_03,
	"Viscount Manor - Path Hidden Chest 1": 175_01,
	"Viscount Manor - Path Hidden Chest 2": 175_02,
	"Viscount Manor - Path Hidden Chest 3": 175_03,
	"Viscount Manor - Right Barricade Stud Path Chest 1": 148_01,
	"Viscount Manor - Right Barricade Stud Path Chest 2": 148_02,
	"Viscount Manor - Lab Top Cache Chest 1": 150_01,
	"Viscount Manor - Lab Top Cache Chest 2": 150_02,
	"Viscount Manor - Lab Top Cache Chest 3": 150_03,
	"Mushroom Cloud Chest 1": 23_01,
	"Mushroom Cloud 2 Chest 1": 24_01,
	"Mushroom Cloud 3 Chest 1": 25_01,
	"Quenchy Desert Chest 1": 26_01,
	"Quenchy Desert 2 Chest 1": 27_01,
	"Quenchy Desert 2 Chest 2": 27_02,
	"Quenchy Desert 3 Chest 1": 28_01,
	"Quenchy Desert 3 Chest 2": 28_02,
	"Stormcloud Crater Chest 1": 142_01,
	"Stormcloud Crater 2 Chest 1": 143_01,
	"Stormcloud Crater 3 Chest 1": 144_01,
	"Town Gate Chest 1": 40_01,
	"Town Gate Chest 2": 40_02,
	"Town Gate Chest 3": 40_03,
	"Toxic Jungle Chest 1": 9_01,
	"Toxic Jungle 2 Chest 1": 10_01,
	"Toxic Jungle 3 Chest 1": 11_01,
	"Viscount Manor Chest 1": 68_01,
	"Viscount Manor Chest 2": 68_02,
	"Tepid Volcano - Volcano Campsite Chest 1": 57_01,
	"Tepid Volcano - Volcano Campsite Chest 2": 57_02,
	"Tepid Volcano - Upper Entrance Chest 1": 102_01,
	"Tepid Volcano - Crater Exit Chest 1": 104_01,
	"Tepid Volcano - Crater Exit Chest 2": 104_02,
	"Tepid Volcano - Crater Chest 1": 100_01,
	"Tepid Volcano - Crater Under Chest 1": 105_01,
	"Tepid Volcano - Crater Under Chest 2": 105_02,
	"Tepid Volcano - Crater Under Chest 3": 105_03,
	"Tepid Volcano - Lava Drain Chest 1": 103_01,
	"Tepid Volcano - Lava Drain Chest 2": 103_02,
	"Tepid Volcano - Eastern Foot Chest 1": 63_01,
	"Tepid Volcano - Eastern Foot Chest 2": 63_02,
	"Tepid Volcano - Fluffy Clouds 3 Chest 1": 65_01,
	"Tepid Volcano - Fluffy Clouds 3 Chest 2": 65_02,
	"Tepid Volcano - Entryway Chest 1": 52_01,
	"Tepid Volcano - Entryway Chest 2": 52_02,
	"Tepid Volcano - Volcano Foot Camp Chest 1": 66_01,
	"Tepid Volcano - Volcano Foot Camp Chest 2": 66_02,
	"Tepid Volcano - Volcano Foot Camp Chest 3": 66_03,
	"Tepid Volcano - Volcano Foot Camp Chest 4": 66_04,
	"Tepid Volcano - Tepid Volcano Chest 1": 49_01,
	"Tepid Volcano - Hopping Left Chest 1": 106_01,
	"Tepid Volcano - Hopping Center-Left Chest 1": 107_01,
	"Tepid Volcano - Hopping Center-Right Chest 1": 108_01,
	"Tepid Volcano - Hopping Right Chest 1": 109_01,
	"Tepid Volcano - Lava Fall Bottom Chest 1": 94_01,
	"Tepid Volcano - Lava Fall Bottom Chest 2": 94_02,
	"Tepid Volcano - Lava Fall Bottom Chest 3": 94_03,
	"Tepid Volcano - Lava Fall Center Chest 1": 93_01,
	"Tepid Volcano - Left Corner Chest 1": 95_01,
	"Tepid Volcano - West Topside Chest 1": 101_01,
	"Tepid Volcano - West Topside Chest 2": 101_02,
	"Tepid Volcano - Scaling Wall Chest 1": 96_01,
	"Tepid Volcano - Lava Rain Bottom Chest 1": 110_01,
	"Tepid Volcano - Lava Rain Center Chest 1": 111_01,
	"Tepid Volcano - Bottom Cave Chest 1": 61_01,
	"Tepid Volcano - Bottom Cave Chest 2": 61_02,
	"Tepid Volcano - Side Cavern Chest 1": 60_01,
	"Tepid Volcano - Side Vent Chest 1": 55_01,
	"Tepid Volcano - Side Vent Chest 2": 55_02,
	"Tepid Volcano - Side Vent Chest 3": 55_03,
	"Tepid Volcano - Throat Chest 1": 54_01,
	"Tepid Volcano - Throat Chest 2": 54_02,
	"Tepid Volcano - Throat Chest 3": 54_03,
	"Tepid Volcano - Top Hole Chest 1": 99_01,
	"Tepid Volcano - Top Open Chest 1": 98_01,
	"Tepid Volcano - East Topside Chest 1": 59_01,
	"Tepid Volcano - Top Entrance Chest 1": 97_01,
	"Tepid Volcano - Vein Chest 1": 53_01,
	"Tepid Volcano - Vein Chest 2": 53_02,
	"Tepid Volcano - Vent Chest 1": 56_01,
	"Wing Challenge 3 Chest 1": 217_01,
}

location_name_to_region_name = {
    # TODO - 
    
	"Wing Challenge 3 Chest 1": "Castle Town",
}

# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class HoVLocation(Location):
    game = "Horde of Viscount"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: HoVWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: HoVWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    world_map_north_west = world.get_region("World Map NorthWest")
    world_map_east = world.get_region("World Map East")
    world_map_south_central = world.get_region("World Map South Central")
    world_map_west = world.get_region("World Map West")
    world_map_southwest = world.get_region("World Map South West")
    world_map_south = world.get_region("World Map South")
    abandon_town = world.get_region("Abandon Town")
    cliffside_climb = world.get_region("Cliffside Climb")
    castle_town = world.get_region("Castle Town")
    kingdom_castle = world.get_region("Kingdom Castle")
    tepid_volcano = world.get_region("Tepid Volcano")
    viscount_manor = world.get_region("Viscount Manor")
    viscount_lab = world.get_region("Viscount Lab")

    # TODO - Add the location_name to region_name map

    # You can then add them to the region.
    for location_name in world.location_name_to_id.keys:
        region_name = world.location_name_to_region_name[location_name]
        world.get_region(region_name).locations.append(HoVLocation(
            world.player, location_name, world.location_name_to_id[location_name], world_map_north_west
        ))

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    bottom_right_room_locations = get_location_names_with_ids(
        ["Bottom Right Room Left Chest", "Bottom Right Room Right Chest"]
    )
    world_map_west.add_locations(bottom_right_room_locations, HoVLocation)

    top_left_room_locations = get_location_names_with_ids(["Top Left Room Chest"])
    world_map_east.add_locations(top_left_room_locations, HoVLocation)

    right_room_locations = get_location_names_with_ids(["Right Room Enemy Drop"])
    world_map_southwest.add_locations(right_room_locations, HoVLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    if world.options.subweapon_spawn:
        top_middle_room = world.get_region("Top Middle Room")
        top_middle_room.add_locations(top_middle_room_locations, HoVLocation)
    else:
        world_map_north_west.add_locations(top_middle_room_locations, HoVLocation)

    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    if world.options.heal_hub:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        world_map_north_west.add_locations(bottom_left_extra_chest, HoVLocation)


def create_events(world: HoVWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = HoVLocation(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.HoVItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "All Chests Opened", "Victory", location_type=HoVLocation, item_type=items.HoVItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
