from datetime import datetime
from datetime import date

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
my_date = datetime.now()
print(my_date)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
my_date = datetime.now()
my_string = my_date.strftime("%m/%d/%y")
print(f"The date is: {my_string} {my_date.strftime('%H:%M:%S')}")
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
date_1 = "2023-01-15"
date_2 = "2023-03-25"
date_format = "%Y-%m-%d"

date_obj1 = datetime.strptime(date_1, date_format)
date_obj2 = datetime.strptime(date_2, date_format)

time_dif = date_obj2 - date_obj1

difference = time_dif.days

print(f"The first date is {date_obj1.date()}")
print(f"The second date is {date_obj2.date()}")
print(f"The difference is {difference} days")
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
while True:
    birthdate_str = input("Enter your birthdate in this format (YYYY-MM-DD)")
    birthdate = datetime.strftime(birthdate_str, "%Y-%m-%d").date()
   
    