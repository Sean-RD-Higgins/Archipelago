from .bases import HoVTestBase


class TestHardMode(HoVTestBase):
    options = {
        "hard_mode": True,
    }

    def test_hard_mode_access(self) -> None:
        # For the sake of brevity, we won't repeat anything we tested in easy mode.
        # Instead, let's use this opportunity to talk a bit more about assertAccessDependency.

        # Let's take the Enemy Drop location.
        # In hard mode, the Enemy has two health. One swipe of the Sword does not kill it.
        # This means that the Enemy has a chance to attack you back.
        # If you only have the Sword, this attack kills you. After respawning, the Enemy has full health again.
        # However, if you have a Shield, you can block the attack (resulting in half damage).
        # Alternatively, if you have found a Health Upgrade, you can tank an extra hit.

        # Why is this important?
        # If we called assertAccessDependency with ["Right Room Enemy Drop"] and [["Shield"]], it would actually *fail*.
        # This is because "Right Room Enemy Drop" is beatable without "Shield" - You can use "Health Upgrade" instead.
        # However, we can call assertAccessDependency with *both* items like this:

        with self.subTest("Test that Whip Durable B in Item Pool"):
            whip_durable_b_in_itempool = self.get_items_by_name("Whip Durable B")

            # ... instead of checking that the len() is 1, we can run this absolutely beautiful statement instead:
            self.assertTrue(len(whip_durable_b_in_itempool) == 0)

        with self.subTest("Test that the final boss isn't beatable without Sword, Shield, and both Health Upgrades"):
            self.assertAccessDependency(
                ["Final Boss Defeated"],
                [["Sword", "Shield", "Health Upgrade"]],
                only_check_listed=True,
            )

        # This would now test the following:
        # 1. Without Sword, nor Shield, nor any Health Upgrades, the final boss is not beatable.
        # 2. With Sword, Shield, and all Health Upgrades, the final boss is beatable.

        # But, it's not really advisable to do this.
        # Think about it: If we implemented our logic incorrectly and forgot to add the Shield requirement,
        # this call would still pass. We'd rather make sure that each item individually is required:
        for item in ["Sword", "Shield", "Health Upgrade"]:
            with self.subTest(f"Test that the final boss requires {item}"):
                self.assertAccessDependency(
                    ["Final Boss Defeated"],
                    [[item]],
                    only_check_listed=True,
                )

        # This now tests that:
        # 1. Without Sword, you can't beat the Final Boss
        # 2. With Sword, you can beat the Final Boss (if you have everything else)
        # 3. Without Shield, you can't beat the Final Boss
        # 4. With Shield, you can beat the Final Boss (if you have everything else)
        # 5. Without Health Upgrades, you can't beat the Final Boss
        # 6. With all Health Upgrades, you can beat the Final Boss (if you have everything else)

        # 2., 4., and 6. are the exact same check, so it is a bit redundant.
        # But crucially, we are ensuring that all three items are actually required.

        # So that's not really why the inner elements are lists.
        # So we ask again: Why are they lists? When is it ever useful?
        # Fair warning: This is probably where you should stop reading this and skip to test_hard_mode_health_upgrades.
        # But if you really want to know why:

        # Having multiple elements in the inner lists is something that only comes up in more complex scenarios.
        # APQuest doesn't have any of these scenarios, but let's imagine one for completeness' sake.
        # Currently, the Enemy can be beaten with these item combinations:
        # 1. Sword and Shield
        # 2. Sword and Health Upgrade
        # Let's say there was also a "Shield Bash". When using the Shield Bash, you cannot use the Shield to defend.
        # This would mean there is a third valid combination:
        # 3. Shield + Health Upgrade
        # We have set up a scenario where none of the three items are enough on their own,
        # but any combination of two items works.
        # The best way to test this would be to call assertAccessDependency with:
        # [["Sword", "Shield"], ["Sword", "Health Upgrade"], ["Shield", "Health Upgrade"]]
        # If we omitted any item from any of the three sub-lists, the check would fail.
        # This is because the item is still *mentioned* in one of the other two conditions,
        # meaning it is not collected into state.
        # Thus, this term cannot be simplified any further without testing something different to what we want to test.

        # You can kinda think of assertAccessDependency as an OR(AND(item_list_1), AND(item_list_2), ...).
        # Except this "AND" is a special "AND" which allows reducing each list to a single representative item.
        # And also, the "OR" is special as well in that has to be exhaustive,
        # where the set of completely unmentioned items must *not* be able to reach the location collectively.
        # And *also*, each "AND" must be enough to access the location *out of the mentioned items*.
        # ... I'm not sure this explanation helps anyone, but most of the time, you really don't have to think about it.

    def test_hard_mode_health_upgrades(self) -> None:
        # We'll also repeat our Health Upgrade test from the Easy Mode test case, but modified for Hard Mode.
        # This will not be explained again here.

        health_upgrades = self.get_items_by_name("Health Upgrade")

        with self.subTest("Test that there are two Health Upgrades in the pool"):
            self.assertEqual(len(health_upgrades), 2)

        with self.subTest("Test that the Health Upgrades in the pool are progression, but not useful."):
            self.assertFalse(any(health_upgrade.useful for health_upgrade in health_upgrades))
            self.assertTrue(all(health_upgrade.advancement for health_upgrade in health_upgrades))
