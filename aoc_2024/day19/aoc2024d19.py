# https://adventofcode.com/2024/day/19

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 293 / 623924810770264
test_file = script_path / "test.txt"  # 6 / 16


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        parts = file.read().split("\n\n")
        components = parts[0].replace(" ", "").split(",")
        designs = parts[1].split("\n")

    return (components, designs)

def can_construct_string(design, components):
    """
    Determines if a design string can be constructed from a word bank.

    Args:
        design: The design string to construct.
        components: A list of words that can be used to construct the design.

    Returns:
        True if the design string can be constructed, False otherwise.
    """

    table = [False] * (len(design) + 1)
    table[0] = True

    for i in range(len(design) + 1):
        if table[i]:
            for word in components:
                if word == design[i:i+len(word)]:
                    table[i+len(word)] = True

    return table[len(design)]


def can_construct_string_count(design, components):
    """
    Determines if a design string can be constructed from a word bank and counts the number of ways.

    Args:
        design: The design string to construct.
        components: A list of words that can be used to construct the design.

    Returns:
        The number of ways the design string can be constructed.
    """

    table = [0] * (len(design) + 1)
    table[0] = 1  # Empty string can be constructed in 1 way

    for i in range(len(design) + 1):
        for word in components:
            if word == design[i:i+len(word)]:
                table[i+len(word)] += table[i]

    return table[len(design)]


def part1(data):
    """Solve part 1"""

    components, designs = data

    count = 0
    for d in designs:
        count += can_construct_string(d, components
                                      )

    return count


def part2(data):
    """Solve part 2"""
    components, designs = data

    count2 = 0
    for d in designs:
        count2 += can_construct_string_count(d,components)

    return count2



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

    bank = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    target_strings = ["brwrr", "bggr", "gbbr", "rrbgbr",
    "ubwu",
    "bwurrg",
    "brgr",
    "bbrgwb"]

    for t in target_strings:
        if can_construct_string(t, bank):
            print(f"{t} can be constructed")
        else:
            print(f"{t} cannot be constructed")


    tests = solve(test_file, run="Test")

    print()
    solutions = solve(soln_file)
