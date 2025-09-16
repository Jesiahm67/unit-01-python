'''
Exercise 1:
Check if an integer is greater than 10.
Return True if both conditions are met, False otherwise.
'''
if_one=int(input("Type a number: "))
if if_one >= 10:
    print("True")
else:
    print("False")
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
status=str(input("Are you under 18: "))
if status == "yes":
    print("Ok the price is 10 dollars")
else:
    print("Ok then the price is 20")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
x=str(input("Name a fruit: "))
fruit_list=["apple", "orange", "banana", "grape"]
if x in fruit_list:
    print("correct")
else:
    print("...")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
y=str(input("What is the order weight"))

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''