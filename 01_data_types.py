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