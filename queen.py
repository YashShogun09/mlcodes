N = 8
board = [[0]*N for _ in range(N)]

def is_safe(row, col):
    # Check this column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve(row):
    if row == N:
        print_board()
        return True  

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = 1
            if solve(row + 1):
                return True
            board[row][col] = 0  

    return False

def print_board():
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()


solve(0)
