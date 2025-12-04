# # https://adventofcode.com/2025/day/3 🏆

import pathlib
import time
from typing import Callable, List, Union
from itertools import combinations

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
soln_file = data_day_path / "input.txt"  # 17412
test_file = data_day_path / "test.txt"  # 357 / 3121910778619


# --- Parsing Functions ---


def parse_lines(puzzle_input: pathlib.Path) -> List[str]:
    """
    Parse input line-by-line.
    Returns a list where each element is one line (string) from the input file,
    stripped of surrounding whitespace (including the newline character).
    """
    content = puzzle_input.read_text(encoding="UTF-8")
    # Splits by newline, strips whitespace from each line, and filters out empty lines.
    lst = [line.strip() for line in content.split("\n") if line.strip()]
    lst = [(s[0], int(s[1:])) for s in lst]
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


from typing import List, Tuple, Optional
import pathlib


def parse_lines_to_tuples_generic(
    puzzle_input: pathlib.Path, separator: Optional[str] = None
) -> List[Tuple[int, ...]]:
    """
    Reads the input file line-by-line and converts each line into a tuple of integers.

    - If 'separator' is None (default), the function treats each character as an
      individual integer (e.g., "123" -> (1, 2, 3)).
    - If 'separator' is provided (e.g., ',' or ' '), it splits the line using that
      separator (e.g., "1,2,3" -> (1, 2, 3)).

     Args:
        puzzle_input: A pathlib.Path object pointing to the input file.
        separator: The character used to split numbers within a line. Defaults to None.

    Returns:
        A list of tuples, where each tuple contains integers from one line.
    """
    # Read the content and split into lines, filtering out empty ones
    content = puzzle_input.read_text(encoding="UTF-8")
    lines = [line.strip() for line in content.split("\n") if line.strip()]

    list_of_tuples = []

    for line in lines:
        # Determine the splitting method based on the 'separator' parameter
        if separator is None:
            # Case 1: No separator provided, treat each character as a number.
            # E.g., line "1234" becomes ['1', '2', '3', '4']
            str_numbers = list(line)
        else:
            # Case 2: Separator provided, split the line using it.
            # E.g., line "1-2-3-4" with separator='-' becomes ['1', '2', '3', '4']
            str_numbers = line.split(separator)

        # Convert the list of string numbers to a tuple of integers.
        # We include 'if n' to filter out potential empty strings resulting from
        # splitting (e.g., from a trailing separator or multiple separators).
        int_tuple = tuple(int(n) for n in str_numbers if n)
        list_of_tuples.append(int_tuple)

    return list_of_tuples


# --- Solving Functions ---
def find_highest_number_from_combinations(
    int_tuple: Tuple[int, ...], combination_size: int = 2
) -> Union[int, None]:
    """
    Finds the highest number that can be formed by taking combinations of
    `combination_size` digits from the input tuple, preserving their
    original relative order.

    The digits in each combination are concatenated to form the number.
    e.g., combination_size=3, (8, 1, 9) forms 819.

    Args:
        int_tuple: A tuple of integers (single digits recommended, but works with any).
        combination_size: The number of elements to combine from the tuple. Defaults to 2.

    Returns:
        The highest number formed, or None if the tuple has fewer than
        combination_size elements.
    """
    if len(int_tuple) < combination_size:
        return None

    # Use itertools.combinations to get all unique tuples of size 'combination_size'
    # while preserving relative order.
    #
    # The generator converts each tuple of ints (e.g., (8, 1, 9)) into strings,
    # joins them ("819"), and converts the final string back to an integer (819).
    generated_numbers = (
        int("".join(map(str, combo)))
        for combo in combinations(int_tuple, combination_size)
    )

    # Find the maximum value from the generated numbers
    return max(generated_numbers)


def find_highest_number_greedy(
    int_tuple: Tuple[int, ...], combination_size: int = 2
) -> Union[int, None]:
    """
    Finds the highest number that can be formed by taking an ordered subsequence
    of `combination_size` digits from the input tuple.

    *OPTIMIZED STRATEGY:* Uses a highly efficient greedy algorithm (O(k * N))
    which is necessary for large inputs.

    The digits in the selected subsequence are concatenated to form the number.
    e.g., combination_size=3, (8, 1, 9) forms 819.

    Args:
        int_tuple: A tuple of integers (single digits recommended).
        combination_size: The number of elements to select. Defaults to 2.

    Returns:
        The highest number formed, or None if the tuple has fewer than
        combination_size elements.
    """
    n = len(int_tuple)
    k = combination_size

    if n < k:
        return None

    result_digits: List[int] = []
    current_index = 0

    for i in range(k):
        # We need to select 'k - i' more digits.
        # The search must stop at an index that leaves exactly 'k - i - 1' digits
        # available to be selected later.
        # max_search_stop is the index *exclusive* where the search window ends.
        max_search_stop = n - (k - (i + 1))

        # Find the maximum digit and its index within the required search window.
        max_digit = -1
        max_index = -1

        # Search window is int_tuple[current_index : max_search_stop]
        for j in range(current_index, max_search_stop):
            digit = int_tuple[j]

            if digit > max_digit:
                max_digit = digit
                max_index = j
                # Optimization: If the best possible digit (9) is found, stop searching this window.
                if max_digit == 9:
                    break

        # Append the best digit found for the current position
        result_digits.append(max_digit)

        # The next search must start immediately after the index of the chosen digit
        current_index = max_index + 1

    # Convert the list of selected digits (e.g., [9, 8, 9, 7]) into a single integer (9897)
    return int("".join(map(str, result_digits)))


def part1(data: List[Union[str, list]]):
    """Solve part 1"""
    total = 0
    for d in data:
        lrg = find_highest_number_from_combinations(d)
        total += lrg

    return total


def part2(data: List[Union[str, list]]):
    """Solve part 2"""
    total = 0
    for d in data:
        lrg = find_highest_number_greedy(d, combination_size=12)
        total += lrg

    return total


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
    SELECTED_PARSER = parse_lines_to_tuples_generic  # Example parser; change as needed

    print(f"Loading data from folder: **{DAY_FOLDER_NAME}**")
    print(f"Using parser: **{SELECTED_PARSER.__name__}**\n")

    # Run tests first
    tests = solve(test_file, parse_func=SELECTED_PARSER, run="Test")

    print("---")
    # Run the actual solution
    solutions = solve(soln_file, parse_func=SELECTED_PARSER)
