#topics: recursion, lists
def convert_to_single_level_list(nested_list):
  if nested_list == []: #base case
    return []
  
  first = nested_list[0]
  rest = nested_list[1:]

  if type(first) == int:
    return [first] + convert_to_single_level_list(rest)
  elif type(first) == list:
    return convert_to_single_level_list(first) + convert_to_single_level_list(rest)
  
nested_list = [1, [2, [3, 4]], 5]
new_list = convert_to_single_level_list(nested_list)
print(new_list)