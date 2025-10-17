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
