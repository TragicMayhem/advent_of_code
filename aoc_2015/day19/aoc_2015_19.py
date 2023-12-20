# https://adventofcode.com/2015/day/19

import pathlib
import time
from pprint import pprint
import re
from collections import defaultdict

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 576 /
test_file = script_path / "test_file.txt"  # 4 distinct in 1 replacements
test_file2 = script_path / "test_file2.txt"  # 7 distinct in 9 replacements
test_file3 = script_path / "test_file3pt2.txt"  # 7 distinct in 9 replacements
test_file4 = script_path / "test_file4pt2.txt"  # 7 distinct in 9 replacements


def parse(puzzle_input):
    """Parse input"""

    replacements = {}

    with open(puzzle_input, "r") as file:
        data = file.read().split("\n")
        chain = data.pop(-1)

        for d in data:
            if d == "":
                continue
            tmp = d.split(" => ")
            if replacements.get(tmp[0], None) == None:
                replacements[tmp[0]] = []
            replacements.get(tmp[0]).append(tmp[1])

        # print("Input: Chain")
        # print(chain)
        # print("\nInput: Replacements")
        # print(replacements)

    return chain, replacements


def part1(chain, replacements):
    """Solve part 1"""

    molecules = set()

    for key, combis in replacements.items():
        pattern = key
        for match in re.finditer(pattern, chain):
            s = match.start()
            for m in combis:
                tmp_molecule = chain[:s] + m + chain[s + len(key) :]
                molecules.add(tmp_molecule)

    return len(molecules)


def part2(medicine, replacements):
    """
    Solve part 2
    Tried: Loops to build up string
    Tried: Recursion to build up string
    Tried: Looking for substring from the right

    After researching hints and tips, learning some new python.
    This solutions reverses the target and replacements then using regular expressions to substitute

    Mainly using because I could follow the logic and understand, and also cool use case to learn Re with functions for future problems

    ONLY WORKS FOR input.txt not the tests (there for part 1 only)

    """

    # Used as parameter in the re.sub call
    def find_replacement(x):
        return reverse_replacements[x.group()]

    reverse_medicine = medicine[::-1]

    # Now the molecule is reversed ALL THE REPLACEMENTS HAVE TO BE TO.
    reverse_replacements = defaultdict(list)

    # Alternate ways to do this (after researching) e.g. using re.findall, and list comprehension. Look at alternates)
    for k, v in replacements.items():
        reversed_key = k[::-1]
        for target in v:
            reversed_value = target[::-1]
            reverse_replacements[reversed_value] = reversed_key

    # print('Medicine:',reverse_medicine)
    # print('Reversed replacements:', reverse_replacements)

    # RegEx search string build from joining all the keys in the dictionary together (using or |)
    search_pattern = "|".join(reverse_replacements.keys())
    # print(search_pattern)

    count = 0
    working_molecule = reverse_medicine

    while working_molecule != "e":
        working_molecule = re.sub(search_pattern, find_replacement, working_molecule, 1)
        count += 1

    return count


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    chain, replacements = parse(puzzle_input)
    times.append(time.perf_counter())

    solution1 = part1(chain, replacements)
    times.append(time.perf_counter())

    solution2 = part2(chain, replacements)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runAllTests():
    print("\nTests\n")
    a, b, t = solve(test_file)
    print(f"Test1 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")

    a, b, t = solve(test_file2)
    print(f"Test2 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":
    # runAllTests()

    sol1, sol2, times = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
