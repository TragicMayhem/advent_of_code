# https://adventofcode.com/2021/day/2

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 2187380 / 2086357770
input_test = script_path / "test.txt"  # 150 / 900


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        instr = [line.split() for line in file]

    return instr


def part1(data):
    """Solve part 1"""
    pos_h = 0
    pos_d = 0

    for l in data:
        direction = l[0][0].upper()
        if direction == "F":
            pos_h += int(l[1])
        elif direction == "U":
            pos_d -= int(l[1])
        elif direction == "D":
            pos_d += int(l[1])

    return pos_d * pos_h


def part2(data):
    """Solve part 2"""

    pos_h = 0
    pos_d = 0
    aim = 0

    for l in data:
        direction = l[0][0].upper()
        if direction == "F":
            pos_h += int(l[1])
            pos_d += aim * int(l[1])
        elif direction == "U":
            aim -= int(l[1])
        elif direction == "D":
            aim += int(l[1])

    return pos_d * pos_h


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
