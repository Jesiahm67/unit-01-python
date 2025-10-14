from datetime import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
my_date = datetime.now()#shows the time and date
print("Task 1:")
print()
print(my_date)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
print("task 2:")
my_date = datetime.now()#shows the date and time
my_string = my_date.strftime("%m/%d/%y")#formats the date into MM/DD/YYYY
print()
print(f"The date is: {my_string} {my_date.strftime('%H:%M:%S')}")
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
print("task 3:")
date_1 = "2023-01-15"#make two different dates of your choosing
date_2 = "2023-03-25"
date_format = "%Y-%m-%d"#makes the date format

date_obj1 = datetime.strptime(date_1, date_format) #shows the format and the dates for the first and second dates
date_obj2 = datetime.strptime(date_2, date_format)

time_dif = date_obj2 - date_obj1#finds the difference between the dates

difference = time_dif.days#shows the difference in days

print(f"The first date is {date_obj1.date()}")#prints the dates and the difference
print()
print(f"The second date is {date_obj2.date()}")
print()
print(f"The difference is {difference} days")
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print("task 4:")
birthdate_input = input("whens your birthdate? answer in (MM/DD/YYYY) format ") # will ask for your bithday 
print()
lovly_date = datetime.strptime(birthdate_input, "%m/%d/%Y") # will change it into the proper format 
today = datetime.today()

todays_date= datetime.now()  #gives todays date 
crazy = todays_date.strftime("%m/%d/%Y")

age = today.year - lovly_date.year #will subtract the two dates 

print(age) #will do its best to give u your age 
   
    