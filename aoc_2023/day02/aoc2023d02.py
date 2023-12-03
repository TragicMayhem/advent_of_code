# https://adventofcode.com/2023/day/2

import pathlib
import time
from collections import defaultdict

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 2795 /
input_test = script_path / "test.txt"  # 8 / 2286

part1_target = {"red": 12, "green": 13, "blue": 14}


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        #  Read each line (split \n) and form a list of strings
        game_records = [d.split(":") for d in file.read().split("\n")]

    game_store = defaultdict(dict)

    for game_info in game_records:
        game_id = game_info[0]
        draws = [
            tuple(p.strip() for p in d.split(",")) for d in game_info[1].split(";")
        ]
        game_store[game_id] = draws
        # print(game_id)
        # print(draws)
        # print(game_store)

    return game_store


def part1(data):
    """Solve part 1"""
    # print()
    # print(data)

    valid_games = []

    for k, v in data.items():
        # print(k,v)

        game_overall = []

        for draws in v:
            draw_colour_check = []

            for draw in draws:
                count, colour = draw.split(" ")
                # print(count, colour)

                if part1_target.get(colour, 0) >= int(count):
                    draw_colour_check.append(True)
                else:
                    draw_colour_check.append(False)
                # print(draw_colour_check)

            if all(draw_colour_check):
                game_overall.append(True)
            else:
                game_overall.append(False)

        if all(game_overall):
            # print(k, "game ok")
            valid_games.append(int(k.split(" ")[1]))

    print()
    print(valid_games)

    return sum(valid_games)


def part2(data):
    """Solve part 2"""

    games_scores = []
    games_overall_total = 0

    for k, v in data.items():
        # print(k,v)
        cube_max = {"red": 0, "blue": 0, "green": 0}
        game_score = 0

        for draws in v:
            for draw in draws:
                count, colour = draw.split(" ")
                # print(count, colour)
                count = int(count)
                cube_max[colour] = {True: count, False: cube_max.get(colour, 0)}[
                    cube_max.get(colour, 0) < count
                ]

        game_score = (
            cube_max.get("red", 0) * cube_max.get("green", 0) * cube_max.get("blue", 0)
        )
        games_scores.append(game_score)

    games_overall_total = sum(games_scores)

    return games_overall_total


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
