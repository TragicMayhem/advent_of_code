
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
