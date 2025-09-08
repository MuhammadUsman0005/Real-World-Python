import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player_choice = None

    while player_choice not in choices:
        player_choice = input("rock, paper or scissors: ").lower()
    if computer == player_choice:
        print("Computer: ",computer)
        print("Player: ",player_choice)
        print("TIE!")
    elif player_choice == "rock":
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player_choice)
            print("YOU LOSE!")
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player_choice)
            print("YOU WIN!")
    elif player_choice == "paper":
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player_choice)
            print("YOU LOSE!")
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player_choice)
            print("YOU WIN!")
    elif player_choice == "scissors":
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player_choice)
            print("YOU LOSE!")
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player_choice)
            print("YOU WIN!")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("BYE!")