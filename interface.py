# -*- coding: utf-8 -*-

import gameplay as gp
import othello_board as ob

#Permet de configurer la partie
def menu():
    choice1 = input("Choose player 1 :\n1. Human\n2. AI\nChoice : ")
    
    if choice1 == "1":
        player1 = "human"
        print("First player is human !\n")
    
    elif choice1 == "2":
        player1 = "ia"
        print("First player is AI !\n")
    
    else:
        print("Error ! Choose a correct player 1 !")
        return

    choice2 = input("Choose player 2 :\n1. Human\n2. AI\nChoice :")

    if choice2 == "1":
        player2 = "human"
        print("Second player is human !\n")
    
    elif choice2 == "2":
        player2 = "ia"
        print("Second player is AI !\n")
    
    else:
        print("Error ! Choose a correct player 2 !")
        return
    
    play(player1, player2)

#Permet de lancer la partie
def play(p1 : 'str', p2 : 'str'):
    board = ob.init_othello()
    turn = 1

    while gp.end(board, turn) == False:

        if turn == 1:
            board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(board)
            coup = input("Player 1 choose a stroke : ")
            board = gp.next_play(board, liste_pos, int(coup), turn)
            turn = 2
        
        else :
            board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(board)
            coup = input("Player 2 choose a stroke : ")
            board = gp.next_play(board, liste_pos, int(coup), turn)
            turn = 1
    
    ob.display_othello(board)
    var = gp.end(board, turn)

    if type(var) == int:
        print("Player ", var, " win the game !")
    
    else:
        print("The match ended in a draw !")

menu()