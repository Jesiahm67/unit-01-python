"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
my_first_list = ["hello", "123", "george", "bye"]
print(my_first_list)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
my_second_list = ["hello"]
my_second_list.append("george")
print(my_second_list)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
my_third_list= ["123", "456", "789"]
my_third_list.remove("123")
print(my_third_list)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
my_fourth_list=["hi","universe", "123"]
my_fourth_list[2] = "$"
print(my_fourth_list)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
my_fifth_list = ["1", "2", "3"]
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
my_sixth_list = ["red", "orange", "yellow"]
del my_sixth_list[0]
print(my_sixth_list)

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
my_seventh_list = ["a", "b", "c"]
new_variable= my_seventh_list[0:2]
print(new_variable)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.

"""
list_1=["a", "b"]
list_2=["c", "d"]
my_eighth_list = list_1 + list_2
print(my_eighth_list)