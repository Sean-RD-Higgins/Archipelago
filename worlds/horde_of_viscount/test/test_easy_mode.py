from worlds.horde_of_viscount.items import EQUIP, SUBWEAPON
from worlds.horde_of_viscount.locations import LOCATION_DATA_LIST
from worlds.horde_of_viscount.options import HoVOptions
from worlds.horde_of_viscount.rules import AbandonHiddenRoom, AbandonWestDrainRoom, CastleColumnRoom, CastlePortcullisRoom, CastleTopRampartsRoom, IronRock2Room, IronRock3Room, VolcanoOpenRoom

from .bases import HoVTestBase


# When writing a test, you'll first need to subclass unittest.TestCase.
# In our case, we'll subclass the APQuestTestBase we defined in bases.py.
class TestEasyModeLogic(HoVTestBase):
    # Our test base is a subclass of WorldTestBase.
    # WorldTestBase takes a dict of options and sets up a multiworld for you with a single world of your game.
    # The world will have the options you specified.
    options: HoVOptions = {
        "hard_mode": False, 
        "level_up_progression": 100,
        # Options you don't specify will use their default values.
        # It is good practice to specify every option that has an impact on your test, even when it's the default value.
        # As such, we'll spell out that hard_mode is meant to be False.
        # All other options in APQuest are cosmetic, so we don't need to list them.
    }

    # At this point, we could stop, and a few default tests would be run on our world.
    # At the time of writing (2025-09-04), this includes the following tests:
    # - If you have every item, every location can be reached
    # - If you have no items, you can still reach something ("Sphere 1" is not empty)
    # - The world successfully generates (Fill does not crash)

    # This is already useful, but we also want to do our own tests.
    # A test is a function whose name starts with "test".
    def test_easy_mode_access(self) -> None:
        # Inside a test, we can manually collect items, check access rules, etc.
        # For example, we could check that the two early chests are already accessible despite us having no items.
        # For the sake of structure, let's have every test item in its own subtest.
        with self.subTest("Test checks accessible with nothing"):

            IronRock2Room_chest = self.world.get_location(
                next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == IronRock2Room)
            )
            IronRock3Room_chest = self.world.get_location(
                next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == IronRock3Room)
            )

            # Since access rules have a "state" argument, we must pass our current CollectionState.
            # Helpfully, since we're in a WorldTestBase, we can just use "self.multiworld.state".
            self.assertTrue(IronRock2Room_chest.can_reach(self.multiworld.state))
            self.assertTrue(IronRock3Room_chest.can_reach(self.multiworld.state))

            # Test the False asserts
            
            AbandonHiddenRoom_chest = self.world.get_location(
                next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == AbandonHiddenRoom)
            )
            CastlePortcullisRoom_chest = self.world.get_location(
                next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == CastlePortcullisRoom)
            )

            # Since access rules have a "state" argument, we must pass our current CollectionState.
            # Helpfully, since we're in a WorldTestBase, we can just use "self.multiworld.state".
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

        with self.subTest("Launch Bomb is required for some castle and abandon town areaas"):
            # Manually checking the dependency in the previous function was a bit of a hassle, wasn't it?
            # Now we are checking four locations. It would be even longer as a result.
            # Well, there is another option. It's the assertAccessDependency function of WorldTestBase.

            self.assertAccessDependency(
                [
                    next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == CastleTopRampartsRoom),
                    next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == AbandonWestDrainRoom),
                    next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == CastleColumnRoom)
                ],
                [[SUBWEAPON.BOMB]],
                only_check_listed=True,
            )

