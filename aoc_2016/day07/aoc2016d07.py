# https://adventofcode.com/2016/day/7

import pathlib
import time
import re
from pprint import pprint as pp

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 105  / 258
input_test1 = script_path / "test1.txt"  #   2  /   -
input_test2 = script_path / "test2.txt"  #   0  /   3

## REGULAR EXPRESSION - CALCULATIONS AND NOTES ##

##  PART 1 ##

# NOTE Includes ALL 4 same letter (which will have to remove later)
#     <--****-->
# abcd[**bddb**]xyyx
check_in_brackets = re.compile(r"\[[a-z]*(([a-z])([a-z])(\3)(\2))[a-z]*\]")

# Option: Checked this, then filter all others out, reduces data to those with potential
check_pattern = re.compile(r"(([a-z])([a-z])(\3)(\2))")

##  PART 2 ##
aba_check = re.compile(r"(?=([a-z]{3}))(?=([a-z])(?!\2)([a-z])(\2))")


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input, "r") as file:
        data = file.read().split("\n")
    return data


def part1(data):
    """Solve part 1"""
    valid_ip = []
    invalid_ip = []
    for d in data:
        if check_in_brackets.search(d):
            # print('pattern in brackets', d[:25])
            invalid_ip.append((d, "pattern in brackets"))
            continue

        chk_pattern = check_pattern.findall(d)
        if chk_pattern:
            # print('findall', len(chk_pattern), chk_pattern, ' >> ', d[:25])
            for pattern in chk_pattern:
                found = pattern[0]
                bad_aba = found == len(found) * found[0]
                break

            if not bad_aba:
                valid_ip.append((d, "good"))
            else:
                invalid_ip.append((d, "pattern all same char"))
        else:
            invalid_ip.append((d, "No TLS checks"))

    print("Record Count:\t", len(data))
    print("TLS Valid IP:\t", len(valid_ip))
    print("TLS Invalid IP:\t", len(invalid_ip))

    return len(valid_ip)


def part2(data):
    """Solve part 2"""
    valid_ip = []

    for d in data:
        line = re.split("\[|\]", d)  # Split line on brackets

        # Split indexes - Odd = open text and Even = bracketted text
        text_open = []
        text_bracketed = []
        for i in range(len(line)):
            if i % 2:
                text_bracketed.append(line[i])
            else:
                text_open.append(line[i])

        # String all together separated by space (so not crating false patterns)
        text_open = " ".join(text_open)
        text_bracketed = " ".join(text_bracketed)

        # Check for aba pattern, the regex will search for ALL including overlapping
        chk_open = aba_check.findall(text_open)
        chk_bracket = aba_check.findall(text_bracketed)
        # if chk_open: print("Open", chk_open)
        # if chk_bracket: print("Bracket", chk_bracket)

        if chk_open and chk_bracket:
            # Use Open patterns to build the 'bab' from the 'aba'. Check the bracket list for match. SSL valid IP
            bracket_check_list = [x[0] for x in chk_bracket]
            for ptn in chk_open:
                tmp = ptn[2] + ptn[1] + ptn[2]
                if tmp in bracket_check_list:
                    valid_ip.append(d)
                    break

    print("Record Count:\t", len(data))
    print("SSL Valid IP:\t", len(valid_ip))

    return len(valid_ip)


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
    a, b, t = solve(input_test1)
    print(f"Test1 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")

    a, b, t = solve(input_test2)
    print(f"Test2 Part 1: {a} in {t[1]-t[0]:.4f}s")
    print(f"      Part 2: {b} in {t[2]-t[1]:.4f}s")
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":  # print()
    runAllTests()

    sol1, sol2, times = solve(input)
    print("\nAOC")
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")
