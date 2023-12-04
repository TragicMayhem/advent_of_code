# https://adventofcode.com/2023/day/4

import pathlib
import time
from copy import deepcopy

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 24542/         XX Too low8724714
input_test = script_path / "test.txt"  # 13 / 30


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

    ans = 0

    max_cards_pos = len(data)
    # working_cards = [0 for c in data]
    # working_cards[0] = 1

    # print(working_cards)
    working_cards = [(0, 0, 0)]

    for d in data:
        card, winners, nums, winning_set, num_winners = d
        working_cards.append((card, num_winners, 1))
    print(working_cards)

    card = 1

    for card in range(len(data)):
        # for next_card_info in working_cards[1:]:
        # card, num_winners, card_count = next_card_info
        card, num_winners, card_count = working_cards[card]
        print("\nLoop #", card, " wins ", num_winners, " card count ", card_count)
        # print(next_card_info)

        if num_winners:
            # number of winning numbers indicates how many cards are duplicated
            # tmp_num, temp_wins, tmp_count = working_cards[card]
            # working_cards[card] = (card, num_winners, tmp_count)
            # print("Next card", working_cards[card])

            loop_stop = card + num_winners + 1
            if loop_stop > max_cards_pos:
                loop_stop = max_cards_pos
            print("stop", loop_stop)

            # indexing starts 0, so added fake zero to use card number
            for i in range(card + 1, loop_stop):
                # cd, wn, nm, ws, num_wins = data[i]
                curr_card, curr_wins, curr_count = working_cards[i]
                print(
                    "   loc",
                    i,
                    ": card",
                    curr_card,
                    "wins",
                    curr_wins,
                    "curr count",
                    curr_count,
                )

                working_cards[i] = (curr_card, curr_wins, curr_count + card_count)

            print(working_cards)

    ans = sum([c for a, b, c in working_cards])

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

    tests = solve(input_test, run="Test")

    print()
    solutions = solve(input)
