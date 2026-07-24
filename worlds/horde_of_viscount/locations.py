from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location
from worlds.horde_of_viscount.items import HoVItem
from worlds.horde_of_viscount.regions import get_region_set


if TYPE_CHECKING:
    from .world import HoVWorld


LOCATION_NAME_TO_ROOM_ID = {
    "Abandon Town - Center Proletariat Chest 1": 73,
	"Abandon Town - Center Proletariat Chest 2": 73,
	"Abandon Town - Center Proletariat Chest 3": 73,


	"Abandon Town - Center Bourgeoisie Chest 1": 76,
	"Abandon Town - Center Bourgeoisie Chest 2": 76,
	"Abandon Town - Center Bourgeoisie Chest 3": 76,


	"Abandon Town - East Proletariat Chest 1": 74,
	"Abandon Town - East Proletariat Chest 2": 74,
	"Abandon Town - East Proletariat Chest 3": 74,


	"Abandon Town - East Bourgeoisie Chest 1": 77,
	"Abandon Town - East Bourgeoisie Chest 2": 77,
	"Abandon Town - East Bourgeoisie Chest 3": 77,


	"Abandon Town - East Sky Chest 1": 80,
	"Abandon Town - East Sky Chest 2": 80,
	"Abandon Town - East Sky Chest 3": 80,


	"Abandon Town - Abandoned Town Chest 1": 71,
	"Abandon Town - Abandoned Town Chest 2": 71,
	"Abandon Town - Abandoned Town Chest 3": 71,


	"Abandon Town - East Entrance Chest 1": 79,
	"Abandon Town - East Entrance Chest 2": 79,
	"Abandon Town - East Entrance Chest 3": 79,


	"Abandon Town - Hidden Chest 1": 84,
	"Abandon Town - Hidden Chest 2": 84,
	"Abandon Town - Hidden Chest 3": 84,


	"Abandon Town - Cold Nest Chest 1": 86,
	"Abandon Town - Cold Nest Chest 2": 86,
	"Abandon Town - Cold Nest Chest 3": 86,
	"Abandon Town - Cold Nest Chest 4": 86,
	"Abandon Town - Cold Nest Chest 5": 86,
	"Abandon Town - Cold Nest Chest 6": 86,
	"Abandon Town - Cold Nest Chest 7": 86,
	"Abandon Town - Cold Nest Chest 8": 86,
	"Abandon Town - Cold Nest Chest 9": 86,
	"Abandon Town - Cold Nest Chest 10": 86,
	"Abandon Town - Cold Nest Chest 11": 86,
	"Abandon Town - Cold Nest Chest 12": 86,


	"Abandon Town - Aqueduct Chest 1": 85,
	"Abandon Town - Aqueduct Chest 2": 85,
	"Abandon Town - Aqueduct Chest 3": 85,


	"Abandon Town - Cold Tunnel Chest 1": 82,
	"Abandon Town - Cold Tunnel Chest 2": 82,
	"Abandon Town - Cold Tunnel Chest 3": 82,


	"Abandon Town - Drain Chest 1": 81,
	"Abandon Town - Drain Chest 2": 81,
	"Abandon Town - Drain Chest 3": 81,


	"Abandon Town - West Proletariat Chest 1": 72,
	"Abandon Town - West Proletariat Chest 2": 72,
	"Abandon Town - West Proletariat Chest 3": 72,


	"Abandon Town - West Bourgeoisie Chest 1": 75,
	"Abandon Town - West Bourgeoisie Chest 2": 75,
	"Abandon Town - West Bourgeoisie Chest 3": 75,


	"Abandon Town - West Sky Chest 1": 78,
	"Abandon Town - West Sky Chest 2": 78,
	"Abandon Town - West Sky Chest 3": 78,



	"Axe Challenge 3 Chest 1": 208,


	"Bomb Challenge 3 Chest 1": 214,


	"GrimeBone Fort Chest 1": 18,
	"GrimeBone Fort Chest 2": 18,
	"GrimeBone Fort Chest 3": 18,


	"Caltrop Challenge 3 Chest 1": 205,


	"Kingdom Castle - Battlements Chest 1": 37,


	"Kingdom Castle - Kingdom Castle Chest 1": 29,
	"Kingdom Castle - Kingdom Castle Chest 2": 29,
	"Kingdom Castle - Kingdom Castle Chest 3": 29,



	"Kingdom Castle - Columns Chest 1": 88,
	"Kingdom Castle - Columns Chest 2": 88,
	"Kingdom Castle - Columns Chest 3": 88,


	"Kingdom Castle - Overhang Chest 1": 89,
	"Kingdom Castle - Overhang Chest 2": 89,


	"Kingdom Castle - Great Hall Chest 1": 33,


	"Kingdom Castle - Barbican Chest 1": 30,


	"Kingdom Castle - Hidden Hidden Storage Chest 1": 87,
	"Kingdom Castle - Hidden Hidden Storage Chest 2": 87,
	"Kingdom Castle - Hidden Hidden Storage Chest 3": 87,


	"Kingdom Castle - Hidden Storage Chest 1": 46,
	"Kingdom Castle - Hidden Storage Chest 2": 46,
	"Kingdom Castle - Hidden Storage Chest 3": 46,
	"Kingdom Castle - Hidden Storage Chest 4": 46,
	"Kingdom Castle - Hidden Storage Chest 5": 46,
	"Kingdom Castle - Hidden Storage Chest 6": 46,


	"Kingdom Castle - Kitchen Chest 1": 44,
	"Kingdom Castle - Kitchen Chest 2": 44,
	"Kingdom Castle - Kitchen Chest 3": 44,


	"Kingdom Castle - Machicolations Chest 1": 36,


	"Kingdom Castle - Portcullis Room Chest 1": 32,
	"Kingdom Castle - Portcullis Room Chest 2": 32,
	"Kingdom Castle - Portcullis Room Chest 3": 32,


	"Kingdom Castle - Ramparts Chest 1": 35,


	"Kingdom Castle - Rear Tower Chest 1": 47,
	"Kingdom Castle - Rear Tower Chest 2": 47,


	"Kingdom Castle - Castle Break Room Chest 1": 45,


	"Kingdom Castle - Lone Tower Chest 1": 91,
	"Kingdom Castle - Lone Tower Chest 2": 91,
	"Kingdom Castle - Lone Tower Chest 3": 91,
	"Kingdom Castle - Lone Tower Chest 4": 91,
	"Kingdom Castle - Lone Tower Chest 5": 91,
	"Kingdom Castle - Lone Tower Chest 6": 91,


	"Kingdom Castle - Top Ramparts Chest 1": 90,


	"Kingdom Castle - Tower Chest 1": 34,
	"Kingdom Castle - Tower Chest 2": 34,
	"Kingdom Castle - Tower Chest 3": 34,


	"Cleat Challenge 3 Chest 1": 211,


	"Cliffside Climb - Elevator Chest 1": 132,


	"Cliffside Climb - Cliffside Climb Chest 1": 115,


	"Cliffside Climb - Hidden Chest 1": 133,
	"Cliffside Climb - Hidden Chest 2": 133,
	"Cliffside Climb - Hidden Chest 3": 133,


	"Cliffside Climb - Stealth Underneath Chest 1": 137,


	"Cliffside Climb - Shining Exit Chest 1": 140,
	"Cliffside Climb - Shining Exit Chest 2": 140,
	"Cliffside Climb - Shining Exit Chest 3": 140,


	"Cliffside Climb - Cliff Exit Chest 1": 141,
	"Cliffside Climb - Cliff Exit Chest 2": 141,
	"Cliffside Climb - Cliff Exit Chest 3": 141,


	"Cliffside Climb - Cliffside Campsite Chest 1": 131,


	"Cliffside Climb - Cliffside Entrance Chest 1": 117,


	"Cliffside Climb - Scalable Cliff Chest 1": 116,


	"Cliffside Climb - Curving Exit Chest 1": 122,


	"Cliffside Climb - Precipice Edge Chest 1": 118,


	"Cliffside Climb - Small Underpass Chest 1": 127,


	"Cliffside Climb - Spiked Underpass Chest 1": 128,


	"Cliffside Climb - Wide Respite Chest 1": 119,


	"Cliffside Climb - Topside Entrance Chest 1": 120,


	"Cliffside Climb - Clifftop Chest 1": 121,


	"Cliffside Climb - Entrance Underpass Chest 1": 126,


	"Cliffside Climb - Underpass Chest 1": 125,












	"Credits Peak Chest 1": 227,
	"Credits Peak Chest 2": 227,


	"Crimson Cove Chest 1": 41,


	"Crimson Cove 2 Chest 1": 42,


	"Crimson Cove 3 Chest 1": 43,



	"Deadland Road Chest 1": 6,


	"Deadland Road 2 Chest 1": 7,


	"Deadland Road 3 Chest 1": 8,


	"Dusty Beach Chest 1": 20,


	"Dusty Beach 2 Chest 1": 21,


	"Dusty Beach 3 Chest 1": 22,


	"Iron Rock Mt Chest 1": 15,


	"Iron Rock Mt 2 Chest 1": 16,


	"Iron Rock Mt 3 Chest 1": 17,


	"Knife Challenge 3 Chest 1": 201,


	"Credits Overlook Chest 1": 198,


	"Larval Forest Chest 1": 12,


	"Larval Forest 2 Chest 1": 13,



	"Larval Forest 3 Chest 1": 14,
	"Larval Forest 3 Chest 2": 14,
	"Larval Forest 3 Chest 3": 14,


	"Viscount Manor - Bottom Path to Attic Chest 1": 193,


	"Viscount Manor - Around Middle Chest 1": 194,
	"Viscount Manor - Around Middle Chest 2": 194,
	"Viscount Manor - Around Middle Chest 3": 194,


	"Viscount Manor - Path to Attic Chest 1": 163,


	"Viscount Manor - Attic Entrance Chest 1": 164,


	"Viscount Manor - Left Attic Chest 1": 165,


	"Viscount Manor - Middle Attic Chest 1": 166,


	"Viscount Manor - Right Attic Chest 1": 167,


	"Viscount Manor - Attic Exit Chest 1": 168,


	"Viscount Manor - Top Lab Entrance Chest 1": 155,


	"Viscount Manor - Right Barbed Hallway Chest 1": 183,
	"Viscount Manor - Right Barbed Hallway Chest 2": 183,


	"Viscount Manor - Left Barbed Hallway Chest 1": 181,


	"Viscount Manor - Barbed Hidden Room Chest 1": 160,
	"Viscount Manor - Barbed Hidden Room Chest 2": 160,
	"Viscount Manor - Barbed Hidden Room Chest 3": 160,


	"Viscount Manor - Manor Barricade Chest 1": 161,


	"Viscount Manor - Center Barricade Chest 1": 176,


	"Viscount Manor - Right Barricade Chest 1": 173,


	"Viscount Manor - Manor Containment Chest 1": 156,


	"Viscount Manor - Containment Chest 1": 185,


	"Viscount Manor - Lab Bottom Cache Chest 1": 179,
	"Viscount Manor - Lab Bottom Cache Chest 2": 179,
	"Viscount Manor - Lab Bottom Cache Chest 3": 179,


	"Viscount Manor - Center Barricade Stud Path Chest 1": 149,


	"Viscount Manor - Testing Room Entrance Chest 1": 157,
	"Viscount Manor - Testing Room Entrance Chest 2": 157,
	"Viscount Manor - Testing Room Entrance Chest 3": 157,


	"Viscount Manor - Manor Center Underbelly Chest 1": 170,
	"Viscount Manor - Manor Center Underbelly Chest 2": 170,
	"Viscount Manor - Manor Center Underbelly Chest 3": 170,


	"Viscount Manor - Manor Right Underbelly Chest 1": 184,
	"Viscount Manor - Manor Right Underbelly Chest 2": 184,
	"Viscount Manor - Manor Right Underbelly Chest 3": 184,


	"Viscount Manor - Manor Left Underbelly Chest 1": 169,


	"Viscount Manor - Manor Cache Chest 1": 152,
	"Viscount Manor - Manor Cache Chest 2": 152,


	"Viscount Manor - Crimson Cove Entrance Chest 1": 162,


	"Viscount Manor - Left Barricade Stud Path Chest 1": 180,


	"Viscount Manor - Lower Hallway to Lab Chest 1": 182,


	"Viscount Manor - Hallway to Lab Chest 1": 192,
	"Viscount Manor - Hallway to Lab Chest 2": 192,
	"Viscount Manor - Hallway to Lab Chest 3": 192,


	"Viscount Manor - Path Hidden Chest 1": 175,
	"Viscount Manor - Path Hidden Chest 2": 175,
	"Viscount Manor - Path Hidden Chest 3": 175,


	"Viscount Manor - Right Barricade Stud Path Chest 1": 148,
	"Viscount Manor - Right Barricade Stud Path Chest 2": 148,


	"Viscount Manor - Lab Top Cache Chest 1": 150,
	"Viscount Manor - Lab Top Cache Chest 2": 150,
	"Viscount Manor - Lab Top Cache Chest 3": 150,


	"Mushroom Cloud Chest 1": 23,


	"Mushroom Cloud 2 Chest 1": 24,


	"Mushroom Cloud 3 Chest 1": 25,


	"Quenchy Desert Chest 1": 26,


	"Quenchy Desert 2 Chest 1": 27,
	"Quenchy Desert 2 Chest 2": 27,


	"Quenchy Desert 3 Chest 1": 28,
	"Quenchy Desert 3 Chest 2": 28,


	"Stormcloud Crater Chest 1": 142,


	"Stormcloud Crater 2 Chest 1": 143,


	"Stormcloud Crater 3 Chest 1": 144,












	"Town Gate Chest 1": 40,
	"Town Gate Chest 2": 40,
	"Town Gate Chest 3": 40,


	"Toxic Jungle Chest 1": 9,


	"Toxic Jungle 2 Chest 1": 10,


	"Toxic Jungle 3 Chest 1": 11,


	"Viscount Manor Chest 1": 68,
	"Viscount Manor Chest 2": 68,


	"Tepid Volcano - Volcano Campsite Chest 1": 57,
	"Tepid Volcano - Volcano Campsite Chest 2": 57,


	"Tepid Volcano - Upper Entrance Chest 1": 102,


	"Tepid Volcano - Crater Exit Chest 1": 104,
	"Tepid Volcano - Crater Exit Chest 2": 104,


	"Tepid Volcano - Crater Chest 1": 100,


	"Tepid Volcano - Crater Under Chest 1": 105,
	"Tepid Volcano - Crater Under Chest 2": 105,
	"Tepid Volcano - Crater Under Chest 3": 105,


	"Tepid Volcano - Lava Drain Chest 1": 103,
	"Tepid Volcano - Lava Drain Chest 2": 103,


	"Tepid Volcano - Eastern Foot Chest 1": 63,
	"Tepid Volcano - Eastern Foot Chest 2": 63,


	"Tepid Volcano - Fluffy Clouds 3 Chest 1": 65,
	"Tepid Volcano - Fluffy Clouds 3 Chest 2": 65,


	"Tepid Volcano - Entryway Chest 1": 52,
	"Tepid Volcano - Entryway Chest 2": 52,


	"Tepid Volcano - Volcano Foot Camp Chest 1": 66,
	"Tepid Volcano - Volcano Foot Camp Chest 2": 66,
	"Tepid Volcano - Volcano Foot Camp Chest 3": 66,
	"Tepid Volcano - Volcano Foot Camp Chest 4": 66,


	"Tepid Volcano - Tepid Volcano Chest 1": 49,


	"Tepid Volcano - Hopping Left Chest 1": 106,


	"Tepid Volcano - Hopping Center-Left Chest 1": 107,


	"Tepid Volcano - Hopping Center-Right Chest 1": 108,


	"Tepid Volcano - Hopping Right Chest 1": 109,


	"Tepid Volcano - Lava Fall Bottom Chest 1": 94,
	"Tepid Volcano - Lava Fall Bottom Chest 2": 94,
	"Tepid Volcano - Lava Fall Bottom Chest 3": 94,


	"Tepid Volcano - Lava Fall Center Chest 1": 93,


	"Tepid Volcano - Left Corner Chest 1": 95,


	"Tepid Volcano - West Topside Chest 1": 101,
	"Tepid Volcano - West Topside Chest 2": 101,


	"Tepid Volcano - Scaling Wall Chest 1": 96,


	"Tepid Volcano - Lava Rain Bottom Chest 1": 110,


	"Tepid Volcano - Lava Rain Center Chest 1": 111,


	"Tepid Volcano - Bottom Cave Chest 1": 61,
	"Tepid Volcano - Bottom Cave Chest 2": 61,


	"Tepid Volcano - Side Cavern Chest 1": 60,


	"Tepid Volcano - Side Vent Chest 1": 55,
	"Tepid Volcano - Side Vent Chest 2": 55,
	"Tepid Volcano - Side Vent Chest 3": 55,












	"Tepid Volcano - Throat Chest 1": 54,
	"Tepid Volcano - Throat Chest 2": 54,
	"Tepid Volcano - Throat Chest 3": 54,


	"Tepid Volcano - Top Hole Chest 1": 99,


	"Tepid Volcano - Top Open Chest 1": 98,


	"Tepid Volcano - East Topside Chest 1": 59,


	"Tepid Volcano - Top Entrance Chest 1": 97,


	"Tepid Volcano - Vein Chest 1": 53,
	"Tepid Volcano - Vein Chest 2": 53,


	"Tepid Volcano - Vent Chest 1": 56,


	"Wing Challenge 3 Chest 1": 217,

}

