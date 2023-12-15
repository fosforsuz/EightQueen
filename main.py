import random
import lib as Control
import numpy as np
import time


def control_cross(row, column):
    return (
            Control.check_down_left(board, row, column, N)
            and Control.check_down_right(board, row, column, N)
            and Control.check_up_left(board, row, column)
            and Control.check_up_right(board, row, column, N)
    )


def control_vertical(row, column):
    return Control.check_vertical(board, row, column, -1, -1) and Control.check_vertical(board, row, column, N, +1)


def choose_position(row: int):
    for _ in range(2_000_000):
        random_col = random.randint(0, N - 1)
        if control_cross(row, random_col) and control_vertical(row, random_col):
            return [row, random_col]

    return [-1, -1]


def print_board():
    print("*" * 50)
    for row in board:
        print(row)


def solve() -> None:
    for row in range(N):
        quuen_index = choose_position(row=row)
        if quuen_index == [-1, -1]:
            continue
        queen_indexes.append(quuen_index)
        board[quuen_index[0]][quuen_index[1]] = 1
        print_board()


if __name__ == "__main__":
    N = 8
    board = np.zeros((N, N))
    queen_indexes = []
    solve()
    print("\n")
    print("==" * 30)
    if len(queen_indexes) != 8:
        print("No Solution Found")
    else:
        print_board()
        print("")
        print(queen_indexes)
