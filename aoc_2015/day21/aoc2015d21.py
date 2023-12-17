# https://adventofcode.com/2015/day/21

import pathlib
import time
from itertools import combinations
from math import inf as INF

script_path = pathlib.Path(__file__).parent

# PART 1 = 78
# Part 2 =


shop_file = script_path / "shop.txt"

stats_me = (
    100,
    0,
    0,
)  # Before buying anything {'Hit Points': 100, 'Damage': 0, 'Armor': 0}
stats_boss = (104, 8, 1)  # {'Hit Points': 104, 'Damage': 8, 'Armor': 1}

stats_test_me = (8, 5, 5)  # {'Hit Points': 8, 'Damage': 5, 'Armor': 5}
stats_test_boss = (12, 7, 2)  # {'Hit Points': 12, 'Damage': 7, 'Armor': 2}

weapons = []
armour = []
rings = []


def parse():
    """Parse input"""
    with open(shop_file, "r") as file:
        data = file.read().split("\n")

        weapon_list = [line.split() for line in data[1:6]]
        armour_list = [line.split() for line in data[8:13]]
        rings_list = [line.replace("e +", "e_").split() for line in data[15:]]

        # Add on empty entries for the armour and rings(*2)
        armour_list.append(["Empty", 0, 0, 0])  # Alt: [0 for i in range(4)]
        rings_list.append(
            ["Empty", 0, 0, 0, 0]
        )  # Alt add two rings: [0 for i in range(5)] for j in range(2)]
        rings_list.append(["Empty", 0, 0, 0, 0])

    return (weapon_list, armour_list, rings_list)


def fight(boss, player):
    boss_hp, boss_damage, boss_armour = boss
    player_hp, player_damage, player_armour = player

    while boss_hp > 0 and player_hp > 0:
        boss_hp -= max(1, player_damage - boss_armour)  # Always does at least 1 damage
        if boss_hp <= 0:
            continue

        player_hp -= max(
            1, boss_damage - player_armour
        )  # Always does at least 1 damage
        if player_hp <= 0:
            continue

    print("Boss:", boss_hp, "Player:", player_hp)
    if boss_hp <= 0:
        return True

    return False


def part1(shop, boss):
    """Solve part 1"""

    weapons_list, armour_list, rings_list = shop
    min_cost = INF

    for weapon in weapons_list:
        for armour in armour_list:
            for ringL, ringR in combinations(rings_list, 2):
                # print(weapon, armour, ringL, ringR)
                player_hp = 100
                player_damage = sum(
                    list(map(int, [weapon[2], armour[2], ringL[2], ringR[2]]))
                )
                player_armour = sum(
                    list(map(int, [weapon[3], armour[3], ringL[3], ringR[3]]))
                )
                print("damage:", player_damage, "armour:", player_armour)
                if fight(boss, (player_hp, player_damage, player_armour)):
                    cost = sum(
                        list(map(int, [weapon[1], armour[1], ringL[1], ringR[1]]))
                    )
                    min_cost = min(min_cost, cost)

    return min_cost


def part2(shop, boss):
    """Solve part 2"""

    weapons_list, armour_list, rings_list = shop
    max_cost = 0

    for weapon in weapons_list:
        for armour in armour_list:
            for ringL, ringR in combinations(rings_list, 2):
                # print(weapon, armour, ringL, ringR)
                player_hp = 100
                player_damage = sum(
                    list(map(int, [weapon[2], armour[2], ringL[2], ringR[2]]))
                )
                player_armour = sum(
                    list(map(int, [weapon[3], armour[3], ringL[3], ringR[3]]))
                )
                print("damage:", player_damage, "armour:", player_armour)
                if not fight(boss, (player_hp, player_damage, player_armour)):
                    cost = sum(
                        list(map(int, [weapon[1], armour[1], ringL[1], ringR[1]]))
                    )
                    max_cost = max(max_cost, cost)

    return max_cost


def solve():
    """Solve the puzzle for the given input"""
    times = []

    shop = parse()
    times.append(time.perf_counter())
    solution1 = part1(shop, stats_boss)
    times.append(time.perf_counter())

    solution2 = part2(shop, stats_boss)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runAllTests():
    print("\nTests\n")
    fight(stats_test_boss, stats_test_me)


if __name__ == "__main__":  # print()
    runAllTests()

    sol1, sol2, times = solve()
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
