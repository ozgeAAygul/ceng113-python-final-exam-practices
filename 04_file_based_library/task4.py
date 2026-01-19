#topics: lists, dicts, files, exceptions
def update_file(books):
  with open("04_file_based_library/books.txt", "w") as file:
    for line in books:
      book_name, author, stock = line
      file.write(f"{book_name},{author},{stock}\n")

def show_books(books):
  count = 0
  for line in books:
    book_name, author, stock = line
    count += 1
    print(f"{count}. {book_name} - {author} (Stock: {stock})")  

def borrow_book(books, chosen_book):
  found = False
  borrowed = False

  for line in books:
    if line[0].lower() == chosen_book.lower():
      found = True

      if line[2] > 0:
        line[2] -=1
        print(f"{chosen_book} borrowed succesfully.")
        borrowed = True
        break
      
  if not found :
    print(f"There is no book called {chosen_book}")
  elif not borrowed:
    print(f"All copies of {chosen_book} are currently borrowed:(")
    
def returning_book(books, return_book):
  count = 0
  for line in books:
    if line[0].lower() == return_book.lower():
      count += 1
      print("Thank you! Hope you enjoyed it:)")
      line[2] += 1
      break
  if count == 0:
    return_author = input("Enter the author: ")
    print("Thank you. Hope you enjoyed it:)")
    books.append([return_book, return_author, 1])

  
def main():
  books = []
  with open("04_file_based_library/books.txt", "r") as file:
    for line in file:
      line = line.strip()
      if line:
        book_name, author, stock = line.split(",")
        stock = int(stock)
        books.append([book_name, author, stock])
  
  while True:
    print("\nMENU\n1)Show Books\n2)Borrow Book\n3)Return Book\n4)Exit\n")
    choice = input("what do you want? ")
    if choice == "1":
      show_books(books)
    elif choice == "2":
      chosen_book = input("Which book do you want to borrow? ").lower().capitalize()
      borrow_book(books, chosen_book)
      update_file(books)
    elif choice == "3":
      return_book = input("Which book you will return? ")
      returning_book(books, return_book)
      update_file(books)
    elif choice == "4":
      print("\nGoodbye:)\n")
      break
    else:
      print("Invalid input!")

main()
