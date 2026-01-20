#topics: recursion, lists
def count_elements(nested_list):
  if nested_list == []:
    return 0
  
  first = nested_list[0]
  rest = nested_list[1:]

  count = 0
  if type(first) == int:
    count += 1
    return count + count_elements(rest)
  elif type(first) == list:
    return count_elements(first) + count_elements(rest)
  
nested_list = [1, [2, [3, 4]], 5]
count = count_elements(nested_list)
print(count)