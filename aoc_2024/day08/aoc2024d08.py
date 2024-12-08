# https://adventofcode.com/2024/day/8

import pathlib
import time
import math
from itertools import combinations as comb

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 394 /
# Wrong: 395=High
test_file = script_path / "test.txt"  # 14 /  34


def find_antinodes(point1, point2):
    """Finds two antinodes on the line connecting the given points.

    Args:
      point1: A tuple representing the coordinates of the first point (x1, y1).
      point2: A tuple representing the coordinates of the second point (x2, y2).

    Returns:
      A list of two tuples, each representing the coordinates of an antinode.
    """

    x1, y1 = point1
    x2, y2 = point2

    # Calculate the vector between the points
    vector_x = x2 - x1
    vector_y = y2 - y1

    # Calculate the antinodes by adding/subtracting the vector from each point
    antinode1 = (x1 - vector_x, y1 - vector_y)
    antinode2 = (x2 + vector_x, y2 + vector_y)

    return [antinode1, antinode2]


def filter_in_range(points_list, height, width):
    """Filters a list of tuples to keep only those within the specified height and width.

    Args:
      tuples_list: A list of tuples, where each tuple represents a point (x, y).
      height: The maximum height of the grid.
      width: The maximum width of the grid.

    Returns:
      A list of tuples that are within the specified height and width.
    """

    return [(x, y) for x, y in points_list if 0 <= x < width and 0 <= y < height]


def create_point_dictionary(grid):
    """
    Creates a dictionary of lists of points from a grid of characters.

    Args:
      grid: A list of strings representing the grid.

    Returns:
      A dictionary where keys are characters and values are
      lists of (x, y) tuples representing the points.
    """

    point_dict = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != ".":
                if char not in point_dict:
                    point_dict[char] = []
                point_dict[char].append((x, y))

    return point_dict


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [list(d) for d in file.read().split("\n")]

    return lst


def part1(data):
    """Solve part 1"""

    h = len(data)
    w = len(data[0])
    print(h, w)

    antennas = create_point_dictionary(data)
    print(antennas)

    antinodes = set()
    full_antinotes = []

    # careful of lone antennas

    for antenna, positions in antennas.items():

        for pt1, pt2 in comb(positions, 2):
            print("\n", antenna, pt1, pt2)

            new_antinodes = find_antinodes(pt1, pt2)
            print(new_antinodes)
            full_antinotes += new_antinodes

            antinodes_in_range = filter_in_range(new_antinodes, h, w)
            antinodes.update(set(antinodes_in_range))

    print()
    print(antinodes)

    print(len(antennas.keys()), len(full_antinotes))
    tmp = filter_in_range(full_antinotes, h, w)
    print(len(tmp), len(set(tmp)))

    return len(antinodes)


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

    print()
    solutions = solve(soln_file)
