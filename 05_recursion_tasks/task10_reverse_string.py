#topics: recursion, strings

def reverse_string(string):
  if string == "":
    return ""
  
  first = string[0]
  rest = string[1:]
  if len(rest) > 1:
    return reverse_string(rest) + first
  else:
    return rest + first

string = "ozge"
reverse = reverse_string(string)
print(reverse)

#hiç slicing kullanmadan
def reverse_string_without_slicing(string, index):
  if index < 0:
    return ""
  
  return string[index] + reverse_string_without_slicing(string, index - 1)

string = "ozge" 
reverse2 = reverse_string_without_slicing(string, len(string)-1)
print(reverse2)
