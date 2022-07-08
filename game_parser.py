from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

def read_lines(filename):
    """Read in a file and return the contents as a list of strings."""
    try:
        f = open(filename, "r")
        lines = f.readlines()
        parsed_lines = parse(lines)
        f.close()
        return parsed_lines
    except FileNotFoundError:
        exit("{} does not exist!".format(filename))

def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """

    joined_lines = "".join(lines)

    #classifying characters
    num_of_x = 0
    num_of_y = 0
    teleporter_count = 0
    i = 0
    classed_lines = []
    while i < len(joined_lines):
        if joined_lines[i] == "X":
            classed_lines.append(Start())
            num_of_x += 1
        elif joined_lines[i] == "Y":
            classed_lines.append(End())
            num_of_y += 1
        elif joined_lines[i] == " ":
            classed_lines.append(Air())
        elif joined_lines[i] == "*":
            classed_lines.append(Wall())
        elif joined_lines[i] == "F":
            classed_lines.append(Fire())
        elif joined_lines[i] == "W":
            classed_lines.append(Water())
        elif joined_lines[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            classed_lines.append(Teleport(joined_lines[i], i))
            teleporter_count += 1
        elif joined_lines[i] == "\n":
            classed_lines.append("\n")
        else:
            bad_letter = "Bad letter in configuration file: {}."
            raise ValueError (bad_letter.format(joined_lines[i]))
        i += 1
    
    if num_of_x != 1:
        x_error = "Expected 1 starting position, got {}."
        raise ValueError (x_error.format(num_of_x))
        
    if num_of_y != 1:
        y_error = "Expected 1 ending position, got {}."
        raise ValueError (y_error.format(num_of_y))

    teleporter_num = 1
    while teleporter_num < 10:
        teleporter_counter = joined_lines.count(str(teleporter_num))
        if teleporter_counter != 0 and teleporter_counter != 2:
            unmatched_teleport = "Teleport pad {} does not have an exclusively matching pad."
            raise ValueError (unmatched_teleport.format(teleporter_num))
        teleporter_num += 1

    # making list of list
    cells = []
    if classed_lines[-1] == "\n":
        classed_lines.pop()
    num_rows = classed_lines.count("\n")
    char_per_row = int(len(classed_lines)/num_rows)
    i = 0
    n = 0
    while i < num_rows:
        cells.append(list(classed_lines[n : n + char_per_row]))
        i += 1
        n += char_per_row + 1

    # finding start coordinates    
    x = classed_lines.index("X")//(char_per_row + 1)
    start_coor = [x, cells[x].index("X")]

    return cells, start_coor
