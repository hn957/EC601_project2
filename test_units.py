from unittest.mock import patch
import sys

"""
test correct parameters if any test returns false => Assertion error will be raised

"""

# expects true and program should continue => normal input for length
def test_correct_length():
    testargs = ["main.py", "apple" ,"apple.json", "100", "hashtag"]

    with patch.object(sys, 'argv',testargs):
         
           assert len(sys.argv) == 5


# expects true and program should continue => hastag testing
def test_hashtag_corect_fourth_parameter():
    testargs = ["main.py", "apple" ,"apple.json", "100", "hashtag"]

    with patch.object(sys, 'argv',testargs):
         
         assert sys.argv[4] == "hashtag" or sys.argv[4] == "user"


# expects true and program should continue  => user testing
def test_user_corect_fourth_parameter():
    testargs = ["main.py", "apple" ,"apple.json", "100", "user"]

    with patch.object(sys, 'argv',testargs):
         
         assert sys.argv[4] == "user" or sys.argv[4] == "hashtag"


# expects true and program should continue => json files
def test_correct_json_extension():
    testargs = ["main.py", "apple" ,"apple.json", "100", "tweet"]

    with patch.object(sys, 'argv',testargs):
         
         assert sys.argv[2].endswith(".json")


"""
test wrong parameters if any test returns false => Assertion error will be raised

"""

# expects true and program should continue => normal input for length
def test_wrong_length():
    testargs = ["main.py", "apple" ,"apple.json", "100", "hashtag","hastag"]

    with patch.object(sys, 'argv',testargs):

         assert len(sys.argv) != 5


# expects true and program should continue => hastag & user testing
def test_wrong_fourth_parameter():
    testargs = ["main.py", "apple" ,"apple.json", "100", "tweet"]

    with patch.object(sys, 'argv',testargs):
         
         assert sys.argv[4] != "hashtag" or sys.argv[4] != "user"


# expects true and program should continue => hastag & user testing
def test_wrong_fourth_parameter():
    testargs = ["main.py", "apple" ,"apple.json", "100", "tweet"]

    with patch.object(sys, 'argv',testargs):
         
         assert sys.argv[4] != "hashtag" or sys.argv[4] != "user"


# expects true and program should continue => json files
def test_wrong_extension():
    testargs = ["main.py", "apple" ,"apple.test", "100", "tweet"]

    with patch.object(sys, 'argv',testargs):
         
         assert sys.argv[2].endswith(".json") is not True


