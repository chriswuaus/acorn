from grid import grid_to_string
from game_parser import parse
from player import Player
# since all input into grid has to pass through parser, all negative and edge cases are caught there
# positive tests 
def test_simple_grid():
    player = Player(1,1)
    board = ["*X*\n", "* *\n", "*Y*\n"]
    expected = "*X*\n*A*\n*Y*\n\nYou have 0 water buckets."
    actual = grid_to_string(parse(board)[0], player)
    assert actual == expected, "simple grid failed"

def test_super_hard_grid():
    player = Player(1,1)
    board = ["*X*************\n","*       2 *  W*\n", "* *** ** **** *\n", "* * WW*   1   *\n", "* ***** ***** *\n", "*  2 *   ** *F*\n", "*W**W***   FFF*\n", "* 1********FFF*\n", "*************Y*\n"]
    expected = "*X*************\n*A      2 *  W*\n* *** ** **** *\n* * WW*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n*W**W***   FFF*\n* 1********FFF*\n*************Y*\n\nYou have 0 water buckets."
    actual = grid_to_string(parse(board)[0], player)
    assert expected == actual, "Super hard grid failed"

def run_tests():
    test_simple_grid()
    test_super_hard_grid()

run_tests()
