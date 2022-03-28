# -*- coding: utf-8 -*-

from math import inf
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
                player.append(["human"])
                print("Player ", k, " is human !\n")
                var1 = True
            
            elif choice == "2":
                var1 = True
                var2 = False
                var3 = False

                while var2 != True:
                    meth_choice = input("\nChoose the AI's method :\n1. Absolute\n2. Positional\n3. Mobility\n4. Mixed\n\nChoice : ")

                    if meth_choice == "1":
                        method = "absolute"
                        var2 = True
                    
                    elif meth_choice == "2":
                        method = "positional"
                        var2 = True
                    
                    elif meth_choice == "3":
                        method = "mobility"
                        var2 = True
                    
                    elif meth_choice == "4":
                        method = "mixed"
                        var2 = True
                    
                    else:
                        print("Error ! This method doesn't exist !")

                while var3 != True:
                    algo_choice = input("\nChoose the AI's algorithm :\n1. Min-Max\n2. Alpha-Beta\n\nChoice : ")

                    if algo_choice == "1":
                        algo = "min-max"
                        var3 = True
                    
                    elif algo_choice == "2":
                        algo = "alpha-beta"
                        var3 = True
                    
                    else:
                        print("Error ! This algorithm doesn't exist !")

                player.append(["ia", method, algo])
                print("Player ", k, " is AI and is using ", method, " method !\n")

            else:
                print("Error ! Choose a correct player !\n")
    
    play(player[0], player[1])

# Permet de lancer la partie
def play(p1 : 'list[list]', p2 : 'list[list]'):
    
    if (p1[0] == "human") and (p2[0] == "human"):
        result = human_human()
        board = result[0]
        turn = result[1]

    elif (p1[0] == "human") and (p2[0] == "ia"):
        result = human_ai(p2[1:3])
        board = result[0]
        turn = result[1]
    
    elif (p1[0] == "ia") and (p2[0] == "ia"):
        result = ai_ai(p1[1:3], p2[1:3])
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
                val_coup = False

                while val_coup == False:
                    coup = input("Player 1 is choosing a stroke : ")
                    print('\n')

                    if (coup == '') or ((int(coup) - 1) >= len(liste_pos)) or (int(coup) <= 0):
                        print("Error ! Choose a correct stroke !\n")
                    
                    else:
                        val_coup = True
                
                board = gp.next_play(board, liste_pos, int(coup), turn)
            
            turn = 2
        
        else :
            board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(board, 0)

            if len(liste_pos) == 0:
                print("Player 2 can't play !\n")

            else:
                val_coup = False

                while val_coup == False:
                    coup = input("Player 2 is choosing a stroke : ")
                    print('\n')

                    if (coup == '') or ((int(coup) - 1) >= len(liste_pos)) or (int(coup) <= 0):
                        print("Error ! Choose a correct stroke !\n")
                    
                    else:
                        val_coup = True
                
                board = gp.next_play(board, liste_pos, int(coup), turn)
            
            turn = 1
    
    return (board, turn)

def human_ai(param : 'list[str]'):
    board = ob.init_othello()
    turn = 1
    list_method = [("absolute", mm.fonct_eval_absolu), ("positional", mm.fonct_eval_positional), ("mobility", mm.fonct_eval_mobility), ("mixed", mm.fonct_eval_mixed)]

    funct_eval = which_method(list_method, param[0])

    while gp.end(board, turn) == False:

        if turn == 1:
            board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(board, 0)

            if len(liste_pos) == 0:
                print("Player 1 can't play !\n")
            
            else:
                val_coup = False

                while val_coup == False:
                    coup = input("Player 1 is choosing a stroke : ")
                    print('\n')

                    if (coup == '') or ((int(coup) - 1) >= len(liste_pos)) or (int(coup) <= 0):
                        print("Error ! Choose a correct stroke !\n")
                    
                    else:
                        val_coup = True
                
                board = gp.next_play(board, liste_pos, int(coup), turn)
                ob.display_othello(board, 0)
            
            turn = 2
        
        else :
            next_board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(next_board, 1)

            if len(liste_pos) == 0:
                print("Player 2 can't play !\n")
            
            else:

                if param[1] == "min-max":
                    result = mm.max_value(board, turn, 0, funct_eval)
                
                else:
                    result = mm.max_alpha_beta(board, turn, 0, -inf, inf, funct_eval)
                
                board = gp.next_pos(board, turn)
                liste_pos = ob.display_othello(board, 1)
                board = gp.next_play(board, liste_pos, result[1], turn)
            turn = 1
    
    return (board, turn)

def ai_ai(param1 : 'list[str]', param2 : 'list[str]'):
    board = ob.init_othello()
    turn = 1
    list_method = [("absolute", mm.fonct_eval_absolu), ("positional", mm.fonct_eval_positional), ("mobility", mm.fonct_eval_mobility), ("mixed", mm.fonct_eval_mixed)]

    funct_eval1 = which_method(list_method, param1[0])
    funct_eval2 = which_method(list_method, param2[0])

    while gp.end(board, turn) == False:
        
        if turn == 1:
            next_board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(next_board, 1)

            if len(liste_pos) == 0:
                print("Player 1 can't play !\n")
            
            else:

                if param1[1] == "min-max":
                    result = mm.max_value(board, turn, 0, funct_eval1)
                
                else:
                    result = mm.max_alpha_beta(board, turn, 0, -inf, inf, funct_eval1)

                board = gp.next_pos(board, turn)
                liste_pos = ob.display_othello(board, 1)
                board = gp.next_play(board, liste_pos, result[1], turn)
                ob.display_othello(board, 0)
            turn = 2
        
        else :
            next_board = gp.next_pos(board, turn)
            liste_pos = ob.display_othello(next_board, 1)

            if len(liste_pos) == 0:
                print("Player 2 can't play !\n")
            
            else:

                if param2[1] == "min-max":
                    result = mm.max_value(board, turn, 0, funct_eval2)
                
                else:
                    result = mm.max_alpha_beta(board, turn, 0, -inf, +inf, funct_eval2)

                board = gp.next_pos(board, turn)
                liste_pos = ob.display_othello(board, 1)
                board = gp.next_play(board, liste_pos, result[1], turn)
                ob.display_othello(board, 0)
            turn = 1

    return (board, turn)

def which_method(list_method : 'list[tuple]', method : 'str'):

    for k in list_method:

        if method == k[0]:
            return k[1]

menu()
#play(["ia", "absolute", "alpha-beta"],["ia", "positional", "alpha-beta"])