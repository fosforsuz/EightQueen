
def  check_up_left(board, row, column):
    if board[row][column] == 1:
        return False
    
    if row > 0 and column > 0:
        return check_up_left(board=board, row=row-1, column=column-1)
    
    return True

def check_up_right(board, row, column, limit):
    if board[row][column] == 1:
        return False
    
    if row < limit and column > 0:
        return check_up_right(board=board, row=row+1, column=column-1, limit=limit)

    return True

def check_down_left(board, row, column, limit):
    if board[row][column] == 1:
        return False
    
    if row < limit and column > 0:
        return check_down_left(board=board, row=row+1, column=column-1, limit=limit)
    
    return True

def check_down_right(board, row, column, limit):
    if board[row][column] == 1:
        return False
    
    if row < limit and column < limit:
        return check_down_right(board=board, row=row+1, column=column+1, limit=limit)
    
    return True

def  write_up_left(board, row, column):
    if board[row][column] == 1:
        return False
    
    if row > 0 and column > 0:
        board[row][column] = 1
        return write_up_left(board=board, row=row-1, column=column-1)
    
    return True

def write_up_right(board, row, column, limit):
    if board[row][column] == 1:
        return False
    
    if row < limit and column > 0:
        board[row][column] = 1
        return write_up_right(board=board, row=row+1, column=column-1, limit=limit)

    return True

def write_down_left(board, row, column, limit):
    if board[row][column] == 1:
        return False
    
    if row < limit and column > 0:
        board[row][column] = 1
        return write_down_left(board=board, row=row+1, column=column-1, limit=limit)
    
    return True

def write_down_right(board, row, column, limit):
    if board[row][column] == 1:
        return False
    
    if row < limit and column < limit:
        board[row][column] = 1
        return write_down_right(board=board, row=row+1, column=column+1, limit=limit)
    
    return True

def check_vertical(board, row, column, limit, value):
    if board[row][column] == 1:
        return False
    
    if column != limit:
        return check_vertical(board=board, row=row, column=column+value, limit=limit, value=value)

    return True


def write_vertical(board, row, column, limit, value):
    if board[row][column] == 1:
        return False
    
    if column != limit:
        board[row][column] = 1
        return write_vertical(board=board, row=row, column=column+value, limit=limit, value=value)

    return True

def write_horizontal(board, row, limit):
    for i in range(limit):
        board[row][i] = 1
    
    return True

