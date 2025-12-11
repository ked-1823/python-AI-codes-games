def print_board(b):
    print('----+---+----')
    print(f'{b[0]}   |  {b[1]}| {b[2]}')
    print('----+---+-----')
    print(f'{b[3]}   | {b[4]} | {b[5]}')
    print('----+---+-----')
    print(f'{b[6]}   | {b[7]} | {b[8]}')
    print('----+---+-----')


def win(b,player):
    win_state=[
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
        ]
    for x,y,z in win_state:
        if b[x]==b[y]==b[z]==player:
            return True
    return False

def tic_tac_toe():
    board=[' ']*9
    current='x'
    
    for _ in range(9):
        print_board(board)
        move=int(input(f'player {current} pick position from (0-8):'))
        if board[move]!=' ':
            print('invalid move')
            continue
        board[move]=current
        if win(board,current):
            print_board(board)
            print(f'player {current} wins !!')
            return 
        current ='o' if current=='x' else 'x'
    print_board(board)
    print('its a draw')

tic_tac_toe()
        
        
        
        
        
        
