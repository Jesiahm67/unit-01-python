"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
print("Excercise 1:")
choc = ["Hershey", "M&M","Reeses"]#create a list of chocolates
for choc in choc:#create a for loop to say the list
    print(choc)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
print("Excercise 2:")
num = [1,2,3,4,5]#create a list of numbers
sum = 0#create a variable called sum
    
for num in num:#create a for loop to say the list
    sum += num#add each number to the sum
    print("The sum is", sum)
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
print("Excercise 3:")
sentance = "This is a sample sentance"#create sentence
words = sentance.split()#create vairable to split sentance and length
length = []
for word in words:#create a for loop to say the lst
    length.append(len(word))
print("length:", length)
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
print("Excercise 4:")
dictionary = {"name":"Jesiah", "age": 16, "city": "New York", "hobby": "coding"}#create dictionary for jesiah
for key, value in dictionary.items():#create for loop to say the dictionry
    print(f'{key}: {value}')
# The output of the code displays each key-value pair in the dictionary. Yes I expected this to happen.
