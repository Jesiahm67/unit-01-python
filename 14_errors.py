"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try:
       result = num1 / num2
       print("Result:", result)
    except:
        print("")
# Example usage:
divide_numbers(10, 2)


"""
Example 2: Opening Files
"""

def read_file(filename):
    try:
        file = open(filename, 'r')
    except:
        print("")
    contents = file.read()
    try:
        print("File contents:", contents)
    except:
        print()
    file.close()

# Example usage:
read_file("nonexistent.txt")
