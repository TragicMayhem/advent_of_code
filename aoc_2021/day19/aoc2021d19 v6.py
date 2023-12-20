import pathlib
import numpy as np
import itertools as its


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 472 / 12092
test_file = script_path / "test.txt"  # 79 / 3621

#### Think the looping round scanners is not right.
#### changing code to reference the last one found (as per examples from others code )


def parse_np(puzzle):
    with open(puzzle, "r") as file:
        scanner_blocks = file.read().split("\n\n")
        scanners = []

        for scanner_data in scanner_blocks:
            # ignore first line, the scanner number is the index of the list.
            # Use numpy to get all the points in to list of arrays
            values = np.array(
                [
                    [int(i) for i in line.split(",")]
                    for line in scanner_data.splitlines()[1:]
                ]
            )
            scanners.append(values)

        # print(scanners)
    return scanners


def distFrom(start, end):
    x1, y1, z1 = start
    x2, y2, z2 = end
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def calc_distances(all_scanners):
    all_distances = []

    # going to take each scanners point data and workout the distances between its beacons
    for scanner in all_scanners:
        this_scanners_distances = []

        for point in scanner:
            # takes scanner which is array of data and works out difference to the current point
            # in the scanner against all others points. including itself (0 distance)
            this_scanners_distances.append(np.sum(np.abs(scanner - point), axis=1))
            # print(this_scanners_distances)
        all_distances.append(this_scanners_distances)

    return all_distances


def look_for_beacon_match(distances, source, target):
    """
    take in two np arrays and look for overlapping beacon distances
    need to run for each scanner combinations
    """
    # print("source",distances[source])
    # print("target",distances[target])

    for source_idx, sd in enumerate(distances[source]):
        # print("  sd", sd)
        for target_idx, td in enumerate(distances[target]):
            # print("    td", td)
            matching_beacons_distances = set(sd).intersection(
                set(td)
            )  # (Think) same as set(sd) & set(td)
            if len(matching_beacons_distances) >= 12:
                # print("<<<< Matching 12 points >>>>")
                # print(matching_beacons_distances)

                # need the id of the two loops in the main program so send back with matches
                return matching_beacons_distances, source_idx, target_idx

    return None


