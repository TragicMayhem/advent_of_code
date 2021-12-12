# https://www.youtube.com/watch?v=oBt53YbR9Kk


def gridtraveller(m, n,  memo=None):
  if memo == None: memo={}
  k = str(m) + ',' + str(n)
  if k in memo.keys(): return memo[k]
  if m == 1 and n == 1: return 1
  if m == 0 or n == 0: return 0

  memo[k] = gridtraveller(m - 1, n, memo) + gridtraveller(m, n -1, memo)
  return memo[k]
  
print("gridtraveller(2, 3)   ", gridtraveller(2, 3)) # 3
print("gridtraveller(18, 18) ", gridtraveller(18, 18)) #2333606220
print("gridtraveller(21, 17) ", gridtraveller(21, 17))
