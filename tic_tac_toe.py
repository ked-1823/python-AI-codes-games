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
