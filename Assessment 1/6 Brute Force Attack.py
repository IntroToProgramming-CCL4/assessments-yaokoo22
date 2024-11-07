correct_password = "12345"
password_attempts = 5

while password_attempts > 0:
  users_password = input("Enter your password: ")
  if users_password == correct_password:
    print("Correct")  
    break
  else:
    password_attempts -= 1
    if password_attempts > 0: 
      print(f"Wrong password {password_attempts} try again")
    else:
      print("Maximum attempts reach pls try again later")