import random

# write 'hello world' to the console 
print('hello world')

# create python minigame with the following rules: 
# -Rock beats Scissors, 
# -Scissors beats Paper, 
# -Paper beats Rock

# Consider the following in the game interactions:
# - the game should a multiplayer game
# - the game should be able to handle multiple rounds
# - the computer will the opponent and can randomly choose one of the elements (Rock, Paper, Scissors) for each move, just like your human opponent
# - your interaction in the game will be through the console
# - the player can choose one of the three options (Rock, Paper, Scissors) and should be warned if they enter an invalid option
# - at each round, the player must enter one of the options in the list and be informed if they won, lost, or if it was a tie
# - by the end of each round, the player can choose whether to continue playing or not
# - display the player's score at the end of each round
# - the minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid
# - the game should be able to handle multiple rounds 

def play_round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def get_player_choice():
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def play_game():
    player_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"Round {round_number}")
        player_choice = get_player_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = play_round(player_choice, computer_choice)
        print(f"You chose {player_choice}. The computer chose {computer_choice}. {result}")

        if result == "You win!":
            player_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

        round_number += 1

play_game()
