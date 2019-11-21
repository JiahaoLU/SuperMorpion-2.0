from TDGUI import *
import pytest


class TestClass:
    # column
    def test_1(setup_module):
        print('Test_1 called.')
        morpion = Morpion()
        morpion.chessboard[1][1][1] = 1
        morpion.chessboard[1][1][0] = 1
        morpion.chessboard[1][1][2] = 1
        print(morpion.chessboard)
        assert (morpion.iswin() is True)

    #row
    def test_2(setup_module):
        print('Test_2 called.')
        morpion = Morpion()
        morpion.chessboard[1][0][1] = 1
        morpion.chessboard[1][1][1] = 1
        morpion.chessboard[1][2][1] = 1
        print(morpion.chessboard)
        assert morpion.iswin() is True

    # player2
    def test_3(setup_module):
        print('Test_3 called.')
        morpion = Morpion()
        morpion.chessboard[0][1][1] = -1
        morpion.chessboard[1][1][1] = -1
        morpion.chessboard[2][1][1] = -1
        print(morpion.chessboard)
        assert morpion.iswin() is True

    #left-up right-down
    def test_4(setup_module):
        print('Test_4 called.')
        morpion = Morpion()
        morpion.chessboard[1][0][0] = 1
        morpion.chessboard[1][1][1] = 1
        morpion.chessboard[1][2][2] = 1
        print(morpion.chessboard)
        assert morpion.iswin() is True

    #left-down right-up
    def test_5(setup_module):
        print('Test_5 called.')
        morpion = Morpion()
        morpion.chessboard[1][0][2] = 1
        morpion.chessboard[1][1][1] = 1
        morpion.chessboard[1][2][0] = 1
        print(morpion.chessboard)
        assert morpion.iswin() is True

    # left-downstairs right-upstairs
    def test_6(setup_module):
        print('Test_5 called.')
        morpion = Morpion()
        morpion.chessboard[0][0][2] = 1
        morpion.chessboard[1][1][1] = 1
        morpion.chessboard[2][2][0] = 1
        print(morpion.chessboard)
        assert morpion.iswin() is True

    # left-upstairs right-downstairs
    def test_7(setup_module):
        print('Test_5 called.')
        morpion = Morpion()
        morpion.chessboard[0][2][0] = 1
        morpion.chessboard[1][1][1] = 1
        morpion.chessboard[2][0][2] = 1
        print(morpion.chessboard)
        assert morpion.iswin() is True


if __name__ == "__main__":
    pytest.main()
