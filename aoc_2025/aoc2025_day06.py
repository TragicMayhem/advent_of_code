# # https://adventofcode.com/2025/day/6 🏆

import pathlib
import time
from typing import Callable, List, Union, Any
import operator

# --- Configuration (These lines are mandatory for the refactor script) ---
CURRENT_AOC_YEAR = 2025
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = 6
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
soln_file = data_day_path / "input.txt"  # 4580995422905 / 10875057285868
test_file = data_day_path / "test.txt"  # 4277556 / 3263827

# ----------------------------------
# Define the mapping of string symbols to actual Python functions
# operator.add is equivalent to num1 + num2
# operator.mul is equivalent to num1 * num2
OP_MAP = {"+": operator.add, "*": operator.mul}


def parse_lines(puzzle_input: pathlib.Path) -> List[str]:
    """
    Parse input line-by-line.
    Returns a list where each element is one line (string) from the input file,
    stripped of surrounding whitespace (including the newline character).
    """
    content = puzzle_input.read_text(encoding="UTF-8")
    # Splits by newline, strips whitespace from each line, and filters out empty lines.
    lst = [line for line in content.split("\n") if line.strip()]
    return lst


# def parse_vertical_blocks_pt1(data: List[str]) -> List[str]:
#     """ """
#     lines = [line.replace("  ", " ").split() for line in data if line.strip()]

#     # cant use zip, the test data is 4 lines and the input data is 5 lines.
#     # need to * unzip the lines instead. into a zip statement to capture all lines

#     # Use zip() to aggregate the elements by their index
#     # zipped_result_iterator = zip(lines[0], lines[1], lines[2], lines[3])
#     zipped_result_iterator = zip(*lines)

#     # Convert the iterator to a list for viewing the final result
#     final_list = list(zipped_result_iterator)

#     # print(final_list)
#     return final_list


# --- Solving Functions ---


def part1(data: List[Union[str, list]]):
    """Solve part 1"""

    lines = [line.replace("  ", " ").split() for line in data if line.strip()]

    # cant use zip, the test data is 4 lines and the input data is 5 lines.
    # need to * unzip the lines instead. into a zip statement to capture all lines
    # Use zip() to aggregate the elements by their index
    # zipped_result_iterator = zip(lines[0], lines[1], lines[2], lines[3])

    data = list(zip(*lines))

    total = 0

    for calc in data:
        # print(calc)

        op = calc[-1]
        operation_function = OP_MAP.get(op)

        tmp = 1 if op == "*" else 0

        if operation_function:
            for c in calc[:-1]:
                num = int(c)
                tmp = operation_function(tmp, num)
        else:
            raise ValueError(f"Unknown operator indicator: {op}")

        total += tmp

    return total


def part2(data: List[Union[str, list]]):
    """Solve part 2"""

    data = list(zip(*data))

    current_block = []
    final_results = []
    total = 0

    operator_row_index = len(data[0]) - 1

    # print(data)
    for d in data:

        is_data_blank = all(c.isspace() for c in d)

        if is_data_blank:
            # print("Skipping blank data row")
            # print(f"current_block: {current_block}")
            final_results.append(tuple(current_block))
            current_block = []
            continue

        op = d[operator_row_index].strip()

        if op:
            current_block.append(op)

        data_part = d[:operator_row_index]
        # reversed_data = tuple(data_part)[::-1]
        # print(f"op: {op} data_part: {data_part}")

        current = "".join(data_part).strip()
        if current:
            current_block.append(int(current))

    if current_block:
        final_results.append(tuple(current_block))

    # print(f"Final current_block: {final_results}")

    for calc in final_results:
        op = calc[0]
        operation_function = OP_MAP.get(op)
        tmp = 1 if op == "*" else 0

        if operation_function:
            for c in calc[1:]:
                num = int(c)
                tmp = operation_function(tmp, num)
        else:
            raise ValueError(f"Unknown operator indicator: {op}")

        total += tmp

    return total


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
