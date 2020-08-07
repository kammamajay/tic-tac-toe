def main():
    board = ['#','', '', '', '', '', '', '', '', '']
    order = take_input() #p1,p2
    chance = 1
    play_game(board, chance, order)
def take_input():
    check = ''
    while not (check == 'X' or check == 'O'):
        print("Player 1, choose X or O: ", end='')
        marker = input().upper()
        player1 = marker#x
        check = player1
        if player1 == "X":
            player2 = 'O'
        else:
            player2 = 'X'
    if player1 == "X":
        return ('X', 'O')
    elif player1 == "O":
        return ('O', 'X')
def play_game(board, chance, order):
    pos = 0
    marker = None
    while not isBoardFull(board) and not check_win(board):
        pos = 0
        while pos not in range(1,10):
            if chance == 1:
                print("Player 1: enter position (1-9): ",end='')
                marker = order[0] #x
                chance = 2
            else:
                print("Player 2: enter position (1-9): ", end='')
                chance = 1
                marker = order[1]
            pos = int(input()) #5
        
            flag=update_board(board, pos, marker)
            if flag==1:
                continue
            if flag==0:
                if chance==1:
                    chance=2
                else:
                    chance=1

    if check_win(board):
        if chance == 2:
            print("player 1 won the game")
        elif chance == 1:
            print("player 2 won the game")
    else:
        print("game draw")

def print_board(board):
    print(board[1]+ " | "+board[2] + " | "+board[3])
    print("-"*10)
    print(board[4]+ " | "+board[5] + " | "+ board[6])
    print("-" * 10)
    print(board[7]+ " | "+board[8] + " | "+ board[9])
    return
def update_board(board, pos, marker):
    if board[pos]=='': 
       board[pos] = marker
       print_board(board)
       return 1
    else:
        print("Invalid Position")
        return 0
def isBoardFull(board):
    for i in range(1,len(board)):
        if board[i] == '':
            return False
    return True
def check_win(board):
    r = False
    for i in [1,4,7]:
        if board[i]  == board[i+1] and board[i] == board[i+2] and board[i] != '': #checking row
            r = True
    for i in [1,2,3]:
         if board[i] == board[i+3] and board[i] == board[i+6] and board[i] != '': #checking col
                 r = True
    if board[1] == board[5] and board[5] == board[9] and board[1] != '':
                        r = True
    elif board[3] == board[5] and board[5] == board[7] and board[3] != '':
             r = True
    return r
main()
