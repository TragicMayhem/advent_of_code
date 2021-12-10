# https://adventofcode.com/2021/day/10

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test.txt'  # 
input = script_path / 'input.txt'  # 
 
file_in = input #_test


def parse(puzzle_input):
    """Parse input - each line of 10 number signals then 4-digit number
    """

    with open(puzzle_input, 'r') as file:
        data = file.read().split('\n')
        print(data)
    return data


def part1(data):
    """Solve part 1""" 

    # ( ) [] <>  {}
    SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
    open_seq = ['(','[','{','<']
    close_seq = [')',']','}','>']

    seq = []
    points = []
    print(len(data))

    for d in data:
        print("\n",d)
        
        found = True
        check = d
        while found:
            if '()' in check or '[]' in check or '{}' in check or '<>' in check:
                check = check.replace('()','').replace('[]','').replace('{}','').replace('<>','')
            else:
                found = False
        
        print("Check",check)

        #add all, then filter out and then sort in one statement?
        closing = dict()
        if check.find(')') > 0:
            closing[")"]=  check.find(')')
        if check.find(']') > 0:
            closing["]"] = check.find(']')
        if check.find('}') > 0:
            closing["}"] = check.find('}')
        if check.find('>') > 0:
            closing[">"] = check.find('>')

        print(closing)

        lowest = None
        error_char = ''
        for k, v in closing.items():
            print(k,v)
            if lowest == None or v < lowest:
                lowest = v
                error_char = k
        
        if error_char == ')': 
            points.append(3)
        elif error_char == ']':
            points.append(57)
        elif error_char == '}':
            points.append(1197)
        elif error_char == '>': 
            points.append(25137)
        print("answer",lowest, error_char,"points",points)

        
    print(points)   

    return sum(points)


def part2(data):
    """Solve part 2"""   
   
    print("PART 2")
     
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

if __name__ == "__main__":    # print()

    solutions = solve(file_in)
    print()
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")