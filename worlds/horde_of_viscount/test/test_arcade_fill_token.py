from .bases import HoVTestBase


# Sometimes, you might want to test something with a specific option disabled, then with it enabled.
# For this purpose, we'll just have two different TestCase classes.
class TestExtraStartingItemsOff(HoVTestBase):
    options = {
        "arcade_token_fill": False,
    }

    # Hmm... This is just default options again.
    # This would run all the default WorldTestBase tests a second time on default options. That's a bit wasteful.
    # Luckily, there is a way to turn off the default tests for a WorldTestBase subclass:
    run_default_tests = False

    # Since the extra_starting_chest option is False, we'll verify that the Extra Starting Chest location doesn't exist.
    def test_extra_starting_arcade_token_doesnt_exit(self) -> None:
        self.assertFalse(self.world.get_pre_fill_items[0] == "Arcade Token")


class TestExtraStartingItemsOn(HoVTestBase):
    options = {
        "arcade_token_fill": True,
    }

    # In this case, running the default tests is acceptable, since this is a unique options combination.

    # Since the extra_starting_chest option is True, we'll verify that the Extra Starting Chest location exists.
    def test_extra_starting_arcade_token_exists(self) -> None:
        self.assertTrue(self.world.get_pre_fill_items[0] == "Arcade Token")