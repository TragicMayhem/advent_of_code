# https://adventofcode.com/2021/day/x

import pathlib
import time
import ast

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 
input_test = script_path / 'test.txt'  # 

'''
list = [[reduce(lambda x, y: x*y, l)] for l in lis]

or 
list = []

for l in lis:
    # do stuff here
    list.append(reduce(lambda x, y: x*y, l))

print(list)
'''

def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        lines = file.read().split('\n')
        data = []
        for d in lines:
            tmp = ast.literal_eval(d)
            print(tmp)
            data.append(tmp)

        print()
        print(data)

    return data

# Always let most pair for the next action  
# file is add first two together, that answer is added to row 3, then row 4 and so on!!

def explode():
    '''
    If embedded in four pairs need to explode
        left number is added to the number to left
        right number is added to the number to the right
        then replace the pair with zero
    '''

    # returns a list of the new pair

    pass


def split():
    '''
    if greater than 10, then
        left div 2 round down
        right div 2 round up
    '''

    pass


def calculate_magnitude():
    pass

# can leave as string and do with regex?

# 


def workrecursive(snailsum):
    # count depth
    # look behind number 
    # look ahead? how?

    # loop and do next action, break and repeat


    # if depth count > 4:
    #     split
    # count [ if gets to 5 then need to split

    # if n > 10:
    #     # explode
    #     n gets replaced with a list

    # # how to check actions? do each pass through recursive

    # if split:
    #     pass



    # new_snaillist = []

    return list



def part1(data):
    """Solve part 1""" 
    # need to loop round all data
    # add 0 and 1 in to a new list and then work on that recursively
    # then take that answer, and add to the next data (recursively)
    # at end of file then calculate the magnitude

    for i, d in enumerate (data):
        print(i,d)
                  
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