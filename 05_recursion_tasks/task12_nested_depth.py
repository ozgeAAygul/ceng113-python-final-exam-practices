'''
def nested_depth(lst, index=0):
  if index == len(lst):
    return 1
  if type(lst[index]) == list:
    depth = 1 + nested_depth(lst[index], 0)
  else:
    depth = 1
  return max(depth, nested_depth(lst, index+1)) 

lst = [1, [2, [3, [4]]]]   
print(nested_depth(lst))
'''
#başka yolu da var 
def nested_depth_second_way(nested_list):
  if nested_list == []:
    return 1
  
  first = nested_list[0]
  rest = nested_list[1:]

  depth_first = 1
  depth_rest = 1

  if type(first) == list:
    depth_first = 1 + nested_depth_second_way(first) #listede aşağı doğru bakıyor

  depth_rest = nested_depth_second_way(rest)  #listede yana doğru bakıyor

  if depth_first > depth_rest:
    return depth_first
  else:
    return depth_rest
  
lst = [1, [2, [3, [4]]]]   
print(nested_depth_second_way(lst))