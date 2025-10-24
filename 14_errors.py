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
        print("Cannot divide by zero")
# Example usage:
divide_numbers(10, 0)


"""
Example 2: Opening Files
"""

def read_file(filename):
    try:
        file = open(filename, 'r')
    except:
        print("No such thing as file")
    try:
        contents = file.read()
    except:
        print("Variale File is found before assignment")
    try:
        print("File contents:", contents)
    except:
        print("Variable contents is found before assignment")
    try:
        file.close()
    except:
        print("Variable file is found before assignment")
# Example usage:
read_file("nonexistent.txt")
"""

Example 3: List Items
"""

def get_item(lst, index):
    try:
      item = lst[index]
    except:
        print("Variable not found")
    try:
      print("Item:", item)
    except:
        print("Index error")

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)

"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    try:
        value = dictionary[key]
    except:
        print("Key error")
    try: 
        print("Value:", value)
    except:
        print("Unbound error: variable before assignment")

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")
"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
        try:
            with open(filename, 'r') as file:
                contents = file.read()
                print("File contents:", contents)
                
        except FileNotFoundError:
            print("Error: File not found.")
        else:
            print("File filed successfuly")
        finally:
            print("File processing complete")
# Example usage:
process_file("example.txt")
