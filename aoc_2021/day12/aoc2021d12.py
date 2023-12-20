# https://adventofcode.com/2021/day/12

import pathlib
import time
from collections import defaultdict
from collections import deque

script_path = pathlib.Path(__file__).parent
soln_file = (
    script_path / "input.txt"
)  # Right answers: 5178 / 130094   (~but test 2 gives wrong answer!)  LUCK?  WHY?
test_file = script_path / "test.txt"  # 10 / 36 matches
test_file2 = script_path / "test2.txt"  #  19 / 103
test_file3 = script_path / "test3.txt"  #  226 / 3509 matches


def parse(puzzle_input):
    """Parse input"""
    instructions = defaultdict(list)
    with open(puzzle_input, "r") as file:
        data = [d.split("-") for d in file.read().split("\n")]

        # Process each instrcution both ways and check to not add start inside the list values
        # But keep start as one of they keys to allow it to be processed as starting cave
        for d in data:
            posStart, posEnd = d

            if posStart != "start":
                instructions[posEnd].append(posStart)

            if posEnd != "start":
                instructions[posStart].append(posEnd)

    return instructions


def navigate(routes, cave, target):
    cave_q = deque([(cave, {cave})])
    # print(cave_q)
    running_total = 0

    while cave_q:
        # Get the next one and list of path options
        current, path_opts = cave_q.pop()
        # print('  Next:',current,'/',path_opts, ' q len:', len(cave_q), running_total)

        # if the current point is the target (end) then new path so count and restart
        if current == target:
            # print("  ++ at end add to path count")
            running_total += 1
            continue

        for c in routes[current]:
            # if already done the point and its lower then need to skip
            # print('loop', c)

            if c in path_opts and c.islower():
                continue

            # join the list of options with the next possible branch
            new_paths = path_opts.union({c})  # Could do x | y
            # print('NEW', new_paths)
            cave_q.append((c, new_paths))

    return running_total


def navigate_extend_rules(routes, starting_cave, target):
    visited_small_cave_twice = False
    cave_q = deque([(starting_cave, {starting_cave}, visited_small_cave_twice)])
    running_total = 0

    while cave_q:
        current_cave, path_options, visited_small_cave_twice = cave_q.pop()

        if current_cave == target:
            running_total += 1
            continue

        for next in routes[current_cave]:
            if next not in path_options or next.isupper():
                cave_q.append(
                    (next, path_options.union({next}), visited_small_cave_twice)
                )
                continue

            if visited_small_cave_twice:
                continue

            # Cant set the variable and then add to the queue.
            # think its because of the passing as reference to objects. Not value.
            # Not sure what I did, or why doesnt work. more investigation and some learning/research. Took a lot of print statements to figure out that!
            # If I use
            #   visited_small_cave_twice = True
            #   cave_q.append((next, path_options, visited_small_cave_twice))
            # then it gives answer 27 instead of 36 (for test 1 - answer from AOC)
            # Setting to True works, and for others tests.
            cave_q.append((next, path_options, True))

    return running_total


def solve(puzzle_input, run="Solution"):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = navigate(data, "start", "end")
    times.append(time.perf_counter())
    solution2 = navigate_extend_rules(data, "start", "end")
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    tests = solve(test_file, run="Test")
    tests2 = solve(test_file2, run="Test2")
    tests3 = solve(test_file3, run="Test3")

    print()
    solutions = solve(soln_file)
