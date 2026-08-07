print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Good Luck!")

user_choice = input("Choose Left or Right: ").strip().lower()

if user_choice == "left":
    print("You came across a river!")
    user_choice_02 = input("Choose Swim or Wait for the Boat: ").strip().lower()

    if user_choice_02 == "swim":
        print("Game Over! Sharks ate you!")
    elif user_choice_02 == "wait":
        print("A boat arrived and took you to the other side of the river.")
        user_choice_03 = input("Choose a door (Red, Blue, Yellow): ").strip().lower()

        if user_choice_03 == "red":
            print("Wrong door chosen! You were burnt by fire!")
        elif user_choice_03 == "blue":
            print("Wrong door chosen! You were eaten by a lion!")
        elif user_choice_03 == "yellow":
            print("Congratulations! You found the treasure! 🪙🪙💰💰")
        else:
            print("Wrong input! Try again.")
    else:
        print("Wrong input! Try again.")
elif user_choice == "right":
    print("Game Over! You fell into a hole.")
else:
    print("Wrong input! Try again.")
