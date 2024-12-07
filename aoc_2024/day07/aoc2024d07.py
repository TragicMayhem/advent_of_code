# https://adventofcode.com/2024/day/

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 465126289353 /
test_file = script_path / "test.txt"  # 3749 / 11387


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [d.split(":") for d in file.read().split("\n")]

    records = []
    for l in lst:
        target = int(l[0])
        values = list(map(int, l[1].strip().split(" ")))
        records.append((target, values))

    print(tuple(records))

    return records


def evaluate_target(target, numbers):
    """
    Evaluates if a target number can be reached by adding or multiplying numbers in the given list,
    following a left-to-right calculation order.

    Args:
      target: The target number to be reached.
      numbers: A list of numbers to be combined.

    Returns:
      True if the target can be reached, False otherwise.
    """

    def calculate(current_result, remaining_numbers):
        if not remaining_numbers:
            return current_result == target

        # Try adding the next number
        if calculate(current_result + remaining_numbers[0], remaining_numbers[1:]):
            return True

        # Try multiplying the next number
        if calculate(current_result * remaining_numbers[0], remaining_numbers[1:]):
            return True

        return False

    return calculate(numbers[0], numbers[1:])


def part1(data):
    """Solve part 1"""

    valid_calibrations = []

    for d in data:
        target, values = d
        if evaluate_target(target, values):
            print("Target can be reached!")
            valid_calibrations.append(target)
        else:
            print("Target cannot be reached.")

    tot = sum(valid_calibrations)

    return tot


def part2(data):
    """Solve part 2"""

    return 1


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

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
    print("\nAOC")

    tests = solve(test_file, run="Test")

    print()
    solutions = solve(soln_file)
