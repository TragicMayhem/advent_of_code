# https://adventofcode.com/2023/day/4

import pathlib
import time
from copy import deepcopy

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 24542/         XX Too low8724714
test_file = script_path / "test.txt"  # 13 / 30


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
            cards.append((card, winners, nums, winning_set, len(winning_set)))

    return cards


def part1(data):
    """Solve part 1"""

    ans = 0

    for d in data:
        card, winners, nums, winning_set, num_winners = d

        # winning_set = nums.intersection(winners)
        if winning_set:
            ans += 2 ** (len(winning_set) - 1)

    return ans


def part2(data):
    """Solve part 2"""

    # Got stuck in loops, and  initial version gets right answer for sample, but not input - too low.
    # Looking for some hints I was over compicating my data in and the lookups to
    # calculate the totals.  Right idea on using the counts just badly coded.
    #
    # Options to explore and get better
    # [x] list comprehension
    # using a dictionary with card as the key to tally each winning count

    # We have 1 card of each initially, and we know how many cards as the length of the list
    card_counts_list = [1] * len(data)

    # V1 Original method for getting a list of the winnning counts per card
    # win_counts_list = []
    # for d in data:
    #     card, winners, nums, winning_set, winning_count = d
    #     win_counts_list.append(winning_count)

    # V2 finally got list comrehension to get just the last value from my input tuples (has 5 values)
    # List comprehension example from web: result = [a for tup in y for a in tup]
    card_wins_list = [d[-1] for d in data]
    print("Initial card wins:\n", card_wins_list)

    # Help https://docs.python.org/3/library/functions.html#enumerate
    # list(enumerate(seasons))
    # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

    for card, winning_count in enumerate(card_wins_list):
        # print(card, winning_count)

        # For the number of wins, we get duplicate of the next cards based on wins value
        # We dont have to look to do a loop for each one, as we can set the range based on
        # the next values based on the number of wins
        # For each of those additional cars we can add the current card's count to it

        for j in range(card + 1, card + winning_count + 1):
            card_counts_list[j] += card_counts_list[card]
            # print(card_counts_list)

    print("\nFinal counts:\n", card_counts_list)
    ans = sum(card_counts_list)

    return ans


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

    tests = solve(test_file, run="Test")

    print()
    solutions = solve(soln_file)
