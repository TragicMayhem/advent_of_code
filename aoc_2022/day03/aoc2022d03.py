# https://adventofcode.com/2022/day/3

import pathlib
import time
import string

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 7811
test_file = script_path / "test.txt"  # 157 / 70

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
