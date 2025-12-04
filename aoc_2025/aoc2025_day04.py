# # https://adventofcode.com/2025/day/4 🏆

import pathlib
import time
from typing import Callable, List, Union, Any
from collections import defaultdict

# --- Configuration (These lines are mandatory for the refactor script) ---
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
soln_file = data_day_path / "input.txt"
test_file = data_day_path / "test.txt"  # 13 / 1370


# --- Parsing Functions ---


def parse_lines(puzzle_input: pathlib.Path) -> List[str]:
    """
    Parse input line-by-line.
    """
    grid = defaultdict(str)
    content = puzzle_input.read_text(encoding="UTF-8")

    data = [
        tuple(list(r))
        for r in [line.strip() for line in content.split("\n") if line.strip()]
    ]

    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell == "@":
                grid[(r, c)] = cell

    size = len(data)

    # print(grid)
    return (grid, size)


# Any helper functions extracted from older scripts or specific to this day


# Assumes square grid: h = w
def get_coords8d(pos, s):
    r, c = pos
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
        if 0 <= rr < s and 0 <= cc < s:
            yield (rr, cc)


def find_rolls_8d(pos, grid, size):
    check_rolls_8d = list()
    # How many rolls around this position?
    for g in list(get_coords8d(pos, size)):
        if g in grid:
            check_rolls_8d.append(g)

    if len(check_rolls_8d) < 4:
        return True

    return False


# --- Solving Functions ---


def part1(data: List[Union[str, list]]):
    """Solve part 1"""

    rolls, size = data
    accessible = list()

    for pos in rolls:
        check_rolls_8d = list()

        # How many rolls around this position?
        for g in list(get_coords8d(pos, size)):
            if g in rolls:
                check_rolls_8d.append(g)

        if len(check_rolls_8d) < 4:
            accessible.append(pos)

    return len(accessible)


def part2(data: List[Union[str, list]]):
    """Solve part 2"""

    rolls, size = data
    processing_rolls = rolls.copy()
    rolls_removed = 0
    still_accessible = True

    while still_accessible:
        still_accessible = False
        to_remove = []
        for pos in processing_rolls:
            if find_rolls_8d(pos, processing_rolls, size):
                to_remove.append(pos)
                still_accessible = True

        for pos in to_remove:
            del processing_rolls[pos]
            rolls_removed += 1

    # print(f"Rolls removed: {rolls_removed}")

    return rolls_removed


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
