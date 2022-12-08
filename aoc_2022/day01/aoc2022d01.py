# https://adventofcode.com/2022/day/1

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 71023 /
input_test = script_path / "test.txt"  # 24000 /


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n\n")

    elfdata = [n.split("\n") for n in lst]
    data = [[int(x) for x in elf] for elf in elfdata]

    return data


def part1(data):
    """Solve part 1"""

    elf_totals = []

    for i in data:
        elf_totals.append(sum(i))

    return max(elf_totals)


def part2(data):
    """Solve part 2"""

    elf_totals = []

    for i in data:
        elf_totals.append(sum(i))

    elf_totals = sorted(elf_totals)

    return sum(elf_totals[-3:])


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