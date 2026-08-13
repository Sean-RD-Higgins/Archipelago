from worlds.horde_of_viscount.items import EQUIP, SUBWEAPON
from worlds.horde_of_viscount.locations import LOCATION_DATA_LIST
from worlds.horde_of_viscount.options import Ending, HoVOptions
from worlds.horde_of_viscount.rules import AbandonHiddenRoom, AbandonWestDrainRoom, CastleColumnRoom, CastlePortcullisRoom, CastleTopRampartsRoom, IronRock2Room, IronRock3Room, VolcanoOpenRoom

from .bases import HoVTestBase

class TestEndingLogic(HoVTestBase):
    options: HoVOptions = {
        "level_up_progression": 100,
        "ending": Ending(0).option_C
    }

    def test_easy_mode_access(self) -> None:
        with self.subTest("Test checks accessible with nothing"):

            IronRock2Room_chest = self.world.get_location(
                next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == IronRock2Room)
            )
            IronRock3Room_chest = self.world.get_location(
                next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == IronRock3Room)
            )

            self.assertTrue(IronRock2Room_chest.can_reach(self.multiworld.state))
            self.assertTrue(IronRock3Room_chest.can_reach(self.multiworld.state))

            AbandonHiddenRoom_chest = self.world.get_location(
                next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == AbandonHiddenRoom)
            )
            CastlePortcullisRoom_chest = self.world.get_location(
                next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == CastlePortcullisRoom)
            )

            self.assertFalse(AbandonHiddenRoom_chest.can_reach(self.multiworld.state))
            self.assertFalse(CastlePortcullisRoom_chest.can_reach(self.multiworld.state))

        with self.subTest("Test Jump Wing is required to get VolcanoOpenRoom chest"):
            VolcanoOpenRoom_chest = self.world.get_location(
                next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == VolcanoOpenRoom)
            )

            # Right now, this location should *not* be accessible, as we don't have the wings yet.
            self.assertFalse(VolcanoOpenRoom_chest.can_reach(self.multiworld.state))

            # Now, let's collect the wings.
            # For this, there is a handy helper function to collect items from the itempool.
            # Keep in mind that while test functions are sectioned off from one another, subtests are not.
            # Collecting this here means that the state will have the Wings for all future subtests in this function.
            self.collect_by_name(SUBWEAPON.WINGS)
            self.collect_by_name(EQUIP.WINGS_ONE_FREE)

            # The chest should now be accessible.
            self.assertTrue(VolcanoOpenRoom_chest.can_reach(self.multiworld.state))

        with self.subTest("Ending requirement does not change Launch Bomb is required for some castle and abandon town areas."):
            for optionValue in [Ending(0).option_A, Ending(0).option_B, Ending(0).option_C, Ending(0).option_D]:
                self.options["ending"] = optionValue
                self.assertAccessDependency(
                    [
                        next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == CastleTopRampartsRoom),
                        next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == AbandonWestDrainRoom),
                        next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == CastleColumnRoom)
                    ],
                    [[SUBWEAPON.BOMB]],
                    only_check_listed=True,
                )