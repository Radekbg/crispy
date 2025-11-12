import random

print("Make your choice by typing rock, paper or scissors followed by enter: \n")
user_choice = input()
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
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

if user_choice == "rock" and computer_choice == "rock":
    print(rock, rock, "Even, try again!")
elif user_choice == "rock" and computer_choice == "paper":
    print(rock, paper, "Paper beats Rock! You lose!")
elif user_choice == "rock" and computer_choice == "scissors":
    print(rock, scissors, "Rock beats scissors! You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print(paper, rock, "Paper beats rock! You win!")
elif user_choice == "paper" and computer_choice == "paper":
    print(paper, paper, "Even, try again!")
elif user_choice == "paper" and computer_choice == "scissors":
    print(paper, scissors, "Scissors beat paper! You lose!")
elif user_choice == "scissors" and computer_choice == "scissors":
    print(scissors, scissors, "Even, try again!")
elif user_choice == "scissors" and computer_choice == "paper":
    print(scissors, paper, "Scissors beat paper! You win!")
elif user_choice == "scissors" and computer_choice == "rock":
    print(scissors, rock, "Rock beats scissors! You lose!")
else: 
    print("Try again with valid input!")
