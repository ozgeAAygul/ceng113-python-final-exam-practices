#topics: strings, sets, functions, files
def is_strong_password(password):
  if len(line) >= 8:
    return False
  
  has_upper = False
  has_digit = False
  has_lower = False
  has_special = False

  special_chars = set("!@#$%")

  for char in password:
    if char.isupper():
      has_upper = True
    elif char.isdigit():
      has_digit = True
    elif char.islower():
      has_lower = True
    elif char in special_chars: 
      has_special = True

  return has_upper and has_lower and has_digit and has_special 
   

password_dict = {
    "Strong Password": [],
    "Weak Password": []
  }

with open("06_password_audit_tool/passwords.txt", "r") as file:
  
  for line in file:
    password = line.strip()
    
    if password:
      if is_strong_password(password):
        password_dict["Strong Password"].append(password)
      else:
        password_dict["Weak Password"].append(password)

print(password_dict)




