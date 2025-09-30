my_list = []
index = 0

print("Welcome to your list")

while True:
    list=input("Would you like to add or remove: ")
    
    if list == "add":
        my_list.append(input("What would you want to add: "))
    if list == "remove":
        index= int("What would you want to remove")
        del my_list[index-1]    
