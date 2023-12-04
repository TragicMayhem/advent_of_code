# https://adventofcode.com/2023/day/4

import pathlib
import time
from copy import deepcopy

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  #
input_test = script_path / "test.txt"  #


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n")
        lst = [x.replace(":", "|").replace("  ", " ").split("|") for x in lst]

        cards = []
        # print(lst)

        for c in lst:
            card = int(c[0].split(" ")[-1])
            winners = set(map(int, c[1].strip().split(" ")))
            nums = set(map(int, c[2].strip().split(" ")))
            winning_set = nums.intersection(winners)
            cards.append((card, winners, nums, winning_set))

    return cards


def part1(data):
    """Solve part 1"""

    ans = 0

    for d in data:
        card, winners, nums, winning_set = d

        # winning_set = nums.intersection(winners)
        if winning_set:
            ans += 2 ** (len(winning_set) - 1)

    return ans


def count_winners():
    # if winning_set:
    #     number_cards_won = len(winning_set)

    #     pass

    pass


def part2(data):
    """Solve part 2"""

    ans = 0

    working_cards = deepcopy(data)

    for d in working_cards:
        card, winners, nums, winning_set = d

    return 1


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(input_test, run="Test")

    print()
    # solutions = solve(input)
