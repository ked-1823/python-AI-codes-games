curr=input('enter who will start the game x or 0 ? : ')

print(f'{curr}  start the game ')
def print_board(b):
    print(f'{b[0]} | {b[1]} | {b[2]}')
    print('--+---+--')
    print(f'{b[3]} | {b[4]} | {b[5]}')
    print('--+---+--')
    print(f'{b[6]} | {b[7]} | {b[8]}')
    print('--+---+--')


def winner(board,player):
    win_chance=[
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
        ]
    
    for a,b,c in win_chance:
        if board[a]==board[b]==board[c]==player:
            return True
    return False

def tic_tac_toe():
    board=[' ']*9
    current=curr
    for _ in range(9):
        print_board(board)
        play=int(input(f'player {current}  pick between  between (0-8):  '))
        if board[play]!=' ':
            print('invalid entry')
            continue
        board[play]=current
    
        if winner(board,current):
            print_board(board)
            print(f'congrats {current} you won !!') 
            return
        
        current='x' if current=='o' else 'o'
    print_board(board)
    print('its a draw')


tic_tac_toe()
    
