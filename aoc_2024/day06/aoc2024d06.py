# https://adventofcode.com/2024/day/6

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #
test_file = script_path / "test.txt"  #


EAST = ">"
WEST = "<"
NORTH = "n"
SOUTH = "v"
EMPTY = "."


def find_obstacles(data):
    start = None
    positions = []
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell == "#":
                positions.append((r, c))
                continue
            elif cell == "^":
                start = (r, c)

    return (positions, start)


def get_points_between(point1, point2, fixed_coordinate=0):
    """
    Generates a list of points between two given points, fixing either the x or y coordinate.

    Args:
        point1 (tuple): The starting point.
        point2 (tuple): The ending point.
        fixed_coordinate (int, optional): The index of the coordinate to fix (0 for row, 1 for col). Defaults to 0.

    Returns:
        list: A list of points between the two input points.
    """

    print(point1, point2, fixed_coordinate)

    x1, y1 = point1
    x2, y2 = point2

    # Ensure the points are in the correct order based on the fixed coordinate
    if fixed_coordinate == 0:
        if x2 < x1:
            x1, x2 = x2, x1
        print(x1, x2, y1, y2)
        return [(x, y1) for x in range(x1 + 1, x2)]
    else:
        if y2 < y1:
            y1, y2 = y2, y1
        print(x1, x2, y1, y2)
        return [(x1, y) for y in range(y1 + 1, y2)]


def check_for_next_obstacle(obs, current_pos, dir):

    # 6,4 N  up the rows in column 4
    print()
    print(obs, current_pos, dir)

    r, c = current_pos

    if dir in ["N", "E"]:
        step = -1
    else:  #  "S" "W"
        step = 1

    if dir in ["N", "S"]:
        target = c
        moveable = r
        lock_in = 1

    else:  # E, W
        target = r
        moveable = c
        lock_in = 0

    filtered_tuples = [tuple for tuple in obs if tuple[lock_in] == target]
    d = 0 if lock_in == 1 else 1

    print(filtered_tuples)
    print("-" * 10)
    print(target, moveable, d)

    if step == -1:
        closest_tuple = [tuple for tuple in filtered_tuples if tuple[d] < moveable]
    else:
        closest_tuple = [tuple for tuple in filtered_tuples if tuple[d] > moveable]

    print(closest_tuple)

    elimination = min(closest_tuple, key=lambda x: abs(x[d] - target))

    print(elimination)

    visited = get_points_between(current_pos, elimination, d)

    print(set(visited))

    # # Example usage:
    # print("_" * 25)
    # my_tuples = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    # target_number = 7
    # print(my_tuples, target_number)
    # closest_tuple = min(my_tuples, key=lambda x: abs(x[1] - target_number))
    # print(closest_tuple)  # Output: (7, 8)

    # my_tuples = [(0, 4), (1, 4), (9, 4)]
    # target_number = 6

    # print(my_tuples, target_number)
    # print(step)
    # if step == -1:
    #     closest_tuple = [tuple for tuple in my_tuples if tuple[d] < target_number]
    # else:
    #     closest_tuple = [tuple for tuple in my_tuples if tuple[d] > target_number]

    # print(closest_tuple)

    # closest_tuple = min(closest_tuple, key=lambda x: abs(x[0] - target_number))
    # print(closest_tuple)  # Output: (7, 8)

    return None


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [list(d) for d in file.read().split("\n")]

    print(lst)

    return lst


# by sets of numbers, ranges?
# get coords of the walls


def part1(data):
    """Solve part 1"""

    obstructions, start_pos = find_obstacles(data)
    path = {start_pos}

    print(obstructions)
    print(start_pos)
    print(path)

    curr = start_pos

    test = check_for_next_obstacle(obstructions, curr, "N")

    print(test)

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

    print()
    # solutions = solve(soln_file)
