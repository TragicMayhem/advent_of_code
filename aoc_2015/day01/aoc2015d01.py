# https://adventofcode.com/2015/day/1

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 74 / 1795
input_test = script_path / 'test1.txt'  # 3 / 7
input_test2 = script_path / 'test2.txt'  # -1 / 5


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.read()
    return data


def part1(data):
    """Solve part 1""" 
    up = data.count('(')
    down = data.count(')')
    # print(f'Up= { up } Down= { down } Final floor = { up-down } \n')             
    return up-down


def part2(data):
    """Solve part 2"""   
    for x in range(len(data)):
        # Use string slicing to take string upto and including current position
        instructions_sofar = data[:x+1]  
        
        up_sofar = instructions_sofar.count('(')
        down_sofar = instructions_sofar.count(')')

        # If more down than up then moving to the basement, so report and stop
        if down_sofar > up_sofar:
            # print(f'\nPos x+1: {x + 1} Up  = { up_sofar } Down = { down_sofar } (Difference should be -1: {up_sofar-down_sofar }) \n')
            break

    return x + 1
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
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