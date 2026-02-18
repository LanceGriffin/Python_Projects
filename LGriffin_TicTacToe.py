#Lance Griffin
# 2/22/26
# This is a tic tac toe game that allows the user to play player vs player
# The user will be prompted to enter their move in the format of "row, column" or "row column"

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (row and column): ")
        move = move.replace(',', ' ')
        parts = move.split()
        if len(parts) != 2:
            print("Invalid input. Enter two numbers separated by space or comma.")
            continue
        try:
            row, col = map(int, parts)
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Invalid move. Row and column must be between 1 and 3.")
                continue
            row -= 1
            col -= 1
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                current_player = "O" if current_player == "X" else "X"
                if all(board[i][j] != " " for i in range(3) for j in range(3)):
                    print_board(board)
                    print("It's a tie!")
                    break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers.")
            continue

if __name__ == "__main__":    main()