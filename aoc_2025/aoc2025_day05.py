# # https://adventofcode.com/2025/day/5 🏆

import pathlib
import time
from typing import Callable, List, Union, Any
from operator import itemgetter

CURRENT_AOC_YEAR = 2025
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = 5
# ---------------------

# Format the day number to a two-digit string (e.g., 1 -> "01")
DAY_FOLDER_NAME = f"d{DAY_NUMBER:02d}"

# --- Path Finding Logic ---

# Find the project root relative to the script location. This assumes
# the script is executed from the AOC year folder or a sibling folder.
script_path = pathlib.Path(__file__).parent
data_root = script_path / "data"
data_day_path = data_root / DAY_FOLDER_NAME

# Construct the final file paths
soln_file = data_day_path / "input.txt"  # 896 / 346240317247002
test_file = data_day_path / "test.txt"  # 3 / 14

# 315999402978300 too low


# --- Parsing Functions ---
def parse_lines(puzzle_input: pathlib.Path) -> List[str]:
    """
    Parse input line-by-line.
    Returns a list where each element is one line (string) from the input file,
    stripped of surrounding whitespace (including the newline character).
    """
    content = puzzle_input.read_text(encoding="UTF-8")
    # Splits by newline, strips whitespace from each line, and filters out empty lines.
    lst = [line.strip() for line in content.splitlines() if line.strip()]

    return lst


def parse_blocks(puzzle_input: pathlib.Path) -> List[str]:
    """
    Parse input into blocks of data separated by double newlines ("\n\n").
    Returns a list of strings, where each string is a block.
    """
    content = puzzle_input.read_text(encoding="UTF-8")
    # Strips overall content and then splits by double newline.
    lst = content.strip().split("\n\n")

    return lst


def parse_blocks_and_process(puzzle_input: pathlib.Path) -> List[str]:
    """ """
    content = puzzle_input.read_text(encoding="UTF-8")
    # Strips overall content and then splits by double newline.
    blocks = content.strip().split("\n\n")

    if len(blocks) != 2:
        return []

    # two blocks return
    # first is ranges to be split by - and converted to int tuples list
    # second is list of numbers to be checked against ranges
    fresh_ranges = []
    for line in blocks[0].splitlines():
        start, end = map(int, line.split("-"))

        fresh_ranges.append(((start, end)))

    check_list = [int(x) for x in blocks[1].splitlines() if x.strip()]

    return fresh_ranges, check_list


# --- Custom Helper Functions ---
# Utility functions for common AOC tasks.


# --- Solving Functions ---


def part1(data: List[Union[str, list]]):
    """Solve part 1"""

    ranges, check_list = data
    fresh_count = 0

    # check each number in check_list against all ranges
    for number in check_list:
        for start, end in ranges:
            if start <= number <= end:
                fresh_count += 1
                break

    return fresh_count


def part2(data: List[Union[str, list]]):
    """Solve part 2"""

    ranges, _ = data

    fresh_id_count = 0

    # works for test set but the ranges are too big for the real set
    # for start, end in ranges:
    #     for i in range(start, end + 1):
    #         fresh_id_set.add(i)5

    # Google Technique: Maths - Need to sort the ranges first, then merge overlapping ranges
    sorted_ranges = sorted(ranges, key=itemgetter(0))
    # I was sorted on the END of the RANGE - which is WRONG!!!
    # sorted_ranges = sorted(ranges, key=itemgetter(1))

    print(f"Sorted Ranges: {len(sorted_ranges)} ranges")

    merged_ranges = [sorted_ranges.pop(0)]

    for current_start, current_end in sorted_ranges:
        last_start, last_end = merged_ranges[-1]
        # Check for overlap, adjacent ranges are considered overlapping
        if current_start <= last_end + 1:
            # Overlapping ranges, merge them
            merged_ranges[-1] = (last_start, max(last_end, current_end))
            # merged_ranges[-1][1] = max(last_end, current_end)
        else:
            # No overlap, add the current range
            merged_ranges.append((current_start, current_end))

    # print(f"Merged Ranges: {merged_ranges}")

    # I do not NEED to know the numbers themselves, just the count of unique numbers!!!
    # for start, end in merged_ranges:
    #     print(f"Adding range: {start}-{end}")
    #     for i in range(start, end + 1):
    #         fresh_id_set.add(i)

    print(f"Merged Ranges: {len(merged_ranges)} ranges")

    for start, end in merged_ranges:
        range_length = end - start + 1
        print(f"Adding range: {start}-{end} (Count: {range_length})")
        # Instead of adding each number, just keep track of the count
        fresh_id_count += range_length

    return fresh_id_count


def solve(puzzle_input: pathlib.Path, parse_func: Callable, run="Solution"):
    """Solve the puzzle for the given input, using the specified parser"""
    times = []

    if not puzzle_input.exists():
        print(
            f"Error: Input file not found at **{puzzle_input.resolve()}**. Skipping {run}."
        )
        return None, None, [0, 0, 0]

    # Use the selected parser function to transform the file path into processed data
    data = parse_func(puzzle_input)

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
    print(f"\n🎄 Advent of Code {CURRENT_AOC_YEAR} Day {DAY_NUMBER} 🎄")

    # 📌 SELECT THE DAY-SPECIFIC PARSER
    # By default, this points to the generic 'parse' function above.
    # If you define a new custom parser (e.g., 'parse_grid'), change it here.
    SELECTED_PARSER = parse_blocks_and_process
    # SELECTED_PARSER = parse_lines
    # SELECTED_PARSER = parse_blocks

    print(f"Loading data from folder: **{DAY_FOLDER_NAME}**")
    print(f"Using parser: **{SELECTED_PARSER.__name__}**\n")

    # Run tests first
    tests = solve(test_file, parse_func=SELECTED_PARSER, run="Test")

    print("---")
    # Run the actual solution
    solutions = solve(soln_file, parse_func=SELECTED_PARSER)
