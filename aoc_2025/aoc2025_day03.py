# # https://adventofcode.com/2025/day/3 🏆

import pathlib
import time
from typing import Callable, List, Union

  # <-- ADD THIS LINE

# --- Configuration (These lines are mandatory for the refactor script) ---
CURRENT_AOC_YEAR = 2025
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = 3
# ---------------------

# Format the day number to a two-digit string (e.g., 1 -> "01")
DAY_FOLDER_NAME = f"d{DAY_NUMBER:02d}"

# --- Path Finding Logic ---

script_path = pathlib.Path(__file__).parent
data_root = script_path / "data"
data_day_path = data_root / DAY_FOLDER_NAME

# Construct the final file paths
soln_file = data_day_path / "input.txt"
test_file = data_day_path / "test.txt"

# --- Functions from Original Script (Do Not Remove Placeholders) ---

# 

# --- Solving Functions ---


def part1(data: List[Union[str, list]]):
    """Solve part 1"""
    pass # Your solution for Part 1 goes here


def part2(data: List[Union[str, list]]):
    """Solve part 2"""
    pass # Your solution for Part 2 goes here


def solve(puzzle_input: pathlib.Path, parse_func: Callable, run="Solution"):
    """Solve the puzzle for the given input, using the specified parser"""
    times = []

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
    print(f"\n🎄 Advent of Code {CURRENT_AOC_YEAR} Day {DAY_NUMBER} 🎄")

    # 📌 SELECT THE DAY-SPECIFIC PARSER
    SELECTED_PARSER = parse

    print(f"Loading data from folder: **{DAY_FOLDER_NAME}**")
    print(f"Using parser: **{SELECTED_PARSER.__name__}**\n")

    # Run tests first
    tests = solve(test_file, parse_func=SELECTED_PARSER, run="Test")

    print("---")
    # Run the actual solution
    solutions = solve(soln_file, parse_func=SELECTED_PARSER)
