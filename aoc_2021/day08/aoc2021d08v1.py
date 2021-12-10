# https://adventofcode.com/2021/day/8

import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # Answers: 245 / 983026
input_test = script_path / 'test.txt'  # 10 lines: 26 / 61229
input_test2 = script_path / 'test2.txt'  # 3 lines: 5 / 23528
 
file_in = input #_test


def parse(puzzle_input):
    """Parse input - each line of 10 number signals then 4-digit number"""

    with open(puzzle_input, 'r') as file:
      data = [d.split(' | ') for d in file.read().split('\n')]
    return data


def part1(data):
    """Solve part 1""" 

    ''' 1 = 2 char
        4 = 4 char
        7 = 3 char
        8 = 7 char    
    '''

    numbers_dict = {"0":0, "1":0, "2":0,"3":0, "4":0,"5":0, "6":0,"7":0, "8":0,"9":0}

    for line in data:
        groups = line[1].split()

        for g in groups:
            if len(g) == 2:
                numbers_dict["1"] += 1 
            if len(g) == 3:
                numbers_dict["7"] += 1 
            if len(g) == 4:
                numbers_dict["4"] += 1 
            if len(g) == 7:
                numbers_dict["8"] += 1 
                  
    return sum(numbers_dict.values())


def containsCount(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    tally=0
    for c in set:
        if c in str: tally +=1
    return tally


def split(word):
    return [char for char in word]


def part2(data):
    """Solve part 2"""   
    '''
        2-char (1) = unique top-right, bottom-right
        3-char (7) = unique top, top-right, botton-right
        4-char (4) = unique top-left, top-right, bottom-right, middle
        7-char (8) = unique all
        In ORDER
            5-char (3) = has 2 in common with 1
            5-char (5) = has 3 matching wih 4
            5-char (2) = remaining 5-char is 2
        then
            6-char (9) = 4 matching from 4
            6-char (6) = 2 matching from 7
            6-char (0) = remaining 6-char is 0
    '''
    results=[]  
    
    for d in data:
        numbers_pattern = {}
        groups = [''.join(sorted(g)) for g in d[0].split()]
        digits = [''.join(sorted(d)) for d in d[1].split()]

        codes_filter_unique = list(filter(lambda g: len(g) in (2,3,4,7), groups))
        codes_filter_5char = list(filter(lambda g: len(g)==5, groups))
        codes_filter_6char = list(filter(lambda g: len(g)==6, groups))
        
        for g in codes_filter_unique:
            if len(g) == 2: numbers_pattern["1"] = g 
            elif len(g) == 3: numbers_pattern["7"] = g
            elif len(g) == 4: numbers_pattern["4"] = g
            elif len(g) == 7: numbers_pattern["8"] = g
        
        for g in codes_filter_5char:

            if "3" not in numbers_pattern.keys() and containsCount(g, numbers_pattern["1"]) == 2:  
                numbers_pattern["3"] = g
                continue

            if "5" not in numbers_pattern.keys() and containsCount(g, numbers_pattern["4"]) == 3: 
                numbers_pattern["5"] = g
                continue
                
            if "2" not in numbers_pattern.keys():
                numbers_pattern["2"] = g
                
        for g in codes_filter_6char:
            # 6 char (9) - 4 matching with 4
            # 6 char (6) - matches 2 from 7
            # 6 char (0) - remaining 6char
            
            if "9" not in numbers_pattern.keys() and containsCount(g, numbers_pattern["4"]) == 4: 
                numbers_pattern["9"] = g
                continue

            if "6" not in numbers_pattern.keys() and containsCount(g, numbers_pattern["7"]) == 2: 
                numbers_pattern["6"] = g
                continue

            if "0" not in numbers_pattern.keys():
                numbers_pattern["0"] = g

        line_results = []
        for digit_code in digits:
            for k,v in numbers_pattern.items():
                if digit_code == v:
                    line_results.append(k)
        
        results.append(int(''.join(line_results)))
        
    return sum(results)
 

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