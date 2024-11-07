def even_odd (number):
  if number % 2 == 0:
    return "The number is Even."
  else:
    print("The Number is Odd.")

users_input = int(input("Enter a number: "))
inputs = even_odd(users_input)
print(inputs)