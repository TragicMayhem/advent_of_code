# https://adventofcode.com/2022/day/4

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 524 //   798
test_file = script_path / "test.txt"  # 2 //


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        data = file.read().split(
            "\n"
        )  # Read file make list by splitting on new line \n
        data = [tuple(d.split(",")) for d in data]
        data = [[tuple(sec.split("-")) for sec in pair] for pair in data]
        data = [[tuple(map(int, sec)) for sec in pair] for pair in data]

    return data


def check_sections_fully_overlap(a, b):
    checks = []
    if a[0] <= b[0] and a[1] >= b[1]:
        checks.append(True)

    if b[0] <= a[0] and b[1] >= a[1]:
        checks.append(True)

    return any(checks)


def check_sections_for_overlap(a, b):
    checks = []

    if a[0] <= b[0] and a[1] >= b[0]:
        checks.append(True)

    if a[0] <= b[0] and a[1] >= b[1]:
        checks.append(True)

    if b[0] <= a[0] and b[1] >= a[0]:
        checks.append(True)

    if b[0] <= a[0] and b[1] >= a[1]:
        checks.append(True)

    return any(checks)


def part1(data):
    """Solve part 1"""
    overlaps = []

    for pair in data:
        section1, section2 = pair
        ans = check_sections_fully_overlap(section1, section2)
        if ans:
            overlaps.append(pair)

    return len(overlaps)


def part2(data):
    """Solve part 2"""

    overlaps = []
    for pair in data:
        section1, section2 = pair
        ans = check_sections_for_overlap(section1, section2)
        if ans:
            overlaps.append(pair)

    return len(overlaps)


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
