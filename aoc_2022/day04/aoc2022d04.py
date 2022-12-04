# https://adventofcode.com/2022/day/4

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 524 //   798
input_test = script_path / "test.txt"  # 2 //


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        data = file.read().split('\n')  # Read file make list by splitting on new line \n
        data = [tuple(d.split(",")) for d in data]
        data = [[tuple(sec.split("-")) for sec in pair] for pair in data]
        data = [[tuple(map(int,sec)) for sec in pair] for pair in data]

    return data


def check_sections_fully_overlap(a,b):
    checks = []
    if a[0] <= b[0] and a[1] >= b[1]:
        checks.append(True)

    if b[0] <= a[0] and b[1] >= a[1]:
        checks.append(True)

    return any(checks)


def check_sections_for_overlap(a,b):

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
        ans = check_sections_fully_overlap(section1,section2)
        if ans:
            overlaps.append(pair)

    return len(overlaps)


def part2(data):
    """Solve part 2"""

    overlaps = []
    for pair in data:
        section1, section2 = pair
        ans = check_sections_for_overlap(section1,section2)
        if ans:
            overlaps.append(pair)
            
    return len(overlaps)


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
