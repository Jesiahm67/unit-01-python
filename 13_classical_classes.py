
"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
"""
Create a class called person 
make a def with self, name and age so in the second def we can write what the name and age is for that person
The second def has hi(self so they can make sure the print say hi in the print for every print statement
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        str(self.age) = age
    
    
    def hi(self):
        print("Hi my name is " + self.name + "")
person = Person("Jesiah", 16)
person.hi()
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
"""
I created one main class called Animal to create a inheritance for the subclasses.
Also I created two subclasses called Dog and Cat with the inheiritance of Animal.
I created a method called speak(self) so the Cat and Dog can speak for themselves and created prints for both of them.
I created variables for Dog and Cat so I can create .speak so they can say the print in the class.
"""
class Animal:
    species = 'american'
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        print("Bark!")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
my_dog = Dog()
my_cat = Cat()

my_dog.speak()
my_cat.speak()
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
"""
Create a class called Banklaccount and makes a def for self, owner and balance starting from 0.0
Creates def for deposit and with if and else statements saying if amount is more than 0 than it will add money but if not then will be incsifficant
create def for withdrawl with if, elif and else statements.
Has test at the bottom to make sure it works

"""
class BankAccount:
    def __init__(self, owner, balance=0.0):
        
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"Successful deposit. New balance: ${self.balance:.2f}")
        else:
            print("Amount must be positive")
            
    def withdrawl(self, amount):
        
        if amount <= 0:
            print("Amount must be positive") 
        if amount > self.balance:
            print("Insufficient balence")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. The new balance is: ${self.balance:.2f}")
if __name__ == "__main__":
    account1 = BankAccount("Jerry Roosevelt", 1000.0)
    print(f"Account owner: {account1.owner}, Initial balance: ${account1.balance: .2f}")
    
    account1.deposit(500.0)
    account1.deposit(-100.0)
    
    account1.withdrawl(200.0)
    account1.withdrawl(1500.0)
    account1.withdrawl(-300.0)
    
    account2 = BankAccount("Bob the builder", 100.0)
    print(f"Account owner: {account2.owner}, Initial balance: ${account2.balance: .2f}")
    account2.deposit(750.0)
    account2.withdrawl(100.0)