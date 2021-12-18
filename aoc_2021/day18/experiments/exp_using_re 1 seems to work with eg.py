import pathlib
import re

script_path = pathlib.Path(__file__).parent
input_test = script_path / 'test2.txt'  # 

def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        lines = file.read().replace(' ','').split('\n')

    return lines


##### PATTERNS #####
two_digits_pattern = re.compile('(\d{2})')
find_digit = re.compile(r'(\d)')
find_last_digit = re.compile(r'(\d)(?!.*\d)')


def make_new_split(big_number):
    ln = big_number // 2
    rn = big_number - ln
    new = '[' + str(ln) + ',' + str(rn) + ']'
    return new

    

def explode_node(data_in, current_pos):
    # need to find number left (or start of string)
    # need to find number right
    # add and replace those numbers at those positions
    # replace this one with 0

    num_explode_to_left = data_in[current_pos]
    num_explode_to_right = data_in[current_pos+2]
    print("\nexploding at pos",current_pos, 'nums', num_explode_to_left, num_explode_to_right)

    to_the_left = data_in[:current_pos]
    to_the_right = data_in[current_pos+3:]

    next_left_num_pos = find_last_digit.search(to_the_left)
    next_right_num_pos = find_digit.search(to_the_right)

    if next_left_num_pos:
        start, end = next_left_num_pos.span()
        new_number = int(to_the_left[start:end]) + int(num_explode_to_left)
        new_left = re.sub(find_last_digit, str(new_number), to_the_left, count=1)[:-1]
    else:
        # cant find a number to the left, so need to keep it and remove bracket!
        new_left = to_the_left[:-1]

    if next_right_num_pos:
        start, end = next_right_num_pos.span()
        new_number = int(to_the_right[start:end]) + int(num_explode_to_right)
        new_right = re.sub(find_digit, str(new_number), to_the_right, count=1)[1:]
    else:
        # cant find number to the right so need to keep string and remove first bracket
        new_right = to_the_right[1:]

    print('  new left:', new_left,' new right:',new_right)

    # data_out = data_in[:current_pos-1] + ['0'] + data_in[current_pos+3:] 
    data_out = new_left + '0' + new_right
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
    big_numbers = two_digits_pattern.search(data_in)

    if big_numbers:
        # start, end = big_numbers.span()
        # data_out = re.sub(r'(\d{2})', make_new_split(big_numbers.group(0)), data_out, count=1)
        return re.sub(r'(\d{2})', make_new_split(int(big_numbers.group(0))), data_in, count=1)

    return False


def reduce_input(data_in):

    answer = data_in.pop(0)  # Get initial answer as first element
    
    for i, elem in enumerate(data_in):
        answer = '[' + answer +',' + elem + ']'

        c = 0

        while True and c < 10:
            print('\nprocess', answer)
            tmp_answer = collapse_next(answer)
            print(tmp_answer)
            if tmp_answer == False:
                break
            else:
                answer = tmp_answer
            c+=1
        
    print(answer)

input_data = parse(input_test)
print(input_data)
print()
reduce_input(input_data)

print('########## AD HOC ###########')
test1 = '[[1, 2], [[1, 2], 3], [9, [8, 7]], [[1, 9], [8, 5]], [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]]'
test2 = '[[1, 2], [[1, 12], 3], [9, [8, 7]], [[1, 19], [8, 15]], [[[[1, 2], [13, 4]], [[5, 6], [7, 8]]], 9]]'

# print(test2)
# output = test2
# big_numbers = two_digits_pattern.search(output)

# while big_numbers:
#     print('\n',big_numbers.span())
#     start, end = big_numbers.span()
#     print('s',start,'e', end,'n', big_numbers.group(0))
#     # print(remaining[start:end])

#     output = re.sub(r'(\d{2})', make_new_split(int(big_numbers.group(0))), output, count=1)
#     print('  o:', output)
#     big_numbers = two_digits_pattern.search(output)

# print(test2)
# print(output)

# # big_numbers = two_digits_pattern.search(test2)
# # print(big_numbers.span())

# find_digits = re.compile(r'(\d+)')

# # print(find_digits.findall(test1))
# # print(find_digits.findall(test1)[::-1])
# next_left_num_pos = find_digits.findall('[[1, 2], [[1, 2], 3], [9, [8, 7]], [[1,')
# print(next_left_num_pos)
# tmp= find_last_digit.search('[[1, 2], [[1, 2], 3], [9, [8, 7]], [[1,')
# if tmp:
#     print(tmp.group(0))
#     print(tmp.span())