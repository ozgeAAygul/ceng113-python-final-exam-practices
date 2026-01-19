#topics: strings, dict, sets, files
'''
import string
translator = str.maketrans("", "", string.punctuation)  burada "değiştirecek karakter", "yerine konulcak karakter", "tamamen silinecek karakter" eğer "abc", "123", "xyz" olsaydı bu a yerine 1 b yerine 2 c yerine 3 koy x y ve z yi tamamen sil demek olurdu

line = line.translate(translator)
'''
word_dict = {}
with open("03_text_intelligence/article.txt", "r") as file:
  for line in file:
    line = line.strip().lower()
    punctuation = "!'^+%&/()=?_-*\"<>£#${}[]|.:,;`"
    for char in punctuation:
      line = line.replace(char, "")

    if line:
      words = line.split()
      for word in words:
        if word in word_dict:
          word_dict[word] += 1
        else:
          word_dict[word] = 1

total = 0

most_common = " " #max(word_dict, key=word_dict.get)
most_count = 0 # word_dict[most_common]
for w, i in word_dict.items():
  if i > most_count:
    most_count = i
    most_common = w
  total += i

print(f"total words: {total}\nuniqe words: {len(word_dict.keys())}\nmost common: {most_common} ({most_count})")