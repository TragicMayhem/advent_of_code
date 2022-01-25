
def show_screen(grid):
    print()
    for line in grid:
        print(' '.join(line).replace('.', '_'))   
    print()


grid = [['.'] * 50] * 6
show_screen(grid)

# So setting this single value to another letter
# ALL rows in the grid COPY that, its not a copy
# its because 
#  1. the list was generated as string *  50
#  2. then that list was replicated 6 times
#  3. python doesnt copy, it REFERENCES
#
# Thats why the arguments are passed by reference
# and not value, so passing grid IS ACTUALLY THE SAME
# GRID. its not a copy and no need to return it.

grid[0][3] = 'S'

show_screen(grid)

print('Show the ids from python for the lists')
for elem in grid:
    print(id(elem))

print('Now check the string items in the sub lists')
for elem in grid[0:2]:
    print()
    print(id(elem))
    for item in elem:
        print(id(item))

print('Lets slice a list and then replace within the grid and print id')

grid[1] = grid[1][-5:] + grid[1][:-5]
print('Show the ids from python for the lists. See [1] different id')
for elem in grid:
    print(id(elem))

print('-'*50)
print()
print('Now to use list comprehension to create the list')
list_of_lists = [['.' for i in range(50)] for i in range(6)]
print(list_of_lists)
for elem in list_of_lists:
    print(id(elem))



