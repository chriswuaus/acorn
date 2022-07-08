from game_parser import parse, read_lines
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)

# negative test cases handed in e2e
# positive cases
def test_readlines(): # tests if readlines returns a list of lists of cell objects
    filename = "board_simple.txt"
    lines = read_lines(filename)
    
    assert isinstance(lines[0][0][0], Wall) == True, "easy readlines failed"
    assert isinstance(lines[0][0][1], Wall) == True, "easy readlines failed"
    assert isinstance(lines[0][0][2], Start) == True, "easy readlines failed"
    assert isinstance(lines[0][0][3], Wall) == True, "easy readlines failed"
    assert isinstance(lines[0][0][4], Wall) == True, "easy readlines failed"
    assert isinstance(lines[0][1][0], Wall) == True, "easy readlines failed"
    assert isinstance(lines[0][1][1], Air) == True, "easy readlines failed"
    assert isinstance(lines[0][1][2], Air) == True, "easy readlines failed"
    assert isinstance(lines[0][1][3], Air) == True, "easy readlines failed"
    assert isinstance(lines[0][1][4], Wall) == True, "easy readlines failed"
    assert isinstance(lines[0][2][0], Wall) == True, "easy readlines failed"
    assert isinstance(lines[0][2][1], Wall) == True, "easy readlines failed"
    assert isinstance(lines[0][2][2], End) == True, "easy readlines failed"
    assert isinstance(lines[0][2][3], Wall) == True, "easy readlines failed"
    assert isinstance(lines[0][2][4], Wall) == True, "easy readlines failed"
    assert lines[1] == [0, 2], "readlines failed - wrong starting coordinate"
    print("simple testcase passed!")

def run_tests():
    test_readlines()
run_tests()
