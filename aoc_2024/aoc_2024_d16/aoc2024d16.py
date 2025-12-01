# https://adventofcode.com/2024/day/16

import pathlib
import time
from queue import PriorityQueue


# Reference https://www.redblobgames.com/pathfinding/a-star/introduction.html


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 102488
test_file = script_path / "test.txt"  # 7036
test_file2 = script_path / "test2.txt"  # 11048


# FACING = {
#     "^": (-1, 0),  # Up
#     "v": (1, 0),  # Down
#     "<": (0, -1),  # Left
#     ">": (0, 1),  # Right
# }


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [[x for x in row] for row in file.read().split("\n")]

    start_pos = end_pos = None
    walls = set()

    for r, row in enumerate(lst):
        for c, cell in enumerate(row):
            if cell == "#":
                walls.add((r, c))
            elif cell == "S":
                start_pos = (r, c)
            elif cell == "E":
                end_pos = (r, c)

    return (walls, start_pos, end_pos)


def get_coords_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def get_next_direction(current_value):
    # Turning right each time
    # dirns = [1, 2, 3, 4]  # N, E, S, W
    return (current_value % 4) + 1


def find_max_coordinates(walls):
    """Finds the largest X and Y coordinates from a set of wall coordinates.

    Args:
      walls: A set of tuples representing the positions of walls.

    Returns:
      A tuple (max_x, max_y) representing the largest X and Y coordinates.
    """

    max_x = max(x for x, _ in walls)
    max_y = max(y for _, y in walls)

    return max_x, max_y


def find_optimal_paths(walls, start, end, h, w, top_k=10):
    """
    Finds the top k optimal paths through a grid with walls, given only wall positions.

    Args:
        walls: A set of tuples representing the positions of walls.
        start: A tuple (x, y) representing the starting position.
        end: A tuple (x, y) representing the end position.
        h: Height of the grid.
        w: Width of the grid.
        top_k: The number of top paths to return.

    Returns:
        A list of top k paths, sorted by cost, in the format (cost, steps, turns, path).
    """

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
    step_cost = 1
    turn_cost = 1000

    def is_valid(x, y):
        return 0 <= x < h and 0 <= y < w and (x, y) not in walls

    def neighbors(x, y, current_direction):
        current_direction_index = directions.index(current_direction)

        # Generate potential next directions: current, clockwise, counterclockwise
        next_directions = [(current_direction_index + i) % 4 for i in range(-1, 2)]

        for direction_index in next_directions:
            dx, dy = directions[direction_index]
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                yield nx, ny, directions[direction_index]

    pq = PriorityQueue()
    pq.put(
        (0, 0, 0, start[0], start[1], (0, 1))
    )  # (cost, turns, steps, x, y, current_direction)

    visited = set()
    parent = {}
    all_paths = []

    while not pq.empty():
        cost, turns, steps, x, y, prev_direction = pq.get()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y, _, _, _ = parent[(x, y)]
            path.append(start)
            all_paths.append(
                (cost, steps, turns, path[::-1])
            )  # Cost, steps, turns, path

        for nx, ny, new_direction in neighbors(x, y, prev_direction):
            new_turns = turns + (new_direction != prev_direction)
            new_steps = steps + 1
            new_cost = step_cost * new_steps + turn_cost * new_turns
            if (nx, ny) not in parent or new_cost < parent[(nx, ny)][0]:
                parent[(nx, ny)] = (x, y, new_cost, new_steps, new_direction)
                pq.put((new_cost, new_turns, new_steps, nx, ny, new_direction))

    all_paths.sort(key=lambda x: x[0])  # Sort by cost
    return all_paths[:top_k]


def part1(data):
    """Solve part 1"""

    walls, start, end = data

    h, w = find_max_coordinates(walls)

    ans = find_optimal_paths(walls, start, end, h, w)

    print(ans)

    return 1


def part2(data):
    """Solve part 2"""

    return 1


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
    tests = solve(test_file2, run="Test 2")

    print()
    solutions = solve(soln_file)
