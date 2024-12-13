# https://adventofcode.com/2024/day/13

import pathlib
import time
import re
import itertools
from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, lpSum
# from z3 import Solver, Int
# import z3



script_path = pathlib.Path(__file__).parent
soln_file = script_path / "input.txt"  # 39290 / 
test_file = script_path / "test.txt"  # 480 (2 machines) / 

# 1: 19332 too low - using the 100 button press limit :'(


def parse(puzzle_input):
    """Parse input"""

    def parse_coordinates(line):
        _, coords = line.split(': ')
        x, y = coords.split(', ')

        # Use regular expression to extract numbers, handling both "+" and "=" formats
        x = int(re.search(r'\d+', x).group())
        y = int(re.search(r'\d+', y).group())

        return (x, y)

    with open(puzzle_input, "r", encoding="UTF-8") as file:
        #  Read each line (split \n) and form a list of strings
        lst = file.read().split("\n\n")

    machines = []

    for l in lst:
        tmp = l.split("\n")

        instruction = {}
        instruction['A'] = parse_coordinates(tmp[0])
        instruction['B'] = parse_coordinates(tmp[1])
        instruction['PRIZE'] = parse_coordinates(tmp[2])

        machines.append(instruction)

    # print(machines)

    return machines


def calculate_combinations(button_a, button_b, prize):
    """Calculates the combinations of pressing buttons A and B to reach the prize.

    Args:
        button_a: A tuple (x, y) representing the movement of button A.
        button_b: A tuple (x, y) representing the movement of button B.
        prize: A tuple (x, y) representing the target coordinates.

    Returns:
        A list of tuples (a, b), where a is the number of times to press button A and b is the number of times to press button B.
    """

    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize

    # Find the maximum number of times each button can be pressed without overshooting the target
    max_a = min(p_x // a_x, p_y // a_y)
    max_b = min(p_x // b_x, p_y // b_y)

    # NO, it says you estimate this, and if you comment this out you get the right answer
    # Games has to be less than 100 presses
    # if max_a > 100 or max_b > 100:
    #     return None

    # Generate all possible combinations of button presses within these limits
    combinations = []

    for a, b in itertools.product(range(max_a + 1), range(max_b + 1)):
        if a * a_x + b * b_x == p_x and a * a_y + b * b_y == p_y:
            combinations.append((a, b))

    # Find the combination with the lowest total number of button presses

    if combinations == []:
        return None

    min_presses = min(combinations, key=lambda x: sum(x))

    # its not x and y its BUTTONS a, b
    costs = [(3 * cmb[0] + cmb[1], cmb) for cmb in combinations]
    costs.sort()

    if len(combinations) > 1:
        print("*"*10)
        print(combinations)
        print(min_presses)
        print(costs)


    return costs


def part1(machines):
    """Solve part 1"""

    total = 0

    for i, m in enumerate(machines):
        print("Machine:", i)
        print(m)

        ans = calculate_combinations(m['A'], m['B'], m['PRIZE'])
        print(ans)

        if ans is None:
            continue

        total += ans[0][0]


    return total


def solve_button_presses(button_a, button_b, prize):
    # Create the LP problem
    prob = LpProblem("ButtonPressProblem", LpMaximize)

    # Create the decision variables
    a = LpVariable("a", lowBound=0, upBound=100, cat='Integer')
    b = LpVariable("b", lowBound=0, upBound=100, cat='Integer')

    # Objective function: Minimize total button presses
    prob += a + b

    # Constraints:
    prob += a * button_a[0] + b * button_b[0] == prize[0]
    prob += a * button_a[1] + b * button_b[1] == prize[1]

    # Solve the problem
    prob.solve()

    if LpStatus[prob.status] == 'Optimal':
        return int(a.varValue), int(b.varValue)
    else:
        return None


def min_button_presses(target_x, target_y, a_x, a_y, b_x, b_y):
    print("start")
    dp = [[float('inf')] * (target_x + 1) for _ in range(target_y + 1)]
    dp[0][0] = 0
    print("here")
    for i in range(target_x + 1):
        for j in range(target_y + 1):
            print(i,j)
            if i - a_x >= 0 and j - a_y >= 0:
                dp[i][j] = min(dp[i][j], dp[i - a_x][j - a_y] + 1)
            if i - b_x >= 0 and j - b_y >= 0:
                dp[i][j] = min(dp[i][j], dp[i - b_x][j - b_y] + 1)

    return dp[target_x][target_y]


def min_button_presses2(target_x, target_y, a_x, a_y, b_x, b_y):
    queue = [(0, 0, 0, 0)]  # (x, y, steps, a_presses, b_presses)
    visited = set()

    while queue:
        x, y, steps, a_presses, b_presses = queue.pop(0)

        if (x, y) == (target_x, target_y):
            return steps, a_presses, b_presses

        if (x, y) not in visited:
            visited.add((x, y))
            queue.append((x + a_x, y + a_y, steps + 1, a_presses + 1, b_presses))
            queue.append((x + b_x, y + b_y, steps + 1, a_presses, b_presses + 1))

    return -1, -1, -1  # If the target is unreachable

# cant get z3 to work on mac
# def solve_with_z3(target_x, target_y, a_x, a_y, b_x, b_y):
#     s = z3.Solver()


#     # Define variables
#     a = Int('a')
#     b = Int('b')

#     # Define constraints
#     s.add(a * a_x + b * b_x == target_x)
#     s.add(a * a_y + b * b_y == target_y)
#     s.add(a >= 0)
#     s.add(b >= 0)

#     # Optionally, add a constraint on the total number of presses:
#     # s.add(a + b <= 100)

#     if s.check() == z3.sat:
#         m = s.model()
#         return m[a].as_long(), m[b].as_long()
#     else:
#         return None  # No solution found


def part2(machines):
    """Solve part 2"""

    # adj = 10000000000000
    # total = 0

    # for i, m in enumerate(machines):
    #     print("Machine:", i)

    #     old_x, old_y = m['PRIZE']
    #     m['PRIZE'] = (old_x+adj, old_y+adj)
    #     print(m)

    #     ans = calculate_combinations(m['A'], m['B'], m['PRIZE'])
    #     print(ans)

    #     if ans is None:
    #         continue

    #     total += ans[0][0]

    sample = {
        'A': (94,34),
        'B': (22,67),
        'PRIZE': (100000008400,100000005400)}

    # print("variation 1 - pulp - infeasible")
    # solve_button_presses(sample['A'],sample['B'],sample['PRIZE'])

    # print("variation 2 - grid - fails")
    # ans = min_button_presses(sample['PRIZE'][0],sample['PRIZE'][1],
    #                          sample['A'][0],
    #                          sample['A'][1],
    #                          sample['B'][0],
    #                          sample['B'][1])
    # print(ans)

    # ans = solve_with_z3(sample['PRIZE'][0],sample['PRIZE'][1],
    #                          sample['A'][0],
    #                          sample['A'][1],
    #                          sample['B'][0],
    #                          sample['B'][1])
    # print(ans)

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
    # solutions = solve(soln_file)
