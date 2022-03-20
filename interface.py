# -*- coding: utf-8 -*-

import gameplay as gp
import othello_board as ob
import min_max as mm

# Permet de configurer la partie
def menu():
    player = []

    for k in range(1,3):
        var1 = False

        while var1 != True:
            print("Choose player ", k, " :\n1. Human\n2. AI\n")
            choice = input("Choice : ")

            if choice == "1":
                player.append(("human", None))
                print("Player ", k, " is human !\n")
                var1 = True
            
            elif choice == "2":
                var1 = True
                var2 = False

                while var2 != True:
                    meth_choice = input("\nChoose the AI's method :\n1. Absolute\n\nChoice : ")

                    if meth_choice == "1":
                        method = "absolute"
                        var2 = True
                    
                    else:
                        print("Error ! That method doesn't exist !")
                
                player.append(("ia", method))
                print("Player ", k, " is AI and is using ", method, " method !\n")

            else:
                print("Error ! Choose a correct player !\n")
    
    play(player[0], player[1])

# Permet de lancer la partie
def play(p1 : 'tuple', p2 : 'tuple'):
    
    if (p1[0] == "human") and (p2[0] == "human"):
        result = human_human()
        board = result[0]
        turn = result[1]

    elif (p1[0] == "human") and (p2[0] == "ia"):
        result = human_ai(p2[1])
        board = result[0]
        turn = result[1]

    else:
        print("Error ! Can't find the correct configuration !")
        return

    ob.display_othello(board, 0)
    var = gp.end(board, turn)

    if (var == 1) or (var == 2):
        print("Player ", var, " win the game !")
    
    else:
        print("The match ended in a draw !")

def human_human():
    board = ob.init_othello()
    turn = 1

    while gp.end(board, turn) == False:

        if turn == 1:
            board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(board, 0)

            if len(liste_pos) == 0:
                print("Player 1 can't play !\n")

            else:
                coup = input("Player 1 is choosing a stroke : ")
                print('\n')
                board = gp.next_play(board, liste_pos, int(coup), turn)

            turn = 2
        
        else :
            board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(board, 0)

            if len(liste_pos) == 0:
                print("Player 2 can't play !\n")

            else:
                coup = input("Player 2 is choosing a stroke : ")
                print('\n')
                board = gp.next_play(board, liste_pos, int(coup), turn)
            
            turn = 1
    
    return (board, turn)

def human_ai(method : 'str'):
    board = ob.init_othello()
    turn = 1
    list_method = [("absolute",mm.fonct_eval_absolu)]

    funct_eval = which_method(list_method, method)

    while gp.end(board, turn) == False:

        if turn == 1:
            board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(board, 0)

            if len(liste_pos) == 0:
                print("Player 1 can't play !\n")
            
            else:
                coup = input("Player 1 is choosing a stroke : ")
                print('\n')
                board = gp.next_play(board, liste_pos, int(coup), turn)
                ob.display_othello(board, 0)
            
            turn = 2
        
        else :
            next_board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(next_board, 1)

            if len(liste_pos) == 0:
                print("Player 2 can't play !\n")
            
            else:
                result = mm.max_value(board, turn, 0, funct_eval)
                board = gp.next_pos(board, turn)
                liste_pos = ob.display_othello(board, 1)
                board = gp.next_play(board, liste_pos, result[1], turn)
            turn = 1
    
    return (board, turn)

def which_method(list_method : 'list[tuple]', method : 'str'):

    for k in list_method:

        if method == k[0]:
            return k[1]

menu()
#play("human","human")