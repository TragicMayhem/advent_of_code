# Function which returns subset or r length from n 
from itertools import combinations 
  
def rSubset(arr, r): 
  
    # return list of all subsets of length r 
    # to deal with duplicate subsets use  
    # set(list(combinations(arr, r))) 
    return list(combinations(arr, r)) 


# Driver Function 
if __name__ == "__main__": 
    arr = [1721, 979, 366, 299, 675, 1456]
    results = rSubset(arr, 3) 
    print(results) 
    print(len(results))

    max_val = 100
    num_splits = 5

    arr = range(1, max_val+1)
    results = rSubset(arr, num_splits)

    keep = []
    for i in results:
        if sum(i) == 100:
            keep.append(i)
    print(keep)
    print(len(keep))