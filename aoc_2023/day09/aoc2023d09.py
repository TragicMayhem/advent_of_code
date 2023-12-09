# https://adventofcode.com/2023/day/9

import pathlib
import time
from itertools import repeat

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 1868368343 / 1022
input_test = script_path / "test.txt"  # 114 / 2

# original_list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# converted_list = [[int(string) for string in sublist] for sublist in original_list]
# print(converted_list)
# # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Difference
# >>> t
# [1, 3, 6]
# >>> [j-i for i, j in zip(t[:-1], t[1:])]  # or use itertools.izip in py2k
# [2, 3]


def check(lst):
    """
    Use the repeat function to generate an iterator that returns the
    0 (zero) repeated len(lst) times
    """
    repeated = list(repeat(0, len(lst)))
    return repeated == lst


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [l.split() for l in file.read().split("\n")]
        lst = [[int(x) for x in sublist] for sublist in lst]
    # print(lst)

    return lst


def part1(data):
    """Solve part 1"""

    predictions = []
    processing = []

    for d in data:
        processing = []
        processing.append(d[:])

        #  all check for zero to stop
        # process while not and add to processing
        #  then loop back adding to the end.  do we need to add or just add last plus new and iterate up to top

        all_zero = False

        while not all_zero:
            latest = processing[-1]
            diffs = [j - i for i, j in zip(latest[:-1], latest[1:])]
            # print(diffs)
            processing.append(diffs)

            all_zero = check(diffs)
            # if all_zero:
            #     print("All Zeros")

        # print("processing", processing)

        last_diff_to_add = 0

        for l in processing[::-1]:
            last_num = l[-1]
            new_last_num = last_num + last_diff_to_add
            last_diff_to_add = new_last_num
            # print(
            #     "last num:",
            #     last_num,
            #     "new last:",
            #     new_last_num,
            #     "new diff:",
            #     last_diff_to_add,
            # )

        predictions.append(new_last_num)

    print()
    print("Part 1:", predictions)

    return sum(predictions)


def part2(data):
    """Solve part 2"""
    print()
    predictions = []
    processing = []

    for d in data:
        processing = []
        processing.append(d[:])

        all_zero = False

        while not all_zero:
            latest = processing[-1]
            diffs = [j - i for i, j in zip(latest[:-1], latest[1:])]
            processing.append(diffs)
            all_zero = check(diffs)

        last_diff_to_add = 0

        for l in processing[::-1]:
            first_num = l[0]
            new_last_num = first_num - last_diff_to_add
            last_diff_to_add = new_last_num

        predictions.append(new_last_num)

    print()
    print(predictions)

    return sum(predictions)


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
