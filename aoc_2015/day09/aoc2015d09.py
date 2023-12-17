# https://adventofcode.com/2015/day/9

import pathlib
import time
import itertools

script_path = pathlib.Path(__file__).parent
input = script_path / "input.txt"  # Part 1 = 141 (Shortest)   Part 2 = 736 (Longest)
input_test = script_path / "test.txt"  # London -> Dublin -> Belfast = 605 / 982


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times = []
    routes = dict()

    with open(puzzle_input, "r") as file:
        lst = file.read().split("\n")
        lst = [x.replace("to ", "").replace("= ", "").split(" ") for x in lst]

    for l in lst:
        if l[0] not in routes.keys():
            routes[l[0]] = dict()
        if l[1] not in routes.keys():
            routes[l[1]] = dict()
        routes[l[0]][l[1]] = int(l[2])
        routes[l[1]][l[0]] = int(l[2])

    times.append(time.perf_counter())

    destinations = set(routes.keys())  # Unique set of destinations
    possible_routes = list(
        itertools.permutations(destinations)
    )  # All the permutations of the destinations/. List tuples

    distances = list()

    for route in possible_routes:
        # print("\n", route)
        running_total = 0
        i = 0
        while (
            i < len(route) - 1
        ):  # Loop until the second to last element (thats the destination)
            # print(i, route[i], routes[route[i]], routes[route[i]][route[i+1]])
            running_total += routes[route[i]][route[i + 1]]
            i += 1

        distances.append(running_total)

    print("\nShortest route:", min(distances))
    print("Longest route:", max(distances))

    times.append(time.perf_counter())

    print(f"\nExecution total: {times[1]-times[0]:.4f} seconds")


if __name__ == "__main__":  # print()
    solve(input_test)
    solve(input)
