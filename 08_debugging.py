"Exercise 1"

text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":#add a space to char for the code to work
       count += 1

print(count)
"Exercise 2"
n = int(input("give me a number: "))

for num in range(1, n):
    if num % 2 == 0:#make the less than sign into ==
        print(num, "is even.")
    else:
        print(num, "is odd.")

"Exercise 3"
num = int(input("Enter an integer: "))

if num < 0:#change -1 into 0
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num):
    result *= i   

  print("Factorial of " + str(num) + " is " +  str(result))
"Exercise 4"

attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == correct_password:#change incorrect password into correct passsword
        print("Correct password!")
        break
    else:
        print("Incorrect password")

    if attempts >= 3:#create greater than or equal sign
        print("Too many attempts")
        break
