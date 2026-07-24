from worlds.horde_of_viscount.items import SUBWEAPON
from worlds.horde_of_viscount.options import HoVOptions

from .bases import HoVTestBase


class TestHardMode(HoVTestBase):
    options: HoVOptions = {
        "hard_mode": True,
    }

    def test_hard_mode_access(self) -> None:
        with self.subTest("Test that Whip Durable B in Item Pool"):
            whip_durable_b_in_itempool = self.get_items_by_name("Whip Durable B")

            # ... instead of checking that the len() is 1, we can run this absolutely beautiful statement instead:
            self.assertTrue(len(whip_durable_b_in_itempool) == 0)

        with self.subTest("Test that the final area isn't reachable without the required items"):
            self.assertAccessDependency(
                ["Credits Peak Chest 2"],
                [[SUBWEAPON.KNIFE, SUBWEAPON.AXE, SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CLEATS, SUBWEAPON.CALTROP]],
                only_check_listed=True,
            )

        for item in [SUBWEAPON.KNIFE, SUBWEAPON.AXE, SUBWEAPON.BOMB, SUBWEAPON.WINGS, SUBWEAPON.CLEATS, SUBWEAPON.CALTROP]:
            with self.subTest(f"Test that the final boss requires {item}"):
                self.assertAccessDependency(
                    ["Credits Peak Chest 2"],
                    [[item]],
                    only_check_listed=True,
                )
