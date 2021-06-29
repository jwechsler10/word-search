import string
import random

def getValidWords():
    with open('words.txt') as wordsFile:
        words = wordsFile.read().splitlines()

    return words


def generateBoard(length, width):
    board = [[random.choice(string.ascii_lowercase) for i in range(length)] for j in range(width)]
    for row in board:
        print(row)

    print(board)
    return board

def findWords(board, length, width, validWords):
# down
    for j in range(length):
        word = ''
        for i in range(width):
            word += board[i][j]
            if word in validWords:
                print('found valid word ' + word)
            print(word)

# up
    for j in range(length - 1, -1, -1):
        word = ''
        for i in range(width - 1, -1, -1):
            word += board[i][j]
            if word in validWords:
                print('found valid word ' + word)
            print(word)

# right
    for i in range(width):
        word = ''
        for j in range(length):
            word += board[i][j]
            if word in validWords:
                print('found valid word ' + word)
            print(word)

# left
    for i in range(width - 1, -1, -1):
        word = ''
        for j in range(length - 1, -1, -1):
            word += board[i][j]
            if word in validWords:
                print('found valid word ' + word)
            print(word)

def main():

    # get board values from CLI input
    length = 2
    width = 3

    validWords = getValidWords()
    gameBoard = generateBoard(length,width)
    findWords(gameBoard, length, width, validWords)

    return

if __name__ == '__main__':
    main()
