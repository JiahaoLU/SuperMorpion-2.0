import os
from socket import *
import threading
def handle(TCPSock):# pseudo-mainthread
    try:
        th1 = threading.Thread(target = thread1,args=(TCPSock,),daemon= True)# thread1 for receiving messenges from client1 and sending it to client0
        th1.start()
    except:
        print("Error: unable to start thread")
        TCPSock.close()
        os._exit(0)

# sub-thread for receiving messenges from client1 and sending it to client0
def thread1(TCPSock):
    while True: #when game is not end
        to_send = input()
        # print(type(to_send))
        TCPSock.send(to_send.encode())
        if to_send == 'exit':
            TCPSock.close()
            os._exit(0)


def client():
# def main():
    host = "138.195.245.214" # set to IP address of target computer
    port = 13000
    addr = (host, port)
    TCPSock = socket(AF_INET, SOCK_STREAM)
    TCPSock.connect(addr)
    th = threading.Thread(target=handle,args=(TCPSock,),daemon= True)
    th.start()

    # main thread to receive info from server
    while True: #when game is not end
        data = TCPSock.recv(1024).decode()
        print("Received message: " + data)
        if data == 'setPlayer1':
            pass
        elif data == 'setPlayer2':
            pass
        elif data == 'exit':
            break
    TCPSock.close()
    os._exit(0)
if __name__ == '__main__':
    client()
