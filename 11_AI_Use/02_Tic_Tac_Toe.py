"""
Tic Tac Toe Game
Player 1 (X) vs Player 2 (O)
"""

def print_board(board):
    """Display the current game board"""
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")


def check_winner(board, player):
    """Check if the current player has won"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False


def is_board_full(board):
    """Check if the board is full (draw)"""
    return all(cell != " " for row in board for cell in row)


def get_valid_move(board, player):
    """Get a valid move from the player"""
    while True:
        try:
            position = int(input(f"Player {player}, enter position (1-9): "))
            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9!")
                continue
            
            row = (position - 1) // 3
            col = (position - 1) % 3
            
            if board[row][col] != " ":
                print("That position is already taken!")
                continue
            
            return row, col
        except ValueError:
            print("Invalid input! Please enter a number.")


def play_game():
    """Main game loop"""
    # Initialize board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("=" * 30)
    print("   WELCOME TO TIC TAC TOE!    ")
    print("=" * 30)
    print("\nPosition numbers:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    
    # Game loop
    while True:
        print_board(board)
        
        # Get player move
        row, col = get_valid_move(board, current_player)
        board[row][col] = current_player
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! Congratulations!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw! Well played both players.")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"
    
    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again in ["yes", "y"]:
        play_game()
    else:
        print("Thanks for playing! Goodbye!")


if __name__ == "__main__":
    play_game()