import numpy as np

N = 9


def check_col(board, row, col, val):
    x = row
    y = col
    if val == 0:
        return True

    for i in range(9):
        if board[i][y] == val and (i, y) != (x, y):
            # print("check_col x")
            return False
    return True


def check_row(board, row, col, val):
    x = row
    y = col
    if val == 0:
        return True

    for i in range(9):
        if board[x][i] == val and (x, i) != (x, y):
            # print("check_row x")
            return False
    return True


def check_box(board, row, col, val):
    x = row
    y = col
    if val == 0:
        return True

    startRow = x - x % 3
    startCol = y - y % 3

    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == val and (i + startRow, j + startCol) != (x, y):
                return False
    return True


def isSafe(board, row, col, num):
    if check_row(board, row, col, num) and check_col(board, row, col, num) and check_box(board, row, col, num):
        return True
    return False


def check_original_board(board):

    for i in range(9):
        for j in range(9):
            if not isSafe(board, i, j, board[i][j]):
                return False
    return True

def solve_board(board, row, col):
    # Check if we have reached the 8th
    # row and 9th column (0
    # indexed matrix) , we are
    # returning true to avoid
    # further backtracking
    if row == N - 1 and col == N:
        return True

    # Check if column value  becomes 9 ,
    # we move to next row and
    # column start from 0
    if col == N:
        row += 1
        col = 0

    # Check if the current position of
    # the grid already contains
    # value >0, we iterate for next column
    if board[row][col] > 0:
        return solve_board(board, row, col + 1)
    for num in range(1, N + 1, 1):

        # Check if it is safe to place
        # the num (1-9)  in the
        # given row ,col  ->we
        # move to next column
        if isSafe(board, row, col, num):

            # Assigning the num in
            # the current (row,col)
            # position of the grid
            # and assuming our assigned
            # num in the position
            # is correct
            board[row][col] = num

            # Checking for next possibility with next
            # column
            if solve_board(board, row, col + 1):
                return True

        # Removing the assigned num ,
        # since our assumption
        # was wrong , and we go for
        # next assumption with
        # diff num value
        board[row][col] = 0
    return False


tab = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
       [5, 2, 0, 0, 0, 0, 0, 0, 0],
       [0, 8, 7, 0, 0, 0, 0, 3, 1],
       [0, 0, 3, 0, 1, 0, 0, 8, 0],
       [9, 0, 0, 8, 6, 3, 0, 0, 5],
       [0, 5, 0, 0, 9, 0, 6, 0, 0],
       [1, 3, 0, 0, 0, 0, 2, 5, 0],
       [0, 0, 0, 0, 0, 0, 0, 7, 4],
       [0, 0, 5, 2, 0, 6, 3, 0, 0]]
tab = np.array(tab)
print(tab)
if check_original_board(tab):
    solve_board(tab, 0, 0)
    print()
    print(tab)
else:
    print("To ustawienie jest bledne!")


