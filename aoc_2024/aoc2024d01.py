# https://adventofcode.com/2024/day/1 🏆

import pathlib
import time
from typing import Callable, List, Union
from collections import Counter

# --- Configuration ---
CURRENT_AOC_YEAR = 2024  # <-- YEAR UPDATED TO 2024
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = 1
# ---------------------

# Format the day number to a two-digit string (e.g., 1 -> "01")
DAY_FOLDER_NAME = f"d{DAY_NUMBER:02d}"

# --- Path Finding Logic ---

# Get the path where this script is located (the year folder, e.g., 'aoc_2024')
script_path = pathlib.Path(__file__).parent

# data_root is the 'data' folder, which is a sibling of the script within the year folder
data_root = script_path / "data"

# data_day_path is the subfolder inside 'data' (e.g., .../data/d01)
data_day_path = data_root / DAY_FOLDER_NAME

# Construct the final file paths
soln_file = data_day_path / "input.txt"
test_file = data_day_path / "test.txt"

# --- Parsing Functions ---


def parse_day_specific(puzzle_input: pathlib.Path) -> List[tuple]:
    """
    Parse input using the specific logic required for Day 1.
    Reads lines, splits by space, converts to int tuples (l, r).
    """

    content = puzzle_input.read_text(encoding="UTF-8")

    lst = []
    for line in content.split("\n"):
        if not line.strip():
            continue

        try:
            # Original logic: replace "   " with " " and split.
            # A more robust alternative would be: parts = line.split()
            # (which handles any number of spaces), but keeping your original for now.
            parts = line.replace("   ", " ").split(" ")
            l, r = parts[0], parts[1]
            lst.append((int(l), int(r)))
        except IndexError as e:
            print(f"Skipping malformed line: '{line}' - Error: {e}")

    return lst


# --- Solving Functions ---


def part1(data: List[tuple]):
    """Solve part 1 - Calculates the sum of absolute differences after sorting."""

    left_list = []
    right_list = []
    for l, r in data:
        left_list.append(l)
        right_list.append(r)

    left_list.sort()
    right_list.sort()

    tot = 0
    for l, r in zip(left_list, right_list):
        diff = abs(l - r)
        tot += diff

    return tot


def part2(data: List[tuple]):
    """Solve part 2 - Calculates the sum of similarities (l * count of r)"""

    left_list = []
    right_list = []
    for l, r in data:
        left_list.append(l)
        right_list.append(r)

    right_counter = Counter(right_list)
    tot_sim = 0

    for l in left_list:
        if l in right_counter:
            tot_sim += l * right_counter[l]

    return tot_sim


def solve(puzzle_input: pathlib.Path, parse_func: Callable, run="Solution"):
    """Solve the puzzle for the given input, using the specified parser"""
    times = []

    # Check if the file exists before attempting to parse
    if not puzzle_input.exists():
        print(
            f"Error: Input file not found at **{puzzle_input.resolve()}**. Skipping {run}."
        )
        return None, None, [0, 0, 0]

    # The data is parsed only once
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
    SELECTED_PARSER = parse_day_specific

    print(f"Loading data from folder: **{DAY_FOLDER_NAME}**")
    print(f"Using parser: **{SELECTED_PARSER.__name__}**\n")

    # Run tests first
    tests = solve(test_file, parse_func=SELECTED_PARSER, run="Test")

    print("---")
    # Run the actual solution
    solutions = solve(soln_file, parse_func=SELECTED_PARSER)
