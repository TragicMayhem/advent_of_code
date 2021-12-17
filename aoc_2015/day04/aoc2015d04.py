# https://adventofcode.com/2015/day/4

import time
import hashlib

# Takes AGES to run :D

input = 'yzbqklnj'  # 282749 / 9962624
input_test = 'abcdef'  # 609043 = 000001dbbfa...   / 6742839
input_test2 = 'pqrstuv'  #  1048970 = 000006136ef....  / 5714438

def part1(key):
    """Solve part 1""" 

    i = 0

    while True:
        current = key + str(i)
        current_hash = hashlib.md5(current.encode()).hexdigest()
        if current_hash.startswith('00000'):
            break
        i += 1

    # print(f"The solution is {i} MD5 of {current} is {current_hash}") 
    
    return i


def part2(key):
    """Solve part 2"""   
    i = 0

    while True:
        current = key + str(i)
        current_hash = hashlib.md5(current.encode()).hexdigest()
        if current_hash.startswith('000000'):
            break
        i += 1

    # print(f"The solution is {i} MD5 of {current} is {current_hash}") 
    return i
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]
    times.append(time.perf_counter())
    solution1 = part1(puzzle_input)
    times.append(time.perf_counter())
    solution2 = part2(puzzle_input)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runSingleTestData(data):
    test_solution1 = part1(data)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runSingleTestData(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')
    a, b  = runSingleTestData(input_test2)
    print(f'Test2.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")