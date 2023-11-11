
def  check_up_left(board, row, column):
    if not (row > 0 and column > 0):
        return True
    
    if board[row][column] == 1:
        return False
    
    if row > 0 and column > 0:
        return check_up_left(board=board, row=row-1, column=column-1)
    
    return True

def check_up_right(board, row, column, limit):
    if not (row < limit and column > 0):
        return True 
    if board[row][column] == 1:
        return False
    
    if row < limit and column > 0:
        return check_up_right(board=board, row=row+1, column=column-1, limit=limit)

    return True

def check_down_left(board, row, column, limit):
    if not (row < limit and column > 0):
        return True
    if board[row][column] == 1:
        return False
    
    if row < limit and column > 0:
        return check_down_left(board=board, row=row+1, column=column-1, limit=limit)
    
    return True

def check_down_right(board, row, column, limit):
    if not (row < limit and column < limit):
        return True
    
    if board[row][column] == 1:
        return False
    
    if row < limit and column < limit:
        return check_down_right(board=board, row=row+1, column=column+1, limit=limit)
    
    return True

def check_vertical(board, row, column, limit, value):
    if row == limit:
        return True

    if board[row][column] == 1:
        return False
    
    if column != limit:
        return check_vertical(board=board, row=row+value, column=column, limit=limit, value=value)

    return True


