# https://adventofcode.com/2021/day/x

import pathlib
import time
import numpy as np

"""
OMg I nearly stopped it thinking another infinite loop, but it was the right answer.... 100% inefficient so room for improvement!

Tests
Test1.  Part1: 39 Part 2: 39
Test2.  Part1: 590784 Part 2: 39769202357821
Test3.  Part1: 474140 Part 2: 2758514936282225

AOC
Solution 1: 583636 in 0.0104s
Solution 2: 1294137045134837 in 36.2598s

only running 1 copy (oops) takes 16.1s  (old laptop ubuntu)  10.1 on new Win11 PC
"""


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 583636 / 1294137045134837
test_file = script_path / "test.txt"  # 39 / 39
test_file2 = script_path / "test2.txt"  # 590784 / maybe 39769202357821
test_file3 = script_path / "test3.txt"  # 474140 / 2758514936282235


def parse(puzzle_input):
    """Parse input"""
    # example: on x=10..10,y=10..10,z=10..10

    instructions = []

    with open(puzzle_input, "r") as file:
        data = file.read().replace(",", " ").split("\n")

        data = [d.split(" ") for d in data]
        # print(data)

        for d in data:
            step = 1 if d[0] == "on" else 0

            first = d[1][2:].split("..")
            second = d[2][2:].split("..")
            third = d[3][2:].split("..")

            (x1, x2) = map(int, first)
            (y1, y2) = map(int, second)
            (z1, z2) = map(int, third)
            instructions.append(tuple([step, (x1, x2), (y1, y2), (z1, z2)]))

    # print(instructions)
    return instructions


def part1(data, reactor_size):
    """Solve part 1"""
    # example: (1, (10, 12), (10, 12), (10, 12))
    size = reactor_size

    reactor = np.zeros((2 * size, 2 * size, 2 * size))

    for d in data:
        # print(d)
        step = d[0]

        (x1, x2), (y1, y2), (z1, z2) = d[1], d[2], d[3]

        if (
            max(abs(x1), abs(x2)) > size
            or max(abs(y1), abs(y2)) > size
            or max(abs(z1), abs(z2)) > size
        ):
            continue

        x1 += size
        x2 += size
        y1 += size
        y2 += size
        z1 += size
        z2 += size

        # plus 1 for the range calculations and loops
        (cx, cy, cz) = (x2 - x1 + 1, y2 - y1 + 1, z2 - z1 + 1)
        # print(cx,cy,cz)

        tmp = np.full((cx, cy, cz), step)
        # print(tmp.shape,'coords',x1,x2,y1,y2,z1,z2)

        reactor[x1 : x2 + 1, y1 : y2 + 1, z1 : z2 + 1] = tmp

    # print(reactor)
    # print(reactor.sum())
    return int(reactor.sum())


def generate_set(x, y, z):
    (x1, x2), (y1, y2), (z1, z2) = x, y, z

    for nx in range(x1, x2 + 1):
        for ny in range(y1, y2 + 1):
            for nz in range(z1, z2 + 1):
                yield (nx, ny, nz)

    # TODO how to collapse the loops?
    # (x,y,z)for x in range(x1,x2+1) for y in range(y1,y2+1) for z in range(z1,z2+1)


# REMINDER Attempt 1 for Part 2
# DO NOT CALCULATE THE TUPLES OF POINTS - Grinds to a halt!
# mySet = set((x,y,z) for x in range(x1,x2+1) for y in range(y1,y2+1) for z in range(z1,z2+1))
# print(len(mySet))
# for item in generate_set(d[1], d[2], d[3]):
#     print(item)
# mySet = set(item for item in generate_set(d[1], d[2], d[3]))
# print('myset len',len(mySet))


def calc_vol(xr, yr, zr):  # Pass in the ranges for the instructions
    return abs((xr[1] - xr[0] + 1) * (yr[1] - yr[0] + 1) * (zr[1] - zr[0] + 1))


def checkaxis(rng1, rng2):
    # deduplicate of the if statement from main code

    # Can use this for any axis (x,y,or z)
    # input - (a1,a2) and (b1,b2)
    # output - overlap range

    (a1, a2) = rng1
    (b1, b2) = rng2

    # check for any of the overlap points within the ranges given
    if (a1 <= b1 < a2) or (b1 <= a1 < b2) or (a1 < b2 <= a2) or (b1 < a2 <= b2):
        # So this indicates there is an overlap with given ranges
        # to find where, need the two numbers as return point , this is not the lowest or highest, so sort them
        overlaps = sorted([a1, a2 - 1, b1, b2 - 1])
        # print(overlaps[1],overlaps[2]+1)
        return (overlaps[1], overlaps[2] + 1)  # Forgot to add one, for range accuracy

    return None  # This shows no overlapping ranges.


