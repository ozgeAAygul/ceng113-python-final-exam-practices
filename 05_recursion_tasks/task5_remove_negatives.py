#topics: recursion, lists
data = [1, -2, [3, -4, [5, -6]], 7]

def clean_data(data):
  i = 0
  while i < len(data):
    if type(data[i]) == int:
      if data[i] < 0:
        data.pop(i) #remove da kullanılır ama tehlikeli çünkü pop indexle remove elemanla çalışır
      else:
        i += 1
    elif type(data[i]) == list:
      clean_data(data[i]) #listenin içine girdin
      i += 1

clean_data(data)
print(data)

    

