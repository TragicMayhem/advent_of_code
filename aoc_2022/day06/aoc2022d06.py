# https://adventofcode.com/2022/day/1

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 1651 //
input_test = script_path / "test0.txt"  # 7 // 19
input_test1 = script_path / "test1.txt"  # 5  // 23
input_test2 = script_path / "test2.txt"  # 6  // 23
input_test3 = script_path / "test3.txt"  # 10  // 29
input_test4 = script_path / "test4.txt"  # 11  // 26


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


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():

    print("Tests")
    a, b = runTest(input_test)
    print(f"Test.  Part1: {a} Part 2: {b}")

    a, b = runTest(input_test1)
    print(f"Test1.  Part1: {a} Part 2: {b}")

    a, b = runTest(input_test2)
    print(f"Test2.  Part1: {a} Part 2: {b}")

    a, b = runTest(input_test3)
    print(f"Test3.  Part1: {a} Part 2: {b}")

    a, b = runTest(input_test4)
    print(f"Test4.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":

    runAllTests()

    solutions = solve(input)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
