print(len("Hello"))
#Subscripting
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[-1])

#String
print("123"+"345")
#Integer
print(123+345)

#For Large Numbers:
print(12_34_56_789)

#Float
print(3.14159)

#Boolean
print(True)
print(False)
print(len("12345"))

#How to Check DataType

print(type("Hello"))
print(type(123))
print(type(123.56))
print(type(True))


#Type Casting

print("123"+"456")
print(int("123")+int("456"))
print()
print("Number of letters in your name: " + str(len(input("Enter your name "))))
print("My age: " + str(12))

#Operators

print(123+456)
print(10-8)
print(7*4)
print(10/5)
print(10//5) # // - does division and then simply removes all decimals
print(5//3)
print(2**8) # 2^8

#PEMDASLR RULE

# ()
# **
# * OR / | ( left --> right )
# + OR - | ( left --> right )

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi)) # removes decimals
print(round(bmi)) # rounds off the digits
print(round(bmi,2)) # rounds off to 2 decimals

#Assignment Operator
# +=
# -=
# *=
# /=

score = 60
score +=1
print(score)
score = 60
score -=1
print(score)
score = 60
score *=2
print(score)
score = 60
score /=3
print(score)

# f-String

print("Your Score is: " + str(score))
#or
print(f"Your Score is: {score}")

# Tip Calculator :-

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? Rs: "))
tip = int(input("What percentage tip would you like to give? 10,12,15: "))
people = int(input("How many people to split the bill?: "))

total_bill = bill + ((tip/100)*bill)
to_pay = total_bill / people

print(f"Each Person Should Pay: Rs {round(to_pay,2)}")
