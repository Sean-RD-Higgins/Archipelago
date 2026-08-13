import json
from worlds.horde_of_viscount.items import FOOD
from worlds.horde_of_viscount.options import HoVOptions
from .bases import HoVTestBase

class TestExtraStartingItemsOff(HoVTestBase):
    options: HoVOptions = {
        "arcade_credit_fill": 0,
    }

    # This would run all the default WorldTestBase tests a second time on default options. That's a bit wasteful.
    run_default_tests = False

    def test_extra_starting_arcade_credit_does_not_exist(self) -> None:
        self.assertFalse(self.world.get_pre_fill_items().__contains__(FOOD.ROOM_REDO))
