# https://adventofcode.com/2024/day/2 🏆

import pathlib
import time
from typing import Callable, List, Union, Tuple
from itertools import tee  # Import for Pythonic sequence checking

# --- Configuration ---
CURRENT_AOC_YEAR = 2024
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = 2
# ---------------------

# Format the day number to a two-digit string (e.g., 2 -> "02")
DAY_FOLDER_NAME = f"d{DAY_NUMBER:02d}"

# --- Path Finding Logic ---

# Get the path where this script is located (the year folder, e.g., 'aoc_2024')
script_path = pathlib.Path(__file__).parent

# data_root is the 'data' folder, which is a sibling of the script
data_root = script_path / "data"

# data_day_path is the subfolder inside 'data' (e.g., .../data/d02)
data_day_path = data_root / DAY_FOLDER_NAME

# Construct the final file paths
soln_file = data_day_path / "input.txt"
test_file = data_day_path / "test.txt"
test_file2 = data_day_path / "test2.txt"  # Added your second test file


# --- Parsing Functions ---


def parse(puzzle_input: pathlib.Path) -> List[List[int]]:
    """
    Parse input. Reads each line, splits by space, and converts to a list of integers.
    """
    content = puzzle_input.read_text(encoding="UTF-8")

    # Read each line, strip whitespace, split by any whitespace, and convert elements to int
    lst = [
        [int(s) for s in line.split()]  # split() handles multiple spaces gracefully
        for line in content.strip().split("\n")
        if line.strip()  # Filter out empty lines
    ]

    return lst


# --- Helper Functions (Refactored) ---


def check_sequence(sequence: List[int]) -> bool:
    """
    Checks if a sequence is 'safe':
    1. All differences (abs) must be between 1 and 3 (inclusive).
    2. The direction (increasing/decreasing) must remain constant.

    Uses Pythonic list zipping to compare adjacent elements.
    """
    if len(sequence) < 2:
        return True

    # Create two iterators, offset by one, to compare adjacent elements (a, b)
    a, b = tee(sequence)
    next(b, None)

    # Calculate differences and directions for all pairs
    diffs_and_dirs = []
    for num_a, num_b in zip(a, b):
        diff = num_b - num_a
        diffs_and_dirs.append(
            {
                "abs_diff": abs(diff),
                "direction": 1 if diff > 0 else (-1 if diff < 0 else 0),
            }
        )

    # Check 1: All absolute differences must be in [1, 3]
    if not all(1 <= d["abs_diff"] <= 3 for d in diffs_and_dirs):
        return False

    # Check 2: Direction must be constant (non-zero directions only)
    directions = [d["direction"] for d in diffs_and_dirs if d["direction"] != 0]

    # If all directions are the same, the set of unique directions must have size 1
    if len(set(directions)) > 1:
        return False

    return True


# --- Solving Functions ---


def part1(data: List[List[int]]):
    """Solve part 1: Count safe sequences."""

    safe_count = 0
    for sequence in data:
        if check_sequence(sequence):
            safe_count += 1

    return safe_count


def part2(data: List[List[int]]):
    """Solve part 2: Count sequences that are safe or can be made safe by removing one element."""

    safe_count = 0

    for original_sequence in data:
        # Check if the original sequence is safe
        if check_sequence(original_sequence):
            safe_count += 1
            continue

        # If not safe, try removing one element and checking the remaining sequence
        made_safe = False

        # Iterate through all possible indices to remove
        for i in range(len(original_sequence)):
            # Create a new sequence with the element at index i removed
            modified_sequence = original_sequence[:i] + original_sequence[i + 1 :]

            if check_sequence(modified_sequence):
                made_safe = True
                break  # Found a valid removal, stop checking other removals

        if made_safe:
            safe_count += 1

    return safe_count


def solve(puzzle_input: pathlib.Path, run="Solution"):
    """Solve the puzzle for the given input, using the specified parser"""
    times = []

    # Check if the file exists before attempting to parse
    if not puzzle_input.exists():
        print(
            f"Error: Input file not found at **{puzzle_input.resolve()}**. Skipping {run}."
        )
        return None, None, [0, 0, 0]

    # The data is parsed only once
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
    print(f"\n🎄 Advent of Code {CURRENT_AOC_YEAR} Day {DAY_NUMBER} 🎄")

    print(f"Loading data from folder: **{DAY_FOLDER_NAME}**")

    # Run tests first
    tests = solve(test_file, run="Test 1")

    print("---")
    tests2 = solve(test_file2, run="Test 2")

    print("---")
    # Run the actual solution
    solutions = solve(soln_file)
