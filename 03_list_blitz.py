"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
my_first_list = ["hello", "123", "george", "bye"]#create variable for first list
print(my_first_list)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
my_second_list = ["hello"]#create variable for second list 
my_second_list.append("george")#add new value to second list
print(my_second_list)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
my_third_list= ["123", "456", "789"]#create variable for third list
my_third_list.remove("123")#remove vlure from old list
print(my_third_list)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
my_fourth_list=["hi","universe", "123"]#create variable for fourth list
my_fourth_list[2] = "$"#create value to replace the third value that starts at 0 to 2
print(my_fourth_list)
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
my_fifth_list = ["1", "2", "3"]#create variable for fifth list
my_fifth_list.append("4")#create append to add more values to the list
my_fifth_list.append("5")
my_fifth_list.append("6")
print(my_fifth_list)
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
my_sixth_list = ["red", "orange", "yellow"]#create variable for sixth list with three values
del my_sixth_list[0]#create del function to delete value from list from 0 to 2
print(my_sixth_list)

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
my_seventh_list = ["a", "b", "c"]#create variable for seventh list 
new_variable= my_seventh_list[0:2]#create new variable to copy the first 2 values in the old variable
print(my_seventh_list)
print(new_variable)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.

"""
list_1=["a", "b"]#create 2 variables for the eigth list
list_2=["c", "d"]
my_eighth_list = list_1 + list_2#create variable for eigth list to combine both recent lists
print(list_1)
print(list_2)
print(my_eighth_list)