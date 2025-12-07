# # https://adventofcode.com/2025/day/7 🏆

import pathlib
import time
from typing import Callable, List, Union, Any


# ----------------------------------

# --- Configuration ---
CURRENT_AOC_YEAR = 2025
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = 7
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
soln_file = data_day_path / "input.txt"  # 1518 /
test_file = data_day_path / "test.txt"  # 21 /


# --- Parsing Functions ---
def parse_lines(puzzle_input: pathlib.Path) -> List[str]:
    """ """
    content = puzzle_input.read_text(encoding="UTF-8")
    # Splits by newline, strips whitespace from each line, and filters out empty lines.
    lst = [line.strip() for line in content.splitlines() if line.strip()]

    splitters = list()
    start = None

    for r, l in enumerate(lst):
        for c, char in enumerate(l):
            if not start and char == "S":
                start = (r, c)

            splitters.append((r, c)) if char == "^" else None

    splitters = tuple(splitters)
    height = len(lst)
    width = len(lst[0]) if lst else 0

    return start, splitters, (height, width)


# --- Custom Helper Functions ---
# Utility functions for common AOC tasks.
def manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    """Calculate the Manhattan distance between two points a and b."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean_distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    """Calculate the Euclidean distance between two points a and b."""
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def grid_neighbors(
    pos: tuple[int, int], max_rows: int, max_cols: int
) -> List[tuple[int, int]]:
    """Get valid neighboring positions in a grid."""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []

    for dr, dc in directions:
        new_r, new_c = pos[0] + dr, pos[1] + dc
        if 0 <= new_r < max_rows and 0 <= new_c < max_cols:
            neighbors.append((new_r, new_c))

    return neighbors


def move_in_direction(
    pos: tuple[int, int], direction: tuple[int, int], steps: int = 1
) -> tuple[int, int]:
    """Move a position in a specified direction by a number of steps."""
    return (pos[0] + direction[0] * steps, pos[1] + direction[1] * steps)


# --- Solving Functions ---


def part1(data: List[Union[str, list]]):
    """Solve part 1"""

    start, splitter_positions, grid_size = data
    h, w = grid_size
    splitters_used = set()
    visited_beams = set()
    # need function to split paths at splitters
    # remove the old beam, and add in two new ones eiether side of the splitter

    beams = [(start, (1, 0))]  # starting beam going down

    # need to check beam direction
    # for now just assume downwards, stop at splitterid

    while beams:
        beam_pos, beam_dir = beams.pop(0)

        check_below = move_in_direction(beam_pos, beam_dir)
        # print("Beam at:", beam_pos, "going", beam_dir)
        # print("Checking below at:", check_below)

        if (check_below, beam_dir) in visited_beams:
            # print("Skipping visited beam:", check_below, "going", beam_dir)
            continue  # Skip to the next beam

        visited_beams.add((check_below, beam_dir))

        # loop until we hit a splitter and within bounds
        while check_below not in splitter_positions and check_below[0] < h:  #
            # print("  Moving to:", check_below)
            beam_pos = check_below
            check_below = move_in_direction(beam_pos, beam_dir)

        # print("  Stopped at:", beam_pos)
        if check_below[0] >= h:
            continue

        # check if splitter below beam position
        if check_below in splitter_positions and check_below[0] < h:
            # print("Splitter at:", check_below)
            splitters_used.add(check_below)

            split_beam_right = (check_below[0], check_below[1] + 1)
            split_beam_left = (check_below[0], check_below[1] - 1)

            if split_beam_right not in visited_beams:
                beams.append((split_beam_right, beam_dir))

            if split_beam_left not in visited_beams:
                beams.append((split_beam_left, beam_dir))

            # beams.append((split_beam_right, (1, 0)))  # right
            # beams.append((split_beam_left, (1, 0)))  # left

        # print(beams)
        # print(splitters_used)

    return len(splitters_used)


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
