import random
import lib as Lib


def control_cross(row, column):
    return (
        Lib.check_down_left(board, row, column, N)
        and Lib.check_down_right(board, row, column, N)
        and Lib.check_up_left(board, row, column)
        and Lib.check_up_right(board, row, column, N)
    )

def control_vertical(row, column):
    return Lib.check_vertical(board, row, column, -1, -1) and Lib.check_vertical(board, row, column, N, +1)

def choose_position(row: int):
    while True:
        random_col = random.randint(0, 7)


def solve() -> None:
    for row in range(N):
        choose_position(row=row)


if __name__ == "__main__":
    N = 8
    board = [[0] * N] * N
    solve()
