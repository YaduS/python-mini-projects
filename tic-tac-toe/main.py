import math
from itertools import chain

X_INPUT = "X"
O_INPUT = "O"
EMPTY = " "


board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
current_player = X_INPUT


def check_winner():

    winner = None
    draw_status = False

    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            winner = board[i][0]
            break

        # check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            winner = board[0][i]
            break
    if winner:
        return draw_status, winner

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != EMPTY:
        winner = board[0][0]
    elif board[2][0] == board[1][1] == board[0][2] and board[1][1] != EMPTY:
        winner = board[0][0]

    # check for draw
    else:
        all_entries = chain.from_iterable(board)
        if EMPTY not in all_entries:
            draw_status = True

    return draw_status, winner


def print_board():
    for i in range(3):
        print(f"\n {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i != 2:
            print("___________\n")
        else:
            print("\n")


def update_board(choice: int):

    global current_player
    # global board

    row = math.ceil(choice / 3) - 1
    column = choice % 3 - 1
    print(row)
    print(column)
    if board[row][column] != EMPTY:
        print("invalid position")
    else:
        board[row][column] = current_player
        current_player = X_INPUT if current_player == O_INPUT else O_INPUT


def main():
    draw, winner = False, None
    while not draw and not winner:
        print_board()
        print(f"Current player: {current_player}")
        choice = int(input("Enter the position (1 to 9): "))
        update_board(choice)
        draw, winner = check_winner()

    if draw:
        print("game is a draw!")
    elif winner:
        print_board()
        print(f"{winner} is the winner")


if __name__ == "__main__":
    main()
