from worlds.horde_of_viscount.options import HoVOptions

from .bases import HoVTestBase


# Sometimes, you might want to test something with a specific option disabled, then with it enabled.
# For this purpose, we'll just have two different TestCase classes.
class TestExtraStartingItemsOff(HoVTestBase):
    options: HoVOptions = {
        "arcade_credit_fill": 0,
    }

    # This would run all the default WorldTestBase tests a second time on default options. That's a bit wasteful.
    run_default_tests = False

    def test_extra_starting_arcade_credit_doesnt_exist(self) -> None:
        self.assertFalse(self.world.multiworld.get_items().__contains__("Arcade Credit"))