LOCATION_ROOM_ID_TO_NAME = [[] for _ in range(244)]
for locationName, roomId in LOCATION_NAME_TO_ROOM_ID.items():
    LOCATION_ROOM_ID_TO_NAME[roomId].append(locationName)

ROOM_ID_TO_LOCATION_NAME_LIST = {
    "AbandonCenterPoorRoom": [
        "Abandon Town - Center Proletariat Chest 1",
        "Abandon Town - Center Proletariat Chest 2",
        "Abandon Town - Center Proletariat Chest 3",
    ],
    "AbandonCenterRichRoom": [
        "Abandon Town - Center Bourgeoisie Chest 1",
        "Abandon Town - Center Bourgeoisie Chest 2",
        "Abandon Town - Center Bourgeoisie Chest 3",
    ],
    "AbandonEastPoorRoom": [
        "Abandon Town - East Proletariat Chest 1",
        "Abandon Town - East Proletariat Chest 2",
        "Abandon Town - East Proletariat Chest 3",
    ],
    "AbandonEastRichRoom": [
        "Abandon Town - East Bourgeoisie Chest 1",
        "Abandon Town - East Bourgeoisie Chest 2",
        "Abandon Town - East Bourgeoisie Chest 3",
    ],
    "AbandonEastSkyRoom": [
        "Abandon Town - East Sky Chest 1",
        "Abandon Town - East Sky Chest 2",
        "Abandon Town - East Sky Chest 3",
    ],
    "AbandonEntranceRoom": [
        "Abandon Town - Abandoned Town Chest 1",
        "Abandon Town - Abandoned Town Chest 2",
        "Abandon Town - Abandoned Town Chest 3",
    ],
    "AbandonExitRoom": [
        "Abandon Town - East Entrance Chest 1",
        "Abandon Town - East Entrance Chest 2",
        "Abandon Town - East Entrance Chest 3",
    ],
    "AbandonHiddenRoom": [
        "Abandon Town - Hidden Chest 1",
        "Abandon Town - Hidden Chest 2",
        "Abandon Town - Hidden Chest 3",
    ],
    "AbandonNestRoom": [
        "Abandon Town - Cold Nest Chest 1",
        "Abandon Town - Cold Nest Chest 2",
        "Abandon Town - Cold Nest Chest 3",
        "Abandon Town - Cold Nest Chest 4",
        "Abandon Town - Cold Nest Chest 5",
        "Abandon Town - Cold Nest Chest 6",
        "Abandon Town - Cold Nest Chest 7",
        "Abandon Town - Cold Nest Chest 8",
        "Abandon Town - Cold Nest Chest 9",
        "Abandon Town - Cold Nest Chest 10",
        "Abandon Town - Cold Nest Chest 11",
        "Abandon Town - Cold Nest Chest 12",
    ],
    "AbandonSewerRoom": [
        "Abandon Town - Aqueduct Chest 1",
        "Abandon Town - Aqueduct Chest 2",
        "Abandon Town - Aqueduct Chest 3",
    ],
    "AbandonTunnelRoom": [
        "Abandon Town - Cold Tunnel Chest 1",
        "Abandon Town - Cold Tunnel Chest 2",
        "Abandon Town - Cold Tunnel Chest 3",
    ],
    "AbandonWestDrainRoom": [
        "Abandon Town - Drain Chest 1",
        "Abandon Town - Drain Chest 2",
        "Abandon Town - Drain Chest 3",
    ],
    "AbandonWestPoorRoom": [
        "Abandon Town - West Proletariat Chest 1",
        "Abandon Town - West Proletariat Chest 2",
        "Abandon Town - West Proletariat Chest 3",
    ],
    "AbandonWestRichRoom": [
        "Abandon Town - West Bourgeoisie Chest 1",
        "Abandon Town - West Bourgeoisie Chest 2",
        "Abandon Town - West Bourgeoisie Chest 3",
    ],
    "AbandonWestSkyRoom": [
        "Abandon Town - West Sky Chest 1",
        "Abandon Town - West Sky Chest 2",
        "Abandon Town - West Sky Chest 3",
    ],

    "Axe3PuzzleRoom": [
        "Axe Challenge 3 Chest 1",
    ],
    "Bomb3PuzzleRoom": [
        "Bomb Challenge 3 Chest 1",
    ],
    "BoneFortRoom": [
        "GrimeBone Fort Chest 1",
        "GrimeBone Fort Chest 2",
        "GrimeBone Fort Chest 3",
    ],
    "Caltrop3PuzzleRoom": [
        "Caltrop Challenge 3 Chest 1",
    ],
    "CastleBattlementsRoom": [
        "Kingdom Castle - Battlements Chest 1",
    ],
    "CastleBridgeRoom": [
        "Kingdom Castle - Kingdom Castle Chest 1",
        "Kingdom Castle - Kingdom Castle Chest 2",
        "Kingdom Castle - Kingdom Castle Chest 3",
    ],

    "CastleColumnRoom": [
        "Kingdom Castle - Columns Chest 1",
        "Kingdom Castle - Columns Chest 2",
        "Kingdom Castle - Columns Chest 3",
    ],
    "CastleDropRoom": [
        "Kingdom Castle - Overhang Chest 1",
        "Kingdom Castle - Overhang Chest 2",
    ],
    "CastleFoyerRoom": [
        "Kingdom Castle - Great Hall Chest 1",
    ],
    "CastleFrontBarbicanRoom": [
        "Kingdom Castle - Barbican Chest 1",
    ],
    "CastleHiddenHiddenRoom": [
        "Kingdom Castle - Hidden Hidden Storage Chest 1",
        "Kingdom Castle - Hidden Hidden Storage Chest 2",
        "Kingdom Castle - Hidden Hidden Storage Chest 3",
    ],
    "CastleHiddenStorageRoom": [
        "Kingdom Castle - Hidden Storage Chest 1",
        "Kingdom Castle - Hidden Storage Chest 2",
        "Kingdom Castle - Hidden Storage Chest 3",
        "Kingdom Castle - Hidden Storage Chest 4",
        "Kingdom Castle - Hidden Storage Chest 5",
        "Kingdom Castle - Hidden Storage Chest 6",
    ],
    "CastleKitchenRoom": [
        "Kingdom Castle - Kitchen Chest 1",
        "Kingdom Castle - Kitchen Chest 2",
        "Kingdom Castle - Kitchen Chest 3",
    ],
    "CastleMachicolationsRoom": [
        "Kingdom Castle - Machicolations Chest 1",
    ],
    "CastlePortcullisRoom": [
        "Kingdom Castle - Portcullis Room Chest 1",
        "Kingdom Castle - Portcullis Room Chest 2",
        "Kingdom Castle - Portcullis Room Chest 3",
    ],
    "CastleRampartsRoom": [
        "Kingdom Castle - Ramparts Chest 1",
    ],
    "CastleRearTowerRoom": [
        "Kingdom Castle - Rear Tower Chest 1",
        "Kingdom Castle - Rear Tower Chest 2",
    ],
    "CastleSaveRoom": [
        "Kingdom Castle - Castle Break Room Chest 1",
    ],
    "CastleSkyRoom": [
        "Kingdom Castle - Lone Tower Chest 1",
        "Kingdom Castle - Lone Tower Chest 2",
        "Kingdom Castle - Lone Tower Chest 3",
        "Kingdom Castle - Lone Tower Chest 4",
        "Kingdom Castle - Lone Tower Chest 5",
        "Kingdom Castle - Lone Tower Chest 6",
    ],
    "CastleTopRampartsRoom": [
        "Kingdom Castle - Top Ramparts Chest 1",
    ],
    "CastleTowerRoom": [
        "Kingdom Castle - Tower Chest 1",
        "Kingdom Castle - Tower Chest 2",
        "Kingdom Castle - Tower Chest 3",
    ],
    "Cleat3PuzzleRoom": [
        "Cleat Challenge 3 Chest 1",
    ],
    "CliffElevatorRoom": [
        "Cliffside Climb - Elevator Chest 1",
    ],
    "CliffEntranceRoom": [
        "Cliffside Climb - Cliffside Climb Chest 1",
    ],
    "CliffHiddenRoom": [
        "Cliffside Climb - Hidden Chest 1",
        "Cliffside Climb - Hidden Chest 2",
        "Cliffside Climb - Hidden Chest 3",
    ],
    "CliffHideUnderRoom": [
        "Cliffside Climb - Stealth Underneath Chest 1",
    ],
    "CliffMiddleExitRoom": [
        "Cliffside Climb - Shining Exit Chest 1",
        "Cliffside Climb - Shining Exit Chest 2",
        "Cliffside Climb - Shining Exit Chest 3",
    ],
    "CliffRightExitRoom": [
        "Cliffside Climb - Cliff Exit Chest 1",
        "Cliffside Climb - Cliff Exit Chest 2",
        "Cliffside Climb - Cliff Exit Chest 3",
    ],
    "CliffSaveRoom": [
        "Cliffside Climb - Cliffside Campsite Chest 1",
    ],
    "CliffSideEntranceRoom": [
        "Cliffside Climb - Cliffside Entrance Chest 1",
    ],
    "CliffSideWallRoom": [
        "Cliffside Climb - Scalable Cliff Chest 1",
    ],
    "CliffSkyTopRightRoom": [
        "Cliffside Climb - Curving Exit Chest 1",
    ],
    "CliffSkyWestTopSkyRoom": [
        "Cliffside Climb - Precipice Edge Chest 1",
    ],
    "CliffSmallUnderpassRoom": [
        "Cliffside Climb - Small Underpass Chest 1",
    ],
    "CliffSpikeRoom": [
        "Cliffside Climb - Spiked Underpass Chest 1",
    ],
    "CliffTopsideLeftRoom": [
        "Cliffside Climb - Wide Respite Chest 1",
    ],
    "CliffTopsideMiddleRoom": [
        "Cliffside Climb - Topside Entrance Chest 1",
    ],
    "CliffTopsideRightRoom": [
        "Cliffside Climb - Clifftop Chest 1",
    ],
    "CliffUnderEntranceRoom": [
        "Cliffside Climb - Entrance Underpass Chest 1",
    ],
    "CliffUnderpassRoom": [
        "Cliffside Climb - Underpass Chest 1",
    ],










    "CreditsParentRoom": [
        "Credits Peak Chest 1",
        "Credits Peak Chest 2",
        #"Credits Peak Event"
    ],
    "CrimsonCove1Room": [
        "Crimson Cove Chest 1",
    ],
    "CrimsonCove2Room": [
        "Crimson Cove 2 Chest 1",
    ],
    "CrimsonCove3Room": [
        "Crimson Cove 3 Chest 1",
    ],

    "DeadlandRoad1Room": [
        "Deadland Road Chest 1",
    ],
    "DeadlandRoad2Room": [
        "Deadland Road 2 Chest 1",
    ],
    "DeadlandRoad3Room": [
        "Deadland Road 3 Chest 1",
    ],
    "DustyBeach1Room": [
        "Dusty Beach Chest 1",
    ],
    "DustyBeach2Room": [
        "Dusty Beach 2 Chest 1",
    ],
    "DustyBeach3Room": [
        "Dusty Beach 3 Chest 1",
    ],
    "IronRock1Room": [
        "Iron Rock Mt Chest 1",
    ],
    "IronRock2Room": [
        "Iron Rock Mt 2 Chest 1",
    ],
    "IronRock3Room": [
        "Iron Rock Mt 3 Chest 1",
    ],
    "Knife3PuzzleRoom": [
        "Knife Challenge 3 Chest 1",
    ],
    "LabCreditsEntranceRoom": [
        "Credits Overlook Chest 1",
    ],
    "LarvelForest1Room": [
        "Larval Forest Chest 1",
    ],
    "LarvelForest2Room": [
        "Larval Forest 2 Chest 1",
    ],

    "LarvelForest3Room": [
        "Larval Forest 3 Chest 1",
        "Larval Forest 3 Chest 2",
        "Larval Forest 3 Chest 3",
    ],
    "ManorAroundBottomRoom": [
        "Viscount Manor - Bottom Path to Attic Chest 1",
    ],
    "ManorAroundMiddleRoom": [
        "Viscount Manor - Around Middle Chest 1",
        "Viscount Manor - Around Middle Chest 2",
        "Viscount Manor - Around Middle Chest 3",
    ],
    "ManorAroundTop1Room": [
        "Viscount Manor - Path to Attic Chest 1",
    ],
    "ManorAroundTop2Room": [
        "Viscount Manor - Attic Entrance Chest 1",
    ],
    "ManorAroundTop3Room": [
        "Viscount Manor - Left Attic Chest 1",
    ],
    "ManorAroundTop4Room": [
        "Viscount Manor - Middle Attic Chest 1",
    ],
    "ManorAroundTop5Room": [
        "Viscount Manor - Right Attic Chest 1",
    ],
    "ManorAroundTop6Room": [
        "Viscount Manor - Attic Exit Chest 1",
    ],
    "ManorAroundTop7Room": [
        "Viscount Manor - Top Lab Entrance Chest 1",
    ],
    "ManorBall1Room": [
        "Viscount Manor - Right Barbed Hallway Chest 1",
        "Viscount Manor - Right Barbed Hallway Chest 2",
    ],
    "ManorBall4Room": [
        "Viscount Manor - Left Barbed Hallway Chest 1",
    ],
    "ManorBallHiddenRoom": [
        "Viscount Manor - Barbed Hidden Room Chest 1",
        "Viscount Manor - Barbed Hidden Room Chest 2",
        "Viscount Manor - Barbed Hidden Room Chest 3",
    ],
    "ManorBlock1Room": [
        "Viscount Manor - Manor Barricade Chest 1",
    ],
    "ManorBlock2Room": [
        "Viscount Manor - Center Barricade Chest 1",
    ],
    "ManorBlock3Room": [
        "Viscount Manor - Right Barricade Chest 1",
    ],
    "ManorBossExitRoom": [
        "Viscount Manor - Manor Containment Chest 1",
    ],
    "ManorBossRushRoom": [
        "Viscount Manor - Containment Chest 1",
    ],
    "ManorBottomRightHiddenRoom": [
        "Viscount Manor - Lab Bottom Cache Chest 1",
        "Viscount Manor - Lab Bottom Cache Chest 2",
        "Viscount Manor - Lab Bottom Cache Chest 3",
    ],
    "ManorCenterPrePuzzleRoom": [
        "Viscount Manor - Center Barricade Stud Path Chest 1",
    ],
    "ManorExitRoom": [
        "Viscount Manor - Testing Room Entrance Chest 1",
        "Viscount Manor - Testing Room Entrance Chest 2",
        "Viscount Manor - Testing Room Entrance Chest 3",
    ],
    "ManorHiddenBottom2Room": [
        "Viscount Manor - Manor Center Underbelly Chest 1",
        "Viscount Manor - Manor Center Underbelly Chest 2",
        "Viscount Manor - Manor Center Underbelly Chest 3",
    ],
    "ManorHiddenBottom3Room": [
        "Viscount Manor - Manor Right Underbelly Chest 1",
        "Viscount Manor - Manor Right Underbelly Chest 2",
        "Viscount Manor - Manor Right Underbelly Chest 3",
    ],
    "ManorHiddenBottomRoom": [
        "Viscount Manor - Manor Left Underbelly Chest 1",
    ],
    "ManorHiddenRoom": [
        "Viscount Manor - Manor Cache Chest 1",
        "Viscount Manor - Manor Cache Chest 2",
    ],
    "ManorHubUnderRoom": [
        "Viscount Manor - Crimson Cove Entrance Chest 1",
    ],
    "ManorLeftPrePuzzleRoom": [
        "Viscount Manor - Left Barricade Stud Path Chest 1",
    ],
    "ManorPathBottomRoom": [
        "Viscount Manor - Lower Hallway to Lab Chest 1",
    ],
    "ManorPathCenterRoom": [
        "Viscount Manor - Hallway to Lab Chest 1",
        "Viscount Manor - Hallway to Lab Chest 2",
        "Viscount Manor - Hallway to Lab Chest 3",
    ],
    "ManorPathHiddenRoom": [
        "Viscount Manor - Path Hidden Chest 1",
        "Viscount Manor - Path Hidden Chest 2",
        "Viscount Manor - Path Hidden Chest 3",
    ],
    "ManorRightPrePuzzleRoom": [
        "Viscount Manor - Right Barricade Stud Path Chest 1",
        "Viscount Manor - Right Barricade Stud Path Chest 2",
    ],
    "ManorTopRightHiddenRoom": [
        "Viscount Manor - Lab Top Cache Chest 1",
        "Viscount Manor - Lab Top Cache Chest 2",
        "Viscount Manor - Lab Top Cache Chest 3",
    ],
    "MushroomClouds1Room": [
        "Mushroom Cloud Chest 1",
    ],
    "MushroomClouds2Room": [
        "Mushroom Cloud 2 Chest 1",
    ],
    "MushroomClouds3Room": [
        "Mushroom Cloud 3 Chest 1",
    ],
    "QuenchyDesert1Room": [
        "Quenchy Desert Chest 1",
    ],
    "QuenchyDesert2Room": [
        "Quenchy Desert 2 Chest 1",
        "Quenchy Desert 2 Chest 2",
    ],
    "QuenchyDesert3Room": [
        "Quenchy Desert 3 Chest 1",
        "Quenchy Desert 3 Chest 2",
    ],
    "StormCloudCrater1Room": [
        "Stormcloud Crater Chest 1",
    ],
    "StormCloudCrater2Room": [
        "Stormcloud Crater 2 Chest 1",
    ],
    "StormCloudCrater3Room": [
        "Stormcloud Crater 3 Chest 1",
    ],










    "TownGateRoom": [
        "Town Gate Chest 1",
        "Town Gate Chest 2",
        "Town Gate Chest 3",
    ],
    "ToxicJungle1Room": [
        "Toxic Jungle Chest 1",
    ],
    "ToxicJungle2Room": [
        "Toxic Jungle 2 Chest 1",
    ],
    "ToxicJungle3Room": [
        "Toxic Jungle 3 Chest 1",
    ],
    "ViscountManorHubRoom": [
        "Viscount Manor Chest 1",
        "Viscount Manor Chest 2",
    ],
    "VolcanoCampsiteRoom": [
        "Tepid Volcano - Volcano Campsite Chest 1",
        "Tepid Volcano - Volcano Campsite Chest 2",
    ],
    "VolcanoCaveTopEntranceRoom": [
        "Tepid Volcano - Upper Entrance Chest 1",
    ],
    "VolcanoCraterExitRoom": [
        "Tepid Volcano - Crater Exit Chest 1",
        "Tepid Volcano - Crater Exit Chest 2",
    ],
    "VolcanoCraterRoom": [
        "Tepid Volcano - Crater Chest 1",
    ],
    "VolcanoCraterUnderRoom": [
        "Tepid Volcano - Crater Under Chest 1",
        "Tepid Volcano - Crater Under Chest 2",
        "Tepid Volcano - Crater Under Chest 3",
    ],
    "VolcanoDrainRoom": [
        "Tepid Volcano - Lava Drain Chest 1",
        "Tepid Volcano - Lava Drain Chest 2",
    ],
    "VolcanoEastFootRoom": [
        "Tepid Volcano - Eastern Foot Chest 1",
        "Tepid Volcano - Eastern Foot Chest 2",
    ],
    "VolcanoEastSpace3Room": [
        "Tepid Volcano - Fluffy Clouds 3 Chest 1",
        "Tepid Volcano - Fluffy Clouds 3 Chest 2",
    ],
    "VolcanoEntrywayRoom": [
        "Tepid Volcano - Entryway Chest 1",
        "Tepid Volcano - Entryway Chest 2",
    ],
    "VolcanoFootCampRoom": [
        "Tepid Volcano - Volcano Foot Camp Chest 1",
        "Tepid Volcano - Volcano Foot Camp Chest 2",
        "Tepid Volcano - Volcano Foot Camp Chest 3",
        "Tepid Volcano - Volcano Foot Camp Chest 4",
    ],
    "VolcanoFootRoom": [
        "Tepid Volcano - Tepid Volcano Chest 1",
    ],
    "VolcanoHop1Room": [
        "Tepid Volcano - Hopping Left Chest 1",
    ],
    "VolcanoHop2Room": [
        "Tepid Volcano - Hopping Center-Left Chest 1",
    ],
    "VolcanoHop3Room": [
        "Tepid Volcano - Hopping Center-Right Chest 1",
    ],
    "VolcanoHop4Room": [
        "Tepid Volcano - Hopping Right Chest 1",
    ],
    "VolcanoLavaFallBottomRoom": [
        "Tepid Volcano - Lava Fall Bottom Chest 1",
        "Tepid Volcano - Lava Fall Bottom Chest 2",
        "Tepid Volcano - Lava Fall Bottom Chest 3",
    ],
    "VolcanoLavaFallCenterRoom": [
        "Tepid Volcano - Lava Fall Center Chest 1",
    ],
    "VolcanoLeftCornerRoom": [
        "Tepid Volcano - Left Corner Chest 1",
    ],
    "VolcanoOpenRoom": [
        "Tepid Volcano - West Topside Chest 1",
        "Tepid Volcano - West Topside Chest 2",
    ],
    "VolcanoPlatformRoom": [
        "Tepid Volcano - Scaling Wall Chest 1",
    ],
    "VolcanoRainBottomRoom": [
        "Tepid Volcano - Lava Rain Bottom Chest 1",
    ],
    "VolcanoRainCenterRoom": [
        "Tepid Volcano - Lava Rain Center Chest 1",
    ],
    "VolcanoSideBottomRoom": [
        "Tepid Volcano - Bottom Cave Chest 1",
        "Tepid Volcano - Bottom Cave Chest 2",
    ],
    "VolcanoSideSideRoom": [
        "Tepid Volcano - Side Cavern Chest 1",
    ],
    "VolcanoSideVentRoom": [
        "Tepid Volcano - Side Vent Chest 1",
        "Tepid Volcano - Side Vent Chest 2",
        "Tepid Volcano - Side Vent Chest 3",
    ],










    "VolcanoThroatRoom": [
        "Tepid Volcano - Throat Chest 1",
        "Tepid Volcano - Throat Chest 2",
        "Tepid Volcano - Throat Chest 3",
    ],
    "VolcanoTopHoleRoom": [
        "Tepid Volcano - Top Hole Chest 1",
    ],
    "VolcanoTopOpenRoom": [
        "Tepid Volcano - Top Open Chest 1",
    ],
    "VolcanoTopSideRoom": [
        "Tepid Volcano - East Topside Chest 1",
    ],
    "VolcanoTopTopEntranceRoom": [
        "Tepid Volcano - Top Entrance Chest 1",
    ],
    "VolcanoVeinRoom": [
        "Tepid Volcano - Vein Chest 1",
        "Tepid Volcano - Vein Chest 2",
    ],
    "VolcanoVentRoom": [
        "Tepid Volcano - Vent Chest 1",
    ],
    "Wing3PuzzleRoom": [
        "Wing Challenge 3 Chest 1",
	],
}

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
	"Abandon Town - Center Proletariat Chest 1": 7301,
	"Abandon Town - Center Proletariat Chest 2": 7302,
	"Abandon Town - Center Proletariat Chest 3": 7303,
	"Abandon Town - Center Bourgeoisie Chest 1": 7601,
	"Abandon Town - Center Bourgeoisie Chest 2": 7602,
	"Abandon Town - Center Bourgeoisie Chest 3": 7603,
	"Abandon Town - East Proletariat Chest 1": 7401,
	"Abandon Town - East Proletariat Chest 2": 7402,
	"Abandon Town - East Proletariat Chest 3": 7403,
	"Abandon Town - East Bourgeoisie Chest 1": 7701,
	"Abandon Town - East Bourgeoisie Chest 2": 7702,
	"Abandon Town - East Bourgeoisie Chest 3": 7703,
	"Abandon Town - East Sky Chest 1": 8001,
	"Abandon Town - East Sky Chest 2": 8002,
	"Abandon Town - East Sky Chest 3": 8003,
	"Abandon Town - Abandoned Town Chest 1": 7101,
	"Abandon Town - Abandoned Town Chest 2": 7102,
	"Abandon Town - Abandoned Town Chest 3": 7103,
	"Abandon Town - East Entrance Chest 1": 7901,
	"Abandon Town - East Entrance Chest 2": 7902,
	"Abandon Town - East Entrance Chest 3": 7903,
	"Abandon Town - Hidden Chest 1": 8401,
	"Abandon Town - Hidden Chest 2": 8402,
	"Abandon Town - Hidden Chest 3": 8403,
	"Abandon Town - Cold Nest Chest 1": 8601,
	"Abandon Town - Cold Nest Chest 2": 8602,
	"Abandon Town - Cold Nest Chest 3": 8603,
	"Abandon Town - Cold Nest Chest 4": 8604,
	"Abandon Town - Cold Nest Chest 5": 8605,
	"Abandon Town - Cold Nest Chest 6": 8606,
	"Abandon Town - Cold Nest Chest 7": 8607,
	"Abandon Town - Cold Nest Chest 8": 8608,
	"Abandon Town - Cold Nest Chest 9": 8609,
	"Abandon Town - Cold Nest Chest 10": 8610,
	"Abandon Town - Cold Nest Chest 11": 8611,
	"Abandon Town - Cold Nest Chest 12": 8612,
	"Abandon Town - Aqueduct Chest 1": 8501,
	"Abandon Town - Aqueduct Chest 2": 8502,
	"Abandon Town - Aqueduct Chest 3": 8503,
	"Abandon Town - Cold Tunnel Chest 1": 8201,
	"Abandon Town - Cold Tunnel Chest 2": 8202,
	"Abandon Town - Cold Tunnel Chest 3": 8203,
	"Abandon Town - Drain Chest 1": 8101,
	"Abandon Town - Drain Chest 2": 8102,
	"Abandon Town - Drain Chest 3": 8103,
	"Abandon Town - West Proletariat Chest 1": 7201,
	"Abandon Town - West Proletariat Chest 2": 7202,
	"Abandon Town - West Proletariat Chest 3": 7203,
	"Abandon Town - West Bourgeoisie Chest 1": 7501,
	"Abandon Town - West Bourgeoisie Chest 2": 7502,
	"Abandon Town - West Bourgeoisie Chest 3": 7503,
	"Abandon Town - West Sky Chest 1": 7801,
	"Abandon Town - West Sky Chest 2": 7802,
	"Abandon Town - West Sky Chest 3": 7803,
    "Axe Challenge 3 Chest 1": 20801,
	"Bomb Challenge 3 Chest 1": 21401,
	"GrimeBone Fort Chest 1": 1801,
	"GrimeBone Fort Chest 2": 1802,
	"GrimeBone Fort Chest 3": 1803,
	"Caltrop Challenge 3 Chest 1": 20501,
	"Kingdom Castle - Battlements Chest 1": 3701,
	"Kingdom Castle - Kingdom Castle Chest 1": 2901,
	"Kingdom Castle - Kingdom Castle Chest 2": 2902,
	"Kingdom Castle - Kingdom Castle Chest 3": 2903,
    "Kingdom Castle - Columns Chest 1": 8801,
	"Kingdom Castle - Columns Chest 2": 8802,
	"Kingdom Castle - Columns Chest 3": 8803,
	"Kingdom Castle - Overhang Chest 1": 8901,
	"Kingdom Castle - Overhang Chest 2": 8902,
	"Kingdom Castle - Great Hall Chest 1": 3301,
	"Kingdom Castle - Barbican Chest 1": 3001,
	"Kingdom Castle - Hidden Hidden Storage Chest 1": 8701,
	"Kingdom Castle - Hidden Hidden Storage Chest 2": 8702,
	"Kingdom Castle - Hidden Hidden Storage Chest 3": 8703,
	"Kingdom Castle - Hidden Storage Chest 1": 4601,
	"Kingdom Castle - Hidden Storage Chest 2": 4602,
	"Kingdom Castle - Hidden Storage Chest 3": 4603,
	"Kingdom Castle - Hidden Storage Chest 4": 4604,
	"Kingdom Castle - Hidden Storage Chest 5": 4605,
	"Kingdom Castle - Hidden Storage Chest 6": 4606,
	"Kingdom Castle - Kitchen Chest 1": 4401,
	"Kingdom Castle - Kitchen Chest 2": 4402,
	"Kingdom Castle - Kitchen Chest 3": 4403,
	"Kingdom Castle - Machicolations Chest 1": 3601,
	"Kingdom Castle - Portcullis Room Chest 1": 3201,
	"Kingdom Castle - Portcullis Room Chest 2": 3202,
	"Kingdom Castle - Portcullis Room Chest 3": 3203,
	"Kingdom Castle - Ramparts Chest 1": 3501,
	"Kingdom Castle - Rear Tower Chest 1": 4701,
	"Kingdom Castle - Rear Tower Chest 2": 4702,
	"Kingdom Castle - Castle Break Room Chest 1": 4501,
	"Kingdom Castle - Lone Tower Chest 1": 9101,
	"Kingdom Castle - Lone Tower Chest 2": 9102,
	"Kingdom Castle - Lone Tower Chest 3": 9103,
	"Kingdom Castle - Lone Tower Chest 4": 9104,
	"Kingdom Castle - Lone Tower Chest 5": 9105,
	"Kingdom Castle - Lone Tower Chest 6": 9106,
	"Kingdom Castle - Top Ramparts Chest 1": 9001,
	"Kingdom Castle - Tower Chest 1": 3401,
	"Kingdom Castle - Tower Chest 2": 3402,
	"Kingdom Castle - Tower Chest 3": 3403,
	"Cleat Challenge 3 Chest 1": 21101,
	"Cliffside Climb - Elevator Chest 1": 13201,
	"Cliffside Climb - Cliffside Climb Chest 1": 11501,
	"Cliffside Climb - Hidden Chest 1": 13301,
	"Cliffside Climb - Hidden Chest 2": 13302,
	"Cliffside Climb - Hidden Chest 3": 13303,
	"Cliffside Climb - Stealth Underneath Chest 1": 13701,
	"Cliffside Climb - Shining Exit Chest 1": 14001,
	"Cliffside Climb - Shining Exit Chest 2": 14002,
	"Cliffside Climb - Shining Exit Chest 3": 14003,
	"Cliffside Climb - Cliff Exit Chest 1": 14101,
	"Cliffside Climb - Cliff Exit Chest 2": 14102,
	"Cliffside Climb - Cliff Exit Chest 3": 14103,
	"Cliffside Climb - Cliffside Campsite Chest 1": 13101,
	"Cliffside Climb - Cliffside Entrance Chest 1": 11701,
	"Cliffside Climb - Scalable Cliff Chest 1": 11601,
	"Cliffside Climb - Curving Exit Chest 1": 12201,
	"Cliffside Climb - Precipice Edge Chest 1": 11801,
	"Cliffside Climb - Small Underpass Chest 1": 12701,
	"Cliffside Climb - Spiked Underpass Chest 1": 12801,
	"Cliffside Climb - Wide Respite Chest 1": 11901,
	"Cliffside Climb - Topside Entrance Chest 1": 12001,
	"Cliffside Climb - Clifftop Chest 1": 12101,
	"Cliffside Climb - Entrance Underpass Chest 1": 12601,
	"Cliffside Climb - Underpass Chest 1": 12501,
	"Credits Peak Chest 1": 22701,
	"Credits Peak Chest 2": 22702,
	"Crimson Cove Chest 1": 4101,
	"Crimson Cove 2 Chest 1": 4201,
	"Crimson Cove 3 Chest 1": 4301,
    "Deadland Road Chest 1": 601,
	"Deadland Road 2 Chest 1": 701,
	"Deadland Road 3 Chest 1": 801,
	"Dusty Beach Chest 1": 2001,
	"Dusty Beach 2 Chest 1": 2101,
	"Dusty Beach 3 Chest 1": 2201,
	"Iron Rock Mt Chest 1": 1501,
	"Iron Rock Mt 2 Chest 1": 1601,
	"Iron Rock Mt 3 Chest 1": 1701,
	"Knife Challenge 3 Chest 1": 20101,
	"Credits Overlook Chest 1": 19801,
	"Larval Forest Chest 1": 1201,
	"Larval Forest 2 Chest 1": 1301,
    "Larval Forest 3 Chest 1": 1401,
	"Larval Forest 3 Chest 2": 1402,
	"Larval Forest 3 Chest 3": 1403,
	"Viscount Manor - Bottom Path to Attic Chest 1": 19301,
	"Viscount Manor - Around Middle Chest 1": 19401,
	"Viscount Manor - Around Middle Chest 2": 19402,
	"Viscount Manor - Around Middle Chest 3": 19403,
	"Viscount Manor - Path to Attic Chest 1": 16301,
	"Viscount Manor - Attic Entrance Chest 1": 16401,
	"Viscount Manor - Left Attic Chest 1": 16501,
	"Viscount Manor - Middle Attic Chest 1": 16601,
	"Viscount Manor - Right Attic Chest 1": 16701,
	"Viscount Manor - Attic Exit Chest 1": 16801,
	"Viscount Manor - Top Lab Entrance Chest 1": 15501,
	"Viscount Manor - Right Barbed Hallway Chest 1": 18301,
	"Viscount Manor - Right Barbed Hallway Chest 2": 18302,
	"Viscount Manor - Left Barbed Hallway Chest 1": 18101,
	"Viscount Manor - Barbed Hidden Room Chest 1": 16001,
	"Viscount Manor - Barbed Hidden Room Chest 2": 16002,
	"Viscount Manor - Barbed Hidden Room Chest 3": 16003,
	"Viscount Manor - Manor Barricade Chest 1": 16101,
	"Viscount Manor - Center Barricade Chest 1": 17601,
	"Viscount Manor - Right Barricade Chest 1": 17301,
	"Viscount Manor - Manor Containment Chest 1": 15601,
	"Viscount Manor - Containment Chest 1": 18501,
	"Viscount Manor - Lab Bottom Cache Chest 1": 17901,
	"Viscount Manor - Lab Bottom Cache Chest 2": 17902,
	"Viscount Manor - Lab Bottom Cache Chest 3": 17903,
	"Viscount Manor - Center Barricade Stud Path Chest 1": 14901,
	"Viscount Manor - Testing Room Entrance Chest 1": 15701,
	"Viscount Manor - Testing Room Entrance Chest 2": 15702,
	"Viscount Manor - Testing Room Entrance Chest 3": 15703,
	"Viscount Manor - Manor Center Underbelly Chest 1": 17001,
	"Viscount Manor - Manor Center Underbelly Chest 2": 17002,
	"Viscount Manor - Manor Center Underbelly Chest 3": 17003,
	"Viscount Manor - Manor Right Underbelly Chest 1": 18401,
	"Viscount Manor - Manor Right Underbelly Chest 2": 18402,
	"Viscount Manor - Manor Right Underbelly Chest 3": 18403,
	"Viscount Manor - Manor Left Underbelly Chest 1": 16901,
	"Viscount Manor - Manor Cache Chest 1": 15201,
	"Viscount Manor - Manor Cache Chest 2": 15202,
	"Viscount Manor - Crimson Cove Entrance Chest 1": 16201,
	"Viscount Manor - Left Barricade Stud Path Chest 1": 18001,
	"Viscount Manor - Lower Hallway to Lab Chest 1": 18201,
	"Viscount Manor - Hallway to Lab Chest 1": 19201,
	"Viscount Manor - Hallway to Lab Chest 2": 19202,
	"Viscount Manor - Hallway to Lab Chest 3": 19203,
	"Viscount Manor - Path Hidden Chest 1": 17501,
	"Viscount Manor - Path Hidden Chest 2": 17502,
	"Viscount Manor - Path Hidden Chest 3": 17503,
	"Viscount Manor - Right Barricade Stud Path Chest 1": 14801,
	"Viscount Manor - Right Barricade Stud Path Chest 2": 14802,
	"Viscount Manor - Lab Top Cache Chest 1": 15001,
	"Viscount Manor - Lab Top Cache Chest 2": 15002,
	"Viscount Manor - Lab Top Cache Chest 3": 15003,
	"Mushroom Cloud Chest 1": 2301,
	"Mushroom Cloud 2 Chest 1": 2401,
	"Mushroom Cloud 3 Chest 1": 2501,
	"Quenchy Desert Chest 1": 2601,
	"Quenchy Desert 2 Chest 1": 2701,
	"Quenchy Desert 2 Chest 2": 2702,
	"Quenchy Desert 3 Chest 1": 2801,
	"Quenchy Desert 3 Chest 2": 2802,
	"Stormcloud Crater Chest 1": 14201,
	"Stormcloud Crater 2 Chest 1": 14301,
	"Stormcloud Crater 3 Chest 1": 14401,
	"Town Gate Chest 1": 4001,
	"Town Gate Chest 2": 4002,
	"Town Gate Chest 3": 4003,
	"Toxic Jungle Chest 1": 901,
	"Toxic Jungle 2 Chest 1": 1001,
	"Toxic Jungle 3 Chest 1": 1101,
	"Viscount Manor Chest 1": 6801,
	"Viscount Manor Chest 2": 6802,
	"Tepid Volcano - Volcano Campsite Chest 1": 5701,
	"Tepid Volcano - Volcano Campsite Chest 2": 5702,
	"Tepid Volcano - Upper Entrance Chest 1": 10201,
	"Tepid Volcano - Crater Exit Chest 1": 10401,
	"Tepid Volcano - Crater Exit Chest 2": 10402,
	"Tepid Volcano - Crater Chest 1": 10001,
	"Tepid Volcano - Crater Under Chest 1": 10501,
	"Tepid Volcano - Crater Under Chest 2": 10502,
	"Tepid Volcano - Crater Under Chest 3": 10503,
	"Tepid Volcano - Lava Drain Chest 1": 10301,
	"Tepid Volcano - Lava Drain Chest 2": 10302,
	"Tepid Volcano - Eastern Foot Chest 1": 6301,
	"Tepid Volcano - Eastern Foot Chest 2": 6302,
	"Tepid Volcano - Fluffy Clouds 3 Chest 1": 6501,
	"Tepid Volcano - Fluffy Clouds 3 Chest 2": 6502,
	"Tepid Volcano - Entryway Chest 1": 5201,
	"Tepid Volcano - Entryway Chest 2": 5202,
	"Tepid Volcano - Volcano Foot Camp Chest 1": 6601,
	"Tepid Volcano - Volcano Foot Camp Chest 2": 6602,
	"Tepid Volcano - Volcano Foot Camp Chest 3": 6603,
	"Tepid Volcano - Volcano Foot Camp Chest 4": 6604,
	"Tepid Volcano - Tepid Volcano Chest 1": 4901,
	"Tepid Volcano - Hopping Left Chest 1": 10601,
	"Tepid Volcano - Hopping Center-Left Chest 1": 10701,
	"Tepid Volcano - Hopping Center-Right Chest 1": 10801,
	"Tepid Volcano - Hopping Right Chest 1": 10901,
	"Tepid Volcano - Lava Fall Bottom Chest 1": 9401,
	"Tepid Volcano - Lava Fall Bottom Chest 2": 9402,
	"Tepid Volcano - Lava Fall Bottom Chest 3": 9403,
	"Tepid Volcano - Lava Fall Center Chest 1": 9301,
	"Tepid Volcano - Left Corner Chest 1": 9501,
	"Tepid Volcano - West Topside Chest 1": 10101,
	"Tepid Volcano - West Topside Chest 2": 10102,
	"Tepid Volcano - Scaling Wall Chest 1": 9601,
	"Tepid Volcano - Lava Rain Bottom Chest 1": 11001,
	"Tepid Volcano - Lava Rain Center Chest 1": 11101,
	"Tepid Volcano - Bottom Cave Chest 1": 6101,
	"Tepid Volcano - Bottom Cave Chest 2": 6102,
	"Tepid Volcano - Side Cavern Chest 1": 6001,
	"Tepid Volcano - Side Vent Chest 1": 5501,
	"Tepid Volcano - Side Vent Chest 2": 5502,
	"Tepid Volcano - Side Vent Chest 3": 5503,
	"Tepid Volcano - Throat Chest 1": 5401,
	"Tepid Volcano - Throat Chest 2": 5402,
	"Tepid Volcano - Throat Chest 3": 5403,
	"Tepid Volcano - Top Hole Chest 1": 9901,
	"Tepid Volcano - Top Open Chest 1": 9801,
	"Tepid Volcano - East Topside Chest 1": 5901,
	"Tepid Volcano - Top Entrance Chest 1": 9701,
	"Tepid Volcano - Vein Chest 1": 5301,
	"Tepid Volcano - Vein Chest 2": 5302,
	"Tepid Volcano - Vent Chest 1": 5601,
	"Wing Challenge 3 Chest 1": 21701,
}

