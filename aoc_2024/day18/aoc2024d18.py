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
        lst = [(int(x), int(y)) for x, y in (line.split(',') for line in file.read().splitlines())]

        print(lst)


    return lst

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

    plt.imshow(grid, cmap='gray')
    plt.axis('off')
    plt.draw()
    plt.pause(0.1)  # Pause to allow the plot to update


def find_shortest_pathv1(h,w, wall_locations):
    """
    Finds the shortest path from top-left (0,0) to bottom-right (grid_size-1, grid_size-1) 
    on a grid with obstacles (walls) added dynamically from a list.

    Args:
        grid_size: Size of the grid (e.g., 7 for a 7x7 grid).
        wall_locations: List of wall coordinates (tuples of (row, col)).

    Returns:
        A list of coordinates representing the shortest path, or None if no path exists.
    """

    def is_valid(row, col, walls):
        return 0 <= row < h and 0 <= col < w and (row, col) not in walls

    def neighbors(row, col, walls):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        return [(row + dr, col + dc) for dr, dc in directions if is_valid(row + dr, col + dc, walls)]

    start = (0, 0)
    end = (h - 1, w - 1)

    queue = deque([(start, 0)])  # (coordinate, distance)
    visited = set([start])
    parent = {}  # Store parent for path reconstruction

    walls = []  # Initialize with no walls

    while queue:

        draw_grid(7, walls)

        (row, col), distance = queue.popleft()

        # Add the next wall from the list
        if wall_locations:
            new_wall = wall_locations.pop(0)
            walls.append(new_wall)

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
        return [(row + dr, col + dc) for dr, dc in directions if is_valid(row + dr, col + dc, walls)]

    start = (0, 0)
    end = (h - 1, w - 1)

    walls = []
    queue = deque([(start, 0)])  # (coordinate, distance)
    visited = set([start])
    parent = {}
    walls_added = 0

    while queue:
        (row, col), distance = queue.popleft()

        # Add a new wall if available and within the limit
        if wall_locations and walls_added < max_walls:
            new_wall = wall_locations.pop(0)
            walls.append(new_wall)
            walls_added += 1

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


    return len(ans) -1 


def part2(data, grid_size):
    """Solve part 2"""

    return 1


def solve(puzzle_input, run="Solution", grid_size=70):
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

    tests = solve(test_file, run="Test", grid_size=7)

    print()
    solutions = solve(soln_file)
