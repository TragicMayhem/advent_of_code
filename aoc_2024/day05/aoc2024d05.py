# https://adventofcode.com/2024/day/5

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 6951 /    #1 4689 too high #2 4121
test_file = script_path / "test.txt"  # 143 / 123


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n\n")

    # File has two parts split by blank line
    page_order = [tuple(map(int, line.split('|'))) for line in lst[0].split('\n')]
    page_order = sorted(page_order, key=lambda x: (x[0], x[1]))

    pages = lst[1].split('\n')

    # print(page_order)
    # print(pages)

    return (page_order, pages)


def part1(data):
    """Solve part 1"""

    page_order, pages = data
    valid_pages = []

    for p in pages:
        pg_valid = True

        for pg_chk in page_order:
            pg1, pg2 = map(str,pg_chk)
            pg_regex = f"{pg1}.*{pg2}"

            # If the pages numbesr are not in the list skip
            if pg1 not in p or pg2 not in p:
                continue

            if not re.search(pg_regex, p):
                pg_valid = False
                break

        if pg_valid:
            valid_pages.append(p)

    # print(valid_pages)

    tot = 0
    for v in valid_pages:
        tmp = list(map(int, v.split(",")))
        mid = len(tmp) // 2
        tot += tmp[mid]

    return tot


def part2(data):
    """Solve part 2"""

    page_order, pages = data
    invalid_pages = []

    for p in pages:
        for pg_chk in page_order:
            pg1, pg2 = map(str,pg_chk)
            pg_regex = f"{pg1}.*{pg2}"

            # If the pages numbesr are not in the list skip
            if pg1 not in p or pg2 not in p:
                continue

            if not re.search(pg_regex, p):
                invalid_pages.append(p)
                break

# I need to recheck these again until NO CHANGES

    print(page_order)

    corrected = []
    for p in invalid_pages:
        numbers = [int(x) for x in p.split(",")]
        more_changes = True

        while more_changes:
            more_changes = False
            for pg_chk in page_order:
                pg1, pg2 = pg_chk
                
                try:
                    index1 = numbers.index(pg1)
                    index2 = numbers.index(pg2)
                except ValueError:
                    continue

                # Not in correct order
                if index1 > index2:
                    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
                    more_changes = True

        corrected.append(numbers[:])

    print(corrected)

    tot = 0
    for v in corrected:
        tot += v[len(v) // 2]

    return tot


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
