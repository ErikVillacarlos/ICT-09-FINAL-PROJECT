import random

def rock_paper_scissors():
    while True:
        options = ["rock", "paper", "scissors"]
        player_wins = 0
        computer_wins = 0

        while player_wins < 2 and computer_wins < 2:
            computer_choice = random.choice(options)
            player_choice = input("Enter rock, paper, or scissors: ").strip().lower()
            
            if player_choice not in options:
                print("Invalid choice! Try again.")
                continue

            print(f"Computer chose: {computer_choice}")
            
            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper"):
                print("You win this round!")
                player_wins += 1
            else:
                print("Computer wins this round!")
                computer_wins += 1

            print(f"Score - You: {player_wins}, Computer: {computer_wins}")

        if player_wins == 2:
            print("Congratulations! You won the game!")
        else:
            print("Sorry! The computer won the game.")
        
        continue_playing = input("Do you want to play again? (yes/no): ").strip().lower()
        if continue_playing != "yes":
            break

rock_paper_scissors()