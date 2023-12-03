# https://adventofcode.com/2021/day/6

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 390011 for 80d   1746710169834 for 256d
input_test = script_path / "test.txt"  # 5934 for 80d   26984457539 for 256d


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input, "r") as file:
        input = [[int(x) for x in row] for row in [line.split(",") for line in file]]
        input = input[0]
    return input


def model_fish(initial_fish, model_days):
    """
    Take in the initial list of fish and use dictionaries to count the number of fish for the model_days
    On day 0, new fish added (day 8) and that parent fish is rest to (dy 6)
    """
    newfish = 0
    dict_fish_days = {}

    for d_count in range(8):
        dict_fish_days[str(d_count)] = +initial_fish.count(d_count)

    for d in range(model_days):
        for k, v in dict_fish_days.items():
            if k == "0":
                newfish = v
            else:
                dict_fish_days[str(int(k) - 1)] = v

        dict_fish_days["6"] += newfish
        dict_fish_days["8"] = newfish

    return sum(dict_fish_days.values())


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = model_fish(data, 80)  # part1(data)
    times.append(time.perf_counter())
    solution2 = model_fish(data, 256)  # part2(data)
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
