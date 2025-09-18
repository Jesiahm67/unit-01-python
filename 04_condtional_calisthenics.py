'''
Exercise 1:
Check if an integer is greater than 10.
Return True if both conditions are met, False otherwise.
'''
if_one=int(input("Type a number: "))#create variable for interger 
if if_one >= 10:#create if and else statements to see if the variable is greater than or equal to 10
    print("True")
else:
    print("False")
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
status=str(input("Are you under 18: "))#create variable for age
if status == "yes":#create if and else statement to see what is the price depending on the age
    print("Ok the price is 10 dollars")
else:
    print("Ok then the price is 20")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
x=str(input("Name a fruit: "))#create variable to name fruit
fruit_list=["apple", "orange", "banana", "grape"]#create list of fruits
if x in fruit_list:#create if and else statements
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

weight=float(input("What is the weight: "))#create variable for weight integer and zone string
zone=str(input("Which zone are you taking: "))
A=5#create varable for zone A and zone B
B=7

if weight <= 0:#first create error if weight is less than or equal to zero
    print("Error")

if zone == "A" or zone == "zone A":#then create if statements for zone a and zone B
    weight * A
    print(weight * A)
elif zone == "B" or zone == "zone B":
    weight * B
    print(weight * B)
else:#create else statement if user does not pick zone A or B
    print("pick a zone")

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
a=int(input("Enter a number: "))#create variables for sides
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))

if a==b==c:#create multiple if sttements to decide what kind of triangle it is
    print("Equilateral")
if a==b or b==c or c==a:
    print("Isocsceles")

else:
    print("Scalene")

if (a + b <=c) or (b+c <=a) or (a+c <=b):#create if statement if 
    print("not a triangle")

