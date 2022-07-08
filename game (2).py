from game_parser import read_lines
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

class Game:
    def __init__(self, filename):
        self.filename = filename
        self.grid = read_lines(self.filename)
        self.num_of_rows = len(self.grid[0])
        self.num_of_cols = len(self.grid[0][0])
        self.player = Player(self.grid[1][0], self.grid[1][1])
        self.cell = self.grid[0][self.player.row][self.player.col]
        self.move_recorder = []
        self.win = None

    def get_display(self):
        display_grid = grid_to_string(self.grid[0], self.player)
        return display_grid

    def gameMove(self, move):
        # Takes in a move (w, a, s, d, e, q) and moves the player on the game board.
        if move.lower() == "q":
            self.win = "quit"

        self.current = (self.player.row, self.player.col)
        self.move_recorder.append(move.lower())
        self.player.move(move.lower())

        if self.border_check() != False:
            self.cell = self.grid[0][self.player.row][self.player.col]
            self.cell.step(self)
        else:
            self.bounce()

    def bounce(self):
        # Moves the player back to previous position, removing that position from the move recorder.
        self.player.row = self.current[0]
        self.player.col = self.current[1]
        self.move_recorder.pop()
        self.cell.msg = "\nYou walked into a wall. Oof!"

    def border_check(self):
        # Checks if player is within the borders of the game board.
        if self.player.row < 0 or self.player.row == self.num_of_rows\
        or self.player.col < 0 or  self.player.col == self.num_of_cols:
            return False

    def finish_string(self):
        move_string = ', '.join(self.move_recorder)
        finish_win = "\n\nYou conquer the treacherous maze set up by the Fire"\
        " Nation and reclaim the Honourable Furious Forest Throne, restoring"\
        " your hometown back to its former glory of rainbow and sunshine! Peace"\
        " reigns over the lands.\n"
        finish_lose = "The Fire Nation triumphs! The Honourable Furious Forest"\
        " is reduced to a pile of ash and is scattered to the winds by the next"\
        " storm... You have been roasted.\n"
        moves = "\nYou made {} move{}.\nYour move{}: {}\n"
        banner = "\n=====================\n====={} =====\n====================="

        s = ""
        if len(self.move_recorder) != 1:
            s = "s"

        moves_formatted = moves.format(len(self.move_recorder), s, s, move_string)
        if self.win == True:
            return finish_win + moves_formatted + banner.format("= YOU WIN!")
        elif self.win == False:
            return finish_lose + moves_formatted + banner.format(" GAME OVER")
