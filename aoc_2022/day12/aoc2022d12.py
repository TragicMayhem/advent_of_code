# https://adventofcode.com/2022/day/12

import pathlib
import time
from collections import deque
from math import inf as INFINITY
from copy import deepcopy

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 330  // 321
input_test = script_path / "test.txt"  # 31  // 29

# need to make the search much better and not replace S E
# Need a better way for part 2, and hints say work backwards - research


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as file:
        data = file.read().split("\n")

    data = [[x for x in row] for row in data]

    return data


def get_cardinals_within_reach(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def find_pos(data, pt):
    for i, row in enumerate(data):
        if pt not in row:
            continue

        for j in range(len(data[0])):
            if data[i][j] == pt:
                return (i, j)


def grid_search(grid, start_point, goal_point):

    h, w = len(grid), len(grid[0])

    # start_point = find_pos(grid, "S")
    # goal_point = find_pos(grid, "E")
    print("Start:", start_point, "Goal:", goal_point)

    # Dont like this, setting the start and end point to repective heights
    # after locating them.
    grid[start_point[0]][start_point[1]] = "a"
    grid[goal_point[0]][goal_point[1]] = "z"

    exploring_queue = deque([(0, start_point)])
    visited_points = set()

    # Construct a map of all possible paths for the startNode across the map
    while exploring_queue:
        dist, current = exploring_queue.popleft()
        # print(
        #     "\nCURRENT",
        #     current,
        #     grid[current[0]][current[1]],
        #     dist,
        #     "Q",
        #     len(exploring_queue),
        # )

        # if point is the End point then return distance
        if current == goal_point:
            return dist

        # Skip if its been visited, and continue
        if current in visited_points:
            continue

        visited_points.add(current)
        r, c = current

        current_height = grid[r][c]
        # Problem with checking S E here, is that when it checks the cardinals the end is still E - doh.
        # Move to replace before loop

        for cardinal_point in get_cardinals_within_reach(r, c, h, w):
            if cardinal_point in visited_points:
                continue

            # Use ORD to get a number for the lower case letter, a < b < c <...< z
            current_step = ord(current_height)
            comp_r, comp_c = cardinal_point
            next_step = ord(grid[comp_r][comp_c])

            # print(
            #     "curr",
            #     current_height,
            #     current_step,
            #     "with",
            #     cardinal_point,
            #     grid[comp_r][comp_c],
            #     next_step,
            # )

            # Pt1?  Gap down can be greater- Doh. This is why my solution fails.
            # Need to rework e.g c down to a is down gap 2
            # if 0 <= abs(current_step - next_step) <= 1:
            if next_step - current_step <= 1:
                exploring_queue.append((dist + 1, cardinal_point))

            # print("Visited:", visited_points)

    return INFINITY  # 404


def part1(data):
    """Solve part 1"""

    grid = deepcopy(data)

    start_point = find_pos(grid, "S")
    goal_point = find_pos(grid, "E")
    ans = grid_search(grid, start_point, goal_point)

    return ans


def part2(data):
    """Solve part 2"""
    print("Part 2")

    grid = deepcopy(data)

    start_point = find_pos(grid, "S")
    goal_point = find_pos(grid, "E")

    # Find all a, build list
    starting_list = []
    results = []

    for i, row in enumerate(data):
        for j, col in enumerate(data[i]):
            if data[i][j] == "a":
                starting_list.append((i, j))

    for start_pos in starting_list:
        results.append((grid_search(grid, start_pos, goal_point), start_pos))

    quickest = INFINITY

    for dist, _ in results:
        quickest = dist if dist < quickest else quickest

    return quickest


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
    print(f"Test1.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":

    runAllTests()

    solutions = solve(input)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
