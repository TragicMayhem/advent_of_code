# https://adventofcode.com/2022/day/15

import pathlib
import time
import re


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #  5809294 (very slow ~10s) //
test_file = script_path / "test.txt"  #  26  //  56000011

TARGET_ROW_TEST = 10
TARGET_ROW_INPUT = 2000000
TARGET_ROW = None

MAX_RANGE_TEST = 20
MAX_RANGE_INPUT = 4000000
MAX_RANGE = None


###  PART 2 DOESNT RUN, WELL DOESNT FINISH
###  REASON IS i AM CALCULATING ALL THE POINTS - MILLIONS.
###  RESEARCH SHOWS I NEED TO KEEP THE RANGES AND THEN CHECK NOT STORE
###  KEEP THIS VERSION FOR REFERENCE


def parse(puzzle_input):
    """Parse input"""

    search_re = re.compile(r"[-]*\d+")
    data = []
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15

    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n")

    for info in lst:
        matching_numbers = list(map(int, search_re.findall(info)))

        if matching_numbers:
            sx = matching_numbers[0]
            sy = matching_numbers[1]
            bx = matching_numbers[2]
            by = matching_numbers[3]

            data.append([(sx, sy), (bx, by)])

    return data


def getRowCover(cave, sensor_y, row, from_x, to_x):
    sensor_range = set()

    y_dist_from_sensor = abs(row - sensor_y)
    start_x = min(from_x, to_x) + y_dist_from_sensor
    end_x = max(from_x, to_x) - y_dist_from_sensor

    # move to calling loop
    # if row == TARGET_ROW:
    for pos in range(start_x, end_x):
        sensor_range.add((pos, row))

    return sensor_range

    # return set()


def row_check(pos_list):
    for i in range(0, len(pos_list) - 1):
        print(pos_list[i], pos_list[i + 1])

        if abs(pos_list[i] - pos_list[i + 1]) >= 2:
            return i + 1

    return None


def part1(data):
    """Solve part 1"""

    cave_cover = set()

    beacons_in_range = set()

    for pair in data:
        sensor, beacon = pair
        (sx, sy) = sensor
        (bx, by) = beacon

        distance = abs(sx - bx) + abs(sy - by)

        # print(sensor, beacon, distance)

        left = sx - distance
        right = sx + distance
        up = sy - distance
        down = sy + distance

        # Diamond. So rather than full square, need to work out the y distance
        # so you can take off the x distance.  The taxicab distance is the sum
        # of the abs x / y so if you know the distance from the sensor in the y
        # you know how big the horizontal can be by subtracting the height from width

        if by == TARGET_ROW:
            beacons_in_range.add(beacon)

        for current_y in range(min(up, down), max(up, down)):
            # Moved if statement here (fom function) to reduce calls and time taken from 32s to 8s
            if current_y == TARGET_ROW:
                cave_row_cover = getRowCover(cave_cover, sy, current_y, left, right)
                cave_cover.update(cave_row_cover)

    print(beacons_in_range)
    print(
        "Beacons",
        len(beacons_in_range),
        "Cave cover for row",
        TARGET_ROW,
        "is",
        len(cave_cover),
    )

    return len(cave_cover)


def part2(data):
    """Solve part 2"""
    print("Part 2")

    cave_coverage = set()

    print("getting coverage")
    for pair in data:
        sensor, beacon = pair
        (sx, sy) = sensor
        (bx, by) = beacon

        distance = abs(sx - bx) + abs(sy - by)

        # print(sensor, beacon, distance)

        pos_left = sx - distance
        pos_right = sx + distance
        pos_up = sy - distance
        pos_down = sy + distance

        for current_y in range(0, MAX_RANGE + 1):
            sensor_range = set()
            y_dist_from_sensor = abs(current_y - sy)
            start_x = pos_left + y_dist_from_sensor
            end_x = pos_right - y_dist_from_sensor

            # New Rule
            start_x = max(0, start_x)
            end_x = min(MAX_RANGE, end_x)

            if pos_up <= current_y <= pos_down:
                for col in range(start_x, end_x + 1):
                    sensor_range.add((col, current_y))
                cave_coverage.update(sensor_range)

    print("Number of cave_points:", len(cave_coverage))

    cave_points = sorted(cave_coverage, key=lambda a: a[1])
    cave_rows = []

    print("Looking for empty position....")
    for current_y in range(0, MAX_RANGE + 1):
        print("current y is...", current_y)
        # Ver 1: Points list for each y level
        # tmp = [tup for tup in cave_points if current_y == tup[1]]

        # VER 2: Only the x coords for each point in a y level
        tmp = sorted([x for x, y in cave_points if current_y == y])
        print(current_y, tmp)
        cave_rows.append(tmp)

        empty_point = row_check(tmp)

        if empty_point:
            break

    print(empty_point)
    ans = empty_point * 4000000 + current_y

    return ans


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
