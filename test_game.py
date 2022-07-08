from game import Game


def generate_new_game(filename, moves):
    game = Game(filename)
    for move in moves:
        game.gameMove(move)
    return game

# since most negative/edge cases are caught through parse for these specific functions, only test positive cases
# the other negative/edge cases are caught through e2e testing (e.g. invalid moves)

# positive test cases 

def test_get_display(): # tests the grid printing to screen is correct
    expected = "*A*************\n*       2 *  W*\n* *** ** **** *\n* * WW*   1   *\n* ***** ***** *\n*  2 *   ** *F*\n*W**W***   FFF*\n* 1********FFF*\n*************Y*\n" + "\nYou have 0 water buckets."
    game = generate_new_game("board_super_hard.txt", [])
    actual = game.get_display()
    assert expected == actual, "get_display failed"
    print("get display testcase passed!")


def test_gameMove(): # tests moves given to board move the player move in correct position
    game = generate_new_game("board_super_hard.txt", [])
    game.gameMove("s")
    expected = (1, 1)
    actual = (game.player.row, game.player.col)
    assert actual == expected, "gameMove failed"
    print("gameMove testcase passed!")


def test_bounce(): # tests that bounce() erases move from moves, moves back the player, and returns correct message
    game = generate_new_game("board_super_hard.txt", ["s"])
    game.bounce()
    moves_expected = []
    moves_actual = game.move_recorder
    assert moves_expected == moves_actual, "moves not recorded properly"

    coor_expected = (0, 1)
    coor_actual = (game.player.row, game.player.col)

    assert coor_actual == coor_expected, "player not bounced back"

    msg_expected = "\nYou walked into a wall. Oof!"
    msg_actual = game.cell.msg
    assert msg_expected == msg_actual, "message returned incorrectly"
    print("bounce testcase passed!")

def test_border_check(): # tests the border check player in board
    game = generate_new_game("board_super_hard.txt", [])
    game.player.row = 1
    game.player.row = 0
    expected = True
    actual = game.border_check()
    assert actual == expected, "border check failed"
    print("bordercheck true testcase passed!")


def test_finish_string_win(): # tests that correct string is returned if win condition is made
    game = generate_new_game("board_super_hard.txt", [])
    game.win = True
    expected = "\n\nYou conquer the treacherous maze set up by the Fire"\
        " Nation and reclaim the Honourable Furious Forest Throne, restoring"\
        " your hometown back to its former glory of rainbow and sunshine! Peace"\
        " reigns over the lands.\n" + "\nYou made 0 moves.\nYour moves: \n" + \
        "\n=====================\n====== YOU WIN! =====\n====================="
    actual = game.finish_string()
    assert actual == expected, "wrong finish string returned"
    print("win string testcase passed!")


def test_finish_string_lose():  # tests that correct string is returned if lose condition is made
    game = generate_new_game("board_super_hard.txt", [])
    game.win = False
    expected = "The Fire Nation triumphs! The Honourable Furious Forest"\
        " is reduced to a pile of ash and is scattered to the winds by the next"\
        " storm... You have been roasted.\n" + "\nYou made 0 moves.\nYour moves: \n" + \
        "\n=====================\n===== GAME OVER =====\n====================="
    actual = game.finish_string()
    assert actual == expected, "wrong finish string returned"
    print("lose string testcase passed!")

def run_tests():
    test_get_display()
    test_gameMove()
    test_bounce()
    test_border_check()
    test_finish_string_win()
    test_finish_string_lose()

run_tests()
