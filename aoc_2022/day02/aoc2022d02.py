# https://adventofcode.com/2022/day/2

import pathlib
import time
from collections import Counter

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 13484  //  13433
test_file = script_path / "test.txt"  # 15  // 12
test_file2 = script_path / "test2.txt"  # 33  // 35


winning_moves = {
    "1": "3",  # Rock / Scissors
    "2": "1",  # Paper / Rock
    "3": "2",  # Scissors / Paper
}

losing_moves = {
    "1": "2",  # Rock / Paper
    "2": "3",  # Paper / Scissors
    "3": "1",  # Scissors / Rock
}

outcome = {
    "1": "Lose",
    "2": "Draw",
    "3": "Win",
}


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        lst = (
            file.read()
            .replace("A", "1")
            .replace("B", "2")
            .replace("C", "3")
            .replace("X", "1")
            .replace("Y", "2")
            .replace("Z", "3")
            .split("\n")
        )

    moves = [tuple(v.split(" ")) for v in lst]
    # If wanted to turn to integers instead of string
    # data = [tuple(int(x) for x in elf) for elf in moves]

    return moves


def part1(data):
    """Solve part 1"""

    total_points = 0
    game_combinations = Counter(data)
    # print(game_combinations)

    for game_moves, count in game_combinations.items():
        elf_move, your_move = game_moves

        if elf_move == your_move:  # Draw
            this_gamescore = 3 + int(your_move)

        elif winning_moves.get(elf_move) == your_move:  # Elf beats you
            this_gamescore = 0 + int(your_move)

        else:  # You win
            this_gamescore = 6 + int(your_move)

        total_points += this_gamescore * count

    return total_points


def part2(data):
    """Solve part 2"""

    total_points = 0
    game_combinations = Counter(data)

    for game_moves, count in game_combinations.items():
        elf_move, outcome_needed = game_moves

        get_your_action = outcome.get(outcome_needed)

        if get_your_action == "Lose":
            this_gamescore = 0 + int(winning_moves.get(elf_move))

        elif get_your_action == "Win":
            this_gamescore = 6 + int(losing_moves.get(elf_move))

        else:
            this_gamescore = 3 + int(elf_move)  # Use Elf move as its draw

        total_points += this_gamescore * count

    return total_points


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

    test1 = solve(test_file, run="Test1")
    test2 = solve(test_file2, run="Test2")

    print()
    solutions = solve(soln_file)
