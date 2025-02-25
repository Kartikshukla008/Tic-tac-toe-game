import random

# Initialize the Tic-Tac-Toe board
def initialize_board():
    return [" " for _ in range(9)]

# Display the board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Check for a win
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check for a draw
def check_draw(board):
    return " " not in board

# Get player move with input validation
def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Basic AI opponent (random move)
def get_ai_move(board):
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(available_moves)

# Main game loop
def play_game():
    board = initialize_board()
    current_player = "X"
    mode = input("Choose mode: (1) Single Player vs AI or (2) Two Players: ")

    while True:
        display_board(board)

        if mode == "1" and current_player == "O":
            print("AI's turn...")
            move = get_ai_move(board)
        else:
            move = get_player_move(board, current_player)

        board[move] = current_player

        if check_win(board, current_player):
            display_board(board)
            if mode == "1" and current_player == "O":
                print("AI wins! Better luck next time.")
            else:
                print(f"Player {current_player} wins! Congratulations!")
            break

        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()