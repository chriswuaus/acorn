
def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """

    grid_string = ""
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if player.row == i and player.col == j:
                grid_string += player.display
            else:
                grid_string += grid[i][j].display
            j += 1
        grid_string += "\n"
        i += 1

    grammar = ""
    if player.num_water_buckets != 1:
        grammar = "s"
    grid_string += "\nYou have {} water bucket{}.".format(player.num_water_buckets, grammar)
    
    return grid_string
