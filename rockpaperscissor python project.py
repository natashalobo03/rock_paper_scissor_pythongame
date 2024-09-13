import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#rock :0 , paper :1,scissor :2
ascii_images = [Rock, Paper, Scissors]

userInput = int(
    input(
        "What do you choose? Type 0 for Rock ,1 for paper or 2 for scissors.\n"
    ))
print(ascii_images[userInput])

computer_choice = random.randint(0, 2)
print("Computer choice:")
print(ascii_images[computer_choice])
if userInput >= 3 or userInput < 0:
    print("You typed an invalid number , you loose!")
elif userInput == 0 and computer_choice == 2:
    print("You win!")
elif userInput == 2 and computer_choice == 0:
    print("You loose!")
elif computer_choice > userInput:
    print("You loose!")
elif computer_choice < userInput:
    print("You win!")
elif computer_choice == userInput:
    print("It's a tie!")
