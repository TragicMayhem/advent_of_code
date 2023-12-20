# https://adventofcode.com/2023/day/3

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 529618 / 77509019
test_file = script_path / "test.txt"  # 4361 / 467835


# Previous AOC
def get_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


# Previous AOC
def get_coords8d(r, c, h, w):
    for delta_r, delta_c in (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def check_all_position(num_start, num_end, row, h, w, grid):
    found_symbol = False
    for s in range(num_start, num_end):
        for i, j in get_coords8d(row, s, h, w):
            val = grid[i][j]

            if val.isdigit():
                continue
            if val == ".":
                continue

            found_symbol = True
            break

    return found_symbol


def find_parts(num_start, num_end, row, h, w, grid):
    # List the points on grid for matches around the gear. Might be same part
    found_parts = []
    for s in range(num_start, num_end):
        for i, j in get_coords8d(row, s, h, w):
            val = grid[i][j]

            if val == ".":
                continue
            if val.isdigit():
                found_parts.append((i, j))

    return found_parts


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        #  Read each line (split \n) and form a list of strings
        lines = file.read().split("\n")

    return lines


def part1(lines):
    """Solve part 1"""

    # loop but what level
    # check for a digit, extrat number anyway temp
    # check each digit in number and all around for at least on symbol - not . and not digit
    # if find stop, store number
    # need to look at all digits, so need to get length of the number and then loop through that coords
    # either way skip to the end of the number and check the next position

    dig_pattern = re.compile(r"(\d+)")
    height = len(lines)
    width = len(lines[0])

    grid = [[c for c in l] for l in lines]
    valid_parts = []

    for r in range(height):
        # temp = re.findall(dig_pattern, line)
        # print('findall', temp)

        tmp_search = re.search(dig_pattern, lines[r])
        # print('tmp_search',tmp_search)

        count = 0
        for match in re.finditer(dig_pattern, lines[r]):
            count += 1
            # print("match", count, match.group(), "start index", match.start(), "End index", match.end())
            # print(list(get_coords8d(match.start(), match.end(), height, width)))
            if check_all_position(match.start(), match.end(), r, height, width, grid):
                valid_parts.append(int(match.group()))

    # print("Valid parts", valid_parts)

    return sum(valid_parts)


def part2(lines):
    """Solve part 2"""

    gear_pattern = re.compile(r"\*")
    dig_pattern = re.compile(r"(\d+)")
    height = len(lines)
    width = len(lines[0])

    grid = [[c for c in l] for l in lines]
    valid_ratios = []

    for r in range(height):
        gear_search = re.search(gear_pattern, lines[r])
        # print('gear_search',gear_search)

        for match in re.finditer(gear_pattern, lines[r]):
            # print("\nmatch", match.group(), "start index", match.start(), "End index", match.end())
            # print(list(get_coords8d(match.start(), match.end(), height, width)))

            # List the points on grid for matches around the gear. Might be same part
            part_coords = find_parts(match.start(), match.end(), r, height, width, grid)
            part_coords.sort()
            # print('part_coords ',part_coords)

            # need to be careful of 2 points but same numbers so not valid
            parts = set()

            for i, j in part_coords:
                for match in re.finditer(dig_pattern, lines[i]):
                    # print("match", match.group(), "start index", match.start(), "End index", match.end())

                    if match.start() <= j <= match.end():
                        # Store number and position, to allow for sets to remove dups
                        parts.add((match.group(), (match.start(), match.end())))

            if len(parts) > 1:
                ratio = 1
                for num, coords in parts:
                    # print(num)
                    ratio *= int(num)
                # print("ratio ", ratio)
                valid_ratios.append(ratio)

    # print("Valid ratios", valid_ratios)

    return sum(valid_ratios)


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
