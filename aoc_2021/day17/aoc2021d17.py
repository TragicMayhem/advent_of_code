# https://adventofcode.com/2021/day/x

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 

re_pattern = '.*x=(-?\d+)\.{2}(-?\d+), y=(-?\d+)\.{2}(-?\d+)'


def num_groups(regex):
    return re.compile(regex).groups


def parse(puzzle_input):
    """Parse input
       target area: x=20..30, y=-10..-5"""
    
    with open(puzzle_input, 'r') as file:
        line = file.readline()
        res = re.search(re_pattern,line)
        # print(len(res.groups()))

        if res:
            # x1, x2, y1, y2 = res.group(1,2,3,4)
            # print(x1,x2,y1,y2)
            target = [int(x) for x in res.groups()]
      
    return tuple(target)


# def inc_x(x_low, x_high):

#     diff = x_high - x_low
    
#     while x_low <= val <= x_high:            
#         for i in range(target, 0, -1):
#             val = val - 1
#             print(i, val)


def part1(data):
    """Solve part 1""" 
    
    (target_x1, target_x2, target_y1, target_y2) = data
    print(data)

    start = (0,0)

    '''
    loop steps
    each one 
        x = x + (x-1 if x>0 or x+1<0 towards 0)  << how many steps to get to zero?
        y = y + (y-1) because of gravity
    '''

    target_xsize = abs(target_x1 - target_x2)
    target_ysize = abs(target_y1 - target_y2)
    print(target_xsize, target_ysize)

    winning_results = []
    xcurr=0 
    ycurr=0
    if target_x1 <= xcurr <= target_x2:
        print("in x target")
    if target_y1 <= ycurr <= target_y2:  # careful of negative, might need to check this
        print("in y target")

    # inc_x(target_xsize)


    # how many steps to get x over to the target
    x_steps_to_target = 0
    val=0


    for i in range(0,target_xsize):
        pass
        # val = 1    
        # x_steps_to_target += i target_xsize 



    for x in range(0,target_xsize+1):
        # fine towards target and getting slower
        print(x)

        for y in range(0,target_ysize):  #not right for parabola
            print(x,y)  



    return 1


def part2(data):
    """Solve part 2"""   
   
    return 1
 

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


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runTest(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

    # solutions = solve(input)
    # print('\nAOC')
    # print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    # print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    # print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")