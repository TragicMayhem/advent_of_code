# https://adventofcode.com/2024/day/6

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 4973 /
test_file = script_path / "test.txt"  #  41 /


EAST = ">"
WEST = "<"
NORTH = "n"
SOUTH = "v"
EMPTY = "."


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
    points = [point1]
    for i in range(1, steps + inclusive):
        new_x = x1 + i * dx // steps
        new_y = y1 + i * dy // steps
        points.append((new_x, new_y))

    return points


def sort_by_distance(coordinate_list, target_number, pos):
    """Sorts a list of coordinate tuples by their distance from a target number.

    Args:
      coordinate_list: A list of tuples, where each tuple represents a coordinate pair (x, y).
      target_number: The target number to compare the first coordinate to.
      pos: The coordinate position int he tuple to compare 0 or 1

    Returns:
      A new list of coordinate tuples sorted by their distance from the target number.
    """

    def distance_key(coordinate):
        return abs(coordinate[pos] - target_number)

    return sorted(coordinate_list, key=distance_key)


def check_for_next_obstacle(h, w, obs, current_pos, dn):

    # print("\nobs, curr, dir")
    # print(obs, current_pos, dn)

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
    print("filtered 1:", filtered_tuples)

    d = 1 - lock_in
    if step == -1:
        filtered_tuples = [tuple for tuple in filtered_tuples if tuple[d] < moveable]
    else:
        filtered_tuples = [tuple for tuple in filtered_tuples if tuple[d] > moveable]

    print("filtered_tuples 2:", filtered_tuples)

    filtered_tuples = sort_by_distance(filtered_tuples, moveable, 1 - lock_in)
    print("filtered_tuples 3:", filtered_tuples)

    # print("-" * 10)
    print("target", target, "moveable", moveable, "d", d, "step", step)

    if filtered_tuples:
        walking_to_pos = filtered_tuples.pop(0)
    else:
        if dn == 1:
            walking_to_pos = (-1, c)
        elif dn == 4:
            walking_to_pos = (r, -1)
        elif dn == 3:
            walking_to_pos = (h, c)
        else:
            walking_to_pos = (r, w)

    visited = get_points_between(current_pos, walking_to_pos)

    print("walking_to_pos", walking_to_pos, "len", len(visited))
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

    while in_area:
        # loop, process pos, direction
        next_path = check_for_next_obstacle(h, w, obstructions, pos, dir)
        # extend set
        path.update(next_path)
        # print("Path:", path)

        new_pos = next_path[-1]

        if (
            (dir == 1 and new_pos[0] == 0)
            or (dir == 3 and new_pos[0] == h - 1)
            or (dir == 2 and new_pos[1] == 0)
            or (dir == 4 and new_pos[1] == w - 1)
        ):
            print("out of area?")
            in_area = False

        print("Path length:", len(path))
        # direction change
        dir = get_next_direction(dir)
        pos = new_pos
        print("\nnew_pos, dir", new_pos, dir)

    print("-" * 10)
    print("Path:", path)

    return len(path)


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
