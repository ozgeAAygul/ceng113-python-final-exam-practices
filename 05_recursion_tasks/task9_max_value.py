#topics: recursion, lists
def find_top_integer(nested_list):
  if nested_list == []:
    return None
  
  first = nested_list[0]
  rest = nested_list[1:]

  if type(first) == int: #eğer ilk eleman int ise geri kalanın maxını hesaplıyo ilk elemanlar karşılaştırıyor
    max_rest = find_top_integer(rest)
    if max_rest == None:
      return first
    elif max_rest > first:
      return max_rest
    else: 
      return first
    
  elif type(first) == list: #eğer ilk eleman listse hem ilk hem sonun ayrı ayrı maxını hesaplayıp hangisi daha büyükse onu döndürüyor
    max_first = find_top_integer(first)  
    max_rest = find_top_integer(rest)
    
    if max_rest == None:
      return max_first
    
    if max_first == None:
      return max_rest
    
    if max_first > max_rest:
      return max_first
    else:
      return max_rest
    
nested_list = [1, [2, [10, 4]], 5]
top_integer = find_top_integer(nested_list)
print(top_integer)
