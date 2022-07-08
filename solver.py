# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!

# sys.setrecursionlimit(100000)
# To create the next child node, you should create the game, apply the parent moves
# then apply your next move that you want to try. I'd think of this as more like a 
# tree that has 5 children for each parent (w a s d e).
import sys
import game

class Node:
    def __init__(self, move):
        self.move = move
        self.next_move = ["w", "a", "s", "d", "e"]
        self.visited_nodes = []
def generate_new_game(filename):
    game = Game(filename)
    for moves in self.visited_nodes:
        game.gameMove(moves)
    

def BFS_iterative(node):
    visited = [node.move]
    nodes_list = [node]
    solution = []

    while True:
        if len(visited) == 0:
            break
        node = nodes_list[0]
        nodes_list = nodes_list[1:]
        solution.append(node.move)

    for node in self.visited_nodes:
        visited.append(node.move)
        nodes_list.append(node)

def DFS_iterative(node):
    print(node.name)
    for node in reversed(node.neighbours):
        if node.name not in visited:
            visited.append(node.name)
            DFS_recursive(node)



def solve(mode, filename):
    if mode == BFS:
        # bfs time
        pass
    elif mode == DFS:
        # dfs time 
        pass
if len(sys.argv) != 3:
    print("Usage: python3 solver.py <filename> <mode>")
    exit()
    


if __name__ == "__main__":
    solution_found = False
    if solution_found:
        pass
        # Print your solution...
    else:
        print("There is no possible path.")
