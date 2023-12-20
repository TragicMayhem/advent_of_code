# https://adventofcode.com/2022/day/15

import pathlib
import time
import re


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  #  5809294 (8+secs) //  10693731308112  (60+sec)
test_file = script_path / "test.txt"  #  26  //  56000011

TARGET_ROW_TEST = 10
TARGET_ROW_INPUT = 2000000
TARGET_ROW = None

MAX_RANGE_TEST = 20
MAX_RANGE_INPUT = 4000000
MAX_RANGE = None


###  PART 2 DOESNT RUN, WELL DOESNT FINISH
###  REASON IS I AM CALCULATING ALL THE POINTS - MILLIONS.
###  RESEARCH SHOWS I NEED TO KEEP THE RANGES AND THEN CHECK NOT STORE
###  KEEP THE OTHER VERSION FOR REFERENCE


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


def range_check(range_list):
    # Assumes list
    _, end_range = range_list[0]

    if len(range_list) == 0:
        return None
    if len(range_list) == 1:
        return None

    for next_start, next_end in range_list[1:]:
        # Check if overlap
        if next_start <= end_range + 1:
            end_range = max(end_range, next_end)
        else:
            return next_start - 1


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


### Version 2 - the first attempt at part 2 never completes.
### Change it round, do every row (y) and look at all beacons
### Rather than all beacons and find all the ranges and coverage


def part2(data):
    """Solve part 2"""
    print("Part 2")

    for current_y in range(0, MAX_RANGE + 1):
        # print("current y is...", current_y)

        beacon_ranges = []

        for pair in data:
            sensor, beacon = pair
            (sx, sy) = sensor
            (bx, by) = beacon

            distance = abs(sx - bx) + abs(sy - by)
            pos_left = sx - distance
            pos_right = sx + distance
            pos_up = sy - distance
            pos_down = sy + distance

            y_dist_from_sensor = abs(current_y - sy)
            start_x = max(0, pos_left + y_dist_from_sensor)
            end_x = min(MAX_RANGE, pos_right - y_dist_from_sensor)

            if pos_up <= current_y <= pos_down:
                beacon_ranges.append((start_x, end_x))

        beacon_ranges.sort()
        # normal: [(0, 11), (5, 11), (11, 15), (13, 20)]
        # gap: [(0, 3), (2, 2), (3, 13), (11, 13), (15, 17), (15, 20)]
        # print(beacon_ranges)
        # print("checked sensors and beacons at y-level = ", current_y)

        empty_point = range_check(beacon_ranges)

        if empty_point:
            break

    print(empty_point)
    ans = empty_point * 4000000 + current_y

    return ans


# def solve(puzzle_input):
#     """Solve the puzzle for the given input"""
#     times = []

#     data = parse(puzzle_input)

#     times.append(time.perf_counter())
#     solution1 = part1(data)
#     times.append(time.perf_counter())
#     solution2 = part2(data)
#     times.append(time.perf_counter())

#     return solution1, solution2, times


# def runTest(test_file):
#     data = parse(test_file)
#     test_solution1 = part1(data)
#     test_solution2 = part2(data)
#     return test_solution1, test_solution2


# def runAllTests():

#     print("Tests")
#     a, b = runTest(test_file)
#     print(f"Test1.  Part1: {a} Part 2: {b}")


# if __name__ == "__main__":

#     TARGET_ROW = TARGET_ROW_TEST
#     MAX_RANGE = MAX_RANGE_TEST
#     runAllTests()

#     TARGET_ROW = TARGET_ROW_INPUT
#     MAX_RANGE = MAX_RANGE_INPUT
#     solutions = solve(soln_file)
#     print("\nAOC")
#     print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
#     print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
#     print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")


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
    TARGET_ROW = TARGET_ROW_TEST
    MAX_RANGE = MAX_RANGE_TEST
    tests = solve(test_file, run="Test")

    print()
    TARGET_ROW = TARGET_ROW_INPUT
    MAX_RANGE = MAX_RANGE_INPUT
    solutions = solve(soln_file)
