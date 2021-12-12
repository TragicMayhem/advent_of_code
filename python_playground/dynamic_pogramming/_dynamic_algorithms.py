
# freecodecamp.org
# Dynamic Programming - Learn to Solve Algorithmic Problems & Coding Challenges
# https://www.youtube.com/watch?v=oBt53YbR9Kk

def factorial(n, memo={}):
  if n in memo.keys():
    return memo[n]
    
  if n == 0:
    return 1
  
  memo[n] = n * factorial(n - 1, memo)
  return memo[n]


def canSum(targetsum, numbers, memo={}):
  if targetsum in memo.keys(): return memo[targetsum]
  if targetsum == 0: return True
  if targetsum < 0: return False
  
  for x in numbers:
    remainder = targetsum - x
    if canSum(remainder, numbers, memo):
      memo[targetsum] = True
      return memo[targetsum]
  
  memo[targetsum] = False
  return memo[targetsum]


def fib(n, memo={}):
  if n in memo.keys(): return memo[n]
  if n <= 2: return 1

  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
  return memo[n]


def gridtraveller(m, n, memo={}):
  k = str(m) + ',' + str(n)
  if k in memo.keys(): return memo[k]
  if m == 1 and n == 1: return 1
  if m == 0 or n == 0: return 0

  memo[k] = gridtraveller(m - 1, n, memo) + gridtraveller(m, n -1, memo)
  return memo[k]
  
print("")
print("factorial(12)",factorial(12))
print("")
print("canSum(7, [5, 3, 4, 7])",canSum(7, [5, 3, 4, 7]))
print("")
print ("fib(8)", fib(8))
print ("fib(50)", fib(50))
print("")
print("gridtraveller(2, 3)", gridtraveller(2, 3))
print("gridtraveller(18, 18)", gridtraveller(18, 18))
