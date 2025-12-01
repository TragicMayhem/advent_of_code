# https://adventofcode.com/2024/day/

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 6951 / 
test_file = script_path / "test.txt"  # 143 / 


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n\n")

    # File has two parts split by blank line

    page_order = [tuple(map(int, line.split('|'))) for line in lst[0].split('\n')]

    pages = lst[1].split('\n')

    print(page_order)
    print(pages)

    return (page_order, pages)


def part1(data):
    """Solve part 1"""

    pages_order, pages = data

    pg_regex = []

    for ord in pages_order:
        pg_regex.append(rf"{str(ord[0])}.*{str(ord[1])}")

    pg_check_list = list(zip(pages_order, pg_regex))
    print(pg_check_list)

    valid_pages = []
    invalid_pages = []

    for p in pages:
        pg_valid = True

        for pg_chk in pg_check_list:
            pg1, pg2 = map(str,pg_chk[0])
            pg_regex = pg_chk[1]

            # If the pages numbesr are not in the list skip
            if pg1 not in p or pg2 not in p:
                continue

            if not re.search(pg_regex, p):
                pg_valid = False
                invalid_pages.append(p)
                break

        if pg_valid:
            valid_pages.append(p)

    print(valid_pages)

    tot = 0
    for v in valid_pages:
        tmp = list(map(int, v.split(",")))
        mid = len(tmp) // 2
        tot += tmp[mid]

    return tot


def part2(data):
    """Solve part 2"""

    return 1


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
