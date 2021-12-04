# https://adventofcode.com/2021/day/XX

import sys

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


print("Advent of Code 2021 - Day 4b")

filename = 'test.txt'  # 148 * 13 = 1924
filename = 'test2.txt'  # 2192?
filename = 'input.txt'  #  8468


def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, 'r') as file:
      lst = file.read().split('\n')   #  Read each line (split \n) and form a list of strings
      input=[line.split() for line in file]
      balls = [ball for line in input[0] for ball in line.split(',')]
      del input[0]

    return 1


def make_grids(data):

  output = []
  tmp = []

  for i, d in enumerate(data):
    if i == 0: 
      continue
    if d == []:
      output.append(tmp)
      tmp = []
      continue
    tmp.append(d)

  output.append(tmp)

  return output


def search_and_mark(source, item):
    for i in range(len(source)):
        if source[i] == item:
            source[i] = source[i]+'x'
            # print(source[i], item)
            return True
    return False


def check_win(grid):
  for row in grid:
    win_row = ''.join(row).count('x') == 5
    if win_row: break
    
  cols = list(zip(*grid))
  for col in cols:
    win_col = ''.join(col).count('x') == 5
    if win_col: break

  return  win_col or win_row



with open(dirpath + filename, 'r') as file:
  input=[line.split() for line in file]

  balls = [ball for line in input[0] for ball in line.split(',')]
  del input[0]
  grids = make_grids(input)

  checked = []
  winning_grid_id = 0
  last_ball = 0

  win_grid_ids = []
  win_combis = []

  while len(balls) > 0 and len(grids) > len(win_grid_ids):
    b = balls.pop(0)
    checked.append(b)

    # print('\n<<<<< BALL >>>>>>>', b, 'WC', win_combis, '/', win_grid_ids)
    
    for i in range(len(grids)):

      if i not in win_grid_ids:
        for row in grids[i]:
          search_and_mark(row, b)
        win_status = check_win(grids[i])

        if win_status: 
          win_grid_ids.append(i)
          win_combis.append([i, int(b)])
          last_ball = int(b)

winning_grid_id = win_grid_ids[-1]
print('------------------')
print('grid', winning_grid_id, 'ball', last_ball)
print(grids[winning_grid_id])

running_total = 0

for i, row in enumerate(grids[winning_grid_id]):
  for j in row:
    if 'x' in j:
      continue
    else:
      running_total += int(j)

print('Ans', running_total * last_ball)