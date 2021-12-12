
def parse(puzzle_input):
    """Parse input"""

    with open(puzzle_input, 'r') as file:
        input = file.read().split('\n')
        input=[[int(x) for x in row] for row in input]      
    
    return input


#---
# eg
# 12345678
# 71252156
#   data = [[int(posn) for posn in row] for row in f.read().splitlines()]
#   grid = [((y,x),int(v)) for y, row in enumerate(open(filepath,'r').read().split('\n')) for x,v in enumerate(row)]
'''
((0,0), 4),
((0,1), 5)
etc
'''