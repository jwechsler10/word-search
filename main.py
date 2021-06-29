import string
import random
import collections

"""Returns  """
def getValidWords():
    with open('words.txt') as wordsFile:
        words = wordsFile.read().splitlines()

    return words

def generateBoard(length, width):
    return [[random.choice(string.ascii_lowercase) for i in range(length)] for j in range(width)]

def findWordsDown(board, length, width, validWords):
    acceptedWords = []
    for j in range(length):
        word = ''
        for i in range(width):
            word += board[i][j]
            if word in validWords:
                acceptedWords.append(word)
    return acceptedWords


def findWordsUp(board, length, width, validWords):
    acceptedWords = []
    for j in range(length - 1, -1, -1):
        word = ''
        for i in range(width - 1, -1, -1):
            word += board[i][j]
            if word in validWords:
                acceptedWords.append(word)
    return acceptedWords

def findWordsAcross(board, length, width, validWords):
    acceptedWords = []
    for i in range(width):
        word = ''
        for j in range(length):
            word += board[i][j]
            if word in validWords:
                acceptedWords.append(word)
    return acceptedWords

def findWordsBackwards(board, length, width, validWords):
    acceptedWords = []
    for i in range(width - 1, -1, -1):
        word = ''
        for j in range(length - 1, -1, -1):
            word += board[i][j]
            if word in validWords:
                acceptedWords.append(word)
    return acceptedWords

def findDiagonalWords(board, length, width, validWords):
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

def displayBoard(gameBoard):
    for row in gameBoard:
        print(row)

def main():
    results = []
    displayBoard = False

    # get board values from CLI input
    length = 15
    width = 15

    validWords = getValidWords()
    gameBoard = generateBoard(length,width)

    # if desired display board
    if displayBoard:
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
