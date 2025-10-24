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
        print("Cannot divide by zero")#create except statement to catch division by zero error
# Example usage:
divide_numbers(10, 0)


"""
Example 2: Opening Files
"""

def read_file(filename):
    try:
        file = open(filename, 'r')
    except:
        print("No such thing as file")#create except statement to say file not found
    try:
        contents = file.read()
    except:
        print("Put variable at top")#create except statement to say variable file is found before assignment
    try:
        print("File contents:", contents)
    except:
        print("Put variable at top")#create except statement to say variable contents is found before assignment
    try:
        file.close()
    except:
        print("file is not defined")#create except statement to say variable file is not defined
read_file("nonexistent.txt")
"""

Example 3: List Items
"""

def get_item(lst, index):
    try:
      item = lst[index]
    except:
        print("Variable not found")#create except statement to say variable item is not found
    try:
      print("Item:", item)
    except:
        print("Index error")#create except statement to say index is out of range

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
        print("Key error")#create except statement to say key is not found
    try: 
        print("Value:", value)
    except:
        print("Unbound error: variable before assignment")#create except statement to say variable value is not assigned

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")
"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
        try:#create try block to open file
            with open(filename, 'r') as file:
                contents = file.read()
                print("File contents:", contents)
                
        except FileNotFoundError:
            print("Error: File not found.")#create except statement to say file is not found
        else:
            print("File filed successfuly")#create else statement to say file opened successfully
        finally:
            print("File processing complete")#create finally statement to say file processing is complete
# Example usage:
process_file("example.txt")
