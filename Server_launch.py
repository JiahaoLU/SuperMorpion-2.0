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
    try:
        server_client = Process(target=server,args=(),)
        server_client.start()
    except OSError:
        print("OSError: each Socket adress can onlu be used once, try to check that server is not already launched locally")
    else:
        process_client = Process(target=client_game,args=(),)
        ip_window = Type_in.Server_window()
        ip_window.show_adress()
        time.sleep(1)
        process_client.start()
if __name__ == '__main__':
    main()
