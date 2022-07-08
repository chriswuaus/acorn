from game import Game
import os
import sys


if len(sys.argv) < 2:
    print("Usage: python3 run.py <filename> [play]")
    exit()

filename = sys.argv[1]
game = Game(filename)

while game.win == None:
    print(game.get_display())

    if game.cell.msg != None:  
        print(game.cell.msg)

    if game.player.invalid == True:
        print("\nPlease enter a valid move (w, a, s, d, e, q).")
        game.player.invalid = False
        game.move_recorder.pop()
        
    move = input("\nInput a move: ")
    game.gameMove(move)

if game.win != "quit":
    print(game.get_display())
    if game.cell.msg != None: 
        print(game.cell.msg)
    print(game.finish_string())
    
else:
    print("\nBye!")
    exit()
