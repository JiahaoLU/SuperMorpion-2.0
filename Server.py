# Save as server.py
# Message Receiver
import os
from socket import *
import threading
from Server_Instructions import *

def handle(clist):#server task function # pseudo-mainthread
    print("Waiting to receive messages...")
    while len(clist) < 2: #wait until 2 clients are all connected
        print(len(clist),'client(s) have(has) connected')
        pass
    thread_over = threading.Event() #thread1 or thread2 over flag. initialize to False
    try:
        td11 = threading.Thread(target = thread11, args = (clist,thread_over,),daemon= True)# subthread1 for receiving messenges from client0 and sending it to client1
        td12 = threading.Thread(target = thread12, args = (clist,thread_over,),daemon= True)# subthread2 for receiving messenges from client1 and sending it to client0
        td21 = threading.Thread(target = thread21, args = (clist,thread_over,),daemon= True)# subthread1 for receiving messenges from client0 and sending it to client1
        td22 = threading.Thread(target = thread22, args = (clist,thread_over,),daemon= True)# subthread2 for receiving messenges from client1 and sending it to client0
        td21.start()
        td22.start()
        td11.start()
        td12.start()
    except:
        print("Error: unable to start thread")# if Error, raise it up and quit socket
        TCPSock.close()
        os._exit(0)
    while not thread_over.is_set():
        pass
    print('main thread over')
    TCPSock.close()
    os._exit(0)




def thread11(clist,thread_over):
    while True: #when game is not end
        data12_append = clist[0].recv(buf).decode()
        print("Received message: " + data12_append,' from player1')
        Server_ins_12.append(data12_append)

def thread12(clist,thread_over):
    while True: #when game is not end
        if len(Server_ins_12) != 0:
            data12_pop = Server_ins_12.popleft()
            clist[1].send(data12_pop.encode())
            if data12_pop == "exit":
                thread_over.set()

def thread21(clist,thread_over):
    while True: #when game is not end
        data21_append = clist[1].recv(buf).decode()
        print("Received message: " + data21_append,' from player1')
        Server_ins_21.append(data21_append)

def thread22(clist,thread_over):
    while True: #when game is not end
        if len(Server_ins_21) != 0:
            data21_pop = Server_ins_21.popleft()
            clist[0].send(data21_pop.encode())
            if data21_pop == "exit":
                thread_over.set()

host = gethostname()
ip = gethostbyname(host)
print(ip)
port = 8080
buf = 10000
addr = (host, port)
TCPSock = socket(AF_INET, SOCK_STREAM)
TCPSock.bind(addr)
TCPSock.listen(100)
clist = []

th = threading.Thread(target=handle,args = (clist,))
th.start()

while True:
    c, addr = TCPSock.accept()
    clist.append(c)


