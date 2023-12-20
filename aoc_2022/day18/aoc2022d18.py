# https://adventofcode.com/2022/day/18

import pathlib
import time
from collections import deque
from itertools import product
from operator import itemgetter

script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 4444 / 2530
test_file = script_path / "test.txt"  # 64 /  58


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r") as fin:
        lines = fin.read().split("\n")

    droplets = {}

    for l in lines:
        nums = tuple(map(int, l.split(",")))
        droplets[nums] = 6

    return droplets


def cardinals(x, y, z):
    # create list and yield from it
    to_check = [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]

    yield from to_check


def check_for_space(alldrops, current, x, y, z):
    checked_drops = set()

    xmin, xmax = x
    ymin, ymax = y
    zmin, zmax = z

    queue = deque([current])
    # print(list(current)) # this is different to[]
    # print([current])

    faces_count = 0

    while queue:
        next_drop = queue.pop()
        # print(next_drop)

        if next_drop in checked_drops:
            continue

        checked_drops.add(next_drop)
        cx, cy, cz = next_drop

        # maybe need +1
        # if xmin > cx or xmax+1 < cx or ymin > cy or ymax+1 < cy  or zmin > cz or zmax+1 <cz:
        # print(next_drop, xmin <= cx < xmax+1,ymin <= cy < ymax+1,zmin <= cz < zmax+1)

        checkx = xmin < cx < xmax
        checky = ymin < cy < ymax
        checkz = zmin < cz < zmax
        # print( checkx, checky, checkz)

        if not checkx or not checky or not checkz:
            return 0, checked_drops

        for tmp in cardinals(cx, cy, cz):
            if tmp in alldrops:
                faces_count += 1
            elif tmp not in checked_drops:
                queue.append(tmp)

    return faces_count, checked_drops


def part1(data):
    """Solve part 1"""

    droplets = data.copy()

    for d in droplets:
        for surrounding in cardinals(*d):
            if surrounding in droplets:
                # print("in list")
                droplets[d] -= 1
    total = 0

    for d in droplets.values():
        # print(d)
        total += d

    # print(total)
    return total


def part2(data):
    """Solve part 2"""
    # need to calculate the 3d space for the droplets

    droplets = data.copy()

    total = part1(droplets)

    xmin = ymin = zmin = 999
    xmax = ymax = zmax = 0

    for d in droplets:
        cx, cy, cz = d
        xmin = min(cx, xmin)
        ymin = min(cy, ymin)
        zmin = min(cz, zmin)
        xmax = max(cx, xmax)
        ymax = max(cy, ymax)
        zmax = max(cz, zmax)

    xmax += 1
    ymax += 1
    zmax += 1
    # print(xmin, xmax)
    # print(ymin, ymax)
    # print(zmin, zmax)

    all_space_visited = set()
    found_faces = 0

    for new_drop in product(
        range(xmin, xmax + 1), range(ymin, ymax + 1), range(zmin, zmax + 1)
    ):
        if new_drop not in droplets:
            if new_drop not in all_space_visited:
                faces_touching, visited = check_for_space(
                    droplets, new_drop, (xmin, xmax), (ymin, ymax), (zmin, zmax)
                )
                # print(new_drop, faces_touching)
                found_faces += faces_touching

                ### IDIOT - Forgot it returns new union and need to assign to varialbe or use |=
                ### e.g. all_space_visited |= visited

                # all_space_visited.union(visited)
                all_space_visited = all_space_visited.union(visited)

    ans = total - found_faces

    # print("total", total)
    # print("found faces", found_faces)
    # print("new", ans)
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
