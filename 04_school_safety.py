#create an input for the grade
grade = int(input("What is your grade level:"))
#create if statement if the grade is less than or equal to and an else state ment if grade is higher than 10
if grade <= 10:
   print("You cannot not park: ")
else:
   print("You can park: ")

permit = input("do you have a permit (yes/no):").strip()#create variable question if the student has a permit or not

if permit == 'yes' and grade >=11:#create if and else statements to see if the student has a permit and a matching permit number
   parking_spot = str(input("what parking spot are you in:"))
   permit_number = input("whats your permit num:")
else:
   print("You need a parking pass or you will get a parking ticket")

if parking_spot == permit_number:# create if statement to see the time
   parking_time = int(input("what time did you arrive (example 730, 830):"))#create int variable to tell the time
else:
   print("you permit number and parking spot dont match")#create else statement to make the student get a parking pass or they will get a parking ticket

if parking_time >=730:# create if statement to see if the student is on time or too early
   print("you may finally park and get your day started")
else:
   print("your too early, come back later")