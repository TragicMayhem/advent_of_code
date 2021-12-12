# https://www.youtube.com/watch?v=oBt53YbR9Kk


def can_sum(targetsum, numbers, memo=None):
  if memo == None: memo = {}
  if targetsum in memo.keys(): return memo[targetsum]
  if targetsum == 0: return True
  if targetsum < 0: return False
  
  for num in numbers:
    remainder = targetsum - num
    if can_sum(remainder, numbers, memo):
      memo[targetsum] = True
      return memo[targetsum]
  
  memo[targetsum] = False
  return memo[targetsum]


def how_sum(targetsum, numbers, memo=None):
  if memo == None: memo = {}
  if targetsum in memo.keys(): return memo[targetsum]
  if targetsum == 0: return []
  if targetsum < 0: return None
  
  for num in numbers:
    remainder = targetsum - num
    remainder_result = how_sum(remainder, numbers, memo)
    if remainder_result != None:
      memo[targetsum] = [ *remainder_result, num] # remainder_result + [num]
      return memo[targetsum]
  
  memo[targetsum] = None
  return None


def best_sum(targetsum, numbers, memo=None):
  if memo == None: memo = {}
  if targetsum in memo.keys(): return memo[targetsum]
  if targetsum == 0: return []
  if targetsum < 0: return None
  
  shortest_combination = None

  for num in numbers:
    remainder = targetsum - num
    remainder_combination = best_sum(remainder, numbers, memo)
    if remainder_combination != None:
      combination = [ *remainder_combination, num]
      if shortest_combination == None or len(combination) < len(shortest_combination):
        shortest_combination = combination
  
  memo[targetsum] = shortest_combination
  return shortest_combination


print("")
print("can_sum(7, [2, 3])       = ", can_sum(7, [2, 3]))  # true
print("can_sum(7, [5, 3, 4, 7]) = ", can_sum(7, [5, 3, 4, 7]))  # true
print("can_sum(7, [2, 4])       = ", can_sum(7, [2, 4]))  # false
print("can_sum(8, [2, 3, 5])    = ", can_sum(8, [2, 3, 5]))  # true
print("can_sum(300, [7, 14])    = ", can_sum(300, [7, 14]))  #false

print("")
print("how_sum(7, [2, 3])       = ", how_sum(7, [2, 3])) # [3,2,2]
print("how_sum(7, [5, 3, 4, 7]) = ", how_sum(7, [5, 3, 4, 7])) # [4,3]
print("how_sum(7, [2, 4])       = ", how_sum(7, [2, 4]))  # None
print("how_sum(8, [2, 3, 5])    = ", how_sum(8, [2, 3, 5])) # [2,2,2,2]

print("")
print("best_sum(7, [5, 3, 4, 7])    = ", best_sum(7, [5, 3, 4, 7])) # [7]
print("best_sum(8, [2, 3, 5])       = ", best_sum(8, [2, 3, 5])) # [3,5]
print("best_sum(8, [1, 4 , 5])      = ", best_sum(8, [1, 4, 5])) # [4,4]
print("best_sum(100, [1, 2, 5, 25]) = ", best_sum(100, (1, 2, 5, 25))) # [25,25,25,25]

