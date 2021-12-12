# https://www.youtube.com/watch?v=oBt53YbR9Kk

def fib(n, memo=None):
  if memo == None: memo={}
  if n in memo.keys(): return memo[n]
  if n <= 2: return 1

  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
  return memo[n]

  
print ("fib(8)  ", fib(8))   # 21
print ("fib(23) ", fib(23))  # 28657
print ("fib(50) ", fib(50))  # 12586269025
print ("fib(238)", fib(238)) # 24522987531716273545293036474970821924473060471519
