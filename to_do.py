my_list = []
print("Your current todo list is: ")#create print to start of the list
print()
while True:
    add = input("Would you like to add or remove a task? ")#create a input to ask the user if they are going to add or remove
    print()
    if add.lower() == "add":#create a if statement if the user says add then they can add on what is on the list
        add_something = input("What task would you like to add to your todo list? ")#asking the user what to add on the list
        print()
        my_list.append(add_something)
        print("Your current to-do list is: ")
        print()
        for x in my_list:#print the updated list
            print(x)
    if add.lower() == "remove":#create a if statement if the user wants to remove a certain item on the list
        remove_something = int(input("which number task would you like to remove? "))#asking what to remove on the list
        print()
        del my_list [remove_something - 1]#removing the normal input minus 1
        print("Your current to-do list is: ")
        print()
        for x in my_list:#print the updated list
            print(x)