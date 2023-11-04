import random

def get_choices():
  player_choice = input("Enter your choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = { "player": player_choice, "computer": computer_choice}
  print(choices)

get_choices()