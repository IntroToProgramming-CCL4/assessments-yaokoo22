names = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = "Sam"

search = input("Enter to search name for Sam: ")

if search in search_name:
  print(f"Hi {search_name} ")
else:
  print("Invalid Input")