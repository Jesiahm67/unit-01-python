num_one = float(input("Type a number: "))#create float variables for the first and second numbers
num_two = float(input("Type a second number: "))
print("1.Addidtion")
print()
print("2.Substraction")
print()
print("3.Multiplication")
print()
print("4.Division")
print()
print("5.Exponents")
print()
print("6.Remainder")
print()
print("7.Floor Division")
print()

user = int(input("Pick a number any number: "))#create variable to pick an operation

if user > 7:#create if statement if the operation number is higher than 7
    print("Invalid number")

if user == 1:#create if statements for each operation
    print(num_one + num_two)
    
if user == 2:
    print(num_one - num_two)
    
if user == 3:
    print(num_one * num_two)
    
if user == 4:
    if num_two == 0:#create nested if statement if the denominater is 0 and giveds an error
        print("Error")
    else:
        print(num_one/num_two)
    
if user == 5:
    print(num_one**num_two)
    
if user == 6:
    
    if num_two == 0 or num_one == 0:
        print("Error")
    else:
        print(num_one%num_two)
        
if user == 7:
    if num_two == 0 or num_one == 0:
        print("Error")
    else:
     print(num_one//num_two)

