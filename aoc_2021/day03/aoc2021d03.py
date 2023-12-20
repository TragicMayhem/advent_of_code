# https://adventofcode.com/2021/day/3

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 2498354 / 3277956
test_file = script_path / "test.txt"  # 198 / 230


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n")

    return lst


def part1(data):
    """Solve part 1"""
    rate_gamma = []
    rate_epsilon = []

    for check_pos in range(len(data[0])):
        count_one = count_zero = 0

        for item in data:
            if item[check_pos] == "1":
                count_one += 1
            else:
                count_zero += 1

        if count_one > count_zero:
            rate_gamma.append("1")
            rate_epsilon.append("0")
        else:
            rate_gamma.append("0")
            rate_epsilon.append("1")

        rate_gamma_bin = "".join(rate_gamma)
        rate_epsilon_bin = "".join(rate_epsilon)
        ans = int(rate_gamma_bin, 2) * int(rate_epsilon_bin, 2)

    return ans


def part2(data):
    """Solve part 2"""

    rate_oxygen = data[:]
    rate_co2 = data[:]

    for check_pos in range(len(rate_oxygen[0])):
        count_one = count_zero = 0

        for item in rate_oxygen:
            if item[check_pos] == "1":
                count_one += 1
            else:
                count_zero += 1

        if len(rate_oxygen) == 1:
            break

        if count_one == count_zero:
            rate_oxygen = [x for x in rate_oxygen if x[check_pos] == "1"]

        elif count_one > count_zero:
            rate_oxygen = [x for x in rate_oxygen if x[check_pos] == "1"]

        elif count_one < count_zero:
            rate_oxygen = [x for x in rate_oxygen if x[check_pos] == "0"]

    for check_pos in range(len(rate_co2[0])):
        count_one = count_zero = 0

        for item in rate_co2:
            if item[check_pos] == "1":
                count_one += 1
            else:
                count_zero += 1

        if len(rate_co2) == 1:
            break

        if count_one == count_zero:
            rate_co2 = [x for x in rate_co2 if x[check_pos] == "0"]

        elif count_one > count_zero:
            rate_co2 = [x for x in rate_co2 if x[check_pos] == "0"]

        elif count_one < count_zero:
            rate_co2 = [x for x in rate_co2 if x[check_pos] == "1"]

    ans = int(rate_oxygen[0], 2) * int(rate_co2[0], 2)

    return ans


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
