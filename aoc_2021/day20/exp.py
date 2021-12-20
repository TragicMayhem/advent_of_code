
import numpy as np

a=[[1,2],[3,4]]
new_a = np.pad(a, ((0,0),(0,3)), mode='constant', constant_values=0)
# array([[1, 2, 0, 0, 0],
#       [3, 4, 0, 0, 0]])

print(new_a)

a=[[1,2],[3,4]]
new_a = np.pad(a, ((1,1),(1,1)), mode='constant', constant_values=0)
# array([[1, 2, 0, 0, 0],
#       [3, 4, 0, 0, 0]])

print(new_a)
