import random
print("Welcome To Rock🪨 Paper📃 Scissor✂️ Python🐍 Game !!!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = ["rock","paper","scissors"]
user_choice = input("r-->Rock\np-->Paper\ns-->Scissors\nGive Your Call: ").lower()
if user_choice == "r":
    print(f"You Choose🙋‍♂️🙋‍♂️: {rock}")
    print("Rock!")
elif user_choice == "p":
    print(f"You Choose🙋‍♂️🙋‍: {paper}")
    print("Paper!")
elif user_choice == "s":
    print(f"You Choose🙋‍♂️🙋‍: {scissors}")
    print("Scissors!")
else:
    print("Wrong Input!!")

pc_choice = random.choice(options)
if pc_choice == "rock":
    print(f"Computer Chooses💻💻🖥️🖥️: {rock}")
    print("Rock!")
elif pc_choice == "paper":
    print(f"Computer Chooses💻💻🖥️🖥️: {paper}")
    print("Paper!")
elif pc_choice == "scissors":
    print(f"Computer Chooses💻💻🖥️🖥️: {scissors}")
    print("Scissors!")
else:
    print("PC Choice Error!!")
user_score = 0
computer_score = 0
if user_choice == "r" and pc_choice == "rock":
    print("Its A Draw !!")
    user_score += 0
    computer_score += 0
    print(f"Your Score: {user_score} , Computer Score: {computer_score}")
elif user_choice == "p" and pc_choice == "paper":
    print("Its A Draw !!")
    user_score += 0
    computer_score += 0
    print(f"Your Score: {user_score} , Computer Score: {computer_score}")
elif user_choice == "s" and pc_choice == "scissors":
    print("Its A Draw !!")
    user_score += 0
    computer_score += 0
    print(f"Your Score: {user_score} , Computer Score: {computer_score}")
elif user_choice == "r" and pc_choice == "paper":
    print("Computer Wins !!")
    user_score += 0
    computer_score += 1
    print(f"Your Score: {user_score} , Computer Score: {computer_score}")
elif user_choice == "r" and pc_choice == "scissors":
    print("You Win !!")
    user_score += 1
    computer_score += 0
    print(f"Your Score: {user_score} , Computer Score: {computer_score}")
elif user_choice == "p" and pc_choice == "rock":
    print("You Win !!")
    user_score += 1
    computer_score += 0
    print(f"Your Score: {user_score} , Computer Score: {computer_score}")
elif user_choice == "p" and pc_choice == "scissors":
    print("Computer Wins !!")
    user_score += 0
    computer_score += 1
    print(f"Your Score: {user_score} , Computer Score: {computer_score}")
elif user_choice == "s" and pc_choice == "rock":
    print("Computer Wins !!")
    user_score += 0
    computer_score += 1
    print(f"Your Score: {user_score} , Computer Score: {computer_score}")
elif user_choice == "s" and pc_choice == "paper":
    print("You Win !!")
    user_score += 1
    computer_score += 0
    print(f"Your Score: {user_score} , Computer Score: {computer_score}")
else:
    print("Score Error!")
