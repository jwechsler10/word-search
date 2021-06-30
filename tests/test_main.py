"""This module contains the unit tests for the crossword puzzle solver.
The tests will be run with pytest.
"""
import string
import pytest
import app

def test_get_valid_words_exits():
    """Tests that the program exists if the file to validate
    words from doesn't exist.
    """
    with pytest.raises(SystemExit):
        app.get_valid_words('I-dont-exist.txt')

def test_get_valid_words():
    """Tests that if a valid file is specifed, a list containing each word
    in the file is returned.
    """
    with open('words.txt') as test_file:
        expected_result = test_file.read().splitlines()

    actual_result = app.get_valid_words()

    assert expected_result == actual_result

def test_generate_board():
    """Tests that given a specifed length and width, a 2D list is returned
    with the specifed length and width. It also verifies that the number of
    letters in the grid is equal to length * width. Lastly, it checks that each
    letter is in [a-z].
    """
    expected_length = 5
    expected_width = 5
    expected_total_number_of_letters = 25

    game_board = app.generate_board(5,5)

    assert expected_length == len(game_board)
    assert expected_width == len(game_board[0])
    assert expected_total_number_of_letters == len(game_board) * len(game_board[0])

    for i in range(expected_length):
        for j in range(expected_width):
            assert game_board[i][j] in string.ascii_lowercase

def test_find_words_down():
    """Tests that given a gameboard of equal length and width,
    a list of valid words found moving down the gameboard are returned.
    """
    test_game_board = [['a', 'q'], ['t', 'z']]
    expected_words = ['at']
    actual_words = app.find_words_down(test_game_board, 2, 2, expected_words)
    assert expected_words == actual_words

def test_find_words_up():
    """Tests that given a gameboard of equal length and width,
    a list of valid words found moving up the gameboard are returned.
    """
    test_game_board = [['t', 't', 't'], ['o', 'o', 'o'], ['h', 'p', 'l']]
    expected_words = ['lot', 'pot', 'hot']
    actual_words = app.find_words_up(test_game_board, 3, 3, expected_words)
    assert expected_words == actual_words

def test_find_words_across():
    """Tests that given a gameboard of equal length and width,
    a list of valid words encountered going right across the gameboard are
    returned.
    """
    test_game_board = [['t', 'o', 'p'], ['r', 'o','d'], ['m', 'e', 't']]
    expected_words = ['top', 'rod', 'met']
    actual_words = app.find_words_across(test_game_board, 3, 3, expected_words)
    assert expected_words == actual_words

def test_find_words_backwards():
    """Tests that given a gameboard of equal length and width,
    a list of valid words found while moving left across
    the gameboard are returned.
    """
    test_game_board = [['t', 'a', 'c'], ['p', 'a', 'g'], ['o', 'w', 't']]
    expected_words = ['two', 'gap', 'cat']
    actual_words = app.find_words_backwards(test_game_board, 3, 3, expected_words)
    assert expected_words == actual_words

def test_find_diagonal():
    """Tests that given a gameboard of equal length and width,
    a list of valid words found moving diagionally
    around the gameboard are returned.
    """
    test_game_board = [['t', 'a', 'q'], ['z', 'o', 'n'], ['v', 'f', 'p']]
    expected_words = ['top']
    actual_words = app.find_words_diagonal(test_game_board, 3, 3, expected_words)
    assert expected_words == actual_words

def test_find_words_down_negative():
    """Tests that given a gameboard of equal length and width,
    an empty list is returned if no valid words are found moving
    down the gameboard.
    """
    test_game_board = [['a', 'a'], ['a', 'a']]
    expected_words = []
    actual_words = app.find_words_down(test_game_board, 2, 2, expected_words)
    assert expected_words == actual_words

def test_find_words_up_negative():
    """Tests that given a gameboard of equal length and width,
    an empty list is returned if no valid words are found moving
    up the gameboard.
    """
    test_game_board = [['t', 't', 't'], ['z', 'z', 'z'], ['h', 'h', 'h']]
    expected_words = []
    actual_words = app.find_words_up(test_game_board, 3, 3, expected_words)
    assert expected_words == actual_words

def test_find_words_across_negative():
    """Tests that given a gameboard of equal length and width,
    an empty list is returned if no valid words are found moving
    right across the gameboard.
    """
    test_game_board = [['q', 'q', 'p'], ['r', 'z','d'], ['m', 'g', 't']]
    expected_words = []
    actual_words = app.find_words_across(test_game_board, 3, 3, expected_words)
    assert expected_words == actual_words

def test_find_words_backwards_negative():
    """Tests that given a gameboard of equal length and width,
    an empty list is returned if no valid words are found moving
    left across the gameboard.
    """
    test_game_board = [['t', 'q', 'c'], ['p', 'k', 'l'], ['n', 'w', 'x']]
    expected_words = []
    actual_words = app.find_words_backwards(test_game_board, 3, 3, expected_words)
    assert expected_words == actual_words

def test_find_diagonal_negative():
    """Tests that given a gameboard of equal length and width,
    an empty list is returned if no valid words are found moving
    diagionally on the gameboard.
    """
    test_game_board = [['t', 'n', 'q'], ['z', 'd', 'n'], ['v', 'f', 'p']]
    expected_words = []
    actual_words = app.find_words_diagonal(test_game_board, 3, 3, expected_words)
    assert expected_words == actual_words
