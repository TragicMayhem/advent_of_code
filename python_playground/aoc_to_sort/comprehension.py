# In [9]: l = [[3,7,2],[1,4,5],[9,8,7]]
# In [10]: [sum(i) for i in zip(*l)]
# Out[10]: [13, 19, 14]
# https://stackoverflow.com/questions/13783315/sum-of-list-of-lists-returns-sum-list

l = [[3,7,2],[1,4,5],[9,8,7]]
ans = [sum(i) for i in zip(*l)]
print(ans)


# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
  
# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)


# These are same
'''6,10
0,14
9,10
0,3
10,4
['6,10', '0,14', '9,10', '0,3', '10,4','''
# print(coords.split('\n'))
# print(list(pair for pair in coords.split('\n')))
        