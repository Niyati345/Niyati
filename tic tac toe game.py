def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")


# Function to check if a player has won
def check_win(board, mark):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [2, 5, 8], [3, 5, 8],  # columns
        [0, 5, 8], [2, 4, 7]  # diagonals
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True
    return False


# Function to check draw
def is_draw(board):
    return " " not in board


# Main game loop
def play_game():
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Enter positions 1–9 to place your X or O.")
    display_board(board)

    while True:
        print(f"Player {current_player}'s turn.")

        try:
            move = int(input("Choose a position (1-9): ")) - 1
        except:
            print("Invalid input. Enter a number from 1–9.")
            continue

        if move not in range(9):
            print("Position out of range. Try again.")
            continue

        if board[move] != " ":
            print("Position already taken. Try another.")
            continue

        board[move] = current_player
        display_board(board)

        if check_win(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


# Start the game
play_game()