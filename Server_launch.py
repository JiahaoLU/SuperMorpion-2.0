from Server import *
from TDGUI import *
from multiprocessing import Process
import Type_in


def main():
    '''
    when the main() is executed, the server thread is launched as well as the client thread so that the server plays as well
    as one client.
    :return:
    '''
    server_client = Process(target=server,args=(),)
    process_client = Process(target=client_game,args=(),)
    server_client.start()
    time.sleep(1)
    process_client.start()
    ip_window = Type_in.Server_window()
    ip_window.show_adress()

if __name__ == '__main__':
    main()
