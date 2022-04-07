import random

while True: # new
    user_action = int(input("Enter a choice \n 1- rock\n 2- paper\n 3- scissors \n "))
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    if user_action == 1 :  print(f"\nYou choose rock, computer choose {computer_action}.\n")
    if user_action == 2 :  print(f"\nYou choose paper, computer choose {computer_action}.\n")
    if user_action == 3 :  print(f"\nYou choose scissors, computer choose {computer_action}.\n")

    if possible_actions[user_action - 1] == computer_action:
        print(f"Both players selected {possible_actions[user_action - 1]}. It's a tie!")
    elif possible_actions[user_action - 1] == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif possible_actions[user_action - 1] == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif possible_actions[user_action - 1] == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ") # new
    if play_again.lower() != "y": # new
        break # new