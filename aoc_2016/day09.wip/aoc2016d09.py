# https://adventofcode.com/2015/day/9

import pathlib
import time
import re

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'       # 152851
input_test = script_path / 'test.txt'   # Not run

marker_pattern = re.compile(r'\((\d+)x(\d+)\)')

def parse(puzzle_input):
    """Parse input """
    with open(puzzle_input, 'r') as file:
        data = file.read()
        # print(data)
    return data


def part1(data):
    """Solve part 1""" 
    
    compressed_data = data
    decompressed_sections = []

    # look_ahead = marker_pattern.search(compressed_data)
    # print(look_ahead.groups())
    # print(look_ahead.group())
    # print(look_ahead.span())
    # print(look_ahead.start(), look_ahead.end())
    '''
    ('192', '7')
    (192x7)
    (0, 7)
    0 7
    192 7'''

    # while current_position < len(compressed_data):
    while len(compressed_data):

        look_ahead = marker_pattern.search(compressed_data)

        if look_ahead:
            marker_length, marker_qty = (int(x) for x in look_ahead.groups())
            match_start, match_end = look_ahead.span()
            print(look_ahead.group(), '  \t', look_ahead.span() )
            # print('length:', marker_length, 'qty:', marker_qty)
            # print('start:', match_start, 'end:', match_end)

            before = compressed_data[:match_start]
            after = compressed_data[match_end:]

            # print('before:', before)
            # print('after :', len(after), '##10', after[:10], '##-20', after[-20:])

            focus_characters = after[:marker_length]
            # print('Focus chars', len(focus_characters))
            
            if len(before): decompressed_sections.append(before)
            
            decompressed_part = focus_characters * marker_qty
            decompressed_sections.append(decompressed_part)
            compressed_data = after[marker_length:]

            # print('decompressed part len:', len(decompressed_part))
            # print('len compressed:', len(compressed_data), 'first 15:', compressed_data[0:15])

            # break

        else:
            # Then is it done, just add last bit of data
            decompressed_sections.append(compressed_data)
            compressed_data = ''
    
    full_decompressed_length = sum(len(x) for x in decompressed_sections)
    print()
    print('how many decompressed data sections?', len(decompressed_sections))
    print('Decompressed length:', full_decompressed_length)
    
    return full_decompressed_length


def decompress_data1(compressed_input):

    look_ahead = marker_pattern.search(compressed_input)

    # need to take account for string BEFORE match??
    # If the compressed input has no instructions, then process that string and return the length
    if not look_ahead:
        return len(compressed_input) ##???

    if look_ahead:
        marker_length, marker_qty = (int(x) for x in look_ahead.groups())
        match_start, match_end = look_ahead.span()
        print(look_ahead.group(), '  \t', look_ahead.span(), '\t')

        before = compressed_input[:match_start]
        after = compressed_input[match_end:]
        print(compressed_input[match_end:match_end+marker_length])

        found = marker_pattern.findall(compressed_input[match_end:match_end+marker_length])
        if found:
            print("more")

            for item in found:
                print(item)

        # base case is what - nothing found, so return the length of that base string up, multiple by qty
        # but what about adding the others to it... how to know?
        # return marker_qty * decompress_data(after)





        # if '(' not in after:
        #     return marker_length * marker_qty

        # # need to do len(before) + recursive call?

        # # canwe look at () then count ( within the first ones range)
        # # process and tally then move on

        # remaining_characters = after[:marker_length]
        
        # # return decompress_data(remaining_characters)

        # if len(before): decompressed_sections.append(before)
        # # this means there are more instructions to process. We have to go deeper


        # decompressed_part = focus_characters * marker_qty
        # decompressed_sections.append(decompressed_part)
        # compressed_data = after[marker_length:]

    return 1


def decompress2(data):

    # what if split all by (
    # build dictionary of the parent childs like a route tree
    # add up the leaves that have no brackest?

    # seq_len: X   seq_rtp: y  child: {same if brackets} data: string remaining
    # len of children is
    # need to sum the children then multiuple by the parent qty

    # or return the new string up. add it to the data  - much too big, point is do by numbers



    return 88


def part2(data):
    """Solve part 2
    For example:
        (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
        X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
        (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
        
        (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.
                9(3*3)  6(2*3) 10(5*2) X        6(3*2) 35(5*7)
              -------------------------       ------------------      
                   25(9+6+10)                      41(6+35)
          75(25*3)                        369(9*41)
                  75+369= 444 + 1 char (X) = 445
    """
    
    # 12×12×14×10×12 = 241920
    # look for first number (x), then x chars after the ).
    #   if ( ) in that sequence, look again
    #   decompress and return the tally
    # recursion?  pass in string left, until terminal and add to next one
    # repeat

    ans = decompress_data1(data)

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