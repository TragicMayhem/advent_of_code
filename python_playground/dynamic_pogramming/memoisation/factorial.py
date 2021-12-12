# https://www.youtube.com/watch?v=oBt53YbR9Kk

def factorial(n, memo=None):
  if memo == None: memo={}
  if n in memo.keys():
    return memo[n]
    
  if n == 0:
    return 1
  
  memo[n] = n * factorial(n - 1, memo)
  return memo[n]


print("factorial(8)  ",factorial(8))  # 40320
print("factorial(12) ",factorial(12)) # 479001600
print("factorial(25) ",factorial(25)) # 15511210043330985984000000
