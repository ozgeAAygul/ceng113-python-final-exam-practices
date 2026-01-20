#topics: dict, set, functions
def add_user(friendship_dict, user_name):
  if user_name in friendship_dict:
    print(f"{user_name} already exist")
    return
  else:
    friendship_dict[user_name] = set()
    print(f"{user_name} added!")
    return
  
def add_friend(friendship_dict, user_name, friend_name):
  if user_name in friendship_dict:
    if friend_name in friendship_dict:
      friendship_dict[user_name].add(friend_name)
      friendship_dict[friend_name].add(user_name)
      print("Added:)")
    else:
      print(f"There is no friend called {friend_name}")
  else:
    print(f"There is no user called {user_name}")

def find_mutual_friend(friendship_dict, user1, user2):
  if user1 in friendship_dict:
    if user2 in friendship_dict:
      mutual_friends = friendship_dict[user1].intersection(friendship_dict[user2])
      if len(mutual_friends) >= 2:
        print(f"common friends of {user1} and {user2} are {', '.join(mutual_friends)}")
      elif len(mutual_friends) == 1:
        print(f"common friend of {user1} and {user2} is {', '.join(mutual_friends)}")
      else:
        print("there is no common friend!")
    else:
      print(f"there is no user called {user2}")
  else:
    print(f"there is no user called {user1}")

def main():
  friendship_dict = {}
  while True:
    print("\nMENU\n1)Add User\n2)Add Friend\n3)Mutual Friends\n4)Exit\n")
    choice = input("Enter a number in menu: ")
    if choice == "1":
      user_name = input("what is user's name? ")
      add_user(friendship_dict, user_name)
    elif choice == "2":
      user_name2 = input("what is user name? ")  
      friend_name = input("what is friend's name? ")
      add_friend(friendship_dict, user_name2, friend_name)
    elif choice == "3":
      first_friend = input("enter the first friend's name: ")
      second_friend = input("enter the second friend's name: ")
      find_mutual_friend(friendship_dict, first_friend, second_friend)
    elif choice == "4":
      print("Goodbye:)")
      break
    else: 
      print("Invalid input!")
      continue

main()
