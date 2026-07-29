from worlds.horde_of_viscount.items import EQUIP, SUBWEAPON
from worlds.horde_of_viscount.locations import LOCATION_DATA_LIST
from worlds.horde_of_viscount.options import HoVOptions
from worlds.horde_of_viscount.rules import CreditsParentRoom

from .bases import HoVTestBase


class TestHardMode(HoVTestBase):
    options: HoVOptions = {
        "hard_mode": True,
    }

    def test_hard_mode_access(self) -> None:
        with self.subTest("Test that Whip Durable B in Item Pool"):
            whip_durable_b_in_itempool = self.get_items_by_name("Whip Durable B")
            self.assertTrue(len(whip_durable_b_in_itempool) == 1)

        with self.subTest("Test that the final area isn't reachable without all required items"):
            self.assertAccessDependency(
                [next(location.ap_location_name for location in LOCATION_DATA_LIST if location.room_id == CreditsParentRoom)],
                [[EQUIP.WINGS_ONE_FREE, SUBWEAPON.KNIFE, SUBWEAPON.AXE, SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CLEATS, SUBWEAPON.CALTROP]],
                only_check_listed=True,
            )
