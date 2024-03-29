# https://adventofcode.com/2021/day/2

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 331067 / 92881128
test_file = script_path / "test.txt"  # 37 / 168


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input, "r") as file:
        lst = [[int(x) for x in row] for row in [line.split(",") for line in file]]
    return lst.pop()


def part1(data):
    """Solve part 1"""
    min_pos = min(data)
    max_pos = max(data)

    answers = {}
    for i in range(min_pos + 1, max_pos + 1):
        answers[str(i)] = 0
        for crabpos in data:
            crab_fuel = abs(crabpos - i)
            answers[str(i)] += crab_fuel

    return min(answers.values())


def part2(data):
    """Solve part 2"""
    min_pos = min(data)
    max_pos = max(data)
    answers = dict()

    for i in range(min_pos + 1, max_pos + 1):
        answers[str(i)] = 0

        for crabpos in data:
            # Slower version using range and lists
            # gap = list(range(1, abs(crabpos - i)+1))
            t = abs(crabpos - i)
            answers[str(i)] += (t * (t + 1)) / 2

    return min(answers.values())


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
