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