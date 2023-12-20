# https://adventofcode.com/2021/day/15

"""
Reference https://www.redblobgames.com/pathfinding/a-star/introduction.html

Version 4
- Mashup of code/ideas
- Converts list integers in to a dictionary for lookup

Problems?
- matches the examples!
- expands grid (check that is correct) so the search must be wrong

"""

import pathlib
import time
import heapq
from collections import defaultdict
from math import (
    inf as INFINITY,
)  ## NEW: I was missing this for the risk checking default value

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 592 /   (target is 2897)
test_file = script_path / "test.txt"  # 40 / 315


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        data = file.read().split("\n")
        data = [[int(x) for x in row] for row in data]
    return data


def build_grid(data):
    grid = defaultdict(int)
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            grid[(r, c)] = cell

    size = len(data)
    return grid, size


def expand_grid(data, from_size):
    grid = defaultdict(int)

    expanded_grid = data[:]

    w = h = from_size
    extra_grids = 4

    # go across
    for _ in range(extra_grids):
        for line in data:
            risks = line[-w:]
            line.extend((x + 1) if x < 9 else 1 for x in risks)

    # go down
    for _ in range(extra_grids):
        for line in expanded_grid[-h:]:
            newline = list((x + 1) if x < 9 else 1 for x in line)
            expanded_grid.append(newline)

    for r, row in enumerate(expanded_grid):
        for c, cell in enumerate(row):
            grid[(r, c)] = cell

    size = len(expanded_grid)

    return grid, size


def get_coords_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def grid_search(grid, size):
    startNode = (0, 0)
    goalNode = (size - 1, size - 1)

    frontier = [(0, startNode)]
    came_from = set()
    risks = defaultdict(lambda: INFINITY, {startNode: 0})
    risks[startNode] = 0

    # Construct a map of all possible paths for the startNode across the map
    while frontier:
        risk, current = heapq.heappop(frontier)
        # print('curr:',current,risk, 'cost', grid.get(current))

        if current == goalNode:
            return risk

        if current in came_from:
            continue

        came_from.add(current)
        # print(came_from)
        x, y = current

        for cardinal in get_coords_cardinals(x, y, size, size):
            # print('cardinal cost',cardinal, grid.get(cardinal))

            if cardinal in came_from:
                continue

            xx, yy = cardinal
            newrisk = risk + grid.get(cardinal)

            if newrisk < risks[cardinal]:
                risks[cardinal] = newrisk
                heapq.heappush(frontier, (newrisk, cardinal))

            # print(frontier)

    return 404


def part1(grid, size):
    """Solve part 1"""

    ans = grid_search(grid, size)

    return ans


def part2(grid, size):
    """Solve part 2"""

    ans = grid_search(grid, size)

    return ans


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)
    initial_size = len(data)

    times.append(time.perf_counter())

    grid, size = build_grid(data)
    solution1 = part1(grid, size)

    times.append(time.perf_counter())

    grid, size = expand_grid(data, initial_size)
    solution2 = part2(grid, size)

    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file):
    data = parse(test_file)

    grid, initial_size = build_grid(data)
    test_solution1 = part1(grid, initial_size)

    grid, size = expand_grid(data, initial_size)
    test_solution2 = part2(grid, size)

    return test_solution1, test_solution2


def runAllTests():
    print("Tests")
    a, b = runTest(test_file)
    print(f"Test1.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":  # print()
    runAllTests()

    # \ not 3330 to high
    # \ not 2905

    solutions = solve(soln_file)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
