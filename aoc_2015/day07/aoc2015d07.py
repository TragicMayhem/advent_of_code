# https://adventofcode.com/2015/day/7

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'           # 46065  / a = 46065 > b and run again. a = 14134
input_test = script_path / 'test.txt'       # a = 930

# input_test = script_path / 'test_data.txt'       # d: 72 e: 507 f: 492 g: 114 h: 65412 i: 65079 x: 123 y: 456

# Input pattern  
#    {change} -> {target wire}
# {change} can be 
#   {Number}                # 123 -> x
#   {wire/#} AND {wire/#}   # x AND y -> d      a & b
#   {wire/#} OR {wire/#}    # x OR y -> e       a | b
#   {wire} LSHIFT {Number}  # x LSHIFT 2 -> f   a << 2
#   {wire} RSHIFT {Number}  # y RSHIFT 2 -> g   a >> 2
#   NOT {wire}              # NOT y -> i        ~a

instructions = dict()


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        data = [x.replace('->', '').split() for x in data]  # Split on 'x' in each string ('1x2x3')

        for l in data:
            instructions[l[-1]] = l[:-1]  # key is the last list item, value is the rest of the list      



def convert_int(val):
  '''
    Check if can convert str to int, if not return the str (ref to another wire)
  '''
  try: 
    return int(val)
  except: 
    return val 


def complete_wire(name, wires = None):
    '''
    Take the name of wire and recursively workout the set value.
    '''
    # print("\n-----\nname:", name)
    if wires == None: wires = dict()
    if name in wires.keys(): return wires.get(name)
    
    values = instructions[name]

    if len(values) == 1:  # SET
        # print("<1>", values)
        tmp = convert_int(values[0])
        wires[name] = tmp if isinstance(tmp, int) else complete_wire(tmp, wires)
        
    elif len(values) == 2:  # NOT
        # print("<2>", values)
        tmp = convert_int(values[1])
        wires[name] = ~ tmp & 0xFFFF if isinstance(tmp, int) else ~ complete_wire(tmp, wires) & 0xFFFF

    elif len(values) == 3:  # AND, OR, LSHIFT, RSHIFT
        # print("<3>", values)
        left_op = convert_int(values[0])
        right_op = convert_int(values[2]) 

        if not isinstance(left_op, int):
            left_op = complete_wire(left_op, wires)

        if not isinstance(right_op, int):
            right_op = complete_wire(right_op, wires)
        
        if isinstance(left_op, int) and isinstance(right_op, int):
            if "AND" in values: wires[name] = left_op & right_op
            if "OR" in values: wires[name] = left_op | right_op
            if "LSHIFT" in values: wires[name] = left_op << right_op
            if "RSHIFT" in values: wires[name] = left_op >> right_op
    
    # print("END:", wires)

    return wires[name]


def part1():
    """Solve part 1""" 
   
    answer = complete_wire('a')
    # print(f'\nValue on "a" = ', answer)

    return answer


def part2():
    """Solve part 2"""   

    instructions['b'] = ['46065']
    answer = complete_wire('a')
    # print(f'\nValue on "a" = ', answer)

    return answer
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1()
    times.append(time.perf_counter())
    solution2 = part2()
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runSingleTestData(test_file):
    data = parse(test_file)
    test_solution1 = part1()
    test_solution2 = part2()
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runSingleTestData(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")