print("Data types")
"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
x = 20.1#create variable for float

y = int(x)#create int func to convert float into integer

print(x)
print(y)

"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
x = float(input("Enter your number:")) #create variable for integer

if x < 0: #create if statement to see if x is negative
 print("negative")
elif x == 0: #create elif statement to see if x is equal to 0
   print("equal to 0")
elif x > 0: #create elif statemenrt to see if x is positive
 print("postive")



"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
x = int(input("Enter an integer:")) #create variable for integer
x1 = int(x)
print()
print()
y = float(input("Enter a float:")) #create variable for float
y2 = float(y)

addition_result = x1 + y2 #create addition results
subtraction_result = x1 - y2 #create subtraction results
multiplication_result = x1 * y2 #create multiplication results

if y2 != 0:
    division_result = x1 / y2 #create division results

else:
    division_result = "Cannot divide by zero" #create division result if divide by zero

print(f"/Results:")#print results for mathamatics
print(f"Addition: {x1} + {y2} = {addition_result} ")
print(f"Subtraction : {x1} - {y2} = {subtraction_result}")
print(f"Multiplication: {x1} * {y2} = {multiplication_result}")
print(f"Division: {x1} / {y2} = {division_result}")


"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
#create variable for fruits and their amount
f = {
  "bananas": 9,
  "mangos": 4,
  "apples": 5,
  "oranges": 7
#print the amounts of fruits listed below
}
print(f"The amount of bananas is: {f['bananas']}")
print()
print(f"The amount of mangos is {f['mangos']}")
print()
print(f"The amount of apples is {f['apples']}")
print()
print(f"The amount of oranges is {f['oranges']}")

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
first_string = "[1.2,3,4,5]"#create variable for the first string

converted_tuple = eval(first_string)#create variable for the tuple

print("first_string:" , first_string)#print the first string
print()
print("converted_tuple" , converted_tuple)#print the converted tuple
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""
fav_subjects = ["math", "history", "Ela"]#create variable for fav subjects
print()
separated_subjects = ",".join(fav_subjects)# create variable for camma free subjects
print()
dash_separated_subjects = "-".join(fav_subjects)# create varibale for dash subjects

print("First list of subjects:", fav_subjects)#print for list for subjects
print()
print("Comma-separated subjects:", separated_subjects)
print()
print("Dash-separated subject:", dash_separated_subjects)





print("Formatting")
"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""

password = "Apple"#create variable for password
new_password = password.upper()#create variable for new password to be uppercase and lowercase
new_password = password.lower()
input("Enter password: ")#create input to enter the password
"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
empty_string = input("say something: ").strip()#create variable for input and strip to remove empty spaces

if empty_string == "":#create invailid statement if nothing is in the variable
    print("invalid")
else:#create vailid statement if something is in the variable
    print("valid")


"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
program = "I really like cats"# create variable for program
new_program = program.replace ("cats", "dogs")# create vairable for new program
print(program)#print original program
print(new_program)#print new program
"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = input("Jesiah")#create inputs for name and age
age = input("16")
name = ("Jesiah")#create variables for the name and age press enter for it to show up without difficulities
age = ("16")
print(f"My name is {name} and I am {age} years old.")#create print sentance

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
num1 = float(input("Enter the first float: "))#create variables for float and input for both the first and second float
num2 = float(input("Enter the second float: "))

if num2 != 0:#create if statement to check if the second float is not equal to zero
    quotient = round(num1 / num2, 1) # Round to 1 decimal place
    print("Quotient (rounded to 1 decimal):", quotient)#prints the quotient rounded to 1 decimal place

else:#create else statement if the second number is equal to zero
    print("Cannot divide by zero.")
    
    
    
    
    
