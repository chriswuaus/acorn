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


# positive cases

def test_parse_simple():  # tests parsing a simple board
    board_simple = ["*X*\n", "* *\n", "*Y*"]
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
    print("simple testcase passed!")

# # negative cases

def test_parse_bad_letter(): # tests if board config has bad letter in it
    try:
        bad_letter_board = ["***XD*\n", "*   *\n", "**Y**\n"]
        parse(bad_letter_board) 
        print("badletter testcase failed, no error thrown!")
    except Exception as e:
        assert type(e) == ValueError, "bad_letter failed, wrong exception thrown"
        assert str(e) == "Bad letter in configuration file: D.", "bad_letter failed, wrong error msg"
        print("bad letter testcase passed!")
def test_parse_many_x(): # tests if there's too many starting positions in board config
    try:
        many_x_board = ["*X*\n", "*X*\n"]
        parse(many_x_board) 
        print("many x test case failed, no error thrown!")
    except Exception as e:
        assert type(e) == ValueError, "many_x failed, wrong exception thrown"
        assert str(e) == "Expected 1 starting position, got 2.", "many_x failed, wrong error msg"
        print("too many x testcase passed!")

def test_parse_no_x():  # tests if there's no starting position in board config
    try:
        no_x_board = ["***\n", "*Y*\n"]
        parse(no_x_board) 
        print("no x testcase failed, no error thrown!")
    except Exception as e:
        assert type(e) == ValueError, "no_x failed, wrong exception thrown"
        assert str(e) == "Expected 1 starting position, got 0.", "no_x failed, wrong error msg"
        print("no x testcase passed!")

def test_parse_many_y():  # tests if there's too many ending positions in board config
    try:
        many_y_board = ["*Y**\n", "*YX*\n"]
        parse(many_y_board) 
        print("many y testcase failed, no error thrown!")
    except Exception as e:
        assert type(e) == ValueError, "many_y failed, wrong exception thrown"
        assert str(e) == "Expected 1 ending position, got 2.", "many_y failed, wrong error msg"
        print("many y testcase passed!")

def test_parse_no_y():  # tests if there's no ending position in board config
    try:
        no_y_board = ["*X*\n", "***\n"]
        parse(no_y_board) 
        print("no y testcase failed, no error thrown!")
    except Exception as e:
        assert type(e) == ValueError, "no_y failed, wrong exception thrown"
        assert str(e) == "Expected 1 ending position, got 0.", "no_y failed, wrong error msg"

def test_parse_unmatched_teleport(): # tests if there's unmatched pairs of teleports in board config
    try:
        bad_teleport = ["**X**\n", "*  1*\n", "**Y**"]
        parse(bad_teleport) 
        print("bad teleport testcase failed, no error thrown!")
    except Exception as e:
        assert type(e) == ValueError, "bad_teleport failed, wrong exception thrown"
        assert str(e) == "Teleport pad 1 does not have an exclusively matching pad.", "bad_teleport failed, wrong error msg"
        print("unmatched teleport testcase passed!")
        
# # edge cases 
def test_parse_empty(): # tests if board config is an empty string
    try: 
        board = [""]
        parse(board)
        print("empty grid testcase failed, no error thrown!")
    except Exception as e:
        assert type(e) == ValueError, "no_x failed, wrong exception thrown"
        assert str(e) == "Expected 1 starting position, got 0.", "no_x failed, wrong error msg"
        print("empty grid testcase passed!")

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
