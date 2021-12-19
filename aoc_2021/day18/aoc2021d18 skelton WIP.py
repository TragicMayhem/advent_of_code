# https://adventofcode.com/2021/day/x

from os import close
import pathlib
import time
import ast
import re
import math

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 
input_test2 = script_path / 'test2.txt'  # 

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
    
def parse_keepstr(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        lines = file.read().split('\n')

    return lines

# Always let most pair for the next action  
# file is add first two together, that answer is added to row 3, then row 4 and so on!!


def check_for_split(input):

    count_depth = 0

    for i in range(len(input)):
        
        if input[i] == '[':
            count_depth += 1
        elif input[i] == ']':
            count_depth -=1

        if count_depth > 4:
            return i  # return the position of the depth 4 pair

    return 0  # return start of string because nothing depth of 4


def count_big_numbers(l):
    if isinstance(l, list):
        return 0 + sum(count_big_numbers(item) for item in l)
    else:
        if l > 10:
            return 1
        else:
            return 0


def explode(number):
    '''
    If embedded in four pairs need to explode
        left number is added to the number to left
        right number is added to the number to the right
        then replace the pair with zero
    '''
    ln = math.floor(number / 2)
    rn = math.ceil(number / 2)
    return [ln,rn]


def split():
    '''
    if greater than 10, then
        left div 2 round down
        right div 2 round up
    '''

    pass


def calculate_magnitude():
    pass


def workrecursive(items, depth):
    # count depth
    # look behind number 
    # look ahead? how?
    
    depth += 1
    l = [1,2]
    # list, depth
    # loop and do next action, break and repeat

    # if list next item [0] then call recurve with next list
    if isinstance(l[0], list):
        change = workrecursive(l[0],depth)

        pass

    # if list next item [1] then call recurve with next list
    if isinstance(l[1], list):
        change = workrecursive(l[1],depth)
        l[1] = change
        pass

    # pass depth count in

    # here need to decide whats first split or explode/.... now

    # if the depth is > 4 need to split
        # need to pass back number to add to the level above
        # need to add number right to the next number in levels above

    # what to return to the calling function, to updates

    # if n > 10:
    #     # explode
    #     n gets replaced with a list

    # # how to check actions? do each pass through recursive

    # if split:
    #     pass



    # new_snaillist = []

    return list

# vowels_check = len(re.findall(r"([aeiou])", current_string)) >= 3
pattern_check2d = re.compile(r'\d{2}')

depth = lambda L: isinstance(L, list) and max(map(depth, L))+1

# def flat(l):
#     depths = []
#     for item in l:
#         if isinstance(item, list):
#             depths.append(flat(item))
#     if len(depths) > 0:
#         return 1 + max(depths)
#     return 1


def part1(data):
    """Solve part 1""" 
    # need to loop round all data
    # add 0 and 1 in to a new list and then work on that recursively
    # then take that answer, and add to the next data (recursively)
    # at end of file then calculate the magnitude

    latest_reduced = [data[0]]
    # for i, d in enumerate(data):
    for i in range(1,len(data)):
        print("\n",i, data[i])
        latest_reduced.append(data[i])
        print(latest_reduced)
        
        depth_count = depth(latest_reduced)

        if depth_count > 4:
            print("Need to explode")



        # new = '[' + latest_reduced + ',' + data[i] + ']'
        # print(new)

        # check explode ppos
        # check split pos
        # whatever is less do first.
        # return string
        # check again until none left.
        # set the string and repeat

        # reduced_calc = ''
        # print(check_explode(new))



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

    parse2(input_test)

    runAllTests()

    # solutions = solve(input)
    # print('\nAOC')
    # print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    # print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    # print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")