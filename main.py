import random

def get_choices():
  player_choice = input("Enter your choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = { "player": player_choice, "computer": computer_choice}
  print(choices)

def check_win(player_choice, computer_choice):
  print(f"You chose {player_choice}, and Computer chose {computer_choice}.")
  if (player_choice == computer_choice):
    return "It's a tie!"

check_win("rock", "rock")