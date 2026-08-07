# if <condition>:
#     do this       <--- indented block of code
# else:
#     do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Yes, You Can Ride!!")
else:
    print("Sorry! You Can't Ride.")

# example:
water_level = int(input("What is the Water Level (in cm): "))
if water_level >= 80 :
    print("Drain Water From the Tub")
else:
    print("Continue Filling the Tub")

# = --> for Assignment
# == --> for checking Condition

value = int(input("Enter Value: "))
if value == 100:
    print("Your Value is 100!")
else:
    print("Your Value is not 100")


# / --> used for division
# % --> used for getting Remainder

print(10/2)
print(10%2)
print(10%3)

# Odd - Even Number Predictor

number = int(input("Type Your Number: "))
if number%2 == 1:
    print("Your Number is Odd!")
else:
    print("Your Number is Even!")



print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: "))
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your Age?: "))
    if age > 18 :
        print("Ticket Price is Rs 12")
    elif age < 18 and age > 12 :
        print("Ticket Price is Rs 7")
    else:
        print("Ticket Price is Rs 5")
else:
    print("Sorry you have to grow taller before you can ride.")

# Score Analysis

maths_score = int(input("How Many Marks in Maths?: "))
english_score = int(input("How Many Marks in English?: "))
if maths_score >= 90:
    if english_score >= 90:
        print("You Are Going Well In Both Subjects")
    else:
        print("You Are Going Well In Maths")
else:
    print("You Ain't Going Well :( ")

# Rollar Coster With Picture Ticket

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child Tickets Are Rs 5.")
    elif age <= 18:
        bill = 7
        print("Teen Tickets Are Rs 7.")
    else:
        bill = 12
        print("Adult Tickets Are Rs 12.")
    want_ticket = input("Do You Want Ticket? (yes or no): ")
    if want_ticket == "yes":
        bill += 3
        print(f"Total Ticket Cost is Rs {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")

# Python Pizza Deliveries 

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
    print("Small Pizza Will Cost you Rs 15")
elif size == "M":
    bill = 20
    print("Medium Pizza Will Cost you Rs 20")
elif size == "L":
    bill = 25
    print("Large Pizza Will Cost you Rs 25")
else:
    bill = 0
    print("Wrong Input")

if pepperoni == "Y":
    bill += 3
    print("Pepperoni Will Cost you Extra Rs 3")
if extra_cheese == "Y":
    bill += 1
    print("Cheese Will Cost you Extra Rs 1")
print(f"Your final bill is: Rs{bill}.")


# Logical Operator:

# And (True and True --> True ; else False)
# Or (True or False ---> True ; False or True ---> True ; True or True --> True : False or False --> False )
# Not (Not True --> False ; Not False --> True)

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12 :
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Free Ride on Us")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

