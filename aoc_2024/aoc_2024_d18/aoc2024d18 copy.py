# https://adventofcode.com/2024/day/18

import pathlib
import time
from collections import deque

import matplotlib.pyplot as plt
import numpy as np


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

        print(lst)

    return lst


def get_coords_cardinals(r, c, h, w):
    for delta_r, delta_c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        if 0 <= rr < h and 0 <= cc < w:
            yield (rr, cc)


def is_valid(row, col, h, w, walls):
    return 0 <= row < h and 0 <= col < w and (row, col) not in walls


def draw_grid(grid_size, walls):
    """Draws a grid with specified size and walls.

    Args:
        grid_size: Size of the grid (integer).
        walls: List of wall coordinates (tuples of (row, col)).
    """

    plt.ion()  # Enable interactive mode

    grid = np.zeros((grid_size, grid_size))

    for wall in walls:
        grid[wall] = 1

    # Transpose the grid to correct orientation
    grid = grid.T

    plt.imshow(grid, cmap="gray")
    plt.axis("off")
    plt.draw()
    plt.pause(0.1)  # Pause to allow the plot to update


def draw_grid2a(grid_size, walls, visited_points, start, end):
    """
    Draws the grid, walls, start, end, and visited points.

    Args:
        grid: A 2D list representing the grid.
        walls: A set of wall coordinates.
        visited_points: A set of visited coordinates.
        start: A tuple representing the start position.
        end: A tuple representing the end position.
    """
    plt.ion()  # Enable interactive mode

    # Convert the grid to a NumPy array
    grid_array = np.zeros((grid_size, grid_size))

    plt.figure(figsize=(10, 10))
    plt.imshow(grid_array, cmap="gray")

    # Plot walls
    x_walls, y_walls = zip(*walls)
    plt.scatter(x_walls, y_walls, color="black", marker="s")

    # Plot start and end points
    plt.scatter(start[0], start[1], color="green", marker="s", s=100)
    plt.scatter(end[0], end[1], color="red", marker="s", s=100)

    # Plot visited points
    x_visited, y_visited = zip(*visited_points)
    plt.scatter(x_visited, y_visited, color="blue", marker=".")

    plt.axis("off")
    plt.draw()
    plt.pause(0.1)  # Pause to allow the plot to update


def find_shortest_path(h, w, wall_locations, max_walls=1024):
    """
    Finds the shortest path from top-left (0, 0) to bottom-right (h-1, w-1)
    on a grid of size h x w with obstacles (walls) added dynamically from a list,
    limited by the `max_walls` parameter.

    Args:
        h: Height of the grid.
        w: Width of the grid.
        wall_locations: List of wall coordinates (tuples of (row, col)).
        max_walls: Maximum number of walls to add.

    Returns:
        A list of coordinates representing the shortest path, or None if no path exists.
    """

    def is_valid(row, col, walls):
        return 0 <= row < h and 0 <= col < w and (row, col) not in walls

    def neighbors(row, col, walls):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        return [
            (row + dr, col + dc)
            for dr, dc in directions
            if is_valid(row + dr, col + dc, walls)
        ]

    start = (0, 0)
    end = (h - 1, w - 1)

    walls = []
    queue = deque([(start, 0)])  # (coordinate, distance)
    visited = set([start])
    parent = {}
    walls_added = 0

    while queue and walls_added < max_walls:
        (row, col), distance = queue.popleft()

        # Add a new wall if available and within the limit
        if wall_locations:  # and walls_added < max_walls:
            walls.append(wall_locations.pop(0))
            walls_added += 1

        # draw_grid(h, walls)

        if (row, col) == end:
            path = []
            while (row, col) != start:
                path.insert(0, (row, col))
                row, col = parent[(row, col)]
            path.insert(0, start)
            return path

        for neighbor in neighbors(row, col, walls):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = (row, col)
                queue.append((neighbor, distance + 1))

    return None  # No path found


def part1(data, grid_size):
    """Solve part 1"""

    h = w = grid_size

    ans = find_shortest_path(h, w, data)

    print(len(ans))
    print(ans)

    # draw_grid(grid_size, ans)

    return len(ans) - 1


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
