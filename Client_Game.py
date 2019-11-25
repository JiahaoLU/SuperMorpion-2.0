import os
from socket import *
import threading
import Client_Instructions
import time


def handle(tcpSock):
    '''
    pseudo-mainthread for running the client-side functions
    :param tcpSock: an instance of sockect connection
    :return: none
    '''
    try:
        th1 = threading.Thread(target=thread1, args=(tcpSock,), daemon=True)# thread1 for receiving messenges from client1 and sending it to client0
        th1.start()
    except:
        print("Error: unable to start thread")
        tcpSock.close()
        os._exit(0)


def thread1(TCPSock):
    '''
    sub-thread for receiving messenges from one client and sending it to another
    :param TCPSock: an instance of sockect connection
    :return: none
    '''
    counter_send = 0
    while True:# when game is not end
        while len(Client_Instructions.Client_ins_send) != 0:
            to_send = Client_Instructions.Client_ins_send.popleft()
            print('counter_send: ', counter_send)
            print('send data pop:', to_send)
            TCPSock.send(to_send.encode())
            if to_send == 'exit':
                TCPSock.close()
                os._exit(0)
            time.sleep(0.05)


def client(host):
    '''
    the main function to establish the socket binding and execute the threads
    :param host: the IP adress of the server, input manually by the player
    :return: none
    '''
    global counter_send
    counter_send = 0
    port = 8080
    print(host)
    addr = (host, port)
    print('host'+host)
    TCPSock = socket(AF_INET, SOCK_STREAM)
    try:
        TCPSock.connect(addr)
    except ConnectionRefusedError:
        print("ConnectionRefusedError: can't connect to the aiming adress")
        TCPSock.close()
        os._exit(0)
    else:
        th = threading.Thread(target=handle,args=(TCPSock,),daemon= True)
        th.start()

        # main thread to receive info from server
        while True: # when game is not end
            data = TCPSock.recv(1024).decode()
            print("Received message: " + data)
            if data == 'setPlayer1':
                Client_Instructions.Client_player = True
            elif data == 'setPlayer2':
                pass
            else:
                Client_Instructions.Client_ins_rece.append(data)
                print('received data append:'+data)
                if data == 'exit':
                    break
        TCPSock.close()
        os._exit(0)


