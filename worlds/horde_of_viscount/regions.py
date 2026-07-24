from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, EntranceType, Region

if TYPE_CHECKING:
    from .world import HoVWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: HoVWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


class HoVRegionSet:
	world_map_room: Region
	world_map_north_west: Region
	world_map_east: Region
	world_map_south_central: Region
	world_map_west: Region
	world_map_southwest: Region
	world_map_south: Region
	abandon_town: Region
	cliffside_climb: Region
	castle_town: Region
	kingdom_castle: Region
	tepid_volcano: Region
	viscount_manor: Region
	viscount_lab: Region
	map_rando_rogue_world: Region
	list: list[Region]

def get_region_set(world: HoVWorld) -> HoVRegionSet:
	hoVRegionSet = HoVRegionSet()
	hoVRegionSet.world_map_room = world.get_region("WorldMapRoom")
	hoVRegionSet.world_map_north_west = world.get_region("World Map NorthWest")
	hoVRegionSet.world_map_east = world.get_region("World Map East")
	hoVRegionSet.world_map_south_central = world.get_region("World Map South Central")
	hoVRegionSet.world_map_west = world.get_region("World Map West")
	hoVRegionSet.world_map_southwest = world.get_region("World Map South West")
	hoVRegionSet.world_map_south = world.get_region("World Map South")
	hoVRegionSet.abandon_town = world.get_region("Abandon Town")
	hoVRegionSet.cliffside_climb = world.get_region("Cliffside Climb")
	hoVRegionSet.castle_town = world.get_region("Castle Town")
	hoVRegionSet.kingdom_castle = world.get_region("Kingdom Castle")
	hoVRegionSet.tepid_volcano = world.get_region("Tepid Volcano")
	hoVRegionSet.viscount_manor = world.get_region("Viscount Manor")
	hoVRegionSet.viscount_lab = world.get_region("Viscount Lab")
	hoVRegionSet.map_rando_rogue_world = world.get_region("Rogue Hub Room")
	hoVRegionSet.list = [hoVRegionSet.world_map_room, hoVRegionSet.world_map_north_west, hoVRegionSet.world_map_east, hoVRegionSet.world_map_south_central, hoVRegionSet.world_map_west, hoVRegionSet.world_map_southwest, hoVRegionSet.world_map_south, hoVRegionSet.abandon_town, hoVRegionSet.cliffside_climb, hoVRegionSet.castle_town, hoVRegionSet.kingdom_castle, hoVRegionSet.tepid_volcano, hoVRegionSet.viscount_manor, hoVRegionSet.viscount_lab, hoVRegionSet.map_rando_rogue_world]
	return hoVRegionSet

def create_all_regions(world: HoVWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
	hoVRegionSet = HoVRegionSet()
	hoVRegionSet.world_map_room = Region("WorldMapRoom", world.player, world.multiworld)
	hoVRegionSet.world_map_north_west = Region("World Map NorthWest", world.player, world.multiworld)
	hoVRegionSet.abandon_town = Region("Abandon Town", world.player, world.multiworld)
	hoVRegionSet.world_map_east = Region("World Map East", world.player, world.multiworld)
	hoVRegionSet.cliffside_climb = Region("Cliffside Climb", world.player, world.multiworld)
	hoVRegionSet.world_map_south_central = Region("World Map South Central", world.player, world.multiworld)
	hoVRegionSet.castle_town = Region("Castle Town", world.player, world.multiworld)
	hoVRegionSet.world_map_west = Region("World Map West", world.player, world.multiworld)
	hoVRegionSet.kingdom_castle = Region("Kingdom Castle", world.player, world.multiworld)
	hoVRegionSet.world_map_southwest = Region("World Map South West", world.player, world.multiworld)
	hoVRegionSet.tepid_volcano = Region("Tepid Volcano", world.player, world.multiworld)
	hoVRegionSet.world_map_south = Region("World Map South", world.player, world.multiworld)
	hoVRegionSet.viscount_manor = Region("Viscount Manor", world.player, world.multiworld)
	hoVRegionSet.viscount_lab = Region("Viscount Lab", world.player, world.multiworld)
	hoVRegionSet.map_rando_rogue_world = Region("Rogue Hub Room", world.player, world.multiworld)
     
    # Let's put all these regions in a list.
	hoVRegionSet.list = [hoVRegionSet.world_map_room, hoVRegionSet.world_map_north_west, hoVRegionSet.abandon_town, 
                      hoVRegionSet.world_map_east, hoVRegionSet.cliffside_climb, 
                      hoVRegionSet.world_map_south_central, hoVRegionSet.castle_town,
                      hoVRegionSet.world_map_west, hoVRegionSet.kingdom_castle, 
						hoVRegionSet.world_map_southwest, hoVRegionSet.tepid_volcano, 
						hoVRegionSet.world_map_south, hoVRegionSet.viscount_manor, hoVRegionSet.viscount_lab, 
						hoVRegionSet.map_rando_rogue_world]

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
	world.multiworld.regions += hoVRegionSet.list


def connect_regions(world: HoVWorld) -> None:
    # The list is sequential in the order that the player would naturally progress through the game, so we can just connect each region to the next one in the list.
    hoVRegionSet = get_region_set(world)
    for i in range(len(hoVRegionSet.list) - 1):
        region = hoVRegionSet.list[i]
        nextRegion = hoVRegionSet.list[i + 1]

		# An even easier way is to use the region.connect helper.
        region.connect(nextRegion, 
			region.name + " to " + nextRegion.name)

    # Fill in the misc connections that aren't just "next region in the list".s
    hoVRegionSet.world_map_north_west.connect(
          hoVRegionSet.world_map_west, 
              hoVRegionSet.world_map_north_west.name + " to " + hoVRegionSet.world_map_west.name, 
						lambda state: state.has("Feather", world.player))
    hoVRegionSet.world_map_north_west.connect(
          hoVRegionSet.world_map_east, 
              hoVRegionSet.world_map_north_west.name + " to " + hoVRegionSet.world_map_east.name + " (Metal)", 
						lambda state: state.has("Metal", world.player))
    hoVRegionSet.world_map_north_west.connect(
          hoVRegionSet.world_map_east, 
              hoVRegionSet.world_map_north_west.name + " to " + hoVRegionSet.world_map_east.name + " (Bone)", 
						lambda state: state.has("Bone", world.player))
    hoVRegionSet.world_map_south_central.connect(
          hoVRegionSet.world_map_south, 
              hoVRegionSet.world_map_south_central.name + " to " + hoVRegionSet.world_map_south.name, 
						lambda state: state.has("Mutagen", world.player))
    
