class Start:
    def __init__(self):
        self.display = 'X'
        self.grid_index = None
        self.msg = None
        self.visits = 0

    def step(self, game):
        self.visits += 1
        pass
    def __eq__(self, other):
        if self.display == "X":
            return True

class End:
    def __init__(self):
        self.display = 'Y'
        self.grid_index = None
        self.msg = None
        self.visits = 0

    def step(self, game):
        game.win = True 
    
class Air:
    def __init__(self):
        self.display = ' '
        self.grid_index = None
        self.msg = None
        self.visits = 0

    def step(self, game):
        self.visits += 1
        pass
    

class Wall:
    def __init__(self):
        self.display = '*'
        self.grid_index = None
        self.msg = None
        self.visits = 0

    def step(self, game):
        self.visits += 1
        game.bounce()
    

class Fire:
    def __init__(self):
        self.display = 'F'
        self.grid_index = None
        self.msg = None
        self.visits = 0
    def step(self, game):
        self.visits += 1
        if game.player.num_water_buckets > 0:
            game.player.take_water()
            # change the Fire() cell to an Air() cell
            game.grid[0][game.player.row][game.player.col] = Air()
            self.msg = "\nWith your strong acorn arms, you throw a water bucket at the fire."\
            " You acorn roll your way through the extinguished flames!"

        else:
            self.msg = "\n\nYou step into the fires and watch your dreams disappear :(.\n"
            game.win = False
        
class Water:
    def __init__(self):
        self.display = 'W'
        self.grid_index = None
        self.msg = None
        self.visits = 0

    def step(self, game):
        self.visits += 1
        game.player.add_water()
        self.msg = "\nThank the Honourable Furious Forest, you've found a bucket of water!"
        # change the Water() cell to an Air() cell
        game.grid[0][game.player.row][game.player.col] = Air()
        
class Teleport:
    def __init__(self, num, grid_index):
        self.display = num
        self.grid_index = grid_index
        self.msg = None
        self.visits = 0


    def step(self, game):
        # prevents invalid inputs from teleporting the player 
        if game.player.invalid == True:
            pass

        

        else:
            self.visits += 1
            for cells in game.grid[0]:
                for tele in cells:

                    # finds the teleport cell with a matching display, but with a different grid index
                    if type(tele) == Teleport and tele.grid_index != self.grid_index\
                    and tele.display == self.display:
                        # sets the players row to the index of the matching teleport cell
                        game.player.row = tele.grid_index//(game.num_of_cols + 1) 
                        i = 0

                        # finds and sets the players col to the index of the matching teleport cell
                        while i < len(game.grid[0][game.player.row]):
                            if game.grid[0][game.player.row][i].grid_index == tele.grid_index:
                                game.player.col = i
                                break
                            i += 1
                      
            self.msg = "\nWhoosh! The magical gates break Physics as we"\
            " know it and opens a wormhole through space and time."
        
