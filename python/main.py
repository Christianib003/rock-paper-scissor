import random

def get_choices():
  player_choice = input("Enter your choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = { "player": player_choice, "computer": computer_choice}
  return choices

def check_win(player_choice, computer_choice):
  print(f"You chose {player_choice}, and Computer chose {computer_choice}.")
  if player_choice == computer_choice:
    return("It's a tie!")
  
  elif player_choice == "rock":
    if computer_choice == "scissors":
      return("Rock smashes scissors. You win! :)")
    else:
      return("Paper covers rock. You lose. :(")

  elif player_choice == "paper":
    if computer_choice == "rock":
      return("Paper covers rock. You win! :)")
    else:
      return("Scissors cuts paper. You lose. :(")

  elif player_choice == "scissors":
    if computer_choice == "paper":
      return("Scissors cuts paper. You win! :)")
    else:
      return("Rock smashes paper. You lose. :(")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)