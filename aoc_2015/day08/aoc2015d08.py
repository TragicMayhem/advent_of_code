# https://adventofcode.com/2015/day/8

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 1350 / 2085
test_file = (
    script_path / "test.txt"
)  # string chars (2 + 5 + 10 + 6 = 23) in memory (0 + 3 + 7 + 1 = 11) so 23 - 11 = 12
# (6 + 9 + 16 + 11 = 42)  42 - 23 = 19
test_file2 = script_path / "test2.txt"  # 50 / 75

# Disregarding the whitespace in the file,
# what is the number of characters of code for string literals minus the number of characters # in memory
# for the values of the strings in total for the entire file?

# (\\\\)  - Expression matches \\  = 2 char-space
# (\\x[0-9a-z]{2})  - Expression matches \x and 2 chars/digits [0-9a-z]  = 4 char-space
# (\\\")  - Expression matches \"  = 2 char-space
# (\\\\)|(\\x[\w]{2})|(\\\")   - Match all but group each component pattern
# (\\\\|\\x[\w]{2}|\\\")   - Match all but just each one separately, so get a single list


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        data = file.read().split("\n")
    return data


def part1(data):
    """Solve part 1"""
    tot_space = 0
    tot_char_len = 0

    for l in data:
        tmp = l[1:-1]

        find_escaped = re.findall(r"(\\\\|\\x[\w]{2}|\\\")", l)
        # print(find_escaped)

        tot_space += len(l)
        tot_char_len += (
            len(l) - 2 - sum(len(f) for f in find_escaped) + len(find_escaped)
        )

    # print("Answer:", tot_space - tot_char_len)
    return tot_space - tot_char_len


def part2(data):
    """Solve part 2"""
    tot_space = 0

    for l in data:
        tmp = l
        tmp = tmp.replace(
            "\\x", "^x"
        )  # 'Cheat' replace this with char not there, replace rest then change this back with extra \
        tmp = tmp.replace("\\", "\\\\").replace('"', '\\"')
        tmp = tmp.replace("^x", "\\\\x")
        tmp = '"' + tmp + '"'

        tot_space += len(tmp) - len(l)

    # print("Answer:", tot_space)
    return tot_space


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


if __name__ == "__main__":  # print()
    runAllTests()

    sol1, sol2, times = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