def range_check(cube1, cube2):
    # cube1 and cube2 need to be (xr,yr,zr) where xr is (x1,x2) the range on an ais to define the cube
    # print("  range check", cube1, cube2)
    c1x, c1y, c1z = cube1
    c2x, c2y, c2z = cube2

    # need to do for each pairing
    overlap_xr = checkaxis(c1x, c2x)
    overlap_yr = checkaxis(c1y, c2y)
    overlap_zr = checkaxis(c1z, c2z)

    # if any are zero is there an overlap?  to check
    if not overlap_xr or not overlap_yr or not overlap_zr:
        return None

    # form the cube points for the intersection
    new_xr = (overlap_xr[0], overlap_xr[1])
    new_yr = (overlap_yr[0], overlap_yr[1])
    new_zr = (overlap_zr[0], overlap_zr[1])

    return (new_xr, new_yr, new_zr)


def part2(data):
    """Solve part 2"""

    # NOTES AS I WORK OUT WHAT THIS IS
    # store count of the number turned on?
    # store number of turned off
    # can even store that many coords numbers.... ha ha, no you cant.
    # use sets but with what?
    #   need to NOT calculate all the points but do need to know union, intersetion
    #   can only do by the input ranges, literally work out the overlap with the ranges for each on/off and action

    reactor_lights_on = 0
    # reactor_lights_off = 0  # Dont need to track off

    track_on_cubes = []
    track_off_cubes = []

    for i, d in enumerate(data):  # Process all the instructions
        # print("\nNEXT:",d)

        # need to get this at the start for checking, so that it doesn't
        # check ones adding as part of the checking on lights.
        # specifically when adding 'off' intersections to the off list, do not want to check
        # again in this iterations - as that would be intersection and then add more lights. wrongly.
        how_many_in_on_list = len(track_on_cubes)
        how_many_in_off_list = len(track_off_cubes)

        step = d[0]
        (x1, x2), (y1, y2), (z1, z2) = xr, yr, zr = d[1], d[2], d[3]
        this_cube = (xr, yr, zr)

        num_changing = calc_vol(xr, yr, zr)

        # On so just need to increase the count.
        # Stop. Need increase by ones outside of range!?
        #   do you add the whole number calculated then take off the overlap?
        # for the offs you need to work out the overlap.
        # kind of the same for the ons.
        # but what are we comparing if we dont know the ranges and points?!
        #   Going to need to parse the instructions on and off, then keep record to check each new one against all previous

        # cube needs to sets of xyz or the ranges of the axis

        if step == 1:  # On instruction
            reactor_lights_on += calc_vol(
                *this_cube
            )  # add all lights to total (take of the intersection next to avoid double counting)
            track_on_cubes.append(this_cube)

        # else:
        #     track_off_cubes.append((xr,yr,zr))

        # Basically going to loop around x,y,z for two cubes
        # Sequence of instructions is important to end with the correct on and off
        # the intersection (overlap), like in sets, will be where the cubes are affecting one another.
        # so each check will create many different cubes of on/off - how to break apart and track?

        # try 1
        # work out intersection(s) this cube and other (all time)
        #   then
        #   if its on thn need to remove vol of the intersection from this volume (not to doubel count)
        #   if its off then need to remove from on total, and ignore rest
        #  update: cant do, need a list of on/off to check the intersections and then do the math

        for i in range(how_many_in_on_list):
            n = track_on_cubes[i]
            # print('looping on list',n)

            # check this new one with all previous on lights
            # anything outside of known ranges increases the lights turned on
            overlap_result = range_check(this_cube, n)
            # print('overlap res', overlap_result)

            if overlap_result:
                reactor_lights_on -= calc_vol(
                    *overlap_result
                )  # Take off the overlap to avoid double count
                track_off_cubes.append(overlap_result)

        # check against the off blocks that is being built up
        for i in range(how_many_in_off_list):
            n = track_off_cubes[i]
            overlap_result = range_check(this_cube, n)
            if overlap_result:
                # checking this cube against the off intersections that have been recorded (tracked)
                # these need to be added back on.
                # This is the mistake I made and took ages to unpick with google and redit
                reactor_lights_on += calc_vol(*overlap_result)
                track_on_cubes.append(overlap_result)

    return reactor_lights_on


def solve(puzzle_input, size):
    """Solve the puzzle for the given input"""
    times = []

    data = parse(puzzle_input)

    times.append(time.perf_counter())

    solution1 = part1(data, size)
    times.append(time.perf_counter())
    solution2 = part2(data)

    times.append(time.perf_counter())

    return solution1, solution2, times


def runTest(test_file, size):
    data = parse(test_file)
    test_solution1 = part1(data, size)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():
    print("Tests")
    a, b = runTest(test_file, 15)
    print(f"Test1.  Part1: {a} Part 2: {b}")
    a, b = runTest(test_file2, 60)
    print(f"Test2.  Part1: {a} Part 2: {b}")
    a, b = runTest(test_file3, 60)
    print(f"Test3.  Part1: {a} Part 2: {b}")


if __name__ == "__main__":  # print()
    runAllTests()

    solutions = solve(input, 50)
    print("\nAOC")
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")
