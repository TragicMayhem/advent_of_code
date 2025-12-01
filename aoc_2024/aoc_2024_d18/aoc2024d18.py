# https://adventofcode.com/2024/day/18

import pathlib
import time
import heapq
from collections import defaultdict


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #
test_file = script_path / "test.txt"  #


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [
            (int(x), int(y))
            for x, y in (line.split(",") for line in file.read().splitlines())
        ]

        # print(lst)

    return lst


def get_coords_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def a_star_search(grid_size, walls, start, end):
    """
    Finds the shortest path between start and end in a grid with dynamic walls.

    Args:
        grid_size: The size of the grid.
        walls: A list of walls, where each wall is a tuple (x, y).
        start: The starting position (x, y).
        end: The end position (x, y).

    Returns:
        A list of coordinates representing the shortest path, or None if no path exists.
    """

    def heuristic(a, b):
        # Manhattan distance heuristic
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(node, walls):
        x, y = node
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [
            (nx, ny)
            for nx, ny in neighbors
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in walls
        ]

    open_set = [(0, 0, heuristic(start, end))]  # (cost, moves, node)
    heapq.heapify(open_set)
    closed_set = set()
    parent = {}

    while open_set:
        cost, moves, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        closed_set.add(current)

        for neighbor in neighbors(current, walls):
            if neighbor not in closed_set:
                new_cost = cost + 1
                new_moves = moves + 1
                if (
                    neighbor not in open_set
                    or new_cost < open_set[open_set.index(neighbor)][0]
                ):
                    heapq.heappush(open_set, (new_cost, new_moves, neighbor))
                    parent[neighbor] = current

        # Add a new wall after each step
        if walls:
            new_wall = walls.pop(0)
            closed_set.add(new_wall)

    return None  # No path found


def part1(data, grid_size):
    """Solve part 1"""

    h = w = grid_size
    start = (0, 0)
    end = (h - 1, w - 1)

    ans = a_star_search(grid_size, data, start, end)

    print(len(ans))
    print(ans)

    return 1


def part2(data, grid_size):
    """Solve part 2"""

    return 1


def solve(puzzle_input, run="Solution", grid_size=71):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data, grid_size)
    times.append(time.perf_counter())
    solution2 = part2(data, grid_size)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print("\nAOC")

    # tests = solve(test_file, run="Test", grid_size=7)

    print()
    solutions = solve(soln_file)
