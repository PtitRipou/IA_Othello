#Implémentation des instrunctions de jeu

#Permet de déterminer les positions suivantes pour une configuration de plateau
def next_pos(board : 'list[list[int]]', player : 'str'):
    
    next_board = board.copy
    player_int = 0

    if player == "player1" :
        player_int = 1
    elif player == "player2" :
        player_int = 2
    else :
        print("Error : Not a valid player !")
    
    for k in range(8):
        for p in range(8):
            if board[k][p] == player_int :
                if exist_neighbor(board, k, p) == True:
                    next_board = 


    return next_board

    def exist_neighbor():
        return