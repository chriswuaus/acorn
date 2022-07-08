class Player:
    def __init__(self, row, col):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = row
        self.col = col
        self.invalid = False

    def move(self, move):
        if move == "w":
            self.row -= 1
        elif move == "a":
            self.col -= 1 
        elif move == "s":
            self.row += 1
        elif move == "d":
            self.col += 1
        elif move == "e":
            pass
        else:
            self.invalid = True

    def add_water(self):
        self.num_water_buckets += 1
    
    def take_water(self):
        self.num_water_buckets -= 1

