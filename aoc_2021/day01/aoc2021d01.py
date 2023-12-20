# https://adventofcode.com/2021/day/1

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #  1195 / 1235
test_file = script_path / "test.txt"  # 7 / 5


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = file.read().split(
            "\n"
        )  #  Read each line (split \n) and form a list of strings

    return [int(n) for n in lst]


def part1(data):
    """Solve part 1"""

    total = 0
    prev = 0
    for x in data[1:]:
        total = total + 1 if (x > prev) else total
        prev = x

    return total


def part2(data):
    """Solve part 2"""

    total = 0
    prev = 0

    for i, x in enumerate(data[:-3]):
        next = sum(data[i : i + 3])
        total = total + 1 if (next > prev) else total
        prev = next

    return total


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
