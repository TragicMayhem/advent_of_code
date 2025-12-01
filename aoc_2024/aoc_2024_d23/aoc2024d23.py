# https://adventofcode.com/2024/day/23

import pathlib
import time
from itertools import combinations
from collections import defaultdict
import networkx as nx
from pprint import pprint as pp


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 1344 / ab,al,cq,cr,da,db,dr,fw,ly,mn,od,py,uh
test_file = script_path / "test.txt"  # 7 / co,de,ka,ta

# not ab,cr,dr,py,uh
# not kp,ld,lj,tp,vd
# not aw,fb,gr,tj,yd

# Had to research modules, networkX to build graphs (need to read up more on this)


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        connections = [tuple(line.strip().split("-")) for line in file]
    return connections


def build_connection_dict(connections):
    """
    Builds a dictionary of connections from a list of tuples.
    """
    connection_dict = {}
    for source, target in connections:
        if source not in connection_dict:
            connection_dict[source] = []
        connection_dict[source].append(target)

        if target not in connection_dict:
            connection_dict[target] = []
        connection_dict[target].append(source)
    return connection_dict


def find_computer_groups3(connection_dict):
    """
    Finds groups of three computers where each computer is directly connected to the other two.
    """
    groups = []
    for computer1, connections1 in connection_dict.items():
        for computer2 in connections1:
            for computer3 in connections1:
                if computer2 != computer3 and computer3 in connection_dict[computer2]:
                    group = sorted(
                        [computer1, computer2, computer3]
                    )  # Ensure consistent group order
                    if group not in groups:
                        groups.append(group)
    return groups


def filter_groups(groups, lett="t"):
    """
    Filters a list of computer groups to include only those
    where at least one computer starts with the letter default = 't'.
    """
    filtered_groups = []
    for group in groups:
        if any(computer.startswith(lett) for computer in group):
            filtered_groups.append(group)
    return filtered_groups


# works for the test data!
def find_largest_combined_group(groups, connection_dict):
    """
    Finds the largest group of computers where each computer in the group is
    directly connected to all other computers in the group.
    """
    largest_group = []

    pp(groups)
    for group1 in groups:
        for group2 in groups:
            if group1 != group2 and set(group1).intersection(set(group2)):
                combined_group = list(set(group1) | set(group2))
                pp(combined_group)
                if is_fully_connected(combined_group, connection_dict):
                    if len(combined_group) > len(largest_group):
                        largest_group = combined_group

    return largest_group


def is_fully_connected(group, connection_dict):
    """
    Checks if all computers in the group are directly connected to each other.
    True if all computers in the group are fully connected, False otherwise.
    """
    for computer1 in group:
        for computer2 in group:
            if computer1 != computer2 and computer2 not in connection_dict[computer1]:
                return False
    return True


# works for the test data!
def find_largest_combined_groups(groups, connection_dict):
    """
    Finds all possible combined groups and returns the largest one.

    Args:
      groups: A list of groups of three computers, where each group is a list
              of computer names.
      connection_dict: A dictionary where keys are computer names
                       and values are sets of connected computers.

    Returns:
      A list representing the largest combined group of computers,
      or an empty list if no such group exists.
    """
    all_combined_groups = set()

    # pp(groups)
    for group1 in groups:
        for group2 in groups:
            if group1 != group2 and set(group1).intersection(set(group2)):
                combined_group = tuple(
                    sorted(set(group1) | set(group2))
                )  # Convert to tuple for set membership
                if is_fully_connected(combined_group, connection_dict) and any(
                    computer.startswith("t") for computer in combined_group
                ):
                    all_combined_groups.add(combined_group)

    pp(all_combined_groups)

    if all_combined_groups:
        largest_group = max(all_combined_groups, key=len)
        return list(largest_group)

    return []


# def find_largest_combined_groups2(groups, connection_dict):
#     """
#     Finds all possible combined groups and returns the largest one.
#     """
#     # all_combined_groups = set()

#     # # pp(groups)
#     # for group1 in groups:
#     #     for group2 in groups:
#     #         if group1 != group2 and set(group1).intersection(set(group2)):
#     #             combined_group = tuple(
#     #                 sorted(set(group1) | set(group2))
#     #             )  # Convert to tuple for set membership
#     #             if is_fully_connected(combined_group, connection_dict):
#     #                 all_combined_groups.add(combined_group)

#     # pp(all_combined_groups)

#     # if all_combined_groups:
#     #     largest_group = max(all_combined_groups, key=len)
#     #     return list(largest_group)
#     # else:
#     #     return []

#     # largest_group = []
#     # for group1 in groups:
#     #     potential_groups = [group1]
#     #     for group2 in groups:
#     #         if group1 != group2 and set(group1).intersection(set(group2)):
#     #             potential_group = list(set(group1) | set(group2))
#     #             if is_fully_connected(potential_group, connection_dict):
#     #                 potential_groups.append(potential_group)
#     #     if potential_groups and len(max(potential_groups, key=len)) > len(
#     #         largest_group
#     #     ):
#     #         largest_group = max(potential_groups, key=len)

#     return largest_group


def part1(data):
    """Solve part 1"""

    conn_dict = build_connection_dict(data)
    grps = find_computer_groups3(conn_dict)
    ans = filter_groups(grps)

    return len(ans)


def part2(data):
    """Solve part 2"""

    # conn_dict = build_connection_dict(data)
    # all_groups = find_computer_groups3(conn_dict)
    # print(len(all_groups))
    # all_groups = filter_groups(all_groups)
    # print(len(all_groups))

    # largest_group = find_largest_combined_groups2(all_groups, conn_dict)
    # print("Largest Combined Group:", largest_group)
    # pwd = sorted(largest_group)

    conn_G = nx.Graph()
    conn_G.add_edges_from(data)

    cliques_list = list(nx.find_cliques(conn_G))
    # print(list(nx.find_cliques(conn_G)))
    print(len(cliques_list))

    largest_group = max(cliques_list, key=len)
    print(largest_group)
    pwd = sorted(largest_group)
    return ",".join(pwd)


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
