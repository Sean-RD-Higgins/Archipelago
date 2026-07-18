from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll
from items import EQUIP, SUBWEAPON, LOCATION_ROOM_ID_TO_NAME
from worlds.horde_of_viscount.regions import get_region_set


if TYPE_CHECKING:
    from .world import HoVWorld

StartRoom = 0
MainMenuRoom = 1
TemplateStage1Room = 2
DemoRoom = 3
WorldMapRoom = 4
TutorialRoom = 5
DeadlandRoad1Room = 6
DeadlandRoad2Room = 7
DeadlandRoad3Room = 8
ToxicJungle1Room = 9
ToxicJungle2Room = 10
ToxicJungle3Room = 11
LarvelForest1Room = 12
LarvelForest2Room = 13
LarvelForest3Room = 14
IronRock1Room = 15
IronRock2Room = 16
IronRock3Room = 17
BoneFortRoom = 18
CorruptWoodsRoom = 19
DustyBeach1Room = 20
DustyBeach2Room = 21
DustyBeach3Room = 22
MushroomClouds1Room = 23
MushroomClouds2Room = 24
MushroomClouds3Room = 25
QuenchyDesert1Room = 26
QuenchyDesert2Room = 27
QuenchyDesert3Room = 28
CastleBridgeRoom = 29
CastleFrontBarbicanRoom = 30
EmptyRoom = 31
CastlePortcullisRoom = 32
CastleFoyerRoom = 33
CastleTowerRoom = 34
CastleRampartsRoom = 35
CastleMachicolationsRoom = 36
CastleBattlementsRoom = 37
TownEntranceRoom = 38
TownCenterRoom = 39
TownGateRoom = 40
CrimsonCove1Room = 41
CrimsonCove2Room = 42
CrimsonCove3Room = 43
CastleKitchenRoom = 44
CastleSaveRoom = 45
CastleHiddenStorageRoom = 46
CastleRearTowerRoom = 47
CastleThroneRoom = 48
VolcanoFootRoom = 49
VolcanoTemplateDARKRoom = 50
VolcanoCaveEntranceRoom = 51
VolcanoEntrywayRoom = 52
VolcanoVeinRoom = 53
VolcanoThroatRoom = 54
VolcanoSideVentRoom = 55
VolcanoVentRoom = 56
VolcanoCampsiteRoom = 57
VolcanoTemplateLIGHTRoom = 58
VolcanoTopSideRoom = 59
VolcanoSideSideRoom = 60
VolcanoSideBottomRoom = 61
VolcanoEastSpaceRoom = 62
VolcanoEastFootRoom = 63
VolcanoEastSpace2Room = 64
VolcanoEastSpace3Room = 65
VolcanoFootCampRoom = 66
VolcanoMansionGateRoom = 67
ViscountManorHubRoom = 68
TestStageRoom = 69
FoeTestRoom = 70
AbandonEntranceRoom = 71
AbandonWestPoorRoom = 72
AbandonCenterPoorRoom = 73
AbandonEastPoorRoom = 74
AbandonWestRichRoom = 75
AbandonCenterRichRoom = 76
AbandonEastRichRoom = 77
AbandonWestSkyRoom = 78
AbandonExitRoom = 79
AbandonEastSkyRoom = 80
AbandonWestDrainRoom = 81
AbandonTunnelRoom = 82
AbandonDropRoom = 83
AbandonHiddenRoom = 84
AbandonSewerRoom = 85
AbandonNestRoom = 86
CastleHiddenHiddenRoom = 87
CastleColumnRoom = 88
CastleDropRoom = 89
CastleTopRampartsRoom = 90
CastleSkyRoom = 91
VolcanoLavaFallTopRoom = 92
VolcanoLavaFallCenterRoom = 93
VolcanoLavaFallBottomRoom = 94
VolcanoLeftCornerRoom = 95
VolcanoPlatformRoom = 96
VolcanoTopTopEntranceRoom = 97
VolcanoTopOpenRoom = 98
VolcanoTopHoleRoom = 99
VolcanoCraterRoom = 100
VolcanoOpenRoom = 101
VolcanoCaveTopEntranceRoom = 102
VolcanoDrainRoom = 103
VolcanoCraterExitRoom = 104
VolcanoCraterUnderRoom = 105
VolcanoHop1Room = 106
VolcanoHop2Room = 107
VolcanoHop3Room = 108
VolcanoHop4Room = 109
VolcanoRainBottomRoom = 110
VolcanoRainCenterRoom = 111
VolcanoRainPegRoom = 112
CliffZemplateLightRoom = 113
CliffZemplateDarkRoom = 114
CliffEntranceRoom = 115
CliffSideWallRoom = 116
CliffSideEntranceRoom = 117
CliffSkyWestTopSkyRoom = 118
CliffTopsideLeftRoom = 119
CliffTopsideMiddleRoom = 120
CliffTopsideRightRoom = 121
CliffSkyTopRightRoom = 122
CliffBossEntranceRoom = 123
CliffBossRoom = 124
CliffUnderpassRoom = 125
CliffUnderEntranceRoom = 126
CliffSmallUnderpassRoom = 127
CliffSpikeRoom = 128
CliffFreeBossRightHitRoom = 129
CliffPegBreakRoom = 130
CliffSaveRoom = 131
CliffElevatorRoom = 132
CliffHiddenRoom = 133
CliffFreeBossLeftHitRoom = 134
CliffHideLeftRoom = 135
CliffHideMiddleRoom = 136
CliffHideUnderRoom = 137
CliffHideRightRoom = 138
CliffHideTopRoom = 139
CliffMiddleExitRoom = 140
CliffRightExitRoom = 141
StormCloudCrater1Room = 142
StormCloudCrater2Room = 143
StormCloudCrater3Room = 144
RogueHubRoom = 145
ManorEntranceRoom = 146
ManorIntroFight2Room = 147
ManorRightPrePuzzleRoom = 148
ManorCenterPrePuzzleRoom = 149
ManorTopRightHiddenRoom = 150
ManorLearnRoom = 151
ManorHiddenRoom = 152
ManorLeftPuzzleRoom = 153
ManorCapsuleTopDropRoom = 154
ManorAroundTop7Room = 155
ManorBossExitRoom = 156
ManorExitRoom = 157
ManorBottomRightDropRoom = 158
ManorCapsuleEntranceRoom = 159
ManorBallHiddenRoom = 160
ManorBlock1Room = 161
ManorHubUnderRoom = 162
ManorAroundTop1Room = 163
ManorAroundTop2Room = 164
ManorAroundTop3Room = 165
ManorAroundTop4Room = 166
ManorAroundTop5Room = 167
ManorAroundTop6Room = 168
ManorHiddenBottomRoom = 169
ManorHiddenBottom2Room = 170
ManorBottomCapsuleRoom = 171
ManorBall2Room = 172
ManorBlock3Room = 173
ManorPathTopRoom = 174
ManorPathHiddenRoom = 175
ManorBlock2Room = 176
ManorCenterPuzzleRoom = 177
ManorRightPuzzleRoom = 178
ManorBottomRightHiddenRoom = 179
ManorLeftPrePuzzleRoom = 180
ManorBall4Room = 181
ManorPathBottomRoom = 182
ManorBall1Room = 183
ManorHiddenBottom3Room = 184
ManorBossRushRoom = 185
ManorTopCapsuleRoom = 186
ManorMiddle1CapsuleRoom = 187
ManorMiddle2CapsuleRoom = 188
ManorMiddle3CapsuleRoom = 189
ManorBall3Room = 190
ManorIntroFightRoom = 191
ManorPathCenterRoom = 192
ManorAroundBottomRoom = 193
ManorAroundMiddleRoom = 194
LabViscountRoom = 195
LabMutatedViscountRoom = 196
LabLashaRoom = 197
LabCreditsEntranceRoom = 198
Knife1PuzzleRoom = 199
Knife2PuzzleRoom = 200
Knife3PuzzleRoom = 201
Caltrop1PuzzleRoom = 202
ZTemplatePuzzleRoom = 203
Caltrop2PuzzleRoom = 204
Caltrop3PuzzleRoom = 205
Axe1PuzzleRoom = 206
Axe2PuzzleRoom = 207
Axe3PuzzleRoom = 208
Cleat1PuzzleRoom = 209
Cleat2PuzzleRoom = 210
Cleat3PuzzleRoom = 211
Bomb1PuzzleRoom = 212
Bomb2PuzzleRoom = 213
Bomb3PuzzleRoom = 214
Wing1PuzzleRoom = 215
Wing2PuzzleRoom = 216
Wing3PuzzleRoom = 217
Deadland2PuzzleRoom = 218
Deadland3PuzzleRoom = 219
Deadland1PuzzleRoom = 220
SplashScreenDevRoom = 221
SplashScreenMusicRoom = 222
ControlSetRoom = 223
AmonStageRoom = 224
HixiStageRoom = 225
CampfireRoom = 226
CreditsParentRoom = 227
TutorialV2Room = 228
UpExitRoom = 229
RightExitRoom = 230
LeftExitRoom = 231
DownExitRoom = 232
UpLeftExitRoom = 233
UpRightExitRoom = 234
DownRightExitRoom = 235
DownLeftExitRoom = 236
AllButLeftExitRoom = 237
AllButUpExitRoom = 238
AllButRightExitRoom = 239
AllButDownExitRoom = 240
AllExitRoom = 241
LeftRightExitRoom = 242
UpDownExitRoom = 243


