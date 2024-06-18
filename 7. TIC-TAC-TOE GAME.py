def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["Player 1", "Player 2"]
    symbols = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        print(f"{players[current_player]}'s turn ({symbols[current_player]})")
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = symbols[current_player]
            if check_win(board, symbols[current_player]):
                print_board(board)
                print(f"Congratulations! {players[current_player]} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = (current_player + 1) % 2
        else:
            print("Invalid move! Try again.")

play_game()
