# https://adventofcode.com/2022/day/3

import pathlib
import time
import string

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 7811
input_test = script_path / "test.txt"  # 157 / 70

alphabet = list(string.ascii_letters)


def parse(puzzle_input):
    """Parse input"""
    data = []
    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n")

    return lst


def part1(backpacks):
    """Solve part 1"""

    data = []
    all_common_items = []
    scores = []

    for pack in backpacks:
        length = int(len(pack) / 2)
        comp1 = pack[:length]
        comp2 = pack[length:]
        comp1_items = comp1.split()
        comp2_items = comp2.split()
        data.append([comp1_items, comp2_items])

    backpacks = data

    for pack in backpacks:
        comp1, comp2 = pack
        items1 = set(comp1[0])
        items2 = set(comp2[0])
        all_common_items.append(items1 & items2)

    for c in all_common_items:
        if len(c) == 1:
            scores.append(alphabet.index(c.pop()) + 1)
        else:
            print("more than 1 item:", c)

    return sum(scores)


def part2(backpacks):
    """Solve part 2"""

    scores = []

    for group_start in range(0, len(backpacks), 3):
        elf1 = set(backpacks[group_start])
        elf2 = set(backpacks[group_start + 1])
        elf3 = set(backpacks[group_start + 2])
        common = elf1 & elf2 & elf3

        if len(common) == 1:
            scores.append(alphabet.index(common.pop()) + 1)
        else:
            print("more than 1 item:", common)

    return sum(scores)


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
