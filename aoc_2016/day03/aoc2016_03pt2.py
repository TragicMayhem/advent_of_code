import sys

# https://adventofcode.com/2016/day/3

print("Advent of Code 2016 - Day 3 part 2")

dirpath = sys.path[0] + '\\'

filename = 'test.txt'  # 4
filename = 'input.txt'  #  1921

impossible = []
valid = []


def tri_validity(sides):
  
  if isinstance(sides, tuple) and len(sides) == 3:
    side1, side2, side3 = sides
  else:
    side1 = side2 = side3 = 0 

  combi1 = side1 + side2 > side3
  combi2 = side1 + side3 > side2
  combi3 = side2 + side3 > side1
  
  return all([combi1, combi2, combi3])


def build_tri(g1, g2 ,g3):
  if not(isinstance(g1, list) and isinstance(g2, list) and isinstance(g3, list) and \
    len(g1) == 3 and len(g2) == 3 and len(g3) == 3):
    return [(),(),()]
  
  t1 = (g1[0], g2[0], g3[0])
  t2 = (g1[1], g2[1], g3[1])
  t3 = (g1[2], g2[2], g3[2])
  
  return [t1, t2, t3]


with open(dirpath + filename, 'r') as file:
  data = file.read().split('\n')  # Read file make list bu splitting on new line \n
  data = [' '.join(d.split()).split() for d in data] # Splits/rejoins (to replace the multiple spaces), the splits into list
  data = [[int(i) for i in d] for d in data]

  for i in range(0,len(data),3 ):
    # print(i)
    tri1, tri2, tri3 = build_tri(data[i], data[i+1], data[i+2])
    # print(f'Tri: {tri1} >>> Status = {tri_validity(tri1)}')
    # print(f'Tri: {tri2} >>> Status = {tri_validity(tri2)}')
    # print(f'Tri: {tri3} >>> Status = {tri_validity(tri3)}')

    valid.append(tri1) if tri_validity(tri1) else impossible.append(tri1)   
    valid.append(tri2) if tri_validity(tri2) else impossible.append(tri2)   
    valid.append(tri3) if tri_validity(tri3) else impossible.append(tri3)   
  
  print()
  print(f"Input: {len(data)} with {len(valid)} valid triangles and {len(impossible)} impossible")

