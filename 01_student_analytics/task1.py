#topics: input, lists, tuples, dict, functions, files, exceptions
name_and_grades_dict = {}
while True:
  name_and_grades_input = input("Please enter the student name and grades like 'özge 10 20 30' (enter q if you want to quit): ").lower()
  if name_and_grades_input == "q":
    break
  else:
    name_and_grades = name_and_grades_input.split() #split yapmadan input üzerinden ayırmaya çalışırsan mesela ali, 10, 20 girildi 0 olarak aldığın ali değil a olur o yüzden split kullanıyoz
    #input doru mu değil mi
    try:
      if len(name_and_grades) != 4:
        print("Invalid input, enter name + 3 grades like özge 10 20 30")
        continue

      name = name_and_grades[0].capitalize()
      if not name.isalpha():#isim sadece harf içermelii
        print("Name must contain only letters.")
        continue
      grades = tuple([int(x) for x in name_and_grades[1:]]) 
      '''burada şunu da kullanabilirdin tuple(map(int, name_and_grades[1:])) ayrıca köşeli parantez kullanmayı unutmuştun list comprehensionda köşeli parantez gerekiyoo
      '''
      name_and_grades_dict[name] = grades
      print("Added:)")
    except ValueError:  
      print("the numbers are incorrect. Try again!")

def calculate_average(grades):
  total = 0
  for grade in grades:
    total += grade
  average = total / len(grades)
  return average

def find_top_student():
  data = {}
  with open('report.txt', 'r') as file:
    for line in file:
      line = line.strip() #baştaki ve sondaki boşlukları siler
      if line:#eğer line boş değilse
        name, average = line.split(": ")
        data[name] = float(average)

  best_student = " "
  best_average = -1
  for name, average in data.items():
    if average > best_average:
      best_average = average
      best_student = name
  return best_student , best_average   

def find_failed_students(): #fonksiyon adlarını fiille yazmak daha profça
  failed_dict = {}
  with open('report.txt', 'r') as file:
    for line in file:
      line = line.strip()
      if line:
        parts = line.split(": ") #burada ben name, average = line.split(": ") şeklinde yapmıştım ama dosya yapısı değişince program çalışmaya devam etsin diye bu kod daha doğru
        if len(parts) != 2:
          continue
        name, average = parts
        average = float(average)
        if average < 60:
          failed_dict[name] = float(average)
  return failed_dict
  
        
def main():
  with open('report.txt', 'w') as file:
    for name, grades in name_and_grades_dict.items():
      average = calculate_average(grades)
      file.write(f"{name}: {average:.2f}\n")

    best_student , best_average = find_top_student()    
    file.write(f"\nTop Student: {best_student}({best_average})\n")

    failed = find_failed_students()  
    for name, average in failed.items():
      file.write(f"Failed: {name} ({average})\n") # yüz kere açma dosyayı

main()
    
