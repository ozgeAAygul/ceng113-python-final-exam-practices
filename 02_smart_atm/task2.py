#Smart ATM Simulator
#topics: decision, loops, functions, exceptions
def main():
  while True:
    balance = input("Enter the balance: ")
    if not balance.isdigit():
      print("Invalid input!")
    else:
      balance = float(balance)
      break

  print("1)Balance\n2)Deposit\n3)withdraw\n4)Exit") 
  choice = input("choose one of them: ")  