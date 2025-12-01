# https://adventofcode.com/2024/day/25

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 3301
test_file = script_path / "test.txt"  # 3


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        grids = file.read().strip().split("\n\n")

    locks = []
    keys = []
    lock_height = None

    for grid_str in grids:
        grid = grid_str.splitlines()
        if grid[0] == "#" * len(grid[0]):  # Check if first row is all '#'
            # print(list(zip(*grid)))
            if lock_height is None:
                lock_height = len(grid)

            grid_data = [
                row.count("#") - 1 for row in zip(*grid)
            ]  # Count '#' in each column
            locks.append(tuple(grid_data))
        elif grid[-1] == "#" * len(grid[-1]):  # Check if last row is all '#'
            grid_data = [row.count("#") - 1 for row in zip(*grid)]
            keys.append(tuple(grid_data))

    return locks, keys, lock_height


def compare_keys_and_locks(keys, locks, lock_height):
    """
    Compares each lock in the 'locks' tuple with each key in the 'keys' tuple.
    A match is found if the sum of the corresponding numbers in the key and lock
    tuples equals the lock height minus 1.

    Args:
      keys: A list of tuples, where each tuple represents a key grid and
            contains the number of '#' in each column.
      locks: A list of tuples, where each tuple represents a lock grid and
            contains the number of '#' in each column.
      lock_height: An integer representing the height of a lock grid.

    Returns:
      A list of tuples, where each tuple contains a key index and a lock index
      representing a matching key-lock pair.
    """

    matches = []
    for lock_index, lock in enumerate(locks):
        for key_index, key in enumerate(keys):
            if len(key) == len(
                lock
            ):  # Ensure key and lock have the same number of columns
                if all(a + b <= lock_height - 2 for a, b in zip(key, lock)):
                    matches.append((key, lock))
    return matches


def part1(data):
    """Solve part 1"""

    l, k, h = data

    right_keys = compare_keys_and_locks(k, l, h)

    # print(right_keys)

    return len(right_keys)


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(test_file, run="Test")

    print()
    solutions = solve(soln_file)
