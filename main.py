import random

def get_choices():
  player_choice = input("Enter your choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = { "player": player_choice, "computer": computer_choice}
  print(choices)

def check_win(player_choice, computer_choice):
  print("You chose " + player_choice + ", And Computer chose " + computer_choice)
  if (player_choice == computer_choice):
    return "It's a tie!"