location_name_to_region_name = {
	"Abandon Town - Center Proletariat Chest 1": "Abandon Town",
	"Abandon Town - Center Proletariat Chest 2": "Abandon Town",
	"Abandon Town - Center Proletariat Chest 3": "Abandon Town",
	"Abandon Town - Center Bourgeoisie Chest 1": "Abandon Town",
	"Abandon Town - Center Bourgeoisie Chest 2": "Abandon Town",
	"Abandon Town - Center Bourgeoisie Chest 3": "Abandon Town",
	"Abandon Town - East Proletariat Chest 1": "Abandon Town",
	"Abandon Town - East Proletariat Chest 2": "Abandon Town",
	"Abandon Town - East Proletariat Chest 3": "Abandon Town",
	"Abandon Town - East Bourgeoisie Chest 1": "Abandon Town",
	"Abandon Town - East Bourgeoisie Chest 2": "Abandon Town",
	"Abandon Town - East Bourgeoisie Chest 3": "Abandon Town",
	"Abandon Town - East Sky Chest 1": "Abandon Town",
	"Abandon Town - East Sky Chest 2": "Abandon Town",
	"Abandon Town - East Sky Chest 3": "Abandon Town",
	"Abandon Town - Abandoned Town Chest 1": "Abandon Town",
	"Abandon Town - Abandoned Town Chest 2": "Abandon Town",
	"Abandon Town - Abandoned Town Chest 3": "Abandon Town",
	"Abandon Town - East Entrance Chest 1": "Abandon Town",
	"Abandon Town - East Entrance Chest 2": "Abandon Town",
	"Abandon Town - East Entrance Chest 3": "Abandon Town",
	"Abandon Town - Hidden Chest 1": "Abandon Town",
	"Abandon Town - Hidden Chest 2": "Abandon Town",
	"Abandon Town - Hidden Chest 3": "Abandon Town",
	"Abandon Town - Cold Nest Chest 1": "Abandon Town",
	"Abandon Town - Cold Nest Chest 2": "Abandon Town",
	"Abandon Town - Cold Nest Chest 3": "Abandon Town",
	"Abandon Town - Cold Nest Chest 4": "Abandon Town",
	"Abandon Town - Cold Nest Chest 5": "Abandon Town",
	"Abandon Town - Cold Nest Chest 6": "Abandon Town",
	"Abandon Town - Cold Nest Chest 7": "Abandon Town",
	"Abandon Town - Cold Nest Chest 8": "Abandon Town",
	"Abandon Town - Cold Nest Chest 9": "Abandon Town",
	"Abandon Town - Cold Nest Chest 10": "Abandon Town",
	"Abandon Town - Cold Nest Chest 11": "Abandon Town",
	"Abandon Town - Cold Nest Chest 12": "Abandon Town",
	"Abandon Town - Aqueduct Chest 1": "Abandon Town",
	"Abandon Town - Aqueduct Chest 2": "Abandon Town",
	"Abandon Town - Aqueduct Chest 3": "Abandon Town",
	"Abandon Town - Cold Tunnel Chest 1": "Abandon Town",
	"Abandon Town - Cold Tunnel Chest 2": "Abandon Town",
	"Abandon Town - Cold Tunnel Chest 3": "Abandon Town",
	"Abandon Town - Drain Chest 1": "Abandon Town",
	"Abandon Town - Drain Chest 2": "Abandon Town",
	"Abandon Town - Drain Chest 3": "Abandon Town",
	"Abandon Town - West Proletariat Chest 1": "Abandon Town",
	"Abandon Town - West Proletariat Chest 2": "Abandon Town",
	"Abandon Town - West Proletariat Chest 3": "Abandon Town",
	"Abandon Town - West Bourgeoisie Chest 1": "Abandon Town",
	"Abandon Town - West Bourgeoisie Chest 2": "Abandon Town",
	"Abandon Town - West Bourgeoisie Chest 3": "Abandon Town",
	"Abandon Town - West Sky Chest 1": "Abandon Town",
	"Abandon Town - West Sky Chest 2": "Abandon Town",
	"Abandon Town - West Sky Chest 3": "Abandon Town",
    "Axe Challenge 3 Chest 1": "World Map East",
	"Bomb Challenge 3 Chest 1": "Tepid Volcano",
	"GrimeBone Fort Chest 1": "World Map East",
	"GrimeBone Fort Chest 2": "World Map East",
	"GrimeBone Fort Chest 3": "World Map East",
	"Caltrop Challenge 3 Chest 1": "World Map East",
	"Kingdom Castle - Battlements Chest 1": "Kingdom Castle",
	"Kingdom Castle - Kingdom Castle Chest 1": "Kingdom Castle",
	"Kingdom Castle - Kingdom Castle Chest 2": "Kingdom Castle",
	"Kingdom Castle - Kingdom Castle Chest 3": "Kingdom Castle",
    "Kingdom Castle - Columns Chest 1": "Kingdom Castle",
	"Kingdom Castle - Columns Chest 2": "Kingdom Castle",
	"Kingdom Castle - Columns Chest 3": "Kingdom Castle",
	"Kingdom Castle - Overhang Chest 1": "Kingdom Castle",
	"Kingdom Castle - Overhang Chest 2": "Kingdom Castle",
	"Kingdom Castle - Great Hall Chest 1": "Kingdom Castle",
	"Kingdom Castle - Barbican Chest 1": "Kingdom Castle",
	"Kingdom Castle - Hidden Hidden Storage Chest 1": "Kingdom Castle",
	"Kingdom Castle - Hidden Hidden Storage Chest 2": "Kingdom Castle",
	"Kingdom Castle - Hidden Hidden Storage Chest 3": "Kingdom Castle",
	"Kingdom Castle - Hidden Storage Chest 1": "Kingdom Castle",
	"Kingdom Castle - Hidden Storage Chest 2": "Kingdom Castle",
	"Kingdom Castle - Hidden Storage Chest 3": "Kingdom Castle",
	"Kingdom Castle - Hidden Storage Chest 4": "Kingdom Castle",
	"Kingdom Castle - Hidden Storage Chest 5": "Kingdom Castle",
	"Kingdom Castle - Hidden Storage Chest 6": "Kingdom Castle",
	"Kingdom Castle - Kitchen Chest 1": "Kingdom Castle",
	"Kingdom Castle - Kitchen Chest 2": "Kingdom Castle",
	"Kingdom Castle - Kitchen Chest 3": "Kingdom Castle",
	"Kingdom Castle - Machicolations Chest 1": "Kingdom Castle",
	"Kingdom Castle - Portcullis Room Chest 1": "Kingdom Castle",
	"Kingdom Castle - Portcullis Room Chest 2": "Kingdom Castle",
	"Kingdom Castle - Portcullis Room Chest 3": "Kingdom Castle",
	"Kingdom Castle - Ramparts Chest 1": "Kingdom Castle",
	"Kingdom Castle - Rear Tower Chest 1": "Kingdom Castle",
	"Kingdom Castle - Rear Tower Chest 2": "Kingdom Castle",
	"Kingdom Castle - Castle Break Room Chest 1": "Kingdom Castle",
	"Kingdom Castle - Lone Tower Chest 1": "Kingdom Castle",
	"Kingdom Castle - Lone Tower Chest 2": "Kingdom Castle",
	"Kingdom Castle - Lone Tower Chest 3": "Kingdom Castle",
	"Kingdom Castle - Lone Tower Chest 4": "Kingdom Castle",
	"Kingdom Castle - Lone Tower Chest 5": "Kingdom Castle",
	"Kingdom Castle - Lone Tower Chest 6": "Kingdom Castle",
	"Kingdom Castle - Top Ramparts Chest 1": "Kingdom Castle",
	"Kingdom Castle - Tower Chest 1": "Kingdom Castle",
	"Kingdom Castle - Tower Chest 2": "Kingdom Castle",
	"Kingdom Castle - Tower Chest 3": "Kingdom Castle",
	"Cleat Challenge 3 Chest 1": "World Map East",
	"Cliffside Climb - Elevator Chest 1": "Cliffside Climb",
	"Cliffside Climb - Cliffside Climb Chest 1": "Cliffside Climb",
	"Cliffside Climb - Hidden Chest 1": "Cliffside Climb",
	"Cliffside Climb - Hidden Chest 2": "Cliffside Climb",
	"Cliffside Climb - Hidden Chest 3": "Cliffside Climb",
	"Cliffside Climb - Stealth Underneath Chest 1": "Cliffside Climb",
	"Cliffside Climb - Shining Exit Chest 1": "Cliffside Climb",
	"Cliffside Climb - Shining Exit Chest 2": "Cliffside Climb",
	"Cliffside Climb - Shining Exit Chest 3": "Cliffside Climb",
	"Cliffside Climb - Cliff Exit Chest 1": "Cliffside Climb",
	"Cliffside Climb - Cliff Exit Chest 2": "Cliffside Climb",
	"Cliffside Climb - Cliff Exit Chest 3": "Cliffside Climb",
	"Cliffside Climb - Cliffside Campsite Chest 1": "Cliffside Climb",
	"Cliffside Climb - Cliffside Entrance Chest 1": "Cliffside Climb",
	"Cliffside Climb - Scalable Cliff Chest 1": "Cliffside Climb",
	"Cliffside Climb - Curving Exit Chest 1": "Cliffside Climb",
	"Cliffside Climb - Precipice Edge Chest 1": "Cliffside Climb",
	"Cliffside Climb - Small Underpass Chest 1": "Cliffside Climb",
	"Cliffside Climb - Spiked Underpass Chest 1": "Cliffside Climb",
	"Cliffside Climb - Wide Respite Chest 1": "Cliffside Climb",
	"Cliffside Climb - Topside Entrance Chest 1": "Cliffside Climb",
	"Cliffside Climb - Clifftop Chest 1": "Cliffside Climb",
	"Cliffside Climb - Entrance Underpass Chest 1": "Cliffside Climb",
	"Cliffside Climb - Underpass Chest 1": "Cliffside Climb",
	"Credits Peak Chest 1": "Viscount Lab",
	"Credits Peak Chest 2": "Viscount Lab",
	"Crimson Cove Chest 1": "Viscount Manor",
	"Crimson Cove 2 Chest 1": "Viscount Manor",
	"Crimson Cove 3 Chest 1": "Viscount Manor",
    "Deadland Road Chest 1": "World Map NorthWest",
	"Deadland Road 2 Chest 1": "World Map NorthWest",
	"Deadland Road 3 Chest 1": "World Map NorthWest",
	"Dusty Beach Chest 1": "Castle Town",
	"Dusty Beach 2 Chest 1": "Castle Town",
	"Dusty Beach 3 Chest 1": "Castle Town",
	"Iron Rock Mt Chest 1": "World Map East",
	"Iron Rock Mt 2 Chest 1": "World Map East",
	"Iron Rock Mt 3 Chest 1": "World Map East",
	"Knife Challenge 3 Chest 1": "World Map NorthWest",
	"Credits Overlook Chest 1": "Viscount Lab",
	"Larval Forest Chest 1": "World Map NorthWest",
	"Larval Forest 2 Chest 1": "World Map NorthWest",
    "Larval Forest 3 Chest 1": "World Map NorthWest",
	"Larval Forest 3 Chest 2": "World Map NorthWest",
	"Larval Forest 3 Chest 3": "World Map NorthWest",
	"Viscount Manor - Bottom Path to Attic Chest 1": "Viscount Manor",
	"Viscount Manor - Around Middle Chest 1": "Viscount Manor",
	"Viscount Manor - Around Middle Chest 2": "Viscount Manor",
	"Viscount Manor - Around Middle Chest 3": "Viscount Manor",
	"Viscount Manor - Path to Attic Chest 1": "Viscount Manor",
	"Viscount Manor - Attic Entrance Chest 1": "Viscount Manor",
	"Viscount Manor - Left Attic Chest 1": "Viscount Manor",
	"Viscount Manor - Middle Attic Chest 1": "Viscount Manor",
	"Viscount Manor - Right Attic Chest 1": "Viscount Manor",
	"Viscount Manor - Attic Exit Chest 1": "Viscount Manor",
	"Viscount Manor - Top Lab Entrance Chest 1": "Viscount Manor",
	"Viscount Manor - Right Barbed Hallway Chest 1": "Viscount Manor",
	"Viscount Manor - Right Barbed Hallway Chest 2": "Viscount Manor",
	"Viscount Manor - Left Barbed Hallway Chest 1": "Viscount Manor",
	"Viscount Manor - Barbed Hidden Room Chest 1": "Viscount Manor",
	"Viscount Manor - Barbed Hidden Room Chest 2": "Viscount Manor",
	"Viscount Manor - Barbed Hidden Room Chest 3": "Viscount Manor",
	"Viscount Manor - Manor Barricade Chest 1": "Viscount Manor",
	"Viscount Manor - Center Barricade Chest 1": "Viscount Manor",
	"Viscount Manor - Right Barricade Chest 1": "Viscount Manor",
	"Viscount Manor - Manor Containment Chest 1": "Viscount Manor",
	"Viscount Manor - Containment Chest 1": "Viscount Manor",
	"Viscount Manor - Lab Bottom Cache Chest 1": "Viscount Manor",
	"Viscount Manor - Lab Bottom Cache Chest 2": "Viscount Manor",
	"Viscount Manor - Lab Bottom Cache Chest 3": "Viscount Manor",
	"Viscount Manor - Center Barricade Stud Path Chest 1": "Viscount Manor",
	"Viscount Manor - Testing Room Entrance Chest 1": "Viscount Manor",
	"Viscount Manor - Testing Room Entrance Chest 2": "Viscount Manor",
	"Viscount Manor - Testing Room Entrance Chest 3": "Viscount Manor",
	"Viscount Manor - Manor Center Underbelly Chest 1": "Viscount Manor",
	"Viscount Manor - Manor Center Underbelly Chest 2": "Viscount Manor",
	"Viscount Manor - Manor Center Underbelly Chest 3": "Viscount Manor",
	"Viscount Manor - Manor Right Underbelly Chest 1": "Viscount Manor",
	"Viscount Manor - Manor Right Underbelly Chest 2": "Viscount Manor",
	"Viscount Manor - Manor Right Underbelly Chest 3": "Viscount Manor",
	"Viscount Manor - Manor Left Underbelly Chest 1": "Viscount Manor",
	"Viscount Manor - Manor Cache Chest 1": "Viscount Manor",
	"Viscount Manor - Manor Cache Chest 2": "Viscount Manor",
	"Viscount Manor - Crimson Cove Entrance Chest 1": "Viscount Manor",
	"Viscount Manor - Left Barricade Stud Path Chest 1": "Viscount Manor",
	"Viscount Manor - Lower Hallway to Lab Chest 1": "Viscount Manor",
	"Viscount Manor - Hallway to Lab Chest 1": "Viscount Manor",
	"Viscount Manor - Hallway to Lab Chest 2": "Viscount Manor",
	"Viscount Manor - Hallway to Lab Chest 3": "Viscount Manor",
	"Viscount Manor - Path Hidden Chest 1": "Viscount Manor",
	"Viscount Manor - Path Hidden Chest 2": "Viscount Manor",
	"Viscount Manor - Path Hidden Chest 3": "Viscount Manor",
	"Viscount Manor - Right Barricade Stud Path Chest 1": "Viscount Manor",
	"Viscount Manor - Right Barricade Stud Path Chest 2": "Viscount Manor",
	"Viscount Manor - Lab Top Cache Chest 1": "Viscount Manor",
	"Viscount Manor - Lab Top Cache Chest 2": "Viscount Manor",
	"Viscount Manor - Lab Top Cache Chest 3": "Viscount Manor",
	"Mushroom Cloud Chest 1": "Castle Town",
	"Mushroom Cloud 2 Chest 1": "Castle Town",
	"Mushroom Cloud 3 Chest 1": "Castle Town",
	"Quenchy Desert Chest 1": "Tepid Volcano",
	"Quenchy Desert 2 Chest 1": "Tepid Volcano",
	"Quenchy Desert 2 Chest 2": "Tepid Volcano",
	"Quenchy Desert 3 Chest 1": "Tepid Volcano",
	"Quenchy Desert 3 Chest 2": "Tepid Volcano",
	"Stormcloud Crater Chest 1": "Tepid Volcano",
	"Stormcloud Crater 2 Chest 1": "Tepid Volcano",
	"Stormcloud Crater 3 Chest 1": "Tepid Volcano",
	"Town Gate Chest 1": "Castle Town",
	"Town Gate Chest 2": "Castle Town",
	"Town Gate Chest 3": "Castle Town",
	"Toxic Jungle Chest 1": "World Map East",
	"Toxic Jungle 2 Chest 1": "World Map East",
	"Toxic Jungle 3 Chest 1": "World Map East",
	"Viscount Manor Chest 1": "Viscount Manor",
	"Viscount Manor Chest 2": "Viscount Manor",
	"Tepid Volcano - Volcano Campsite Chest 1": "Tepid Volcano",
	"Tepid Volcano - Volcano Campsite Chest 2": "Tepid Volcano",
	"Tepid Volcano - Upper Entrance Chest 1": "Tepid Volcano",
	"Tepid Volcano - Crater Exit Chest 1": "Tepid Volcano",
	"Tepid Volcano - Crater Exit Chest 2": "Tepid Volcano",
	"Tepid Volcano - Crater Chest 1": "Tepid Volcano",
	"Tepid Volcano - Crater Under Chest 1": "Tepid Volcano",
	"Tepid Volcano - Crater Under Chest 2": "Tepid Volcano",
	"Tepid Volcano - Crater Under Chest 3": "Tepid Volcano",
	"Tepid Volcano - Lava Drain Chest 1": "Tepid Volcano",
	"Tepid Volcano - Lava Drain Chest 2": "Tepid Volcano",
	"Tepid Volcano - Eastern Foot Chest 1": "Tepid Volcano",
	"Tepid Volcano - Eastern Foot Chest 2": "Tepid Volcano",
	"Tepid Volcano - Fluffy Clouds 3 Chest 1": "Tepid Volcano",
	"Tepid Volcano - Fluffy Clouds 3 Chest 2": "Tepid Volcano",
	"Tepid Volcano - Entryway Chest 1": "Tepid Volcano",
	"Tepid Volcano - Entryway Chest 2": "Tepid Volcano",
	"Tepid Volcano - Volcano Foot Camp Chest 1": "Tepid Volcano",
	"Tepid Volcano - Volcano Foot Camp Chest 2": "Tepid Volcano",
	"Tepid Volcano - Volcano Foot Camp Chest 3": "Tepid Volcano",
	"Tepid Volcano - Volcano Foot Camp Chest 4": "Tepid Volcano",
	"Tepid Volcano - Tepid Volcano Chest 1": "Tepid Volcano",
	"Tepid Volcano - Hopping Left Chest 1": "Tepid Volcano",
	"Tepid Volcano - Hopping Center-Left Chest 1": "Tepid Volcano",
	"Tepid Volcano - Hopping Center-Right Chest 1": "Tepid Volcano",
	"Tepid Volcano - Hopping Right Chest 1": "Tepid Volcano",
	"Tepid Volcano - Lava Fall Bottom Chest 1": "Tepid Volcano",
	"Tepid Volcano - Lava Fall Bottom Chest 2": "Tepid Volcano",
	"Tepid Volcano - Lava Fall Bottom Chest 3": "Tepid Volcano",
	"Tepid Volcano - Lava Fall Center Chest 1": "Tepid Volcano",
	"Tepid Volcano - Left Corner Chest 1": "Tepid Volcano",
	"Tepid Volcano - West Topside Chest 1": "Tepid Volcano",
	"Tepid Volcano - West Topside Chest 2": "Tepid Volcano",
	"Tepid Volcano - Scaling Wall Chest 1": "Tepid Volcano",
	"Tepid Volcano - Lava Rain Bottom Chest 1": "Tepid Volcano",
	"Tepid Volcano - Lava Rain Center Chest 1": "Tepid Volcano",
	"Tepid Volcano - Bottom Cave Chest 1": "Tepid Volcano",
	"Tepid Volcano - Bottom Cave Chest 2": "Tepid Volcano",
	"Tepid Volcano - Side Cavern Chest 1": "Tepid Volcano",
	"Tepid Volcano - Side Vent Chest 1": "Tepid Volcano",
	"Tepid Volcano - Side Vent Chest 2": "Tepid Volcano",
	"Tepid Volcano - Side Vent Chest 3": "Tepid Volcano",
	"Tepid Volcano - Throat Chest 1": "Tepid Volcano",
	"Tepid Volcano - Throat Chest 2": "Tepid Volcano",
	"Tepid Volcano - Throat Chest 3": "Tepid Volcano",
	"Tepid Volcano - Top Hole Chest 1": "Tepid Volcano",
	"Tepid Volcano - Top Open Chest 1": "Tepid Volcano",
	"Tepid Volcano - East Topside Chest 1": "Tepid Volcano",
	"Tepid Volcano - Top Entrance Chest 1": "Tepid Volcano",
	"Tepid Volcano - Vein Chest 1": "Tepid Volcano",
	"Tepid Volcano - Vein Chest 2": "Tepid Volcano",
	"Tepid Volcano - Vent Chest 1": "Tepid Volcano",
	"Wing Challenge 3 Chest 1": "Castle Town",
    
	#"Credits Peak Event": "Viscount Lab"
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
    for location_name in world.location_name_to_id.keys():
        region_name = location_name_to_region_name[location_name]
        regionInstance = world.get_region(region_name)
        regionInstance.locations.append(HoVLocation(
            world.player, location_name, world.location_name_to_id[location_name], regionInstance
        ))


def create_events(world: HoVWorld) -> None:
    hoVRegionSet = get_region_set(world)
    #hoVRegionSet.viscount_lab.locations.append(HoVLocation(world.player, "Credits Peak Event", None, hoVRegionSet.viscount_lab))

    # hoVRegionSet.viscount_lab.add_event(
    #     "Credits Peak Event", "Credits Peak Event", location_type=HoVLocation, item_type=HoVItem
    # )
    
    # hoVRegionSet.map_rando_rogue_world.add_event(
    #     "All Chests Opened", "Victory", location_type=HoVLocation, item_type=items.HoVItem
    # )
