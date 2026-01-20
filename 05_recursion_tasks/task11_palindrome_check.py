#topics: recursion, strings
def is_palindrome(word):
  word = word.lower()
  if len(word) == 0:
    return True
  if len(word) == 1:
    return True
  else:
    if word[0] == word[-1]:
      return is_palindrome(word[1:-1])
    else:
      return False
    
#başka yol da var 
def is_palindrome_second_way(word, left, right):
  word = word.lower()
  if left >= right:
    return True    
  if word[left] != word[right]:
    return False
  return is_palindrome_second_way(word, left+1, right-1)

word = "ozzo"
print(is_palindrome(word))
print(is_palindrome_second_way(word, 0, len(word)-1))

