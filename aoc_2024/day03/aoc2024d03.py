# https://adventofcode.com/2024/day/3

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 182619815 /
test_file = script_path / "test.txt"  # 161 (with two examples its 322) / 48

# 18041735 too low
# 85770822 too high


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
            for i in result:
                tot += int(i.group(1)) * int(i.group(2))

    return tot


#  Future me:
#  4 groups from the findall, can put directly into 4 variables
#  a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", d)
#  function enabled = bool(do)

# 1 Original - works when put enabled outside loop :/


def part2_v1(data):
    """Solve part 2"""

    re_pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))"

    tot = 0
    enabled = True
    for d in data:
        results = re.findall(re_pattern, d)

        if results:
            print(results)
            for res in results:
                print(enabled, res, tot)

                if res[0].startswith("mul"):
                    if enabled:
                        # print(res[1], res[2])
                        tot += int(res[1]) * int(res[2])
                elif res[0] == "do()":
                    enabled = True
                elif res[0] == "don't()":
                    enabled = False

    return tot


# 2 STACK version


def part2_v2(data):
    """Solve part 2"""

    re_pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))"

    tot = 0
    enabled_stack = [True]

    for d in data:
        results = re.findall(re_pattern, d)

        for res in results:
            print(enabled_stack[-1], res, tot)

            if res[0] == "do()":
                enabled_stack.append(True)
            elif res[0] == "don't()":
                enabled_stack.append(False)
            elif res[0].startswith("mul"):
                if enabled_stack[-1]:
                    tot += int(res[1]) * int(res[2])

    return tot


# 3 Using 0/1 to simplify if
def part2(data):
    """Solve part 2"""

    re_pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))"

    tot = 0
    enabled = 1
    for d in data:
        results = re.findall(re_pattern, d)

        if results:
            # print(results)
            for res in results:
                # print(enabled, res, tot)

                if res[0] == "do()":
                    enabled = 1
                elif res[0] == "don't()":
                    enabled = 0

                if res[0].startswith("mul"):
                    tot += int(res[1]) * int(res[2]) * enabled

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
    solutions = solve(soln_file)
