contact = {}

def display_contact():#helps define the contact
    print("Name\t\tContact Number")
    for name, phone in contact.items():#create a for loop for the format
        print("{}\t\t{}".format(name, phone))

while True:#create while statement for contacts
    try:
        choice = int(input(#create variable for input
            " 1. Add new contact \n"
            " 2. Search contact \n"
            " 3. Display all contacts \n"
            " 4. Edit contact \n"
            " 5. Delete contact \n"
            " 6. Exit \n"
            " Enter Your Choice: "
        ))
    except ValueError:#create an error if not between 1 to 6
        print("Please enter a number between 1 and 6.")
        continue

    if choice == 1:#create if/elif statements for each choice from 1 to 6 and an error statement
        name = input("Enter the contact name: ").strip()
        phone = input("Enter the mobile number: ").strip()
        contact[name] = phone
        print("Contact added.")
    elif choice == 2:
        search_name = input("Enter the contact name: ").strip()#create an input for the search name
        if search_name in contact:
            print(search_name, "'s contact number is", contact[search_name])#create search name input to find input
        else:
            print("Name is not found in contact book.")
    elif choice == 3:
        if not contact:
            print("Empty contact book.")#prints empty if there are no added contacts
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited: ").strip()#creates input to edit the contact
        if edit_contact in contact:
            phone = input("Enter mobile number: ").strip()#edits the mobile number
            contact[edit_contact] = phone
            print("Contact updated.")
            display_contact()
        else:
            print("Name is not found in contact book.")#prints that the number is not found
    elif choice == 5:
        del_choice = input("Enter the contact to delete: ").strip()#delete the contact 
        if del_choice in contact:
            del contact[del_choice]
            print("Contact deleted.")
        else:
            print("Name is not found in contact book.")
    elif choice == 6:
        break#ends the list if the user picks 6(exit)
    else:
        print("Invalid choice. Choose 1-6.")#if user does not pick an integer from 1 to 6




   
   

       
   