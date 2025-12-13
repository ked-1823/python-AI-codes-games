import random

def print_board(b):

    print(f'{b[0]} | {b[1]} | {b[2]}')
    print('--+---+--')
    print(f'{b[3]} | {b[4]} | {b[5]}')
    print('--+---+--')
    print(f'{b[6]} | {b[7]} | {b[8]}')
    print('--+---+--')

def winner(board,player):
    win_rate=[
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
        ]
    for x,y,z in win_rate:
        if board[x]==board[y]==board[z]==player:
            return True
    return False
    
def tic_tac_toe():
    board=[' ']*9
    curr='x'
    for _ in range(9):
        print_board(board)
        if curr=='x':
            play=int(input(f'player {curr} enter your choice betweeon position (0-8): '))
            if board[play]!=' ':
                print('inavlid')
                continue
        else:
            empty=[i for i,spot in enumerate(board) if spot==' ']
            play=random.choice(empty)
            print(f'computer chooses {play}')
          
            
        board[play]=curr
        if winner(board,curr):
            if curr=='x':
                print_board(board)
                print('congrats player you won 🤩🥳!!')
            else:
                print_board(board)
                print('computer won !!')
            return
        
        curr='o' if curr=='x' else 'x'
    print_board(board)
    print('its a draw')

tic_tac_toe()
    
    
    
    
        
    
