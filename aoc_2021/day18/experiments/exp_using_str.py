import pathlib
import re

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test2.txt'  # 

def parse_keepstr(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        lines = file.read().replace(',',' ').split('\n')

        data = []
        for d in lines:
            tmp = [char for char in d if char != ' ']
            data.append(tmp)

    return data



def make_new_split(big_number):
    ln = big_number // 2
    rn = big_number - ln
    return ['['] + [str(ln)] + [str(rn)] + [']']


def find_number(txt, pos, dir):
    i = pos
    delta = -1 if dir == 'L' else 1

    while i < len(txt):
        i+=delta
        if txt[i].isdigit():
            return i
            
    return None  # now equates to False, not 0 as thats also the start, causes confusion?
            

def explode_node(data_in, current_pos):
    # need to find number left (or start of string)
    # need to find number right
    # add and replace those numbers at those positions
    # replace this one with 0

    num_explode_to_left = data_in[current_pos]
    num_explode_to_right = data_in[current_pos+1]
    print("exploding at pos",current_pos, 'nums', num_explode_to_left, num_explode_to_right)

    next_left_num_pos = find_number(data_in, current_pos, 'L')
    next_right_num_pos = find_number(data_in, current_pos+1, 'R')
    print('  left:', next_left_num_pos,'right:',next_right_num_pos)

    print (data_in)
    if next_left_num_pos:
        data_in[next_left_num_pos] = str(int(num_explode_to_left) + int(data_in[next_left_num_pos]))

    if next_right_num_pos:    
        data_in[next_right_num_pos] = str(int(num_explode_to_right) + int(data_in[next_right_num_pos]))

    data_out = data_in[:current_pos-1] + ['0'] + data_in[current_pos+3:] 
    print(data_out)
    return data_out


def collapse_next(data_in):

    depth = 0

    # I think you do explodes first. then splits. I think.  hard to tell if always do leftmost change first?!?!
    for current_pos in range(len(data_in)):
        if data_in[current_pos] == "[": 
            depth += 1
        elif data_in[current_pos] == "]": 
            depth -= 1
        elif depth == 5: 
            # If it goes 5 deep, then need to explode and this will stop this loop and re-start
            return explode_node(data_in, current_pos)

    # Here means there are no more explosions. so now to check for big numbers and replace.
    for current_pos in range(len(data_in)):
        if data_in[current_pos].isdigit () and int(data_in[current_pos]) >= 10: 
            # Take before number, split out new list of breakdown, add in remaining string. Like insert.
            data_out = data_in[:current_pos] + make_new_split(data_in, current_pos) + data_in[current_pos+1:]
            return data_out

    return False
    


# def add_list(numbers):
#     result = numbers.pop(0)
#     for i in numbers:
#         result = reduce_fully(add(result, i))
#     return(result)

def reduce_input(data_in):

    answer = data_in.pop(0)  # Get initial answer as first element
    
    for i, elem in enumerate(data_in):
        answer = ['['] + answer + elem + [']']
        c = 0
        while True and c < 10:
            print('process', answer)
            tmp_answer = collapse_next(answer)
            print(tmp_answer)
            if tmp_answer == False:
                break
            else:
                answer = tmp_answer
            c+=1
        
    print(answer)


input_data = parse_keepstr(input_test)

reduce_input(input_data)