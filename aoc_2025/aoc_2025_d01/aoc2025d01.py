# https://adventofcode.com/2025/day/1

import pathlib
import time
from typing import Callable, List, Union

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 1018 /  5815
test_file = script_path / "test.txt"  # 3 / 6

# too low 1989 3968
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


# --- Solving Functions ---


def part1(data: List[Union[str, list]]):
    """Solve part 1"""
    lowhigh = (0, 99)
    pos = 50

    zero_count = 0

    for dir_char, turns in data:

        direction = 1 if dir_char == "R" else -1

        next_pos = (pos + direction * turns) % 100

        pos = next_pos

        if pos == 0:
            zero_count += 1

    return zero_count


def part2(data: List[Union[str, list]]):
    """Solve part 2"""
    lowhigh = (0, 99)
    pos_cur = 50

    zero_count = 0

    for this_dir, this_turns in data:

        # Check if we crossed the zero boundary
        # check the turn direction and see if we crossed over 0
        # modular arithmetic wrap-around logic
        # of number of turns exceeding the distance to the boundary then wraps around
        # e.g. from 98 to 2 with R 5 crosses the boundary
        # e.g. from 2 to 98 with L 5 crosses the boundary

        direction = 1 if this_dir == "R" else -1
        pos_next = (pos_cur + direction * this_turns) % 100

        # if the number of turns greater than 100 how many times we cross the boundary?
        num_of_turns = this_turns // 100

        # print("\nTop D #: ", this_dir, this_turns, " / S: ", pos_cur, " / E:", pos_next)
        # print("num_of_turns:", num_of_turns)

        if pos_cur != 0:
            # A < B and we cross the boundary
            # how to know if crossed the boundary?
            # e.g. from 98 to 2 with R 5 crosses the boundary
            if direction == 1 and (pos_cur > pos_next or pos_next == 0):
                zero_count = zero_count + 1

            # e.g. from 2 to 98 with L 5 crosses the boundary
            # -1 and not starting at zero to avoid double count, as pos_next can be 0
            if direction == -1 and (pos_cur < pos_next or pos_next == 0):
                zero_count = zero_count + 1

        # add any full 100 turns crossing
        zero_count += num_of_turns

        pos_cur = pos_next

    return zero_count


def solve(puzzle_input: pathlib.Path, parse_func: Callable, run="Solution"):
    """Solve the puzzle for the given input, using the specified parser"""
    times = []

    # The data is parsed only once using the selected function
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
    print("\n🎄 Advent of Code 🎄")

    # 📌 CHOOSE YOUR PARSER HERE
    # Use parse_lines for standard input, or parse_blocks for block-based input
    SELECTED_PARSER = parse_lines
    # SELECTED_PARSER = parse_blocks

    print(f"Using parser: **{SELECTED_PARSER.__name__}**\n")

    # Run tests first
    tests = solve(test_file, parse_func=SELECTED_PARSER, run="Test")

    print("---")
    # Run the actual solution
    solutions = solve(soln_file, parse_func=SELECTED_PARSER)
