from game_parser import parse
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
board_simple = ["*X*\n", "* *\n", "*Y*"]

# board_super_hard = ["*X*************\n","*       2 *  W*\n", "* *** ** **** *\n", "* * WW*   1   *\n", "* ***** ***** *\n", "*  2 *   ** *F*\n", "*W**W***   FFF*\n", "* 1********FFF*\n", "*************Y*\n"]
# positive cases
def test_parse_simple():
    simple_parse = parse(board_simple)
    assert isinstance(simple_parse[0][0][0], Wall) == True, "easy parse failed"
    assert isinstance(simple_parse[0][0][1], Start) == True, "easy parse failed"
    assert isinstance(simple_parse[0][0][2], Wall) == True, "easy parse failed"
    assert isinstance(simple_parse[0][1][0], Wall) == True, "easy parse failed"
    assert isinstance(simple_parse[0][1][1], Air) == True, "easy parse failed"
    assert isinstance(simple_parse[0][1][2], Wall) == True, "easy parse failed"
    assert isinstance(simple_parse[0][2][0], Wall) == True, "easy parse failed"
    assert isinstance(simple_parse[0][2][1], End) == True, "easy parse failed"
    assert isinstance(simple_parse[0][2][2], Wall) == True, "easy parse failed"
    assert simple_parse[1] == [0, 1], "easy parse failed - wrong starting coordinate"

# # negative cases

def test_parse_bad_letter():
    try:
        bad_letter_board = ["***XD*\n", "*   *\n", "**Y**\n"]
        parse(bad_letter_board) 
    except Exception as e:
        assert type(e) == ValueError, "bad_letter failed, wrong exception thrown"
        assert str(e) == "Bad letter in configuration file: D.", "bad_letter failed, wrong error msg"

def test_parse_many_x():
    try:
        many_x_board = ["*X*\n", "*X*\n"]
        parse(many_x_board) 
    except Exception as e:
        assert type(e) == ValueError, "many_x failed, wrong exception thrown"
        assert str(e) == "Expected 1 starting position, got 2.", "many_x failed, wrong error msg"
    
def test_parse_no_x():
    try:
        no_x_board = ["***\n", "*Y*\n"]
        parse(no_x_board) 
    except Exception as e:
        assert type(e) == ValueError, "no_x failed, wrong exception thrown"
        assert str(e) == "Expected 1 starting position, got 0.", "no_x failed, wrong error msg"

def test_parse_many_y():
    try:
        many_y_board = ["*Y**\n", "*YX*\n"]
        parse(many_y_board) 
    except Exception as e:
        assert type(e) == ValueError, "many_y failed, wrong exception thrown"
        assert str(e) == "Expected 1 ending position, got 2.", "many_y failed, wrong error msg"

def test_parse_no_y():
    try:
        no_y_board = ["*X*\n", "***\n"]
        parse(no_y_board) 
    except Exception as e:
        assert type(e) == ValueError, "no_y failed, wrong exception thrown"
        assert str(e) == "Expected 1 ending position, got 0.", "no_y failed, wrong error msg"

def test_parse_unmatched_teleport():
    try:
        bad_teleport = ["**X**\n", "*  1*\n", "**Y**"]
        parse(bad_teleport) 
    except Exception as e:
        assert type(e) == ValueError, "bad_teleport failed, wrong exception thrown"
        assert str(e) == "Teleport pad 1 does not have an exclusively matching pad.", "bad_teleport failed, wrong error msg"

# # edge cases 
def test_parse_empty():
    try: 
        board = [""]
        parse(board)
    except Exception as e:
        assert type(e) == ValueError, "no_x failed, wrong exception thrown"
        assert str(e) == "Expected 1 starting position, got 0.", "no_x failed, wrong error msg"

def run_tests():
    test_parse_simple()
    test_parse_bad_letter()
    test_parse_many_x()
    test_parse_no_x()
    test_parse_many_y()
    test_parse_no_y()
    test_parse_unmatched_teleport()
    test_parse_empty()

run_tests()
