#Smart ATM Simulator
#topics: decision, loops, functions, exceptions
def save_accounts_to_file(accounts):
  with open("02_smart_atm/account.txt", "w") as file:
    for account_number, (name, balance) in accounts.items():
      file.write(f"{account_number},{name},{balance}\n")
  
def show_balance(accounts, account_number):
  balance = accounts[account_number][1]
  print(f"Your balance: {balance}")

def deposit_money(accounts, account_number, amount):
  try:
    amount = float(amount)
  except ValueError:
    print("Invalid input")
    return

  if amount <= 0:
    print("Invalid amount.")
    return
  
  accounts[account_number][1] += amount
  
  print(f"money deposited. your new balance is {accounts[account_number][1]}")
  
def withdraw_money(accounts, account_number, withdraw_amount):
  try:
    amount = float(withdraw_amount)
  except ValueError:
    print("invalid input")
    return

  if amount <= 0:
    print("Invalid amount.")
    return
  
  if amount > accounts[account_number][1]:
    print("insufficient balance")
    return
  
  accounts[account_number][1] -= amount
  print(f"withdrawal successfull. new balance is {accounts[account_number][1]}")

def transfer_money(accounts, account_number, transfer_amount, target_account):
  try:
    amount = float(transfer_amount)
  except ValueError:
    print("invalid input")
    return

  if amount <= 0:
    print("Transaction rejected.")
    return
  
  if target_account not in accounts:
    print("Target account not found.")
    return
  
  if amount > accounts[account_number][1]:
    print("Insufficient balance.")
    return
  
  accounts[account_number][1] -= amount
  accounts[target_account][1] += amount

  print("Transfer successful.")
  
def main():
  accounts = {}
  with open("02_smart_atm/account.txt", "r", encoding="utf-8") as file:
    for line in file:
      line = line.strip()
      if line:
        number, name, balance = line.split(",")
        accounts[number] = [name , float(balance)]
  while True:
    print("1)Login\n2)Exit")
    choice = input("what do you want? ")
    if choice == "1":
      account_number = input("Enter account number: ")
      if not account_number.isdigit():
        print("Account number must be numeric")
        continue
      else:
        if account_number in accounts:
          account_name = accounts[account_number][0]
          print(f"Welcome {account_name}")
          while True:
            
            print("\n1)Show Balance\n2)Deposit\n3)Withdraw\n4)Transfer Money\n5)Logout\n")
            choice2 = input("What do you want to do? ")
            if choice2 == "1":
              show_balance(accounts, account_number)
            elif choice2 == "2":
              amount = input("Enter the amount: ")
              deposit_money(accounts,account_number, amount) 

            elif choice2 == "3":
              withdraw_amount = input("Enter amount: ")
              withdraw_money(accounts,account_number, withdraw_amount)

            elif choice2 == "4":
              target_account = input("Enter target account: ")
              transfer_amount = input("Enter amount: ")
              transfer_money(accounts, account_number, transfer_amount, target_account)

            elif choice2 == "5":
              print(f"Goodbye {account_name}")
              save_accounts_to_file(accounts)
              break

            else:
              print("Invalid input!")

        else: 
          print("Account not found!")
          continue
    elif choice == "2":
      print("Goodbye:)")
      save_accounts_to_file(accounts)
      
      break
    else:
      print("Invalid input!")
main()