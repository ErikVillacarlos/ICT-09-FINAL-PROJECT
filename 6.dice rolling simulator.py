import random

def dice_rolling_game():
    while True:
        player1_wins = 0
        player2_wins = 0

        while player1_wins < 2 and player2_wins < 2:
            player1_roll = random.randint(1, 6)
            player2_roll = random.randint(1, 6)

            print(f"Player 1 rolled: {player1_roll}")
            print(f"Player 2 rolled: {player2_roll}")

            if player1_roll > player2_roll:
                print("Player 1 wins this round!")
                player1_wins += 1
            elif player2_roll > player1_roll:
                print("Player 2 wins this round!")
                player2_wins += 1
            else:
                print("It's a tie!")

            print(f"Score - Player 1: {player1_wins}, Player 2: {player2_wins}")

        if player1_wins == 2:
            print("Congratulations! Player 1 won the game!")
        else:
            print("Congratulations! Player 2 won the game!")

        continue_playing = input("Do you want to play again? (yes/no): ").strip().lower()
        if continue_playing != "yes":
            break

dice_rolling_game()