# https://www.youtube.com/watch?v=oBt53YbR9Kk



def can_construct(target, wordbank, memo=None):
  if memo == None: memo = {}
  if target in memo.keys(): return memo[target]
  if target == '': return True
    
  for word in wordbank:
    if target.find(word) == 0:
      suffix = target[len(word):]
      if can_construct(suffix, wordbank, memo) == True:
        memo[target] = True
        return True
    
  memo[target] = False
  return False


def count_construct(target, wordbank, memo=None):
  if memo == None: memo = {}
  if target in memo.keys(): return memo[target]
  if target == '': return 1
    
  totalcount = 0

  for word in wordbank:
    if target.find(word) == 0:
      numways = count_construct(target[len(word):], wordbank, memo)
      totalcount += numways
    
  memo[target] = totalcount
  return totalcount


def all_construct(target, wordbank, memo=None):
  if memo == None: memo = {}
  if target in memo.keys(): return memo[target]
  if target == '': return [[]]
    
  result = []

  for word in wordbank:
    if target.find(word) == 0:
      suffix = target[len(word):]
      suffixways = all_construct(suffix, wordbank, memo)
      targetways = [word, *suffixways]
      result.append(targetways)
    
  memo[target] = result
  return result


print("can_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) =")
print("   = ", can_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # True
print("can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) =")
print("   = ", can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # Treu
print("can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) =")
print("   = ", can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # False
print("can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']) =")
print("   = ", can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4

print("")
print("count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) =")
print("   = ", count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # 2
print("count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) =")
print("   = ", count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))  # 1
print("count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) =")
print("   = ", count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # 0
print("count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']) =")
print("   = ", count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # 4

print("")
print("all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) =")
print("   = ", all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # Ture