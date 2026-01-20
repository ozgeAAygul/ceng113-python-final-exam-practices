#topics: recursion, lists
def sum_of_all_integers(data):
  if data == []:#Base Case
    return 0
  
  first = data[0]#Problemi küçült
  rest = data[1:]

  if type(first) == int: #recursive
    return first + sum_of_all_integers(rest)
  elif type(first) == list:
    return sum_of_all_integers(first) + sum_of_all_integers(rest)

data = [1, [2, [3, 4]], 5]
print(f"Sum of all integers: {sum_of_all_integers(data)}")


