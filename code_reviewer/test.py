
import sys

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

board = [[" ", " ", " "] for _ in range(3)]

players = ["X", "O"]
current_player = players[0]

while True:
    print_board(board)
    try:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            raise ValueError("Invalid move. Please choose a cell within the board limits.")
    except ValueError as e:
        print(str(e))
        continue
    if board[row][col] == " ":
        board[row][col] = current_player
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            sys.exit(0)
        current_player = players[1] if current_player == players[0] else players[0]
    else:
        print("Invalid move. Please choose an empty cell.")
    if all(cell != " " for row in board for cell in row):
        print("It's a tie!")
        sys.exit(0)    
        