print("List_blitz")
"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
my_first_list = ["hello", "123", "george", "bye"]#create variable for first list
print(my_first_list)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
my_second_list = ["hello"]#create variable for second list 
my_second_list.append("george")#add new value to second list
print(my_second_list)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
my_third_list= ["123", "456", "789"]#create variable for third list
my_third_list.remove("123")#remove vlure from old list
print(my_third_list)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
my_fourth_list=["hi","universe", "123"]#create variable for fourth list
my_fourth_list[2] = "$"#create value to replace the third value that starts at 0 to 2
print(my_fourth_list)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
my_fifth_list = ["1", "2", "3"]#create variable for fifth list
my_fifth_list.append("4")#create append to add more values to the list
my_fifth_list.append("5")
my_fifth_list.append("6")
print(my_fifth_list)
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
my_sixth_list = ["red", "orange", "yellow"]#create variable for sixth list with three values
del my_sixth_list[0]#create del function to delete value from list from 0 to 2
print(my_sixth_list)

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
my_seventh_list = ["a", "b", "c"]#create variable for seventh list 
new_variable= my_seventh_list[0:2]#create new variable to copy the first 2 values in the old variable
print(my_seventh_list)
print(new_variable)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.

"""
list_1=["a", "b"]#create 2 variables for the eigth list
list_2=["c", "d"]
my_eighth_list = list_1 + list_2#create variable for eigth list to combine both recent lists
print(list_1)
print(list_2)
print(my_eighth_list)



print("Conditionals")
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





print("School safety")
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




print("Calculator")



num_one = float(input("Type a number: "))#create float variables for the first and second numbers
num_two = float(input("Type a second number: "))
print("1.Addidtion")#create prints to show what each number means as an operation
print()
print("2.Substraction")
print()
print("3.Multiplication")
print()
print("4.Division")
print()
print("5.Exponents")
print()
print("6.Remainder")
print()
print("7.Floor Division")
print()

user = int(input("Pick a number any number: "))#create variable to pick an operation

if user > 7:#create if statement if the operation number is higher than 7
    print("Invalid number")

if user == 1:#create if statements for each operation
    print(num_one + num_two)
    
if user == 2:
    print(num_one - num_two)
    
if user == 3:
    print(num_one * num_two)
    
if user == 4:
    if num_two == 0:#create nested if statement if either number is 0 and giveds an error
        print("Error")
    else:
        print(num_one/num_two)
    
if user == 5:
    print(num_one**num_two)
    
if user == 6:
    
    if num_two == 0 or num_one == 0:
        print("Error")#create nested if statement if either number is zero and gives an error
    else:
        print(num_one%num_two)
        
if user == 7:
    if num_two == 0 or num_one == 0:
        print("Error")#create nested if statement if either number is zero and gives an error
    else:
     print(num_one//num_two)




print("Whimsical while loops")



"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
num = 1#create variable for number interger
print("task one")

while num < 10:#create while functon if num is less than one
    num += 1#add num by one
    print(num)
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

num = 10#create variable for number integer
print("task two")

while num > 1:#create while if number is greater than 1
    
    num -= 1
    print(num)

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
num = int(input("give me a number: "))#create variable for int
result = 1 #create variable for result
print("task 3")
while num > 0:#create while if num is greater than 0
    print(num)
    print()
    result = num *result #result would equal number input times the result
    num -= 1 # minus 1 from num
    
print(result)
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password="password"#create variable for password 
print("task 4")
user=str(input("Type the password: "))#create variable input for user to guess passwor
while user != password:#creatw while if the user input is not the password then it would print try again
    print("try again")
    user=str(input("Type the password: "))

else: #if the while statement is false then it would print that you are correct
    print("you are correct")




"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""




print("Flipping fors")


"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print("Excercise 1:")
choc = ["Hershey", "M&M","Reeses"]#create a list of chocolates
for choc in choc:#create a for loop to say the list
    print(choc)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print("Excercise 2:")
num = [1,2,3,4,5]#create a list of numbers
sum = 0#create a variable called sum
    
for num in num:#create a for loop to say the list
    sum += num#add each number to the sum
    print("The sum is", sum)
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print("Excercise 3:")
sentance = "This is a sample sentance"#create sentence
words = sentance.split()#create vairable to split sentance and length
length = []
for word in words:#create a for loop to say the list
    length.append(len(word))#add length for each word in numbers
print("length:", length)
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
print("Excercise 4:")
dictionary = {"name":"Jesiah", "age": 16, "city": "New York", "hobby": "coding"}#create dictionary for jesiah
for key, value in dictionary.items():#create for loop to say the dictionry
    print(f'{key}: {value}')
# The output of the code displays each key-value pair in the dictionary. Yes I expected this to happen.




print("rootin ranges")


"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
print("Excercise 1:")
x = range(1, 11)#create a range from 1 to 10
print(list(x))

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
print("Excercise 2:")
x = range(900, 1001, 10)#create a range from 900 to 1000 counting by 10s
print(list(x))
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
print("Excercise 3:")
x = range(1, 101, 9)#create a range from 1 to 100 by 9s
print(list(x))
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
x = range(1, 11)#create a rrange from 1 to 10
sum = 0#create a variable called sum
print("Excercise 4:")
for num in x:#create a for loop to say the range
    sum += num#add each number to the sum
print("The sum is", sum)
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5#create variable for rows
 
for i in range(rows):#create for loop for rows
     for j in range(i + 1):#create for loop for columns
         print('*', end=' ')#print star and end with a space
     print()

# rows = 5
# 
# for i in range(rows):
#     for j in range(i + 1):
#         print('*', end=' ')
#     print()



print("Stock_price")


# Hint: Market conditions are unpredictable - you monitor until something happens
stock_symbol = input("Enter stock symbol: ")
current_price = float(input("Enter starting price: "))
target_price = float(input("Enter target price: "))
stop_loss = float(input("Enter stop-loss price: "))
price_updates = 0
alert_triggered = False
# Think: What approach handles unpredictable market timing?
# Your monitoring logic here

while current_price < target_price: # create a while loop for the variable
     current_price = float(input("Enter starting price: ")) #create multiple if statements to see if the current price is zero(Error), if the currentprice is less than stop_loss(Stop loss hit) or greater than target price(Target hist)
     if current_price == 0:
      print("ERROR")
      break
     if current_price <= stop_loss:
      print("Stop-loss hit")
      break
     if current_price >= target_price:
      print("Target hit")
      break
         








print("Debugging")



"Exercise 1"
temperature = 55

if temperature > 80:
    print("It's hot")
    
elif temperature > 50:
    print("It's temperate")
    
elif temperature < 50 and temperature > 0:
    print("It's a little cold")
    
elif temperature < 0:
    print("It's cold")
"Exercise 2"

text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":#add a space to char for the code to work
       count += 1

print(count)
"Exercise 3"
n = int(input("give me a number: "))

for num in range(1, n):
    if num % 2 == 0:#make the less than sign into ==
        print(num, "is even.")
    else:
        print(num, "is odd.")

"Exercise 4"
num = int(input("Enter an integer: "))

if num < 0:#change -1 into 0
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num):
    result *= i   

  print("Factorial of " + str(num) + " is " +  str(result))
"Exercise 5"

attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:#change incorrect password into correct passsword
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts >= 3:#create greater than or equal sign
        print("Too many attempts")
        break



print("dubious_dates")



"Exercise 1"
temperature = 55

if temperature > 80:
    print("It's hot")
    
elif temperature > 50:
    print("It's temperate")
    
elif temperature < 50 and temperature > 0:
    print("It's a little cold")
    
elif temperature < 0:
    print("It's cold")
"Exercise 2"

text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":#add a space to char for the code to work
       count += 1

print(count)
"Exercise 3"
n = int(input("give me a number: "))

for num in range(1, n):
    if num % 2 == 0:#make the less than sign into ==
        print(num, "is even.")
    else:
        print(num, "is odd.")

"Exercise 4"
num = int(input("Enter an integer: "))

if num < 0:#change -1 into 0
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num):
    result *= i   

  print("Factorial of " + str(num) + " is " +  str(result))
"Exercise 5"

attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:#change incorrect password into correct passsword
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts >= 3:#create greater than or equal sign
        print("Too many attempts")
        break




print("modules")



import os
import os.path
import sys
"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
print("Task 1:")
directory = os.getcwd#create a variable for directory

print("Current working directory:", directory)#print the working directory

"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
print("Task 2:")
print()
print()

# Create a new directory called 'test_folder' if it doesn't already exist
os.makedirs('test_folder', exist_ok=True)

# List all files and directories in the current directory
items = os.listdir('.')

# Print the list
print("Files and directories in current directory:")
for item in items:
    print(item)

print()
print()
print()


"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
print("Task 3:")
print()
print()
# Define the directory name
dir_name = "data"

# Check if the directory exists
if os.path.isdir(dir_name):
    print("Directory already exists.")
else:
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' created.")
"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
print("Task 4:")
filename = "config.txt"#creates a varibale for the filename

file_path = os.path.join(os.getcwd(), filename)#create file path by joining the current working directory and filename

if not os.path.isfile(file_path):#checks if the file is found
    print(f"File found at: {file_path}")
else:
    print("File not found.")

"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print("Task 5:")
print("Python version:", sys.version)#prints the python version

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
print("Task 6:")
platform_ID = sys.platform#creates a vairable for the platform IF
platform = {#creats a dictionary for the platform names
    'linux': 'linux',
    'win32': 'Windows',
    'darwin': 'MacOS',
    'e.g.,': 'e.g.,'
}
print("Platform:", platform.get(platform_ID, f"Unknown ({platform_ID})"))#prints the platform name or unknown



print("randoms")


import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
print()
print("----Task 1------")
print()
for i in range(10):#create for loop to print numbers from 1 to 6 10 times on it's own
    dice = random.randint(1, 6)
    print()
    print(f"Dice number is {dice}")#prints the dic number
"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
print()
print("-----Task 2----")
print()
# Generate 5 random floating-point numbers between 0 and 1
print()
print("0-1")
print()
for i in range(5):#creates a for loop for range
    roll = random.uniform(0,1)#rolls between 0 and 1
    print()
    print(f"roll: {roll}")
    
print()#generate 5 random floating-point numbers between 10 and 20
print("10-20")
print()
for i in range(5):
    roll = random.uniform(10, 20)#rolls between 10 and 29=0
    print()
    print(f"roll: {roll}")
"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
print()
print("----Task 3---")
print()
#make list
my_list = ["red", "blue", "green", "yellow", "purple"]
selected_colors = random.sample(my_list, 3)#makes sure color does not repeat itself
for my_list in selected_colors:
   print()
   print(my_list) #print random color

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
print()
print("----Task 4----")
print()
#make list 1-10
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#shuffle the list
print()
print(my_list)#prints ordinary list
print()
random.shuffle(my_list)
print(my_list)#prints the list
print()




print("contact dictionary")


contact = {}

def display_contact():#helps define the contact
    print("Name\t\tContact Number")
    for name, phone in contact.items():#create a for loop for the format
        print("{}\t\t{}".format(name, phone))

while True:#create while statement for contacts
    try:
        choice = int(input(#create variable for input
            " 1. Add new contact \n"
            " 2. Search contact \n"
            " 3. Display all contacts \n"
            " 4. Edit contact \n"
            " 5. Delete contact \n"
            " 6. Exit \n"
            " Enter Your Choice: "
        ))
    except ValueError:#create an error if not between 1 to 6
        print("Please enter a number between 1 and 6.")
        continue

    if choice == 1:#create if/elif statements for each choice from 1 to 6 and an error statement
        name = input("Enter the contact name: ").strip()
        phone = input("Enter the mobile number: ").strip()
        contact[name] = phone
        print("Contact added.")
    elif choice == 2:
        search_name = input("Enter the contact name: ").strip()#create an input for the search name
        if search_name in contact:
            print(search_name, "'s contact number is", contact[search_name])#create search name input to find input
        else:
            print("Name is not found in contact book.")
    elif choice == 3:
        if not contact:
            print("Empty contact book.")#prints empty if there are no added contacts
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited: ").strip()#creates input to edit the contact
        if edit_contact in contact:
            phone = input("Enter mobile number: ").strip()#edits the mobile number
            contact[edit_contact] = phone
            print("Contact updated.")
            display_contact()
        else:
            print("Name is not found in contact book.")#prints that the number is not found
    elif choice == 5:
        del_choice = input("Enter the contact to delete: ").strip()#delete the contact 
        if del_choice in contact:
            del contact[del_choice]
            print("Contact deleted.")
        else:
            print("Name is not found in contact book.")
    elif choice == 6:
        break#ends the list if the user picks 6(exit)
    else:
        print("Invalid choice. Choose 1-6.")#if user does not pick an integer from 1 to 6




   
   

       
   




print("Functions")


"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""

def my_func(name):
    """
    Making a def function and having an argument for the name
    """
    print("Hello " + name)
    
my_func("James")#make the arguement in the function named james

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def expon_num(n, d):
    """
    Create a def func to make an number multiply by itself multiple times
    """
    return n ** d

x = expon_num(16, 4)#create the arguement for the function and make it 16 to the power of 4

print(x)


"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

def T_N(n):
    """
    Create a def boolean to see if the number is even it is considered true and if odd it turns false
    """
    if n % 2 == 0:#create a if statement to see if the number is even and an else statement if number is odd
        return True
    else:
        return False
    
x = T_N(2)#create the arguement for the function and make it 2

print(x)
        

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def W_L_R(W, L):
    """
    Create a def function to multipky the width with the length to get the are
    """
    return W * L

x = W_L_R(4, 8)#create the arguement for the function and make it 4 width and 8 length
print(x)

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def F_C(C):
    """
    Create a def function to make a equation to make celsius
    """
    return C * 9/5 + 32

x = F_C(14)#create the arguement for the funtion and make it 14 celsius
print(x)
"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
def List(numbers):
    """
    Create def function for a list of numbers
    """
    return sum(numbers) // len(numbers)
x = List([14, 24, 39, 52, 63, 84])#create the arguement for the function and make it a list of numbers
print(x)

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
def P_Q(p, q , discount= 0.0 ):
    """
   Create a def function to make a equation for price and quantity with a discount option

    """

    t = p * q
    a = t * discount
    final_amount = t - a
    return final_amount
x = P_Q(100.0, 5, 0.20)#create the arguement for the function and make the price 100, quantity 5, and discount 20%
print(x)
y = P_Q(100.0, 5)#create the arguement for the function and make the price 100 and quantity 5
print(y)







print("Classical classes")



"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
"""
Create a class called person 
make a def with self, name and age so in the second def we can write what the name and age is for that person
The second def has hi(self so they can make sure the print say hi in the print for every print statement
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def hi(self):
        print("Hi my name is " + self.name + " and your age is " + str(self.age))
person = Person("Jesiah", 16)
person.hi()
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
"""
I created one main class called Animal to create a inheritance for the subclasses.
Also I created two subclasses called Dog and Cat with the inheiritance of Animal.
I created a method called speak(self) so the Cat and Dog can speak for themselves and created prints for both of them.
I created variables for Dog and Cat so I can create .speak so they can say the print in the class.
"""
class Animal:
    species = 'american'
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("Bark!")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
my_dog = Dog()
my_cat = Cat()

my_dog.speak()
my_cat.speak()
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
"""
Create a class called Banklaccount and makes a def for self, owner and balance starting from 0.0
Creates def for deposit and with if and else statements saying if amount is more than 0 than it will add money but if not then will be incsifficant
create def for withdrawl with if, elif and else statements.
Has test at the bottom to make sure it works

"""
class BankAccount:
    def __init__(self, owner, balance=0.0):
        
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"Successful deposit. New balance: ${self.balance:.2f}")
        else:
            print("Amount must be positive")
            
    def withdrawl(self, amount):
        
        if amount <= 0:
            print("Amount must be positive") 
        if amount > self.balance:
            print("Insufficient balence")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. The new balance is: ${self.balance:.2f}")
if __name__ == "__main__":
    account1 = BankAccount("Jerry Roosevelt", 1000.0)
    print(f"Account owner: {account1.owner}, Initial balance: ${account1.balance: .2f}")
    
    account1.deposit(500.0)
    account1.deposit(-100.0)
    
    account1.withdrawl(200.0)
    account1.withdrawl(1500.0)
    account1.withdrawl(-300.0)
    
    account2 = BankAccount("Bob the builder", 100.0)
    print(f"Account owner: {account2.owner}, Initial balance: ${account2.balance: .2f}")
    account2.deposit(750.0)
    account2.withdrawl(100.0)
    
    






print("Errors")









print("trippy testing")