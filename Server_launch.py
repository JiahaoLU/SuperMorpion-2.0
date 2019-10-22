from Server import *
from TDGUI import *
from multiprocessing import Process,Pipe

def main():
    server_client = Process(target=server,args=(),)
    process_client = Process(target=client_game,args=(),)
    server_client.start()
    time.sleep(1)
    process_client.start()

if __name__ == '__main__':
    main()
