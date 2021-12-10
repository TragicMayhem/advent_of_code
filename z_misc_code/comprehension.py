# In [9]: l = [[3,7,2],[1,4,5],[9,8,7]]
# In [10]: [sum(i) for i in zip(*l)]
# Out[10]: [13, 19, 14]
# https://stackoverflow.com/questions/13783315/sum-of-list-of-lists-returns-sum-list

l = [[3,7,2],[1,4,5],[9,8,7]]
ans = [sum(i) for i in zip(*l)]
print(ans)