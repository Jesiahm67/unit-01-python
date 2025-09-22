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