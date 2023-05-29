# Creating an empty board
board=[' ' for _ in range(9)]

# Creating a function to display the current board
def print_board():
    print('-------------')
    for i in range(3):
        print('|',board[i*3],'|',board[i*3+1],'|',board[i*3+2],'|')
        print('-------------')

# Creating a function to check if any player has won
def check_winner():
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2]!=' ':
            return True,board[i]
 
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]!=' ':
            return True, board[i]

    if board[0]==board[4]==board[8]!=' ':
        return True,board[0]
    if board[2]==board[4]==board[6]!=' ':
        return True,board[2]
    return False,''

# Creating a function to play the game
def play_game():
    current_player='X'
    while True:
        print_board()
        print("It's",current_player,"player's turn.")
        position=int(input("Enter a position (1-9): "))-1
        if position<0 or position>=9 or board[position]!=' ':
            print('It is an Invalid move. Please, Try again.')
            continue
        board[position]=current_player
        winner,symbol=check_winner()
        if winner:
            print_board()
            print('Congrats, Player',symbol,'wins!')
            break
        if ' ' not in board:
            print_board()
            print("It's a tie!")
            break
        current_player='O' if current_player=='X' else 'X'

play_game()
