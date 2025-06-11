# Initial board shows position numbers
board = [' '] + [str(i) for i in range(1, 10)]  # index 1-9 used

# Winning positions
wins = [
    [1,2,3], [4,5,6], [7,8,9],  # rows
    [1,4,7], [2,5,8], [3,6,9],  # columns
    [1,5,9], [3,5,7]            # diagonals
]

def show():
    print()
    print(board[1], '|', board[2], '|', board[3])
    print('--+---+--')
    print(board[4], '|', board[5], '|', board[6])
    print('--+---+--')
    print(board[7], '|', board[8], '|', board[9])
    print()

def check_win(sym):
    for w in wins:
        if all(board[pos] == sym for pos in w):
            return True
    return False

player = 1 

for i in range(9):
    show()
    val = int(input(f"Player {player} ({'X' if player==1 else 'O'}), enter position (1-9): "))
    
    if board[val] == 'X' or board[val] == 'O':
        print(" Already taken. Try again.")
        continue
    
    board[val] = 'X' if player == 1 else 'O'
    
    if check_win(board[val]):
        show()
        print(f" Player {player} ({board[val]}) wins!")
        break

    player = 2 if player == 1 else 1
else:
    show()
    print("🤝 It's a draw!")
