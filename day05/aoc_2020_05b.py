import sys
import math

print("Advent of Code 2020 - Day 5 part 2")

dirpath = sys.path[0] + '\\'

# handle = open(dirpath + 'test.txt', 'r')
handle = open(dirpath + 'input.txt', 'r')

data = handle.readlines()
handle.close()

seats = []


def locate(input_text, low_ind, high_ind, l_bound, u_bound):
  '''
    F(ront) and B(ack), 128 rows
    3-character string of L(eft) and R(ight), 8 columns
    A letter indicates whether the seat is in the front/left or the back/right
    The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
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
  row = locate(boarding_card[:7], 'F', 'B', 0 ,127)
  col = locate(boarding_card[7:], 'L', 'R', 0, 7)
  seats.append(row * 8 + col)

print("Max seat ID: ", max(seats))

seats = sorted(seats)

for i in range(len(seats)):
  if i == 0:
    continue
  if (seats[i] - seats[i-1] == 2):
    print(f"Your seat: {seats[i] - 1}")

