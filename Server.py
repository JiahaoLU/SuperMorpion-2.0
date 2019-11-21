import os
from socket import *
import threading
import time


def handle(clist,TCPSock,buf):
    '''
    server task function pseudo-mainthread
    :param clist: a list to stock players connected by socket
    :param TCPSock: an instance of sockect connection
    :param buf: the buffer size of data for recv()
    :return: none
    '''
    print("Waiting to receive messages...")
    while len(clist) < 2:  # wait until 2 clients are all connected
        print(len(clist))
        time.sleep(1)
    thread_over = threading.Event()  # thread1 or thread2 over flag. initialize to False
    try:
        td1 = threading.Thread(target = thread1, args = (clist,thread_over,buf,),daemon= True)  # subthread1 for receiving messenges from client0 and sending it to client1
        td2 = threading.Thread(target = thread2, args = (clist,thread_over,buf,),daemon= True)  # subthread2 for receiving messenges from client1 and sending it to client0
        td1.start()
        td2.start()
    except:
        print("Error: unable to start thread")  # if Error, raise it up and quit socket
        TCPSock.close()
        os._exit(0)
    while not thread_over.is_set():
        pass
    print('main thread over')
    TCPSock.close()
    os._exit(0)


def thread1(clist,thread_over,buf):
    """
    subthread1 for receiving messenges from client0 and sending it to client1
    :param thread_over: flag over the thread to monitor if it is ended, initialised to false
    :return:
    """
    clist[0].send("setPlayer1".encode())
    while True:  # when game is not end
        data = clist[0].recv(buf).decode()
        print("Received message: " + data,' from player1')
        clist[1].send(data.encode())
        if data == "exit":
            thread_over.set()


def thread2(clist,thread_over,buf):
    """
    subthread2 for receiving messenges from client1 and sending it to client0
    :return:
    """
    clist[1].send("setPlayer2".encode())
    while True: #when game is not end
        data = clist[1].recv(buf).decode()
        print("Received message: " + data,' from player2')
        clist[0].send(data.encode())
        if data == "exit":
            thread_over.set()


def server():
    '''
    the main function to establish the socket binding and execute the threads for the server
    :return:
    '''
    host = gethostname()
    ip = gethostbyname(host)
    print(ip)
    port = 8080
    buf = 1024
    addr = (host, port)
    TCPSock = socket(AF_INET, SOCK_STREAM)
    TCPSock.bind(addr)
    TCPSock.listen(100)
    clist = []

    th = threading.Thread(target=handle,args = (clist,TCPSock,buf,))
    th.start()

    while len(clist) < 2:
        c, addr = TCPSock.accept()
        clist.append(c)


if __name__ == '__main__':
    server()

