# https://adventofcode.com/2025/day/2

import pathlib
import re
import time
from typing import Callable, List, Union

CURRENT_AOC_YEAR = 2025
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = 4
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
soln_file = data_day_path / "input.txt"  # 23560874270 / 44143124633
test_file = data_day_path / "test.txt"  # 1227775554 / 4174379265

# --- Parsing Functions ---


def parse_lines(puzzle_input: pathlib.Path) -> List[str]:
    """
    Parse input line-by-line.
    """
    content = puzzle_input.read_text(encoding="UTF-8")
    lst = [
        tuple(r.split("-"))
        for r in [line.strip() for line in content.split(",") if line.strip()]
    ]
    return lst


def parse_blocks(puzzle_input: pathlib.Path) -> List[str]:
    """
    Parse input into blocks of data separated by double newlines ("\n\n").
    """
    content = puzzle_input.read_text(encoding="UTF-8")
    lst = content.strip().split("\n\n")

    return lst


# --- Solving Functions ---


def part1(data: List[Union[str, list]]):
    """Solve part 1"""

    invalid_id = []

    for d in data:
        # print("\n", d)
        s, t = d
        for i in range(int(s), int(t) + 1):
            current = str(i)
            m = len(current) // 2
            if current[:m] == current[m:]:
                # print(current)
                invalid_id.append(i)

    total = sum(invalid_id)

    return total


def part2(data: List[Union[str, list]]):
    """Solve part 2"""

    invalid_id = []

    for d in data:
        # print("\n", d)
        s, t = d
        for i in range(int(s), int(t) + 1):
            current = str(i)
            m = len(current) // 2

            # Regex Breakdown:
            # 1. '^'        -> Anchors the match to the start of the string.
            # 2. '(.+?)'    -> Captures the shortest possible pattern P (e.g., '12').
            # 3. '\1+'      -> Checks if that captured pattern P repeats 1 or more times.
            # 4. '$'        -> Anchors the match to the end of the string, ensuring the entire number is covered.

            match = re.fullmatch(r"^(.+?)\1+$", current)

            if match:
                invalid_id.append(i)
            #     # match.group(1) is the core pattern (e.g., '12')
            #     # match.group(0) is the full match (e.g., '1212')
            #     num_repeats = len(current) // len(match.group(1))
            #     ans = (True, match.group(1), num_repeats)
            # else:
            #     ans = (False, None, None)

    total = sum(invalid_id)

    return total


def solve(puzzle_input: pathlib.Path, parse_func: Callable, run="Solution"):
    """Solve the puzzle for the given input, using the specified parser"""
    times = []

    # Check if the file exists before attempting to parse
    if not puzzle_input.exists():
        print(
            f"Error: Input file not found at **{puzzle_input.resolve()}**. Skipping {run}."
        )
        return None, None, [0, 0, 0]

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
    print(f"\n🎄 Advent of Code Day {DAY_NUMBER} 🎄")

    # 📌 CHOOSE YOUR PARSER HERE
    SELECTED_PARSER = parse_lines
    # SELECTED_PARSER = parse_blocks

    print(f"Loading data from folder: **{DAY_FOLDER_NAME}**")
    print(f"Using parser: **{SELECTED_PARSER.__name__}**\n")

    # Run tests first
    tests = solve(test_file, parse_func=SELECTED_PARSER, run="Test")

    print("---")
    # Run the actual solution
    solutions = solve(soln_file, parse_func=SELECTED_PARSER)
