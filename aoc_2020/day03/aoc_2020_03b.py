import sys

print("Advent of Code 2020 - Day 3 part 2")

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"


# Input pattern of trees(#) and space(.)
# This repeats to the the right indefinately
# Going right 3, down 1 - how many trees would encounter?

# handle = open(dirpath + 'test.txt', 'r')
handle = open(dirpath + 'input.txt', 'r')
lines = handle.readlines()
handle.close()

for i in range(len(lines)):
  lines[i] = lines[i].rstrip()

# There are a number of route variations to check format: (Right, down)
variations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_counts = []
answer = 1
tree = "#"
pattern_width = len(lines[0].rstrip()) - 1

# Outerloop checks each variation and the inner loop processes and stores answers
for var in variations:
  # Reset at start of the look, var is a tuple (x,y)
  count_trees = 0
  pos_x = 0
  move_x, move_y = var 

  for pos_y in range(len(lines)): 

    # Use to know if you need to skip a line(s) where the move_y > 1
    if pos_y % move_y > 0:
      continue

    # check if the position is a tree ( >0 just to skip first iteration)  
    if pos_y > 0 and lines[pos_y][pos_x] == tree:
      count_trees += 1      
    
    pos_x += move_x
    
    # Readjust the x position based on the pattern width
    if pos_x > pattern_width:
      pos_x = pos_x - pattern_width - 1
  
  tree_counts.append(count_trees)  # Store this route number of tress
  answer *= count_trees  # Calculate the answer as you process each route

print("Tree counts: ", tree_counts, " final answer: ", answer)

