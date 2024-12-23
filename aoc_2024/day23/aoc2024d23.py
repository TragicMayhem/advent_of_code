# https://adventofcode.com/2024/day/23

import pathlib
import time
from pprint import pprint as pp


script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 1344 /
test_file = script_path / "test.txt"  # 7 /


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


def find_computer_groups(connection_dict):
    """
    Finds groups of computers with at least three members and filters
    for groups containing at least one computer starting with 't'.

    Args:
      connection_dict: A dictionary where keys are computer names
                       and values are lists of connected computers.

    Returns:
      A list of groups of computers, where each group is a list
      of computer names.
    """
    groups = []
    for computer, connections in connection_dict.items():
        if len(connections) >= 2:  # At least two connections for a potential group
            group = set([computer] + connections)  # Create a set to avoid duplicates
            if len(group) >= 3 and any(c.startswith("t") for c in group):
                groups.append(list(group))  # Convert set back to list
    return groups


def find_computer_groups2(connection_dict):
    """
    Finds groups of computers with at least three members and filters
    for groups containing at least one computer starting with 't'.

    Args:
      connection_dict: A dictionary where keys are computer names
                       and values are lists of connected computers.

    Returns:
      A list of groups of computers, where each group is a list
      of computer names.
    """
    groups = set()  # Use a set to avoid duplicate groups

    for computer in connection_dict:
        # Get all connected computers, including the current computer
        group = set(connection_dict[computer] + [computer])

        # Add connections to the current computer from other computers
        for connected in connection_dict[computer]:
            group.update(connection_dict[connected])

        # Check if the group has at least three members
        if len(group) >= 3:
            groups.add(frozenset(group))  # Use frozenset for hashability

    # Filter groups where at least one computer starts with 't'
    filtered_groups = [
        list(group) for group in groups if any(c.startswith("t") for c in group)
    ]

    return filtered_groups


def find_computer_groups3(connection_dict):
    """
    Finds groups of three computers where each computer is directly connected to the other two.

    Args:
      connection_dict: A dictionary where keys are computer names
                       and values are lists of connected computers.

    Returns:
      A list of groups of computers, where each group is a list
      of computer names.
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


def part1(data):
    """Solve part 1"""

    conn_dict = build_connection_dict(data)
    print(conn_dict)

    grps = find_computer_groups3(conn_dict)
    pp(grps)
    print(len(grps))

    ans = filter_groups(grps)
    pp(ans)
    print(len(ans))

    return 1


def part2(data):
    """Solve part 2"""

    return 1


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
