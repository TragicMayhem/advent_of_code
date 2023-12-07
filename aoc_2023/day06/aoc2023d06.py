# https://adventofcode.com/2023/day/6

import pathlib
import time
from math import ceil, floor

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 1413720 / 30565288
input_test = script_path / "test.txt"  # 288 / 71503


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n")

    # Doesnt deal with unknown multiple spaces (for input)
    # times = lst[0][9:].strip().split("  ")

    # splits and then rejoins to replace spaces with single space, then splits again
    times = " ".join(lst[0][9:].split()).split()
    times = list(map(int, times))

    dists = " ".join(lst[1][9:].split()).split()
    dists = list(map(int, dists))

    race_targets = list(zip(times, dists))

    return race_targets


def part1(data):
    """Solve part 1"""

    # times, dists = zip(*data)
    # print(times)
    # print(dists)

    total = 1

    for t, d in data:
        # print(t, d)

        game_wins = 0

        # Hold buttton at least 1 and upto t
        for button_hold_time in range(1, t):
            time_left = t - button_hold_time

            # hold time is speed * time = distance
            run_dist = time_left * button_hold_time

            if run_dist > d:
                game_wins += 1

        total *= game_wins

    return total


def compute(t, d):
    # square roots are **0.5
    # the overall math to calculate is below. That is a Quadratic equation
    # hold time * (time - hold time) > distance

    # Help on quadratics from internet: Hold = x, time = t, dist = d
    # -x**2 + tx -2d >= 0
    # x = (t - root(t**2 - 4d)) /2
    # then its  t - or t + variations (in the brackets)

    # Need to work out the min and max and then difference to get final answer
    # Had to look up ceil and floor math methods

    part = (t**2 - 4 * d) ** 0.5
    count_min = (t - part) / 2
    count_max = (t + part) / 2

    # Stumped for ages, need to take 1 from this ans
    ans = ceil(count_max) - floor(count_min) - 1
    print(count_min, count_max, ans)

    return ans


# math, the loops approach is too slow. Too many combinations and overcomplicated it. doh
# Hints from web - quadratic


def part2(data):
    """Solve part 2"""

    times, dists = zip(*data)
    # print(times)
    # print(dists)

    correct_time = ""
    correct_dist = ""

    for t in times:
        correct_time += str(t)

    for d in dists:
        correct_dist += str(d)

    print(correct_time, correct_dist)

    total = 1

    for t, d in [(int(correct_time), int(correct_dist))]:
        game_wins = 0

        game_wins = compute(t, d)
        total *= game_wins

    return total


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

    tests = solve(input_test, run="Test")

    print()
    solutions = solve(input)
