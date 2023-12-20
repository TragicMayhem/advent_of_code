# https://adventofcode.com/2022/day/1

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 1651 //  3837
test_file = script_path / "test0.txt"  # 7 // 19
test_file1 = script_path / "test1.txt"  # 5  // 23
test_file2 = script_path / "test2.txt"  # 6  // 23
test_file3 = script_path / "test3.txt"  # 10  // 29
test_file4 = script_path / "test4.txt"  # 11  // 26


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = file.read().split()
        lst = list(lst[0])

    return lst


def find_marker(data, marker_length):
    for i in range(len(data) - marker_length):
        current = data[i : i + marker_length]
        count_chars = set(current)
        # print(i, current, count_chars)
        if len(count_chars) == marker_length:
            break

    return i + len(current)


def part1(data):
    """Solve part 1"""

    # for i in range(len(data) - 3):
    #     current = data[i : i + 4]
    #     count_chars = set(current)
    #     if len(count_chars) == 4:
    #         break

    # ans = i + len(current)

    return find_marker(data, 4)


def part2(data):
    """Solve part 2"""
    # for i in range(len(data) - 14):
    #     current = data[i : i + 14]
    #     count_chars = set(current)
    #     # print(i, current, count_chars)
    #     if len(count_chars) == 14:
    #         break

    # ans = i + len(current)

    return find_marker(data, 14)


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
    tests1 = solve(test_file1, run="Test")
    tests2 = solve(test_file2, run="Test")
    tests3 = solve(test_file3, run="Test")
    tests4 = solve(test_file4, run="Test")

    print()
    solutions = solve(soln_file)
