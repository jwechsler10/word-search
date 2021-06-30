# in order to run tests, set PYTHONPATH='.' and run tests from root
import pytest
import app
import string

def testGetValidWordsExits():
    with pytest.raises(SystemExit):
        app.getValidWords('I-dont-exist.txt')

def testGetValidWords():
    with open('words.txt') as f:
        expectedResult = f.read().splitlines()

    actualResult = app.getValidWords()

    assert expectedResult == actualResult

def testGenerateBoard():
    expectedLength = 5
    expectedWidth = 5
    expectedTotalNumberOfLetters = 25

    gameBoard = app.generateBoard(5,5)

    assert expectedLength == len(gameBoard)
    assert expectedWidth == len(gameBoard[0])
    assert expectedTotalNumberOfLetters == len(gameBoard) * len(gameBoard[0])

    for i in range(expectedLength):
        for j in range(expectedWidth):
            assert gameBoard[i][j] in string.ascii_lowercase

def testFindWordsDown():
    testGameBoard = [['a', 'q'], ['t', 'z']]
    expectedWords = ['at']
    actualWords = app.findWordsDown(testGameBoard, 2, 2, expectedWords)
    assert expectedWords == actualWords

def testFindWordsUp():
    testGameBoard = [['t', 't', 't'], ['o', 'o', 'o'], ['h', 'p', 'l']]
    expectedWords = ['lot', 'pot', 'hot']
    actualWords = app.findWordsUp(testGameBoard, 3, 3, expectedWords)
    assert expectedWords == actualWords

def testFindWordsAcross():
    testGameBoard = [['t', 'o', 'p'], ['r', 'o','d'], ['m', 'e', 't']]
    expectedWords = ['top', 'rod', 'met']
    actualWords = app.findWordsAcross(testGameBoard, 3, 3, expectedWords)
    assert expectedWords == actualWords

def testFindWordsBackwards():
    testGameBoard = [['t', 'a', 'c'], ['p', 'a', 'g'], ['o', 'w', 't']]
    expectedWords = ['two', 'gap', 'cat']
    actualWords = app.findWordsBackwards(testGameBoard, 3, 3, expectedWords)
    assert expectedWords == actualWords

def testFindDiagonal():
    testGameBoard = [['t', 'a', 'q'], ['z', 'o', 'n'], ['v', 'f', 'p']]
    expectedWords = ['top']
    actualWords = app.findWordsDiagonal(testGameBoard, 3, 3, expectedWords)
    assert expectedWords == actualWords

def testFindWordsDownNegative():
    testGameBoard = [['a', 'a'], ['a', 'a']]
    expectedWords = []
    actualWords = app.findWordsDown(testGameBoard, 2, 2, expectedWords)
    assert expectedWords == actualWords

def testFindWordsUpNegative():
    testGameBoard = [['t', 't', 't'], ['z', 'z', 'z'], ['h', 'h', 'h']]
    expectedWords = []
    actualWords = app.findWordsUp(testGameBoard, 3, 3, expectedWords)
    assert expectedWords == actualWords

def testFindWordsAcrossNegative():
    testGameBoard = [['q', 'q', 'p'], ['r', 'z','d'], ['m', 'g', 't']]
    expectedWords = []
    actualWords = app.findWordsAcross(testGameBoard, 3, 3, expectedWords)
    assert expectedWords == actualWords

def testFindWordsBackwards():
    testGameBoard = [['t', 'q', 'c'], ['p', 'k', 'l'], ['n', 'w', 'x']]
    expectedWords = []
    actualWords = app.findWordsBackwards(testGameBoard, 3, 3, expectedWords)
    assert expectedWords == actualWords

def testFindDiagonal():
    testGameBoard = [['t', 'n', 'q'], ['z', 'd', 'n'], ['v', 'f', 'p']]
    expectedWords = []
    actualWords = app.findWordsDiagonal(testGameBoard, 3, 3, expectedWords)
    assert expectedWords == actualWords
