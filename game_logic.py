# Initialize the game board
board = [" " for _ in range(9)]
current_player = "X"


# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False


# Function to check for a draw
def check_draw():
    return all(space != " " for space in board)


# Function to handle button clicks
def on_click(index, buttons, update_ui):
    global current_player
    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled", disabledforeground="black")
        if check_winner():
            update_ui(f"Player {current_player} wins!")
            reset_game(buttons)
        elif check_draw():
            update_ui("It's a draw!")
            reset_game(buttons)
        else:
            current_player = "O" if current_player == "X" else "X"


# Function to reset the game
def reset_game(buttons):
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ", state="normal", disabledforeground="#333333")
