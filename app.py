import string
import random
import collections
import sys
import argparse

def getValidWords(filePath='words.txt'):
    """Returns a list of valid words read in from a file.

    Keyword arguments:
    filePath -- the path to the file of valid words (default words.txt)
    """
    try:
        with open(filePath) as wordsFile:
            words = wordsFile.read().splitlines()
        return words
    except FileNotFoundError as e:
        sys.exit('File not found, please check the file path and try again.')

def generateBoard(length, width):
    """Generate a gameboard based on a user provided length and width.

    Keyword arguments:
    length -- the length of the board
    width -- the width of the board

    Returns a 2D array with random lowercase letters to represent the gameboard.
    """
    return [[random.choice(string.ascii_lowercase) for i in range(length)] for j in range(width)]

def findWordsDown(board, length, width, validWords):
    """Finds all matching words going down the gameboard.

    Keyword arguments:
    board -- the gameboard to look for words in
    length -- the length of the gameboard
    width -- the width of the gameboard
    validWords -- a list of valid words to compare against
    """
    acceptedWords = []
    for j in range(length):
        word = ''
        for i in range(width):
            word += board[i][j]
            if word in validWords:
                acceptedWords.append(word)
    return acceptedWords


def findWordsUp(board, length, width, validWords):
    """Finds all matching words going up the gameboard.

    Keyword arguments:
    board -- the gameboard to look for words in
    length -- the length of the gameboard
    width -- the width of the gameboard
    validWords -- a list of valid words to compare against
    """
    acceptedWords = []
    for j in range(length - 1, -1, -1):
        word = ''
        for i in range(width - 1, -1, -1):
            word += board[i][j]
            if word in validWords:
                acceptedWords.append(word)
    return acceptedWords

def findWordsAcross(board, length, width, validWords):
    """Finds all matching words going right across the gameboard.

    Keyword arguments:
    board -- the gameboard to look for words in
    length -- the length of the gameboard
    width -- the width of the gameboard
    validWords -- a list of valid words to compare against
    """
    acceptedWords = []
    for i in range(width):
        word = ''
        for j in range(length):
            word += board[i][j]
            if word in validWords:
                acceptedWords.append(word)
    return acceptedWords

def findWordsBackwards(board, length, width, validWords):
    """Finds all matching words going left across the gameboard.

    Keyword arguments:
    board -- the gameboard to look for words in
    length -- the length of the gameboard
    width -- the width of the gameboard
    validWords -- a list of valid words to compare against
    """
    acceptedWords = []
    for i in range(width - 1, -1, -1):
        word = ''
        for j in range(length - 1, -1, -1):
            word += board[i][j]
            if word in validWords:
                acceptedWords.append(word)
    return acceptedWords

def findDiagonalWords(board, length, width, validWords):
    """Finds all matching words diagionally on the gameboard.

    Keyword arguments:
    board -- the gameboard to look for words in
    length -- the length of the gameboard
    width -- the width of the gameboard
    validWords -- a list of valid words to compare against
    """
    acceptedWords = []
    diagonals = collections.defaultdict(list)
    for i in range(length):
        word = ''
        for j in range(width):
            diagonals[j-i].append(board[i][j])

    for i in diagonals:
        word = ''
        for str in diagonals[i]:
            word += str
            if word in validWords:
                acceptedWords.append(word)

    return acceptedWords

def displayBoard(board):
    """Prints the gameboard in an easy to read format.

    Keyword arguments:
    board -- the board to display
    """
    for row in board:
        print(row)


def main():
    parser = argparse.ArgumentParser(description='Generates a gameboard of desired length and width and prints any words found within it.')
    parser.add_argument("-l", "--length", type=int, required=True, help='length of gameboard')
    parser.add_argument("-w", "--width", type=int, required=True, help='width of gameboard')
    parser.add_argument("-sb", "--show-board", action='store_true', required=False, default=False, help='print the gameboard')
    parser.add_argument("-f", "--file", required=False, default='words.txt', help='path to file of valid words to search for')
    args = parser.parse_args()

    results = []
    length = int(args.length)
    width = int(args.width)

    if length != width:
        sys.exit('Length and width must be equal. Please enter equal length and width')

    if length < 0 or width < 0:
        sys.exit('Please enter positive values for length and width')

    validWords = getValidWords(args.file)
    gameBoard = generateBoard(length,width)
    print(gameBoard)

    if args.show_board:
        displayBoard(gameBoard)

    results += findWordsDown(gameBoard, length, width, validWords)
    results += findWordsUp(gameBoard, length, width, validWords)
    results += findWordsAcross(gameBoard, length, width, validWords)
    results += findWordsBackwards(gameBoard, length, width, validWords)
    results += findDiagonalWords(gameBoard, length, width, validWords)

    print('valid words are:')
    for result in set(results):
        print(result)

    return

if __name__ == '__main__':
    main()
