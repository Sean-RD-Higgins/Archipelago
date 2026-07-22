from worlds.horde_of_viscount.locations import ROOM_ID_TO_LOCATION_NAME_LIST
from worlds.horde_of_viscount.options import HoVOptions
from worlds.horde_of_viscount.rules import CastleBridgeRoom

from .bases import HoVTestBase


class TestWhipRank2Off(HoVTestBase):
    options: HoVOptions  = {
        "Whip Rank 2": False,
    }

    # Once again, this is just default settings, so running the default tests would be wasteful.
    run_default_tests = False

    # The hammer option adds the Hammer item to the itempool.
    # Since the hammer option is off in this TestCase, we have to verify that the Hammer is *not* in the itempool.
    def test_rank2_doesnt_exist(self) -> None:
        # An easy way to verify that an item is or is not in the itempool is by using WorldTestBase.get_items_by_name().
        # This will return a list of all matching items, which we can check for its length.
        whip_rank_2_in_itempool = self.get_items_by_name("Whip Durable A")
        self.assertEqual(len(whip_rank_2_in_itempool), 0)

    # If the hammer option is not enabled, the Top Middle Chest should just be accessible with nothing.
    def test_hammer_is_not_required_for_top_middle_chest(self) -> None:
        # To check whether an item is required for a location, we would use self.assertAccessDependency.
        # However, in this case, we want to check that the Hammer *isn't* required for the Top Middle Chest location.
        # The robust way to do this is to collect every item into the state except for the Hammer,
        # then assert that the location is reachable.
        # Luckily, there is a helper for this: "collect_all_but".
        self.collect_all_but("Whip Durable B")

        # Now, we manually check that the location is accessible using location.can_reach(state):
        top_middle_chest_player_one = self.world.get_location(ROOM_ID_TO_LOCATION_NAME_LIST[CastleBridgeRoom][0])
        self.assertTrue(top_middle_chest_player_one.can_reach(self.multiworld.state))


class TestWhipRank2On(HoVTestBase):
    options: HoVOptions = {
        "Whip Rank 2": True,
    }

    # When the hammer option is on, the Hammer should exist in the itempool. Let's verify that.
    def test_durable_exists(self) -> None:
        # Nothing new to say here, but I do want to take this opportunity to teach you some Python magic. :D
        # In Python, when you check for the truth value of something that isn't a bool,
        # it will be implicitly converted to a bool automatically.
        # Which instances of a class convert to "False" and which convert to "True" is class-specific.
        # In the case of lists (or containers in general), empty means False, and not-empty means True.
        # bool([]) -> False
        # bool([1, 2, 3]) -> True
        # So, after grabbing all instances of the Hammer item from the itempool as a list ...
        whip_duarble_in_itempool = self.get_items_by_name("Whip Durable B")

        # ... instead of checking that the len() is 1, we can run this absolutely beautiful statement instead:
        self.assertTrue(whip_duarble_in_itempool)

