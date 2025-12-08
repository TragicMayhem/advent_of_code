# # https://adventofcode.com/2025/day/8 🏆

import pathlib
import time
from typing import Callable, List, Union, Any
import math


# ----------------------------------

# --- Configuration ---
CURRENT_AOC_YEAR = 2025
# 📌 SET THE DAY NUMBER HERE
DAY_NUMBER = 8
# ---------------------

# Format the day number to a two-digit string (e.g., 1 -> "01")
DAY_FOLDER_NAME = f"d{DAY_NUMBER:02d}"

# --- Path Finding Logic ---

# Find the project root relative to the script location. This assumes
# the script is executed from the AOC year folder or a sibling folder.
script_path = pathlib.Path(__file__).parent
data_root = script_path / "data"
data_day_path = data_root / DAY_FOLDER_NAME

# Construct the final file paths
soln_file = data_day_path / "input.txt"  # 153328 /
test_file = data_day_path / "test.txt"  # 40 / 25272


# --- Parsing Functions ---
def parse_lines(puzzle_input: pathlib.Path) -> List[str]:
    """
    Parse input line-by-line.
    Returns a list where each element is one line (string) from the input file,
    stripped of surrounding whitespace (including the newline character).
    """
    content = puzzle_input.read_text(encoding="UTF-8")
    # Splits by newline, strips whitespace from each line, and filters out empty lines.
    lst = [line.strip() for line in content.splitlines() if line.strip()]

    points = [
        (float(x), float(y), float(z))
        for point_str in lst
        for x, y, z in [point_str.split(",")]
    ]
    return points


# --- Custom Helper Functions ---
# Utility functions for common AOC tasks.
def distance_3d(p1, p2):
    """Calculates the Euclidean distance between two 3D points."""
    return math.dist(p1, p2)


def build_distance_list(points):
    """Builds a list of distances between all pairs of 3D points."""
    dist_list = []
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            dist = distance_3d(points[i], points[j])
            dist_list.append((dist, (points[i], points[j])))

    return dist_list


def build_network_graph(points):
    """Builds a graph representation of the points and their distances."""
    graph = {p: [] for p in points}
    distances = build_distance_list(points)

    for dist, (p1, p2) in distances:
        graph[p1].append((p2, dist))
        graph[p2].append((p1, dist))

    return graph


def build_full_network(points):

    # Initialize each point as its own network
    networks = [{p} for p in points]

    distances = build_distance_list(points)
    distances.sort(key=lambda x: x[0])

    # The final list of connections that form the MST
    mst_edges = []

    for dist, (p1, p2) in distances:
        # Find the indices of the networks (sets) that p1 and p2 belong to
        net_idx_1 = -1
        net_idx_2 = -1

        for i, network in enumerate(networks):
            if p1 in network:
                net_idx_1 = i
            if p2 in network:
                net_idx_2 = i

        # Check if the points are already in the SAME network
        if net_idx_1 != net_idx_2:
            mst_edges.append((dist, p1, p2))

            lower_idx = min(net_idx_1, net_idx_2)
            higher_idx = max(net_idx_1, net_idx_2)

            # Merge the two networks (sets)
            networks[lower_idx].update(networks[higher_idx])

            # Remove the now-merged network 2 from the list
            networks.pop(higher_idx)

            # Stop if the entire network is connected (only one set remains)
            if len(networks) == 1:
                print("All points connected into a single network.")
                print(p1, p2, dist)

                break

    x1, _, _ = p1
    x2, _, _ = p2

    return networks, x1 * x2


# --- Solving Functions ---


# My version, there is another to look at that doesnt use indexing
def part1(points: List[Union[str, list]], max_connections=1000):
    """Solve part 1"""

    # Initialize each point as its own network
    networks = [{p} for p in points]

    distances = build_distance_list(points)
    distances.sort(key=lambda x: x[0])

    # for d in distances[:max_connections]:
    #     print(d)

    # The final list of connections that form the MST
    mst_edges = []

    for dist, (p1, p2) in distances[:max_connections]:
        # Find the indices of the networks (sets) that p1 and p2 belong to
        net_idx_1 = -1
        net_idx_2 = -1

        for i, network in enumerate(networks):
            if p1 in network:
                net_idx_1 = i
            if p2 in network:
                net_idx_2 = i

        # Check if the points are already in the SAME network
        if net_idx_1 != net_idx_2:
            mst_edges.append((dist, p1, p2))

            lower_idx = min(net_idx_1, net_idx_2)
            higher_idx = max(net_idx_1, net_idx_2)

            # Merge the two networks (sets)
            networks[lower_idx].update(networks[higher_idx])

            # Remove the now-merged network 2 from the list
            networks.pop(higher_idx)

            # Stop if the entire network is connected (only one set remains)
            if len(networks) == 1:
                break

    print(p1, p2, dist)
    # for network in networks:
    #     print(network)
    # print("-" * 20)

    networks.sort(key=len, reverse=True)
    total = 1
    for network in networks[:3]:
        total *= len(network)

    return total


def part2(points: List[Union[str, list]]):
    """Solve part 2"""

    network, val = build_full_network(points)

    if len(network) != 1:
        print("Warning: Network is not fully connected!")
        return -1

    return val


def solve(
    puzzle_input: pathlib.Path,
    parse_func: Callable,
    run="Solution",
    max_connections=1000,
):
    """Solve the puzzle for the given input, using the specified parser"""
    times = []

    if not puzzle_input.exists():
        print(
            f"Error: Input file not found at **{puzzle_input.resolve()}**. Skipping {run}."
        )
        return None, None, [0, 0, 0]

    # Use the selected parser function to transform the file path into processed data
    data = parse_func(puzzle_input)

    times.append(time.perf_counter())
    solution1 = part1(data, max_connections=max_connections)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())

    print(f"{run} 1: {str(solution1)} in {times[1]-times[0]:.4f}s")
    print(f"{run} 2: {str(solution2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")

    return solution1, solution2, times


if __name__ == "__main__":
    print(f"\n🎄 Advent of Code {CURRENT_AOC_YEAR} Day {DAY_NUMBER} 🎄")

    # 📌 SELECT THE DAY-SPECIFIC PARSER
    # By default, this points to the generic 'parse' function above.
    # If you define a new custom parser (e.g., 'parse_grid'), change it here.
    SELECTED_PARSER = parse_lines
    # SELECTED_PARSER = parse_blocks

    print(f"Loading data from folder: **{DAY_FOLDER_NAME}**")
    print(f"Using parser: **{SELECTED_PARSER.__name__}**\n")

    # Run tests first
    tests = solve(test_file, parse_func=SELECTED_PARSER, run="Test", max_connections=10)

    print("---")
    # Run the actual solution
    solutions = solve(soln_file, parse_func=SELECTED_PARSER)
