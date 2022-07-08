# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!


# To create the next child node, you should create the game, apply the parent moves
# then apply your next move that you want to try. I'd think of this as more like a 
# tree that has 5 children for each parent (w a s d e).
import sys
# from game import Game
# # sys.setrecursionlimit(100000)


# visited = []

# # def DFS_recursive(filename, copied_moves, allowed_moves):
# #     global visited
# #     game = Game_node(filename, copied_moves, allowed_moves)
# #     print(game.moves)
# #     if game.state.win == True:
# #         solution_found = True
# #         return game.moves
# #     if game.moves not in visited:
# #         visited.append(game.moves)
# #         if game.state.cell.msg == "\nYou walked into a wall. Oof!" or game.state.win == False:
# #             game.allowed_moves.pop()
# #             DFS_recursive(filename, game.moves, game.allowed_moves)
        
# #         if len(game.moves) > 3:
# #             if game.moves [-1] and game.moves[-2] and game.moves[-3] == "e":
# #                 game.allowed_moves.pop()
# #                 DFS_recursive(filename, game.moves, game.allowed_moves)

# #         game.moves += [game.allowed_moves[-1]]
# #         game.allowed_moves = ["e", "w", "a", "s", "d"]
# #         DFS_recursive(filename, game.moves, game.allowed_moves)
# #     else:
# #         game.moves.pop()
# #         game.allowed_moves.pop()
# #         DFS_recursive(filename, game.moves, game.allowed_moves)

# visited = []
# allowed_moves = ["e", "w", "a", "s", "d"]

# # Put current node on stack
# # In a while loop pop the stack if not empty
# # visit(popped node)
# # push all Unvisited and NotVisiting neighbors of popped node on the stack
# # End while

# class Game_node:
#     def __init__(self, filename, parent_moves):
#         self.parent_moves = parent_moves
#         self.state = generate_new_game(filename, self.parent_moves)
#         self.moves = self.state.move_recorder

# # applies parent moves to a new game instance 
# def generate_new_game(filename, moves):
#     game = Game(filename)
#     for move in moves:
#         game.gameMove(move)
#     return game

# def DFS(filename):
#     game = Game_node(filename, [])
#     visited = []
#     allowed_moves = ["e", "w", "a", "s", "d"]
#     while True:
#         game = Game_node(filename, game.moves)
#         print("game moves:", game.moves)
#         print("visited:", visited)
#         print("allowed moves:", allowed_moves)
#         print("\n")
#         if game.state.win == True:
#             visited.append(game.moves)
#             print(game.moves)
#             break

#         if game.state.cell.msg == "\nYou walked into a wall. Oof!":
            
#             # game.moves += allowed_moves[-1]
#             game.state.move_recorder += allowed_moves[-1]
#             visited.append(game.moves)
#             allowed_moves.pop()
#             continue
        
#         if game.moves not in visited:
#             visited.append(game.moves)
#             game.moves += [allowed_moves[-1]]
#             if game.state.cell.msg == "\nYou walked into a wall. Oof!":
#                 allowed_moves.pop()
#                 continue

#             elif game.state.win == False:
#                 allowed_moves.pop()
#                 game.moves.pop()
#                 continue

#             elif game.state.cell.visits > 2:
#                 allowed_moves.pop()
#                 game.moves.pop()
#                 continue

#             if len(allowed_moves) == 0:
#                 game.moves.pop()
#                 allowed_moves = ["e", "w", "a", "s", "d"]
#                 continue
            
#             elif len(game.moves) > 3:
#                 if game.moves[-1] == "e" and game.moves[-2] == "e":
#                     allowed_moves.pop()
#                     continue
#                 else:
#                     allowed_moves = ["e", "w", "a", "s", "d"]
#                     continue

#             else:
#                 allowed_moves = ["e", "w", "a", "s", "d"]
#                 continue

#         elif game.moves in visited:
#             game.moves.pop()
#             allowed_moves.pop()
#             continue







# def DFS(filename, parent_moves):
#     global visited
#     global allowed_moves

#     # makes a new game instance 
#     game = Game_node(filename, parent_moves)
#     game.moves += [allowed_moves[-1]]
#     print("new moves:", game.moves)
#     print("visited:", visited)
#     print("allowed moves:", allowed_moves)
#     print("\n")

#     if game.state.win == True:
#         #stops recursion if finds the end cell
#         print(7)
#         return game.moves

#     if game.moves not in visited:
#         #if new moves, append to visited 
#         visited.append(game.moves)
        
#         if game.state.cell.msg == "\nYou walked into a wall. Oof!":
#             # delete that move, remove it from pool of possible moves and DFS again
#             allowed_moves.pop()
#             # game.moves.pop()
#             DFS(filename, game.moves)
        
#         elif game.state.win == False:
#             # delete that move, remove it from pool of possible moves and DFS again
#             allowed_moves.pop()
#             game.moves.pop()
#             DFS(filename, game.moves)
            
        
#         elif len(game.moves) >= 3:
#             # if last 3 moves were "e", remove e from possible pool
                
#             if game.moves[-1] == "e" and game.moves[-2] == "e":
#                 # print("new allowed moves: ", allowed_moves)
#                 # print("\n")
#                 allowed_moves.pop()
#                 DFS(filename, game.moves)
#             else:
#                 # if game.moves[-2:] == game.moves[-4:-2]:
#                 #     allowed_moves.pop()
#                 #     DFS(filename, game.moves)
#                 # else:
#                     allowed_moves = ["e", "w", "a", "s", "d"]
#                     DFS(filename, game.moves)
#         else:
#             # adds last element from allowed moves
#             # resets allowed moves 
#             allowed_moves = ["e", "w", "a", "s", "d"]
#             # print("new allowed moves: ", allowed_moves)
#             DFS(filename, game.moves)

#     else:
#         # print("repeated: ", game.moves)
#         allowed_moves.pop()
#         game.moves.pop()
#         DFS(filename, game.moves)
  
# def BFS_iterative(node, filename):
#     nodes_list = [node]

#     while True:
#         if game.cell.display == "Y":
#             return game.move_recorder 
#             break
        
#         generate_new_game()
        
#         node = nodes_list[0]
#         nodes_list = nodes_list[1:]
#         solution.append(node.move)

#     for node in self.visited_nodes:
#         visited.append(node.move)
#         nodes_list.append(node)

# def BFS(filename):
#     global visited
#     global allowed_moves
#     while True:
#         while game.moves not in visited:
#             game = Game_node(filename, game.moves)
#             game.moves += allowed_moves[-1]
#             allowed_moves.pop()
            
#         game.moves.pop()
#         allowed_moves.pop()
#         continue 


mode = sys.argv[1]
filename = sys.argv[2]

if len(sys.argv) != 3:
    print("Usage: python3 solver.py <filename> <mode>")
    exit()


def solve(mode):
    pass


if __name__ == "__main__":
    solution_found = False
    if solution_found:
        pass
        # Print your solution...
    else:
        print("There is no possible path.")
