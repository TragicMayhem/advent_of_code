# https://adventofcode.com/2022/day/13w

import pathlib
import time
from pprint import pprint as pp
import json
from copy import deepcopy
from functools import cmp_to_key

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  #  5280  // 25792
input_test = script_path / "test.txt"  # 13 //  140


def parse(puzzle_input):
    """Parse input"""

    # dont bother with regex, data is json readable
    # regexp = re.compile(r"\[([\d|,]*)\]")

    with open(puzzle_input, "r") as file:
        pairs = [n.split("\n") for n in file.read().split("\n\n")]

    for pair in pairs:
        pair[0] = json.loads(pair[0])
        pair[1] = json.loads(pair[1])

    # pp(pairs)

    return pairs


def comparison(left, right):
    # print("Compare", left, "with", right)

    if isinstance(left, int) and isinstance(right, int):
        return left - right

    # Cant use list(right) need to use [right] < Need to look at why
    # "TypeError: 'int' object is not iterable"
    if isinstance(left, list) and isinstance(right, int):
        return comparison(left, [right])

    if isinstance(left, int) and isinstance(right, list):
        return comparison([left], right)

    if isinstance(left, list) and isinstance(right, list):
        # Using the Python zip() Function for Parallel Iteration
        for l, r in zip(left, right):
            check = comparison(l, r)
            if check != 0:
                return check

    return len(left) - len(right)


def part1(data):
    """Solve part 1"""
    print("Part 1")
    ans = 0
    for id, pair in enumerate(data, 1):  # enumerate can specify start
        # print(id, pair)

        left = pair[0]
        right = pair[1]
        # dont need to check if list in list with function to check each
        # left_contains_list = any(isinstance(l, list) for l in left)
        # right_contains_list = any(isinstance(l, list) for l in right)

        result = comparison(left, right)
        # print("res:", result)
        if result < 0:
            ans += id

    return ans


def part2(data):
    """Solve part 2"""
    print("Test 2")

    new_data = deepcopy(data)

    # need to unpack
    signals = []
    for p in new_data:
        signals.extend(p)
    signals.append([[2]])
    signals.append([[6]])

    # functools can provide function to use as a key.
    signals.sort(key=cmp_to_key(comparison))
    # pp(signals)

    pos1 = signals.index([[2]]) + 1
    pos2 = signals.index([[6]]) + 1

    return pos1 * pos2


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():

    print("Tests")
    a, b = runTest(input_test)
    print(f"Test1.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":

    runAllTests()

    solutions = solve(input)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
