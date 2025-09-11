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
x = input("Enter an integer:") #create variable for integer
x1 = int(x)

y = input("Enter a float:") #create variable for float
y2 = float(y)

addition_result = x1 + y2 #create addition results
subtraction_result = x1 - y2 #create subtraction results
multiplication_result = x1 * y2 #create multiplication results

division_result = x1/y2 #create division resukts

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
x = {
  "bananas": 9,
  "mangos": 4

}
print(x["bananas"])

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""