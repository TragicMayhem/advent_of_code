# {AOC_URL_PLACEHOLDER} 🏆

import pathlib
import time
from typing import Callable, List, Union, Any


{EXTRA_IMPORTS_PLACEHOLDER}
# ----------------------------------

# --- Configuration ---
CURRENT_AOC_YEAR = {AOC_YEAR_PLACEHOLDER}
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = {AOC_DAY_PLACEHOLDER}
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
soln_file = data_day_path / "input.txt"
test_file = data_day_path / "test.txt"


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


# --- Custom Helper Functions ---
# Utility functions for common AOC tasks.


# --- Solving Functions ---


def part1(data: List[Union[str, list]]):
    """Solve part 1"""

    pass


def part2(data: List[Union[str, list]]):
    """Solve part 2"""
    pass


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
    SELECTED_PARSER = parse_lines
    # SELECTED_PARSER = parse_blocks

    print(f"Loading data from folder: **{DAY_FOLDER_NAME}**")
    print(f"Using parser: **{SELECTED_PARSER.__name__}**\n")

    # Run tests first
    tests = solve(test_file, parse_func=SELECTED_PARSER, run="Test")

    print("---")
    # Run the actual solution
    solutions = solve(soln_file, parse_func=SELECTED_PARSER)
