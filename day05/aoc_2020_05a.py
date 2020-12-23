import sys
import math

print("Advent of Code 2020 - Day 5 part 1")

dirpath = sys.path[0] + '\\'

# handle = open(dirpath + 'test.txt', 'r')
handle = open(dirpath + 'input.txt', 'r')

data = handle.readlines()
handle.close()

seats = []

# def locate_row(row_string):
#   '''
#     7-character string of F(ront) and B(ack), 128 rows
#     A letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127)
#     The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
#   '''
#   lower = 0
#   upper = 127

#   for x in row_string:
#     gap = math.ceil((upper - lower) / 2)
#     if x == 'F':
#       upper = upper - gap
#     else:
#       lower = lower + gap

#   return lower


# def locate_col(cols_string):
#   '''
#     3-character string of L(eft) and R(ight), 8 columns
#     The last three characters will be either L or R; 
#     these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). 
#   '''
#   lower = 0
#   upper = 7

#   for x in cols_string:
#     gap = math.ceil((upper - lower) / 2)
#     if x == 'L':
#       upper = upper - gap
#     else:
#       lower = lower + gap

#   return lower

def locate(input_text, low_ind, high_ind, l_bound, u_bound):
  '''
    Must be able to make that generic?
  '''
  lower = l_bound
  upper = u_bound

  for x in input_text:
    gap = math.ceil((upper - lower) / 2)
    if x == low_ind:
      upper = upper - gap
    else:
      lower = lower + gap

  return lower


for boarding_card in data:
  # row = locate_row(boarding_card[:7])
  # col = locate_col(boarding_card[7:])
  row = locate(boarding_card[:7], 'F', 'B', 0 ,127)
  col = locate(boarding_card[7:], 'L', 'R', 0, 7)
  seats.append(row * 8 + col)

print("Max seat ID: ", max(seats))

