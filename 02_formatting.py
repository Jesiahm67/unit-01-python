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