# https://adventofcode.com/2022/day/1

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # 757 //  24943
input_test = script_path / "test.txt"  # 24 // 93

# Options
# Grid and replace recursive
# Would node tee - Left, down, right child work... pattern down until stop, set

SAND_SOURCE = (500, 0)

AIR = 0
SAND = 1
ROCK = 2


def parse(puzzle_input):
    """Parse input"""
    # 503,4 -> 502,4 -> 502,9 -> 494,9

    rocks = []
    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n")

    for l in lst:
        parts = l.split(" -> ")
        rock_path = []
        for p in parts:
            coords = tuple(map(int, p.split(",")))
            rock_path.append(coords)

        rocks.append(rock_path)

    return rocks


def get_moves(r, c):
    # DOWN then LEFT then RIGHT
    for delta_r, delta_c in ((0, 1), (-1, 1), (1, 1)):
        rr, cc = (r + delta_r, c + delta_c)
        yield (rr, cc)


def fill_v1(point, cave, max_y):
    print(point)
    print("Points in cave", len(cave))
    print("Max Y", max_y)

    grainsOfSand = 0
    keepPouring = True

    while keepPouring:
        current = point
        moving = True

        while moving:
            sand_x, sand_y = current

            # Lesson: Pt1 failure, I put the wrong coords in wront variable (wasted hours)
            pt_down, pt_left, pt_right = get_moves(sand_x, sand_y)
            # print(pt_left, pt_down, pt_right)

            # NEED TO CHECK Y + 1
            if sand_y > max_y:
                # print("lowest", current)
                keepPouring = False
                break

            # 1st: down
            if pt_down not in cave:
                # print("down", pt_down)
                current = pt_down
                continue

            # 2nd: left
            if pt_left not in cave:
                # print("left", pt_left)
                current = pt_left
                continue

            # 3rd: right
            if pt_right not in cave:
                # print("right", pt_right)
                current = pt_right
                continue

            # Actualy, only add if no free space down, left and right!
            cave.add(current)
            moving = False
            grainsOfSand += 1
            break

    print("Sand count  :", grainsOfSand)
    # print(cave)

    return grainsOfSand


def fill_v2(point, cave, max_y):
    print(point)
    print("Points in cave", len(cave))
    print("Max Y", max_y)

    grainsOfSand = 0
    keepPouring = True

    while keepPouring:
        current = point
        moving = True

        while moving:
            sand_x, sand_y = current

            pt_down, pt_left, pt_right = get_moves(sand_x, sand_y)
            # print(pt_left, pt_down, pt_right)

            # if current in cave and current == SAND_SOURCE:
            #     pass

            if sand_y == max_y:
                print("At floor", current)
                cave.add(current)
                moving = False

            if sand_y > max_y:
                # print("lowest", current)
                keepPouring = False
                break

            # 1st: down
            if pt_down not in cave:
                # print("down", pt_down)
                current = pt_down
                continue

            # 2nd: left
            if pt_left not in cave:
                # print("left", pt_left)
                current = pt_left
                continue

            # 3rd: right
            if pt_right not in cave:
                # print("right", pt_right)
                current = pt_right
                continue

            # Actualy, only add if no free space down, left and right!
            moving = False
            print("Adding new grain", current)
            cave.add(current)
            grainsOfSand += 1

            if current == SAND_SOURCE:
                keepPouring = False
                break

    print("Sand count  :", grainsOfSand)
    # print(cave)

    return grainsOfSand


def set_cave_blocks(rocks):
    blocks = set()

    for rock_path in rocks:
        # print(rock_path)

        for c in range(len(rock_path) - 1):
            from_x, from_y = rock_path[c]
            to_x, to_y = rock_path[c + 1]

            start_x = min(from_x, to_x)
            end_x = max(from_x, to_x)

            start_y = min(from_y, to_y)
            end_y = max(from_y, to_y)

            # print(from_x, from_y, to_x, to_y)

            for r in range(start_x, end_x + 1):
                for c in range(start_y, end_y + 1):
                    blocks.add((r, c))

    # print(blocks)
    return blocks


def part1(data):
    """Solve part 1"""

    cave = set_cave_blocks(data)

    # Get highest y
    max_y = max([y for (x, y) in cave])
    print("Max y = ", max_y)

    ans = fill_v1(SAND_SOURCE, cave, max_y)

    return ans


def part2(data):
    """Solve part 2"""

    cave = set_cave_blocks(data)

    # Get highest y , add 2 fo the floor
    max_y = max([y for (x, y) in cave]) + 2
    print("Max y (floor) = ", max_y)

    ans = fill_v2(SAND_SOURCE, cave, max_y)

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

    tests = solve(input_test, run="Test")

    print()
    solutions = solve(input)
