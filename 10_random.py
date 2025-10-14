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