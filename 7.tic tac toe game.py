
def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" | ")
        print()

def check_win(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]!= " ":
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]!= " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]!= " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]!= " ":
        return True
    # If no one has won
    return False

def play_game():
    while True:
        board = [[" " for j in range(3)] for i in range(3)]
        
        # Get player names
        player1 = input("Enter name for Player 1 (X): ")
        player2 = input("Enter name for Player 2 (O): ")
        
        player = player1
        while True:
            print_board(board)
            print(f"{player}'s turn")
            row = int(input("Enter the row (1-3): ")) - 1
            col = int(input("Enter the column (1-3): ")) - 1
            
            if board[row][col] == " ":
                board[row][col] = "X" if player == player1 else "O"
                if check_win(board):
                    print_board(board)
                    print(f"{player} wins!")
                    break
                elif all(board[i][j]!= " " for i in range(3) for j in range(3)):
                    print_board(board)
                    print("It's a draw!")
                    break
                else:
                    player = player2 if player == player1 else player1
            else:
                print("Invalid move, try again.")
        
        # Ask players if they want to continue playing
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

play_game()


### Explanation:

