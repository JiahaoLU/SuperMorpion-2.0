from TDGUI import *
from multiprocessing import Process
from Type_in import *

def main():
    tiw = Type_in_window()
    tiw.type_in()


    client_game(tiw.ip)

if __name__ == '__main__':
    main()