LOCATION_ROOM_ID_LIST = [
	StartRoom,
	MainMenuRoom,
	TemplateStage1Room,
	DemoRoom,
	WorldMapRoom,
	TutorialRoom,
	DeadlandRoad1Room,
	DeadlandRoad2Room,
	DeadlandRoad3Room,
	ToxicJungle1Room,
	ToxicJungle2Room,
	ToxicJungle3Room,
	LarvelForest1Room,
	LarvelForest2Room,
	LarvelForest3Room,
	IronRock1Room,
	IronRock2Room,
	IronRock3Room,
	BoneFortRoom,
	CorruptWoodsRoom,
	DustyBeach1Room,
	DustyBeach2Room,
	DustyBeach3Room,
	MushroomClouds1Room,
	MushroomClouds2Room,
	MushroomClouds3Room,
	QuenchyDesert1Room,
	QuenchyDesert2Room,
	QuenchyDesert3Room,
	CastleBridgeRoom,
	CastleFrontBarbicanRoom,
	EmptyRoom,
	CastlePortcullisRoom,
	CastleFoyerRoom,
	CastleTowerRoom,
	CastleRampartsRoom,
	CastleMachicolationsRoom,
	CastleBattlementsRoom,
	TownEntranceRoom,
	TownCenterRoom,
	TownGateRoom,
	CrimsonCove1Room,
	CrimsonCove2Room,
	CrimsonCove3Room,
	CastleKitchenRoom,
	CastleSaveRoom,
	CastleHiddenStorageRoom,
	CastleRearTowerRoom,
	CastleThroneRoom,
	VolcanoFootRoom,
	VolcanoTemplateDARKRoom,
	VolcanoCaveEntranceRoom,
	VolcanoEntrywayRoom,
	VolcanoVeinRoom,
	VolcanoThroatRoom,
	VolcanoSideVentRoom,
	VolcanoVentRoom,
	VolcanoCampsiteRoom,
	VolcanoTemplateLIGHTRoom,
	VolcanoTopSideRoom,
	VolcanoSideSideRoom,
	VolcanoSideBottomRoom,
	VolcanoEastSpaceRoom,
	VolcanoEastFootRoom,
	VolcanoEastSpace2Room,
	VolcanoEastSpace3Room,
	VolcanoFootCampRoom,
	VolcanoMansionGateRoom,
	ViscountManorHubRoom,
	TestStageRoom,
	FoeTestRoom,
	AbandonEntranceRoom,
	AbandonWestPoorRoom,
	AbandonCenterPoorRoom,
	AbandonEastPoorRoom,
	AbandonWestRichRoom,
	AbandonCenterRichRoom,
	AbandonEastRichRoom,
	AbandonWestSkyRoom,
	AbandonExitRoom,
	AbandonEastSkyRoom,
	AbandonWestDrainRoom,
	AbandonTunnelRoom,
	AbandonDropRoom,
	AbandonHiddenRoom,
	AbandonSewerRoom,
	AbandonNestRoom,
	CastleHiddenHiddenRoom,
	CastleColumnRoom,
	CastleDropRoom,
	CastleTopRampartsRoom,
	CastleSkyRoom,
	VolcanoLavaFallTopRoom,
	VolcanoLavaFallCenterRoom,
	VolcanoLavaFallBottomRoom,
	VolcanoLeftCornerRoom,
	VolcanoPlatformRoom,
	VolcanoTopTopEntranceRoom,
	VolcanoTopOpenRoom,
	VolcanoTopHoleRoom,
	VolcanoCraterRoom,
	VolcanoOpenRoom,
	VolcanoCaveTopEntranceRoom,
	VolcanoDrainRoom,
	VolcanoCraterExitRoom,
	VolcanoCraterUnderRoom,
	VolcanoHop1Room,
	VolcanoHop2Room,
	VolcanoHop3Room,
	VolcanoHop4Room,
	VolcanoRainBottomRoom,
	VolcanoRainCenterRoom,
	VolcanoRainPegRoom,
	CliffZemplateLightRoom,
	CliffZemplateDarkRoom,
	CliffEntranceRoom,
	CliffSideWallRoom,
	CliffSideEntranceRoom,
	CliffSkyWestTopSkyRoom,
	CliffTopsideLeftRoom,
	CliffTopsideMiddleRoom,
	CliffTopsideRightRoom,
	CliffSkyTopRightRoom,
	CliffBossEntranceRoom,
	CliffBossRoom,
	CliffUnderpassRoom,
	CliffUnderEntranceRoom,
	CliffSmallUnderpassRoom,
	CliffSpikeRoom,
	CliffFreeBossRightHitRoom,
	CliffPegBreakRoom,
	CliffSaveRoom,
	CliffElevatorRoom,
	CliffHiddenRoom,
	CliffFreeBossLeftHitRoom,
	CliffHideLeftRoom,
	CliffHideMiddleRoom,
	CliffHideUnderRoom,
	CliffHideRightRoom,
	CliffHideTopRoom,
	CliffMiddleExitRoom,
	CliffRightExitRoom,
	StormCloudCrater1Room,
	StormCloudCrater2Room,
	StormCloudCrater3Room,
	RogueHubRoom,
	ManorEntranceRoom,
	ManorIntroFight2Room,
	ManorRightPrePuzzleRoom,
	ManorCenterPrePuzzleRoom,
	ManorTopRightHiddenRoom,
	ManorLearnRoom,
	ManorHiddenRoom,
	ManorLeftPuzzleRoom,
	ManorCapsuleTopDropRoom,
	ManorAroundTop7Room,
	ManorBossExitRoom,
	ManorExitRoom,
	ManorBottomRightDropRoom,
	ManorCapsuleEntranceRoom,
	ManorBallHiddenRoom,
	ManorBlock1Room,
	ManorHubUnderRoom,
	ManorAroundTop1Room,
	ManorAroundTop2Room,
	ManorAroundTop3Room,
	ManorAroundTop4Room,
	ManorAroundTop5Room,
	ManorAroundTop6Room,
	ManorHiddenBottomRoom,
	ManorHiddenBottom2Room,
	ManorBottomCapsuleRoom,
	ManorBall2Room,
	ManorBlock3Room,
	ManorPathTopRoom,
	ManorPathHiddenRoom,
	ManorBlock2Room,
	ManorCenterPuzzleRoom,
	ManorRightPuzzleRoom,
	ManorBottomRightHiddenRoom,
	ManorLeftPrePuzzleRoom,
	ManorBall4Room,
	ManorPathBottomRoom,
	ManorBall1Room,
	ManorHiddenBottom3Room,
	ManorBossRushRoom,
	ManorTopCapsuleRoom,
	ManorMiddle1CapsuleRoom,
	ManorMiddle2CapsuleRoom,
	ManorMiddle3CapsuleRoom,
	ManorBall3Room,
	ManorIntroFightRoom,
	ManorPathCenterRoom,
	ManorAroundBottomRoom,
	ManorAroundMiddleRoom,
	LabViscountRoom,
	LabMutatedViscountRoom,
	LabLashaRoom,
	LabCreditsEntranceRoom,
	Knife1PuzzleRoom,
	Knife2PuzzleRoom,
	Knife3PuzzleRoom,
	Caltrop1PuzzleRoom,
	ZTemplatePuzzleRoom,
	Caltrop2PuzzleRoom,
	Caltrop3PuzzleRoom,
	Axe1PuzzleRoom,
	Axe2PuzzleRoom,
	Axe3PuzzleRoom,
	Cleat1PuzzleRoom,
	Cleat2PuzzleRoom,
	Cleat3PuzzleRoom,
	Bomb1PuzzleRoom,
	Bomb2PuzzleRoom,
	Bomb3PuzzleRoom,
	Wing1PuzzleRoom,
	Wing2PuzzleRoom,
	Wing3PuzzleRoom,
	Deadland2PuzzleRoom,
	Deadland3PuzzleRoom,
	Deadland1PuzzleRoom,
	SplashScreenDevRoom,
	SplashScreenMusicRoom,
	ControlSetRoom,
	AmonStageRoom,
	HixiStageRoom,
	CampfireRoom,
	CreditsParentRoom,
	TutorialV2Room,
	UpExitRoom,
	RightExitRoom,
	LeftExitRoom,
	DownExitRoom,
	UpLeftExitRoom,
	UpRightExitRoom,
	DownRightExitRoom,
	DownLeftExitRoom,
	AllButLeftExitRoom,
	AllButUpExitRoom,
	AllButRightExitRoom,
	AllButDownExitRoom,
	AllExitRoom,
	LeftRightExitRoom,
	UpDownExitRoom,
]


