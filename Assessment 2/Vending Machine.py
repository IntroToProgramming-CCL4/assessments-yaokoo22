print("Hi Welcome to Samuel's Chocolate's Vending Machine !")
chocolates_item = {
  1:{"name" :"M&M's","price" : "6.00"},
  2:{"name" :"Maltesers","price" : "5.50"},
  3:{"name" :"Bounty","price" : "5.00"},
  4:{"name" :"Mars","price" : "4.00"},
  5:{"name" :"Kinder Bueno","price" : "4.00"},
  6:{"name" :"Reese's","price" : "4.75"},
  7:{"name" :"Twix Top Chocolate Bar","price" : "2.00"},
  8:{"name" :"Hershey's Milk Chocolate","price" : "4.50"},
  9:{"name" :"Cadbury Dairy Milk","price" : "3.75"},
  10:{"name":"Galaxy Smooth Chocolate Bar","price" : "4.75"},
}
def menu_display():
    ### Displays the Menu ###
  print("Here are the available Chocolates")
  for code, details in chocolates_item.items():
    print(f"{code}. {details['name']} - AED {float(details['price']):.2f}") 
    

def select_quantity(budget):
  ### It allows the user to select and specify their orders quantity ###
  shopping_cart = {}
  total_cost = 0
  while True:
    ### Display the menu ###
    menu_display()  

    ### Get users chocolate selection ###
    try:
      choices = int(input("\nEnter the number of chocolate  you want to buy: "))
      if choices not in chocolates_item:
        print("Invalid choice !! Please select a valid number from the list of items.")
        continue
    except ValueError:
        print("Please enter valid number.")
        continue

    ### Get users quantity of order ###
    try:
      quantities = int(input(f"\nEnter the quantity of {chocolates_item[choices]['name']} you want to purchase: "))
      if quantities <= 0:
        print("Quantity atleast must be more than 1. ")
        continue
    except ValueError:
        print("Please enter valid number.")
        continue

    cost = float(chocolates_item[choices]['price']) * quantities

    if total_cost + cost > budget:
      print(f"I apologize, but this choice is too expensive for you! You have AED left over from your budget is {budget - total_cost:2f}. ")
      continue

    ### Shopping cart and update total cost of budget !!

    if choices in shopping_cart:
      shopping_cart[choices] += quantities
    else:
      shopping_cart[choices] = quantities
    total_cost += cost

    ### Ask user if the users want to order more ###

    more = str(input("\nWould you want to choose a different chocolate? PRESS Either yes or no: ")).strip().lower()
    if more != "yes":
      break

  return shopping_cart, total_cost

### Main program ###
try:
  users_money = float(input("Enter your money in AED: "))
  if users_money <= 0:
    print("Money must be more than 0.")
  else:
        cart, total = select_quantity(users_money)
        print("\nYour Shopping Cart:")
        for code, quantity in cart.items():
            name = chocolates_item[code]['name']
            price = float(chocolates_item[code]['price']) 
            subtotal = price * quantity
            print(f"{name} x {quantity} = AED {subtotal:.2f}")
        print(f"Total: AED {total:.2f}")
        print(f"Remaining Budget: AED {users_money - total:.2f}")   
except ValueError:
    print("Please enter a valid budget.")


while True:
    try:
        feedback = int(input("Rate us from 1 to 10: "))
        if 1 <= feedback <= 10:
            if feedback == 10:
                print("Thank you! We're thrilled you loved it! Please come again.")
            elif 7 <= feedback < 10:
                print("Thank you for your feedback! We're glad you had a good experience.")
            elif 4 <= feedback < 7:
                print("Thank you! We'll work on improving your experience.")
            else:
                print("We're sorry to hear that. We'll strive to do better next time.")
            break
        else:
            print("Invalid input. Please rate us between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")

