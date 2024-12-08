# https://adventofcode.com/2024/day/6

import pathlib
import time

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 4973 /  High:2313
test_file = script_path / "test.txt"  #  41 / 6


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = [list(d) for d in file.read().split("\n")]

    # print(lst)

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

    filtered_tuples = [tup for tup in obs if tup[lock_in] == target]

    d = 1 - lock_in
    if step == -1:
        filtered_tuples = [tup for tup in filtered_tuples if tup[d] < moveable]
    else:
        filtered_tuples = [tup for tup in filtered_tuples if tup[d] > moveable]

    filtered_tuples = sort_by_distance(filtered_tuples, moveable, 1 - lock_in)

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

    # print("walking_to_pos", walking_to_pos, "len", len(visited))
    return visited


def get_next_direction(current):
    # Turning right each time
    # dirns = [1, 2, 3, 4]  # N, E, S, W
    return (current % 4) + 1


def find_guard_path(data):

    h = len(data)
    w = len(data[0])

    obstructions, pos = find_obstacles(data)
    path = {pos}
    direct = 1
    in_area = True

    while in_area:
        next_path = check_for_next_obstacle(h, w, obstructions, pos, direct)
        path.update(next_path)

        new_pos = next_path[-1]

        if (
            (direct == 1 and new_pos[0] == 0)
            or (direct == 3 and new_pos[0] == h - 1)
            or (direct == 2 and new_pos[1] == 0)
            or (direct == 4 and new_pos[1] == w - 1)
        ):
            in_area = False

        direct = get_next_direction(direct)
        pos = new_pos

    return path


def part1(data):
    """Solve part 1"""

    return len(find_guard_path(data))


def run_scenario(obstructions, h, w, pos):

    in_area = True
    direct = 1
    path = set()
    visited = set()

    while in_area:
        next_path = check_for_next_obstacle(h, w, obstructions, pos, direct)

        for new in next_path:
            check = (new, direct)
            if check in visited:
                return True
            visited.add(check)

        path.update(next_path)
        new_pos = next_path[-1]

        if (
            (direct == 1 and new_pos[0] == 0)
            or (direct == 3 and new_pos[0] == h - 1)
            or (direct == 2 and new_pos[1] == 0)
            or (direct == 4 and new_pos[1] == w - 1)
        ):
            in_area = False
            break

        direct = get_next_direction(direct)
        pos = new_pos

    return False


def part2(data):
    """Solve part 2"""

    print("Part 2")

    # Start is (44, 69)

    # Notes
    # Some input from web using delta_r (dr) and delta_c (dc) -1 0 1 to show directions
    # Need to cature the path (so visited)
    #   also direction guard was going to see if repeating and in a loop.
    #   Then break and count
    # I dont see how I can do as I did in part 1 and a set of tuple coordinates.
    # How would you change one of them... and then rest of the grid?

    # Need to MOVE along the original path, change by adding an obstacle (and remembering it)
    # Then try and solve

    h = len(data)
    w = len(data[0])

    initial_obstructions, start_pos = find_obstacles(data)
    intial_path = find_guard_path(data)

    # print(start_pos, initial_obstructions)
    # print(intial_path)

    possible_options = 0

    for seen_coords in intial_path:
        if seen_coords == start_pos:
            print("start ignored")
            continue

        obstructions = initial_obstructions.copy()
        obstructions.append(seen_coords)

        tmp = run_scenario(obstructions, h, w, start_pos)

        if tmp:
            # print(seen_coords, tmp, possible_options)
            possible_options += 1

    return possible_options


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