def workout_all_scanners(scanners, distances):
    # verts = [None]*1000
    scanner_coordinates = [None] * len(scanners)
    scanner_coordinates[0] = np.array(
        [0, 0, 0]
    )  # Assumes scanner 0 is at position 0,0,0

    list_with_matches = {0}
    tally = 1

    # Repeat for all scanners <<<< DOESNT WORK. Too high and multiple scanners at 0,0,0 :'(   why?
    # for outer_scanner_count in range(len(scanners)):

    # v4 updates after looking at others solutions
    # incorporating the logic improvements
    # the big difference to get the answer was a while loop
    # when you found a matching pattern (of 12) then add that to the list to pull from
    # that way you form a sequence from scanner 0 through all the scanners in the list
    # stop when you have processed all (tally = 5)

    while tally < len(scanners):
        outer_scanner_count = list_with_matches.pop()

        for inner_scanner_loop in range(len(scanners)):
            if outer_scanner_count == inner_scanner_loop:
                # print(inner_scanner_loop, "out = inner")
                continue

            if scanner_coordinates[inner_scanner_loop] is not None:
                # print("scanner coords is not none")
                # print(inner_scanner_loop, scanner_coordinates[inner_scanner_loop])
                continue

            # how to skip ones done?
            results = look_for_beacon_match(
                distances, outer_scanner_count, inner_scanner_loop
            )

            if not results:
                continue

            any_matches, s_idx, t_idx = results
            # print(len(any_matches),"pos:", s_idx, t_idx)
            # find positions, to then calculate unique using len of set
            # np.where
            # need to get the index of the matching beacon distances
            #   where will search for the postions in an array in numpy
            #   where the distance calculated matches the distance in the array
            # then need to work out the difference between the points to get distance to the scanner
            # That should value but orientation might be the sign is different.
            # Use to correctly orient them all and work out the positions

            for md in any_matches:
                # print("="*50)
                # print("match dist", md)
                if md == 0:
                    continue

                if md != 0:
                    # x,y are the locations of the coordinates that are the same distance
                    #     from the two scanners (outer and inner) [0][0] just returns the first
                    #     where returns e.g. (array([1], dtype=int64),)
                    #     pos1 and pos2 are the indexes of the scanners that they were found
                    # the differences will be an <class 'numpy.ndarray'> of x y z
                    # example
                    # x,y, 6, 13
                    # source_diff [-1125    78   319]
                    # target_diff [   78 -1125  -319]

                    x = np.where(distances[outer_scanner_count][s_idx] == md)[0][0]
                    y = np.where(distances[inner_scanner_loop][t_idx] == md)[0][0]
                    source_diff = (
                        scanners[outer_scanner_count][s_idx]
                        - scanners[outer_scanner_count][x]
                    )
                    target_diff = (
                        scanners[inner_scanner_loop][t_idx]
                        - scanners[inner_scanner_loop][y]
                    )

                    # print(x,y)
                    # print(type(source_diff))
                    # print("source diff", source_diff)
                    # print("target diff", target_diff)

                    # check they are matching values
                    # if np.absolute(source_diff) == np.absolute(target_diff):

                    # the distance matching provides coord but they are in different order
                    # so need to find index of each one to align and then re-orient
                    # print(np.absolute(target_diff))
                    # print(np.absolute(source_diff[0]))

                    if len(set(np.abs(source_diff))) < 3:
                        continue

                    seq = []
                    sign = []

                    try:
                        for value in source_diff:
                            find_coord_pos = np.where(
                                np.absolute(target_diff) == abs(value)
                            )[0][0]
                            seq.append(find_coord_pos)
                            sign.append(target_diff[find_coord_pos] // value)

                        adjust_scanner = scanners[inner_scanner_loop][
                            :, seq
                        ] * np.array(sign)
                        # print(seq, sign)
                        # print('scanners[inner_scanner_loop]\n',scanners[inner_scanner_loop])
                        # print('adjust_scanner\n',adjust_scanner)

                    except:
                        continue

                    # if the computations worked, then break out
                    break

            # So we know the matches we found ( the indexes found earlier s_idx and t_idx )
            # we have changed the orientation of the coordinates (adjust_scanner)
            # so if we take away, we get the delta and that leaves the position of the scanner.
            # then if we add the positions of the scanner to the adjusted scanner we get the new coordinates

            actual_scanner_coordinates = (
                scanners[outer_scanner_count][s_idx] - adjust_scanner[t_idx]
            )
            new_coords = adjust_scanner + actual_scanner_coordinates

            # print('scanners[outer_scanner_count][s_idx]',scanners[outer_scanner_count][s_idx])
            # print('adjust_scanner[t_idx]',adjust_scanner[t_idx])
            # print('scanner_coordinates',actual_scanner_coordinates)
            # print('new_coords\n',new_coords)

            scanner_coordinates[inner_scanner_loop] = actual_scanner_coordinates
            scanners[inner_scanner_loop] = new_coords

            tally += 1
            list_with_matches.add(inner_scanner_loop)

    return scanners, scanner_coordinates


def calculate_beacons(scanners):
    identified_beacons = set()

    for beacons in scanners:
        # np arrays so need to change them to list of coordinates (list comprehension)
        beacons = [tuple(pos) for pos in beacons]
        identified_beacons.update(
            beacons
        )  # Using sets will force only keeping unique. you Update with a new set of data

    return identified_beacons


###############################################

print("=" * 50)
scanners = parse_np(soln_file)
beacon_distances = calc_distances(scanners)
# print("Beacon distances")
# print(beacon_distances[0])
# print(beacon_distances)

# TODO Do I need to copy the lists because its passing references so all the same data/lists?
# print(scanners)

# Scanners is referenced so updates anyway, returning seems pointless!  so does sending as an argument
new_scanners, scanner_coords = workout_all_scanners(scanners, beacon_distances)
# print(scanners)
# print(len(new_scanners))
# print(new_scanners)
print("Scanner locations:\n", scanner_coords)

print("=" * 50)
beacons_coordinates = calculate_beacons(scanners)
# print(beacons_coordinates)
print("How many Beacons?", len(beacons_coordinates))
print("=" * 50)

largest_distance = 0

for p in its.permutations(scanner_coords, 2):
    # version 1
    x = abs(p[0][0] - p[1][0])
    y = abs(p[0][1] - p[1][1])
    z = abs(p[0][2] - p[1][2])
    total = x + y + z
    largest_distance = total if total > largest_distance else largest_distance
print("v1", largest_distance)

for p in its.permutations(scanner_coords, 2):
    # version 2 after realising they are np arrays
    # print(p)
    # print(p[0]-p[1])
    # print(abs(p[0]-p[1]))
    # print(sum(abs(p[0]-p[1])))
    largest_distance = max(largest_distance, sum(abs(p[0] - p[1])))

print("v2", largest_distance)


# def find_one_overlap(scan0, scan1):
#     for i, d0 in enumerate(beacon_distances[scan0]):
#         print("d0",d0)
#         for j, d1 in enumerate(beacon_distances[scan1]):
#             print(i,j,"d1",d1)
#             overlaps = set(d0) & set(d1)
#             print("overlaps", overlaps)
#             if len(overlaps) >= 12:
#                 print("++++++++++++++++")
#                 return i, j, overlaps

# print()
# print(find_one_overlap(0,0))
# print(find_one_overlap(0,1))
# print(find_one_overlap(0,2))
# print(find_one_overlap(0,3))
# print(find_one_overlap(0,4))
# print(find_one_overlap(1,0))


# for line in lines:
# 	if not line:
# 		continue
# 	if line.startswith('---'):
# 		scanners.append([])
# 		continue

# 	scanners[-1].append(tuple(map(int, line.split(','))))

# scanners = list(map(set, scanners))
