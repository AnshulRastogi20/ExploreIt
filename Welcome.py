#This is a programme which wil welcom you when you will tell him your name and will also identify your category of age.
name , age = input("Enter your name and age").split('')
print("Welcome" + " " + name)
age = int(age)
if(age >= 13 & age <=19):
 print("You are in teenage")
if(age>19):
 print("You are in adulthood")
if(age<13):
 print("You are in childhood")
