# https://adventofcode.com/2015/day/24

import pathlib
import time
import itertools
from pprint import pprint
import math

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'       #  11266889531 / 77387711
input_test = script_path / 'test.txt'   #  Num parcels 10 with total weight of 60 Group target weight is 20.0  > 99 

# NOTE
# Quick only calcs group 1! Not ALL. That was taking FOREVER (AND EVER)

# PART1 with 3 groups = Num parcels 28 with total weight of 1548 Group target weight is 516.0  > 11266889531  
# PART2 with 4 groups = Num parcels 28 with total weight of 1548 Group target weight is 387.0  > 77387711 


def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        data = [int(d) for d in data]
        data.sort(reverse=True)
    return data


def calc_weight_groups(weight_list, num_of_groups):
    ''' Second attempt
        Calculates group combination for the first group ONLY.
        If it matches the target, then assumes the other groups can be calculated too (maybe bad!) but runs now
    '''
    num_parcels = len(weight_list)
    total_weight = sum(weight_list)
    target_weight = total_weight / num_of_groups
    
    print("\nParcels:", weight_list)
    print('-'*50)
    print(f"Solving for {len(weight_list)} parcel weights and {num_of_groups} groups and target of {target_weight}")

    ans = []
    # The limiter is set here to allow the test file to be processed!  If not then the loops dont run and its empty, and if 
    # change to allow every single combincation then it runs to 60s for each part.  (with this it runs iun  0.8s)
    limiter = num_parcels if num_parcels < 15 else num_parcels // num_of_groups

    for g1_size in range(1, limiter):
        print("Working....", g1_size)

        for c1 in itertools.combinations(weight_list, g1_size):
            if sum(c1) == target_weight:  # Group 1 target weight met
                ans.append(c1)
   
    '''
    Take in list of answers for combinations for group 1
    '''

    print('-'*50)
    print('Processing for the answer....')
    print("Number of combinations for group 1:", len(ans), "the first few shown below:")  
    pprint(ans[:6])
    
    min_group_count = min([len(a) for a in ans])
    print("\nSmallest number of parcels in Group 1 = ", min_group_count)

    smallest_g1_combinations = [a for a in ans if len(a) == min_group_count]
    smallest_g1_combinations.sort()
    
    print("Number of combinations with smallest size:",len(smallest_g1_combinations), "the first few shown below:")
    pprint(smallest_g1_combinations[:6])

    qe = [math.prod(a) for a in smallest_g1_combinations]
    qe.sort()

    print("\nThe first few quantum entanglements with smallest number of parcels:")
    pprint(qe[:5])
    print("\nThe lowest qe:", qe[0])

    return qe[0]        
    return res
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    times.append(time.perf_counter())

    solution1 = calc_weight_groups(data[:], 3)
    times.append(time.perf_counter())

    solution2 = calc_weight_groups(data[:], 4)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runAllTests():

    print("\nTests\n")
    a, b, t  = solve(input_test)
    print(f'Test1 Part 1: {a} in {t[1]-t[0]:.4f}s')
    print(f'      Part 2: {b} in {t[2]-t[1]:.4f}s')
    print(f"      Execution total: {t[-1]-t[0]:.4f} seconds")


if __name__ == "__main__":    # print()

    runAllTests()

    sol1, sol2, times = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(sol1)} in {times[1]-times[0]:.4f}s")
    print(f"Solution 2: {str(sol2)} in {times[2]-times[1]:.4f}s")
    print(f"\nExecution total: {times[-1]-times[0]:.4f} seconds")