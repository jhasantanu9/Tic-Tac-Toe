from random import randrange

def print_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def initialize_board():
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

def user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] in ['O', 'X']:
                    print("This square is already taken. Try again.")
                else:
                    board[row][col] = 'O'
                    break
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board):
    while True:
        move = randrange(1, 10)
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] not in ['O', 'X']:
            board[row][col] = 'X'
            break

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell in ['O', 'X'] for row in board for cell in row)

def main():
    board = initialize_board()
    print_board(board)

    for _ in range(4):  # The game has at most 4 moves per player
        user_move(board)
        print_board(board)

        if is_winner(board, 'O'):
            print("You won!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        computer_move(board)
        print_board(board)

        if is_winner(board, 'X'):
            print("Computer won!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
