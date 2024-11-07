first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

hometown = input("Enter your hometown: ")

age = input("Enter your age: ")

while not age.isdigit():
  print("Please enter a valid number for age. ")
  age = input("Enter your age: ")

age = int(age)

persons_information = {
  "First Name" : first_name, 
  "Last Name" : last_name,
  "Hometown" : hometown,
  "Age" : age
}

print(f"Name : {persons_information['First Name']} {persons_information['Last Name']}")
print(f"Hometown: {persons_information['Hometown']}")
print(f"Age {persons_information['Age']}")