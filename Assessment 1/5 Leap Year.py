#Days in each month.
month_days = {'1' : '30', '2' : '29' , '3' : '31' , '4' : '30' , '5' : '31', '6' : '30' , '7' : '31',
              '8' : '31' , '9' : '30', '10' : '31' , '11' : '30' , '12' : '31'} 
  
#It ask the user to input a month number.
month = int(input("Enter the month number (1 - 12) : "))

if month == 2:
    year = int(input("Which year of Febuary: "))
    if (year%400 == 0) or (year%4==0 and year%100!=0) :
      days = 29
    else:
       days = 28  
else:
   days = month_days(month)

if 1 <= month <= 12:
    print(f"The number of days in {month} is {days}.")

else:
   print("Invalid number.")