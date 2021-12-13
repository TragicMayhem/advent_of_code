import sys

'''
68,125
113,69
65,86
108,149
152,53
78,90
54,160
20,137
107,90
48,12

to

[(68, 125), (113, 69), (65, 86), (108, 149), (152, 53), (78, 90), (54, 160), (20, 137), (107, 90), (48, 12)] 

'''


def test(filename):
    f = open(filename)
    lines = f.readlines()
    lines = [item.rstrip("\n") for item in lines]
    newList = list()
    for item in lines:
            item = item.split(",")
            item = tuple(int(items) for items in item)
            newList.append(item)                
    f.close()
    print newList

# OR

with open("my_txt_file") as f:
  lines = f.readlines()
result = [tuple(int(s) for s in line.strip().split(",")) for line in lines]

# OR 

with open("my_txt_file") as f:
  result = [tuple(int(s) for s in line.strip().split(",")) for line in f]