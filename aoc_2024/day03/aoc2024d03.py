# https://adventofcode.com/2024/day/

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 182619815
test_file = script_path / "test.txt"  # 161


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n")

    return lst


def part1(data):
    """Solve part 1"""

    re_pattern = r"mul\((\d+),(\d+)\)"

    tot = 0

    for d in data:
        result = re.finditer(re_pattern, d)

        if result:
            # print(result)
            for i in result:
                # print(i)
                # print(i.group())
                # print(i.group(1))
                # print(i.group(2))
                tot += int(i.group(1)) * int(i.group(2))

    return tot


def part2(data):
    """Solve part 2"""

    re_pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))"
    re_pattern = r"do\(\)"

    tot = 0
    enabled = True

    for d in data:
        result = re.finditer(re_pattern, d)

        if result:
            print(result)
            for i in result:
                print(i)
                # print(i.group())
                # print(i.group(1))
                # print(i.group(2))
                # tot += int(i.group(1)) * int(i.group(2))

    return tot


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
    # solutions = solve(soln_file)
