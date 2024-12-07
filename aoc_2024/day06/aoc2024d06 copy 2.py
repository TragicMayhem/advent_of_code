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


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [list(d) for d in file.read().split("\n")]

    print(lst)

    return lst


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


def get_points_between(point1, point2, inclusive=0):
    """Generates a list of points between two given points, taking the shortest path.

    Args:
        point1 (tuple): The starting point.
        point2 (tuple): The ending point.
        inclusive: Wheter to include or exclude point2 from the list.
        Default not including the last point = 0

    Returns:
        list: A list of points between the two input points.
    """

    x1, y1 = point1
    x2, y2 = point2

    # Determine the direction of movement
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the number of steps in each direction
    steps = max(abs(dx), abs(dy))

    # Generate points along the shortest path
    points = []
    for i in range(1, steps + inclusive):
        new_x = x1 + i * dx // steps
        new_y = y1 + i * dy // steps
        points.append((new_x, new_y))

    return points


def check_for_next_obstacle(obs, current_pos, dn):

    print("\nobs, curr, dir")
    print(obs, current_pos, dn)

    r, c = current_pos

    if dn in [1, 4]:  # N W
        step = -1
    else:  #  "S" "E"
        step = 1

    if dn in [1, 3]:  # N S
        target = c
        moveable = r
        lock_in = 1

    else:  # E, W
        target = r
        moveable = c
        lock_in = 0

    filtered_tuples = [tuple for tuple in obs if tuple[lock_in] == target]
    d = 0 if lock_in == 1 else 1

    print("-" * 10)
    print("filtered:", filtered_tuples)
    print("target, moveable, d, step")
    print(target, moveable, d, step)

    if step == -1:
        closest_tuple = [tuple for tuple in filtered_tuples if tuple[d] < moveable]
    else:
        closest_tuple = [tuple for tuple in filtered_tuples if tuple[d] > moveable]

    # If there are NO obstacles in the directional path, means the guard will walk out of area
    # Get the last point and path. How to tell

    print(closest_tuple)

    walking_to_pos = min(closest_tuple, key=lambda x: abs(x[d] - target))
    print(walking_to_pos)

    visited = get_points_between(current_pos, walking_to_pos)

    print(visited)
    print(set(visited))

    return visited


def get_next_direction(current_value):
    # Turning right each time
    # dirns = [1, 2, 3, 4]  # N, E, S, W
    return (current_value % 4) + 1


def part1(data):
    """Solve part 1"""

    h = len(data)
    w = len(data[0])

    obstructions, start_pos = find_obstacles(data)
    path = {start_pos}

    print(obstructions)
    print(start_pos)
    print(path)

    # dirns = [1, 2, 3, 4]  # N, E, S, W

    pos = start_pos
    dir = 1
    in_area = True

    # print("TEST")
    # test = check_for_next_obstacle(obstructions, pos, dir)
    # print(test)
    # print("TEST OVER")

    while in_area:
        # loop
        # process pos, direction
        next_path = check_for_next_obstacle(obstructions, pos, dir)
        new_pos = next_path[-1]

        # extend set
        path.update(next_path)
        print("Path:", path)

        if (
            (dir == 1 and new_pos[0] == 0)
            or (dir == 3 and new_pos[0] == h)
            or (dir == 2 and new_pos[1] == 0)
            or (dir == 4 and new_pos[1] == w)
        ):
            print("out of area?")
            in_area = False

        # direction change
        dir = get_next_direction(dir)
        pos = new_pos
        # if not left area then
        print(new_pos, dir)

        # in_area = False

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
