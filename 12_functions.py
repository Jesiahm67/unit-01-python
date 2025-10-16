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
    
my_func("James")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def expon_num(n, d):
    """
    Create a def func to make an number multiply by itself multiple times
    """
    return n ** d

x = expon_num(16, 4)

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
    if n % 2 == 0:
        return True
    else:
        return False
    
x = T_N(2)

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

x = W_L_R(4, 8)
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

x = F_C(14)
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
x = List([14, 24, 39, 52, 63, 84])
print(x)

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
def P_Q(n, r , discount=0.0):
    t = n * r
    a = t * discount
    f = t - a
    return f
x = P_Q(100.0, 5, 0.20)
print(x)