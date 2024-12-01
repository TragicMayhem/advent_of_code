# https://adventofcode.com/2023/day/1

import pathlib
import time
from collections import Counter

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 2086478 / 24941624
test_file = script_path / "test.txt"  # 11 / 31


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        #  Read each line (split \n) and form a list of strings
        lst = []
        for l, r in [x.replace("   ", " ").split(" ") for x in file.read().split("\n")]:
            lst.append((int(l), int(r)))

    return lst


def part1(data):
    """Solve part 1"""

    left_list = []
    right_list = []
    for l, r in data:
        left_list.append(l)
        right_list.append(r)

    left_list.sort()
    right_list.sort()

    if len(left_list) != len(right_list):
        print("Lists not equal")

    tot = 0

    for l, r in zip(left_list, right_list):
        diff = abs(l - r)
        tot += diff

    return tot


def part2(data):
    """Solve part 2"""

    left_list = []
    right_list = []
    for l, r in data:
        left_list.append(l)
        right_list.append(r)

    right_counter = Counter(right_list)
    tot_sim = 0

    for l in left_list:
        if l in right_counter.keys():
            tot_sim += l * right_counter[l]

    return tot_sim


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