def set_all_rules(world: HoVWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


class RoomMetadata:
    def __init__(roomId = None, firstRoomId = None, worldMapId = None, soundID = None, isStageRoom = True, isSaveRoom = False, 
                 isBossRoom = False, isRandomizerRoom = True, isPuzzleRoom = False, maxLoot = 0, isChestBreakRequired = False,
                 subweaponsRequireAll = False, isFillerRoom = False):
        roomId = roomId
        firstRoomId = firstRoomId
        worldMapId = worldMapId
        soundId = soundID
        isStageRoom = isStageRoom
        isSaveRoom = isSaveRoom
        isBossRoom = isBossRoom
        isRandomizerRoom = isRandomizerRoom
        isDependant = False
        dependRoom = EmptyRoom
        subweaponRequiredList = []
        isPuzzleRoom = isPuzzleRoom
        maxLoot = maxLoot
        isChestBreakRequired = isChestBreakRequired
        subweaponsRequireAll = subweaponsRequireAll
        isFillerRoom = isFillerRoom
        northSubweaponRequiredList = []

def set_all_location_rules(world: HoVWorld) -> None:
    
    # Pasted logic from built in game randomizer.
    roomMetadata = [RoomMetadata() for _ in range(len(LOCATION_ROOM_ID_LIST))]

    roomMetadata[WorldMapRoom] = RoomMetadata(WorldMapRoom, WorldMapRoom, WorldMapRoom, None, False, True, False, False)
    roomMetadata[TutorialRoom] = RoomMetadata(TutorialRoom, DeadlandRoad1Room, WorldMapRoom, None, True, False, False, False)
    roomMetadata[TutorialV2Room] = RoomMetadata(TutorialV2Room, DeadlandRoad1Room, WorldMapRoom, None, True, False, False, False)
    roomMetadata[TestStageRoom] = RoomMetadata(TestStageRoom, TestStageRoom, WorldMapRoom, None, True, False, False, False)
    roomMetadata[TemplateStage1Room] = RoomMetadata(TemplateStage1Room, WorldMapRoom, WorldMapRoom, None, True, False, False, False)
    roomMetadata[DemoRoom] =  RoomMetadata(DemoRoom, WorldMapRoom, WorldMapRoom, None, True, False, False, False)
    roomMetadata[VolcanoTemplateDARKRoom] =  RoomMetadata(VolcanoTemplateDARKRoom, WorldMapRoom, WorldMapRoom, None, True, False, False, False)
    roomMetadata[VolcanoTemplateLIGHTRoom] =  RoomMetadata(VolcanoTemplateLIGHTRoom, WorldMapRoom, WorldMapRoom, None, True, False, False, False)
    roomMetadata[CliffZemplateDarkRoom] =  RoomMetadata(CliffZemplateDarkRoom, WorldMapRoom, WorldMapRoom, None, True, False, False, False)
    roomMetadata[CliffZemplateLightRoom] =  RoomMetadata(CliffZemplateLightRoom, WorldMapRoom, WorldMapRoom, None, True, False, False, False)
    roomMetadata[EmptyRoom] =  RoomMetadata(EmptyRoom, WorldMapRoom, WorldMapRoom, None, True, False, False, False)

    roomMetadata[CorruptWoodsRoom] = RoomMetadata(CorruptWoodsRoom, CorruptWoodsRoom, WorldMapRoom, None, True, False, True, False)
    roomMetadata[BoneFortRoom] = RoomMetadata(BoneFortRoom, BoneFortRoom, WorldMapRoom, None, True, False, True, False)
    roomMetadata[AmonStageRoom] =  RoomMetadata(AmonStageRoom, AmonStageRoom, WorldMapRoom, None, True, False, True, False)
    roomMetadata[AmonStageRoom].isPuzzleRoom = True
    roomMetadata[AmonStageRoom].maxLoot = 1
    roomMetadata[HixiStageRoom] =  RoomMetadata(HixiStageRoom, HixiStageRoom, WorldMapRoom, None, True, False, True, False)
    roomMetadata[AmonStageRoom].isPuzzleRoom = True
    roomMetadata[HixiStageRoom].maxLoot = 1

    roomMetadata[ViscountManorHubRoom] =  RoomMetadata(ViscountManorHubRoom, ViscountManorHubRoom, ViscountManorHubRoom, None, False, True, False, False)
    roomMetadata[RogueHubRoom] =  RoomMetadata(RogueHubRoom, RogueHubRoom, RogueHubRoom, None, False, False, False, False)
    roomMetadata[CampfireRoom] =  RoomMetadata(CampfireRoom, CampfireRoom, WorldMapRoom, None, False, True, False, False)
    roomMetadata[CreditsParentRoom] =  RoomMetadata(CreditsParentRoom, CreditsParentRoom, LabCreditsEntranceRoom, None, False, False, False, False)

    WORLD_ID = {
        "WORLD_MAP": 0,
        "ABANDONED_TOWN": 1,
        "CLIFFSIDE_CLIMB": 2,
        "KINGDOM_CASTLE_TOWN": 3,
        "KINGDOM_CASTLE": 4,
        "TEPID_VOLCANO": 5,
        "MISTIQUE_MINES": 6,
        "VISCOUNT_MANOR": 7,
        "VISCOUNT_LABS": 8
    }

    # All of viscount manor, by default, will require at least 1 of these 3 subweapons.
    for roomId in [ 
        ManorEntranceRoom, ManorIntroFight2Room, ManorRightPrePuzzleRoom, ManorCenterPrePuzzleRoom, ManorTopRightHiddenRoom, 
        ManorLearnRoom, ManorHiddenRoom, ManorLeftPuzzleRoom, ManorCapsuleTopDropRoom, ManorAroundTop7Room,
        ManorBossExitRoom, ManorExitRoom, ManorBottomRightDropRoom, ManorCapsuleEntranceRoom, ManorBallHiddenRoom,
        ManorBlock1Room, ManorHubUnderRoom, ManorAroundTop1Room, ManorAroundTop2Room, ManorAroundTop3Room, ManorAroundTop4Room,
        ManorAroundTop5Room, ManorAroundTop6Room, ManorHiddenBottomRoom, ManorHiddenBottom2Room, ManorBottomCapsuleRoom,
        ManorBall2Room, ManorBlock3Room, ManorPathTopRoom, ManorPathHiddenRoom, ManorBlock2Room, ManorCenterPuzzleRoom,
        ManorRightPuzzleRoom, ManorBottomRightHiddenRoom, ManorLeftPrePuzzleRoom, ManorBall4Room, ManorPathBottomRoom,
        ManorBall1Room, ManorHiddenBottom3Room, ManorBossRushRoom, ManorTopCapsuleRoom, ManorMiddle1CapsuleRoom,
        ManorMiddle2CapsuleRoom, ManorMiddle3CapsuleRoom, ManorBall3Room, ManorIntroFightRoom, ManorPathCenterRoom,
        ManorAroundBottomRoom, ManorAroundMiddleRoom
                   ]:
        roomMetadata[roomId].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.CALTROP, SUBWEAPON.BOMB]
    

    simplePairs = [
        [Knife1PuzzleRoom, None, WorldMapRoom],
        [Knife2PuzzleRoom, None, WorldMapRoom],
        [Knife3PuzzleRoom, None, WorldMapRoom],
        [Caltrop1PuzzleRoom, None, WorldMapRoom],
        [Caltrop2PuzzleRoom, None, WorldMapRoom],
        [Caltrop3PuzzleRoom, None, WorldMapRoom],
        [Axe1PuzzleRoom, None, WorldMapRoom],
        [Axe2PuzzleRoom, None, WorldMapRoom],
        [Axe3PuzzleRoom, None, WorldMapRoom],
        [Cleat1PuzzleRoom, None, WorldMapRoom],
        [Cleat2PuzzleRoom, None, WorldMapRoom],
        [Cleat3PuzzleRoom, None, WorldMapRoom],
        [Bomb1PuzzleRoom, None, VolcanoFootRoom],
        [Bomb2PuzzleRoom, None, VolcanoFootRoom],
        [Bomb3PuzzleRoom, None, VolcanoFootRoom],
        [Wing1PuzzleRoom, None, TownEntranceRoom],
        [Wing2PuzzleRoom, None, TownEntranceRoom],
        [Wing3PuzzleRoom, None, TownEntranceRoom],
    ]
    for pair in simplePairs:
        roomId = pair[0]
        musicId = pair[1]
        worldRoomId = pair[2]
        roomMetadata[roomId] = RoomMetadata(roomId, roomId, worldRoomId, musicId, True, False, False, False, True, 3)
        
    fillerTable = [
            UpExitRoom, RightExitRoom, LeftExitRoom, DownExitRoom, 
            UpLeftExitRoom, UpRightExitRoom, DownRightExitRoom, DownLeftExitRoom, 
            UpDownExitRoom, LeftRightExitRoom, 
            AllButLeftExitRoom, AllButUpExitRoom, AllButRightExitRoom, AllButDownExitRoom, 
            AllExitRoom
       	]
    for roomId in fillerTable:
        roomMetadata[roomId] = RoomMetadata(roomId, roomId, RogueHubRoom, None, False, False, False, True)
        roomMetadata[roomId].isFillerRoom = True
    
    roomMetadata[CliffSaveRoom].isSaveRoom = True
    roomMetadata[TownGateRoom].isSaveRoom = True
    roomMetadata[TownCenterRoom].isSaveRoom = True
    roomMetadata[TownEntranceRoom].isSaveRoom = True
    roomMetadata[CastleSaveRoom].isSaveRoom = True
    roomMetadata[VolcanoFootRoom].isSaveRoom = True
    roomMetadata[VolcanoFootCampRoom].isSaveRoom = True
    roomMetadata[VolcanoCraterRoom].isSaveRoom = True
    roomMetadata[VolcanoCampsiteRoom].isSaveRoom = True
    roomMetadata[ViscountManorHubRoom].isSaveRoom = True
    roomMetadata[ManorHubUnderRoom].isSaveRoom = True
    roomMetadata[ManorBlock1Room].isSaveRoom = True
    roomMetadata[ManorBossExitRoom].isSaveRoom = True
    roomMetadata[LabCreditsEntranceRoom].isSaveRoom = True

    dependantRoomList = [
        [AbandonExitRoom, AbandonEastSkyRoom],
        [CliffBossEntranceRoom, CliffPegBreakRoom],
        [CliffMiddleExitRoom, CliffTopsideMiddleRoom],
        [CastleFoyerRoom, CastleMachicolationsRoom],
        [VolcanoCaveEntranceRoom, VolcanoCaveEntranceRoom],
        [VolcanoEntrywayRoom, VolcanoEntrywayRoom],
        [VolcanoLavaFallCenterRoom, VolcanoLavaFallTopRoom],
        [VolcanoLavaFallBottomRoom, VolcanoLavaFallTopRoom],
        [VolcanoRainPegRoom, VolcanoRainPegRoom],
        [VolcanoRainCenterRoom, VolcanoRainPegRoom],
        [VolcanoRainBottomRoom, VolcanoRainPegRoom],
        [VolcanoCraterUnderRoom, VolcanoCraterExitRoom],
        [ManorBlock1Room, ManorLeftPuzzleRoom],
        [ManorBlock2Room, ManorCenterPuzzleRoom],
        [ManorBlock3Room, ManorRightPuzzleRoom],
        [ManorIntroFight2Room, ManorIntroFight2Room],
        
    ]
    for i in range(len(dependantRoomList)):
        roomId = dependantRoomList[i][0]
        dependRoomId = dependantRoomList[i][1]
        roomMetadata[roomId].isDependant = True
        roomMetadata[roomId].dependRoom = dependRoomId

    doubleJumpRequiredList = [
        AbandonWestDrainRoom, AbandonExitRoom, 
        CastleHiddenStorageRoom, CastleKitchenRoom, CastleBridgeRoom, CastleFrontBarbicanRoom,
        
        CliffHideTopRoom, CliffMiddleExitRoom, CliffSkyWestTopSkyRoom, CliffHideUnderRoom, 
        CliffHideRightRoom, CliffRightExitRoom, CliffPegBreakRoom, CliffFreeBossRightHitRoom,
        CliffSpikeRoom, CliffSmallUnderpassRoom, CliffUnderEntranceRoom, CliffUnderpassRoom, 
        CliffEntranceRoom, CliffHideMiddleRoom, CliffHideLeftRoom, CliffSideEntranceRoom, 
        CliffTopsideLeftRoom, 
        
        VolcanoLavaFallTopRoom, VolcanoLavaFallCenterRoom, VolcanoLavaFallBottomRoom,
        VolcanoFootRoom, VolcanoOpenRoom, VolcanoDrainRoom, VolcanoThroatRoom, VolcanoTopOpenRoom,
        VolcanoPlatformRoom, VolcanoCaveTopEntranceRoom, VolcanoEastFootRoom, VolcanoVeinRoom, 
        VolcanoCraterUnderRoom, VolcanoEastSpaceRoom, VolcanoEastSpace2Room, VolcanoEastSpace3Room, 
        VolcanoCraterExitRoom, VolcanoRainPegRoom,  
        
        StormCloudCrater1Room, 
        StormCloudCrater2Room, StormCloudCrater3Room, ToxicJungle1Room, ToxicJungle3Room, MushroomClouds2Room,
        DustyBeach1Room, DustyBeach2Room, DustyBeach3Room, QuenchyDesert1Room, QuenchyDesert3Room,
        CrimsonCove3Room, StormCloudCrater1Room, StormCloudCrater2Room, StormCloudCrater3Room
    ]
    for i in range(len(doubleJumpRequiredList)):
        roomId = doubleJumpRequiredList[i]
        roomMetadata[roomId].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.CALTROP, SUBWEAPON.BOMB]
    
    cleatAndJumpRequiredList = [
        AbandonSewerRoom, ViscountManorHubRoom, ManorEntranceRoom, 
    ]
    for i in range(len(cleatAndJumpRequiredList)):
        roomId = cleatAndJumpRequiredList[i]
        roomMetadata[roomId].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.CLEATS]
        roomMetadata[roomId].subweaponsRequireAll = True
    
    # TODO - Add all available hardmode tech
    techEnabled = []
    
    roomMetadata[AbandonEntranceRoom].subweaponRequiredList = [SUBWEAPON.KNIFE, SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[AbandonEntranceRoom].subweaponsRequireAll = True
    roomMetadata[AbandonEastPoorRoom].subweaponRequiredList = [SUBWEAPON.KNIFE, SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[AbandonCenterPoorRoom].subweaponRequiredList = [SUBWEAPON.KNIFE, SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[AbandonEastSkyRoom].subweaponRequiredList = [SUBWEAPON.KNIFE, SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CALTROP]
    roomMetadata[AbandonWestPoorRoom].subweaponRequiredList = [SUBWEAPON.KNIFE, SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CALTROP]
    roomMetadata[AbandonWestDrainRoom].subweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[AbandonWestSkyRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.CALTROP]
    roomMetadata[AbandonWestSkyRoom].subweaponsRequireAll = True
    roomMetadata[AbandonTunnelRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.KNIFE]
    roomMetadata[AbandonTunnelRoom].subweaponsRequireAll = True
    roomMetadata[AbandonTunnelRoom].isChestBreakRequired = True
    roomMetadata[AbandonNestRoom].subweaponRequiredList = [SUBWEAPON.BOMB]
    
    roomMetadata[CastleHiddenHiddenRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP, SUBWEAPON.AXE]
    roomMetadata[CastleKitchenRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CastleRearTowerRoom].subweaponRequiredList = [SUBWEAPON.AXE, SUBWEAPON.BOMB, SUBWEAPON.CALTROP, SUBWEAPON.WINGS]
    roomMetadata[CastleDropRoom].subweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[CastleTopRampartsRoom].subweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[CastleMachicolationsRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.CLEATS, SUBWEAPON.KNIFE]
    roomMetadata[CastleMachicolationsRoom].subweaponsRequireAll = True
    roomMetadata[CastleMachicolationsRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CastleBridgeRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CALTROP]
    roomMetadata[CastleFrontBarbicanRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CALTROP]
    roomMetadata[CastlePortcullisRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP, SUBWEAPON.AXE]
    roomMetadata[CastleRampartsRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    if "CastleRampartsRoom Axe" in techEnabled:
        roomMetadata[CastleRampartsRoom].northSubweaponRequiredList.append(SUBWEAPON.AXE)
    
    roomMetadata[CastleBattlementsRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CastleFoyerRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CastleHiddenStorageRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB]
    roomMetadata[CastleColumnRoom].subweaponRequiredList = [SUBWEAPON.BOMB]

        
    roomMetadata[CliffElevatorRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    if "CliffElevatorRoom Axe" in techEnabled:
        roomMetadata[CliffElevatorRoom].subweaponRequiredList.append(SUBWEAPON.AXE)

    roomMetadata[CliffTopsideRightRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.KNIFE, SUBWEAPON.CALTROP, SUBWEAPON.CLEATS]
    roomMetadata[CliffSideEntranceRoom].subweaponRequiredList = [SUBWEAPON.KNIFE, SUBWEAPON.CALTROP]
    roomMetadata[CliffHiddenRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.CALTROP, SUBWEAPON.BOMB]
    roomMetadata[CliffHideTopRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CliffSideWallRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CliffSideEntranceRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.KNIFE, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CliffHideMiddleRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.AXE]
    roomMetadata[CliffHideMiddleRoom].subweaponsRequireAll = True
    roomMetadata[CliffEntranceRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[CliffSideWallRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[CliffSideEntranceRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[CliffFreeBossLeftHitRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[CliffUnderEntranceRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[CliffHideLeftRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.AXE]
    roomMetadata[CliffHideLeftRoom].subweaponsRequireAll = True
    roomMetadata[CliffMiddleExitRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]

    roomMetadata[CliffSmallUnderpassRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.KNIFE]
    roomMetadata[CliffSmallUnderpassRoom].subweaponsRequireAll = True
    if "CliffSmallUnderpassRoom Caltrop" in techEnabled:
        roomMetadata[CliffSmallUnderpassRoom].subweaponRequiredList = [SUBWEAPON.CALTROP]
        roomMetadata[CliffSmallUnderpassRoom].subweaponsRequireAll = False    
    roomMetadata[CliffSmallUnderpassRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]

    roomMetadata[CliffHideUnderRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CliffSpikeRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CliffHideRightRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.AXE]
    roomMetadata[CliffHideRightRoom].subweaponsRequireAll = True
    roomMetadata[CliffRightExitRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[CliffFreeBossRightHitRoom].northSubweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    
    roomMetadata[VolcanoTopTopEntranceRoom].subweaponRequiredList = [SUBWEAPON.AXE, SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    
    roomMetadata[VolcanoHop1Room].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.KNIFE, SUBWEAPON.CALTROP, SUBWEAPON.CLEATS]
    roomMetadata[VolcanoHop2Room].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.KNIFE, SUBWEAPON.CALTROP, SUBWEAPON.CLEATS]
    roomMetadata[VolcanoHop3Room].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.KNIFE, SUBWEAPON.CALTROP, SUBWEAPON.CLEATS]
    roomMetadata[VolcanoHop4Room].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.KNIFE, SUBWEAPON.CALTROP, SUBWEAPON.CLEATS]
    if "VolcanoHop Rooms Damage Boost" in techEnabled:
        roomMetadata[VolcanoHop1Room].subweaponRequiredList = []
        roomMetadata[VolcanoHop2Room].subweaponRequiredList = []
        roomMetadata[VolcanoHop3Room].subweaponRequiredList = []
        roomMetadata[VolcanoHop4Room].subweaponRequiredList = []
    
     
    roomMetadata[VolcanoOpenRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.CALTROP]
    if "VolcanoOpenRoom Damage Boost" in techEnabled:
        roomMetadata[VolcanoHop4Room].subweaponRequiredList = [SUBWEAPON.KNIFE]
    
    roomMetadata[VolcanoDrainRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.KNIFE, SUBWEAPON.CLEATS]
    roomMetadata[VolcanoDrainRoom].subweaponsRequireAll = True
    roomMetadata[VolcanoSideSideRoom].subweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[VolcanoSideVentRoom].subweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[VolcanoSideBottomRoom].subweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[VolcanoTopSideRoom].subweaponRequiredList = [SUBWEAPON.KNIFE, SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[VolcanoTopSideRoom].subweaponRequiredList = [SUBWEAPON.KNIFE, SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[VolcanoTopSideRoom].subweaponsRequireAll = True
    roomMetadata[VolcanoThroatRoom].subweaponRequiredList = [SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[VolcanoLeftCornerRoom].subweaponRequiredList = [SUBWEAPON.CALTROP, SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[VolcanoLeftCornerRoom].subweaponsRequireAll = True
    roomMetadata[VolcanoTopHoleRoom].subweaponRequiredList = [SUBWEAPON.AXE, SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CALTROP]
    roomMetadata[VolcanoEastFootRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[VolcanoSideBottomRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[VolcanoSideVentRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[VolcanoThroatRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[VolcanoSideSideRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[VolcanoCraterUnderRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CALTROP]
    
    roomMetadata[ManorCapsuleTopDropRoom].subweaponRequiredList = [SUBWEAPON.AXE]
    roomMetadata[ManorAroundMiddleRoom].subweaponRequiredList = [SUBWEAPON.AXE, SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CALTROP]
    roomMetadata[ManorAroundMiddleRoom].subweaponsRequireAll = True
    roomMetadata[ManorHiddenBottomRoom].subweaponRequiredList = [SUBWEAPON.KNIFE, SUBWEAPON.WINGS]
    roomMetadata[ManorHiddenBottomRoom].subweaponsRequireAll = True
    roomMetadata[ManorHiddenBottom2Room].subweaponRequiredList = [SUBWEAPON.AXE, SUBWEAPON.CALTROP]
    roomMetadata[ManorHiddenBottom2Room].subweaponsRequireAll = True
    roomMetadata[ManorHiddenBottom3Room].subweaponRequiredList = [SUBWEAPON.CLEATS, SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[ManorHiddenBottom3Room].subweaponsRequireAll = True
    roomMetadata[ManorIntroFightRoom].subweaponRequiredList = [SUBWEAPON.WINGS, SUBWEAPON.KNIFE, SUBWEAPON.CALTROP]
    roomMetadata[ManorIntroFightRoom].subweaponsRequireAll = True
    roomMetadata[ManorIntroFight2Room].isRandomizerRoom = False
    roomMetadata[ManorLearnRoom].subweaponRequiredList = [SUBWEAPON.CLEATS]
    roomMetadata[ManorTopRightHiddenRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB, SUBWEAPON.WINGS]
    roomMetadata[ManorRightPrePuzzleRoom].northSubweaponRequiredList = [SUBWEAPON.BOMB]
    
    
    roomMetadata[DeadlandRoad1Room].subweaponRequiredList = [SUBWEAPON.KNIFE]
    roomMetadata[DeadlandRoad2Room].subweaponRequiredList = [SUBWEAPON.KNIFE]
    roomMetadata[DeadlandRoad3Room].subweaponRequiredList = [SUBWEAPON.KNIFE]
    if "DeadlandRoad Rooms Damage Boost" in techEnabled:
        roomMetadata[DeadlandRoad1Room].subweaponRequiredList = []
        roomMetadata[DeadlandRoad2Room].subweaponRequiredList = []
        roomMetadata[DeadlandRoad3Room].subweaponRequiredList = []
    
    
    roomMetadata[LarvelForest1Room].subweaponRequiredList = [SUBWEAPON.KNIFE]
    roomMetadata[LarvelForest2Room].subweaponRequiredList = [SUBWEAPON.BOMB]
    roomMetadata[LarvelForest3Room].subweaponRequiredList = [SUBWEAPON.KNIFE]
    roomMetadata[IronRock1Room].subweaponRequiredList = [SUBWEAPON.BOMB, SUBWEAPON.CALTROP]
    roomMetadata[ToxicJungle2Room].subweaponRequiredList = [SUBWEAPON.AXE, SUBWEAPON.WINGS]
    roomMetadata[QuenchyDesert2Room].subweaponRequiredList = [SUBWEAPON.BOMB]
    
    chestBreakerList = [
        AbandonCenterRichRoom, AbandonEastRichRoom, AbandonWestRichRoom, ManorExitRoom, LabCreditsEntranceRoom, 
        ManorBallHiddenRoom, ManorRightPrePuzzleRoom, ManorCenterPrePuzzleRoom
    ]
    for i in range(len(chestBreakerList)):
        roomId = chestBreakerList[i]
        roomMetadata[roomId].isChestBreakRequired = True

    roomMetadata[VolcanoRainPegRoom].isRandomizerRoom = False
        
    # Now apply the game map rando logic rules into AP rules
    for roomMetadataItem in roomMetadata:
        
        # Iterate through each room ID and set the rules for the corresponding locations in the world.
        locationList = LOCATION_ROOM_ID_TO_NAME[roomMetadataItem.roomId]
        for locationName in locationList:
            location = world.get_location(locationName)

            # If the room has a dependency, we need to set a rule on the location that requires the player to be able to reach the dependent room's locations.
            if roomMetadataItem.isDependant:
                dependantLocationList = LOCATION_ROOM_ID_TO_NAME[roomMetadataItem.dependRoom]
                for dependLocationName in dependantLocationList:
                    dependLocation = world.get_location(dependLocationName)
                    world.set_rule(location, lambda state: state.can_reach_location(dependLocation.name, world.player))

            # If the room has subweapon requirements, we need to set a rule on the location that requires the player to have the required subweapons.
            if len(roomMetadataItem.subweaponRequiredList) > 0:
                if roomMetadataItem.subweaponsRequireAll:
                    subweaponRule = HasAll(*[SUBWEAPON[subweapon] for subweapon in roomMetadataItem.subweaponRequiredList])
                else:
                    subweaponRule = Has(roomMetadataItem.subweaponRequiredList[0])
                    for subweapon in roomMetadataItem.subweaponRequiredList[1:]:
                        subweaponRule = subweaponRule | Has(SUBWEAPON[subweapon])
                world.set_rule(location, subweaponRule)

            # The north exit of a room has special rules for subweapons
            if len(roomMetadataItem.northSubweaponRequiredList) > 0:
                northSubweaponRule = Has(*[SUBWEAPON[subweapon] for subweapon in roomMetadataItem.northSubweaponRequiredList])
                for subweapon in roomMetadataItem.northSubweaponRequiredList[1:]:
                    northSubweaponRule = northSubweaponRule | Has(SUBWEAPON[subweapon])
                # TODO add North Exit Rules
                # I can bring the castle maps matrix in and have it reference it as the ENTRANCE to the upper one.
                #world.set_rule(location, northSubweaponRule)

            # Some rooms have floating chests, which can only be opened by equipping the Chest Breaker EQUIP
            if roomMetadataItem.isChestBreakRequired:
                chestBreakRule = Has(EQUIP["CHEST_BREAKER"])
                world.set_rule(location, chestBreakRule)


def set_completion_condition(world: HoVWorld) -> None:
    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.set_completion_rule( world.get_location("Credits Peak Event"))


# One final comment about rules:
# If your world exclusively uses Rule Builder rules (like APQuest), it's worth trying CachedRuleBuilderWorld.
# CachedRuleBuilderWorld is a subclass of World that has a bunch of caching magic to make rules faster.
# Just have your world class subclass CachedRuleBuilderWorld instead of World:
#   class APQuestWorld(CachedRuleBuilderWorld): ...
# This may speed up your world, or it may make it slower.
# The exact factors are complex and not well understood, but there is no harm in trying it.
# Generate a few seeds and see if there is a noticeable difference!
# If you're wondering, author has checked: APQuest is too simple to see any benefits, so we'll stick with "World".
