# Rock, Paper, Scissors

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

import random

choices = [rock, paper, scissors]

player_choice = int(input("Choose between 0 for rock, 1 for paper, or 2 for scissors --> "))

if player_choice < 0 or player_choice >= 3:
    print("Invalid number. Try again!")
else:
    print("You chose: ")
    print(choices[player_choice])
    
    print("Computer chose")
    computer_choice = random.randint(0, 2)
    print(choices[computer_choice])
    
    if player_choice == computer_choice:
        print("It's a draw.")
    elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
        print("You won!")
    else:
        print("You lost!")

