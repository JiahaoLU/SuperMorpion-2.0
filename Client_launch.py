from TDGUI import *
from Type_in import *


def main():
    '''
    when main() is launched, the IP adress and the player name will be demanded in a log-in window. Then the player will
    get acess to the chessboard and start the game.
    :return: none
    '''
    tiw = Type_in_window()
    tiw.type_in()
    client_game(tiw.ip)


if __name__ == '__main__':
    main()
