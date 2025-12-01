# https://adventofcode.com/2025/day/2

import pathlib
import time
from typing import Callable, List, Union

# --- Configuration ---
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = 1  # <--- CHANGE THIS VALUE FOR EACH DAY!

# Format the day number to a two-digit string (e.g., 1 -> "01", 12 -> "12")
DAY_FOLDER_NAME = f"d{DAY_NUMBER:02d}"

# --- Path Finding Logic ---

# Get the path where this script is located (the project root folder)
script_path = pathlib.Path(__file__).parent

# data_root is the 'data' folder located in the same directory as the script
data_root = script_path / "data"

# data_day_path is the subfolder inside 'data' (e.g., .../data/d01)
data_day_path = data_root / DAY_FOLDER_NAME

# Construct the final file paths
soln_file = data_day_path / "input.txt"
test_file = data_day_path / "test.txt"

# --- Parsing Functions ---


def parse_lines(puzzle_input: pathlib.Path) -> List[str]:
    """
    Parse input line-by-line.
    """
    content = puzzle_input.read_text(encoding="UTF-8")
    lst = [line.strip() for line in content.split("\n") if line.strip()]

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

    return 1


def part2(data: List[Union[str, list]]):
    """Solve part 2"""

    return 1


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
