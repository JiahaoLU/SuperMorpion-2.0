import os
from socket import *
import threading
import Client_Instructions
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
        if len(Client_Instructions.Client_ins_send) != 0:
            to_send = Client_Instructions.Client_ins_send.popleft()
            print('send data pop:',to_send)
            # print(type(to_send))
            TCPSock.send(to_send.encode())
            if to_send == 'exit':
                TCPSock.close()
                os._exit(0)
            to_send = None


def client():
# def main():
    host = "138.195.243.44" # set to IP address of target computer
    port = 2101
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
# if __name__ == '__main__':
#     main()

