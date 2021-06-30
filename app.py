"""This module will create a grid to represent crossword puzzle of a user
defined size. It will then output any words that match a list of predefined
words that can be specifed from a file.
"""
import string
import random
import collections
import sys
import argparse

def get_valid_words(file_path='words.txt'):
    """Returns a list of valid words read in from a file.

    Keyword arguments:
    file_path -- the path to the file of valid words (default words.txt)
    """
    try:
        with open(file_path) as words_file:
            words = words_file.read().splitlines()
        return words
    except FileNotFoundError:
        sys.exit('File not found, please check the file path and try again.')

def generate_board(length, width):
    """Generate a game_board based on a user provided length and width.

    Keyword arguments:
    length -- the length of the board
    width -- the width of the board

    Returns a 2D array with random lowercase letters to represent the game_board.
    """
    return [[random.choice(string.ascii_lowercase) for i in range(length)] for j in range(width)]

def find_words_down(board, length, width, valid_words):
    """Finds all matching words going down the game_board.

    Keyword arguments:
    board -- the game_board to look for words in
    length -- the length of the game_board
    width -- the width of the game_board
    valid_words -- a list of valid words to compare against
    """
    accepted_words = []
    for j in range(length):
        word = ''
        for i in range(width):
            word += board[i][j]
            if word in valid_words:
                accepted_words.append(word)
    return accepted_words


def find_words_up(board, length, width, valid_words):
    """Finds all matching words going up the game_board.

    Keyword arguments:
    board -- the game_board to look for words in
    length -- the length of the game_board
    width -- the width of the game_board
    valid_words -- a list of valid words to compare against
    """
    accepted_words = []
    for j in range(length - 1, -1, -1):
        word = ''
        for i in range(width - 1, -1, -1):
            word += board[i][j]
            if word in valid_words:
                accepted_words.append(word)
    return accepted_words

def find_words_across(board, length, width, valid_words):
    """Finds all matching words going right across the game_board.

    Keyword arguments:
    board -- the game_board to look for words in
    length -- the length of the game_board
    width -- the width of the game_board
    valid_words -- a list of valid words to compare against
    """
    accepted_words = []
    for i in range(width):
        word = ''
        for j in range(length):
            word += board[i][j]
            if word in valid_words:
                accepted_words.append(word)
    return accepted_words

def find_words_backwards(board, length, width, valid_words):
    """Finds all matching words going left across the game_board.

    Keyword arguments:
    board -- the game_board to look for words in
    length -- the length of the game_board
    width -- the width of the game_board
    valid_words -- a list of valid words to compare against
    """
    accepted_words = []
    for i in range(width - 1, -1, -1):
        word = ''
        for j in range(length - 1, -1, -1):
            word += board[i][j]
            if word in valid_words:
                accepted_words.append(word)
    return accepted_words

def find_words_diagonal(board, length, width, valid_words):
    """Finds all matching words diagionally on the game_board.

    Keyword arguments:
    board -- the game_board to look for words in
    length -- the length of the game_board
    width -- the width of the game_board
    valid_words -- a list of valid words to compare against
    """
    accepted_words = []
    diagonals = collections.defaultdict(list)
    for i in range(length):
        word = ''
        for j in range(width):
            diagonals[j-i].append(board[i][j])

    for i in diagonals:
        word = ''
        for letter in diagonals[i]:
            word += letter
            if word in valid_words:
                accepted_words.append(word)

    return accepted_words

def display_board(board):
    """Prints the game_board in an easy to read format.

    Keyword arguments:
    board -- the board to display
    """
    for row in board:
        print(row)

def main():
    """Main runner for the module. Ensures the proper values are passed in,
    and then calls functions to generate the gameboard and then find any
    matching words. Once completed, it will display the results
    """
    parser = argparse.ArgumentParser(description='Generates a gameboard and prints any words found within it.')
    parser.add_argument("-l", "--length", type=int, required=True, help='length of gameboard')
    parser.add_argument("-w", "--width", type=int, required=True, help='width of game_board')
    parser.add_argument("-sb", "--show-board", action='store_true', required=False, default=False, help='print the game_board')
    parser.add_argument("-f", "--file", required=False, default='words.txt', help='path to file of valid words to search for')
    args = parser.parse_args()

    results = []
    length = int(args.length)
    width = int(args.width)

    if length != width:
        sys.exit('Length and width must be equal. Please enter equal length and width')

    if length < 0 or width < 0:
        sys.exit('Please enter positive values for length and width')

    valid_words = get_valid_words(args.file)
    game_board = generate_board(length,width)

    if args.show_board:
        display_board(game_board)

    results += find_words_down(game_board, length, width, valid_words)
    results += find_words_up(game_board, length, width, valid_words)
    results += find_words_across(game_board, length, width, valid_words)
    results += find_words_backwards(game_board, length, width, valid_words)
    results += find_words_diagonal(game_board, length, width, valid_words)

    print('valid words are:')
    for result in set(results):
        print(result)

if __name__ == '__main__':
    main()
