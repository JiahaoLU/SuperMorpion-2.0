import tkinter as tk
from tkinter import ttk
from socket import *

class Server_window():
    def __init__(self):
        self.adress = gethostbyname(gethostname())
        self.root = tk.Tk()

    def show_adress(self):
        l1 = tk.Label(self.root, text = 'the server IP is: ' + self.adress)
        l1.pack()
        ttk.Button(self.root, text="OK", command = self.on_click).pack()
        self.center_window()
        self.root.wm_attributes('-topmost',1)
        self.root.mainloop()

    def on_click(self):
        self.root.destroy()

    def center_window(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - self.root.winfo_width()/2
        y = (hs/2) - self.root.winfo_height()/2
        self.root.geometry('+%d+%d' % (x, y))



class Type_in_window():
    def __init__(self):
        '''
        the class where the log-in window is created
        '''
        self.root = tk.Tk()
        self.name = None
        self.ip = None

    def type_in(self):
        '''
        graphique and button of the window. When the button is clicked, info in the text boxes will be registered.
        :return:
        '''
        self.root.title("Welcome to SuperMorpion")
        self.root.geometry('300x300')

        photo = tk.PhotoImage(file="./welcome.gif")
        imglabel = tk.Label(self.root, image=photo)
        imglabel.pack()
        slogan = tk.Label(self.root, text="Please log in",font = ('Arial', 20))
        slogan.pack()

        l1 = tk.Label(self.root, text="username")
        l1.pack()
        global username
        username = tk.StringVar()
        uns = tk.Entry(self.root, textvariable = username)
        username.set("player_client")
        uns.pack()

        l2 = tk.Label(self.root, text="ip")
        l2.pack()
        global ip_adress
        ip_adress = tk.StringVar()
        sheet = tk.Entry(self.root, textvariable = ip_adress)
        ip_adress.set("")
        sheet.pack()
        ttk.Button(self.root, text="OK", command = self.on_click).pack()
        self.root.mainloop()

    def on_click(self):
        '''
        The click-button movement
        :return:
        '''
        self.name = username.get()
        self.ip = ip_adress.get()
        self.ip = self.ip.replace(' ', '')
        self.root.destroy()


if __name__ == '__main__':
    tiw = Type_in_window()
    tiw.type_in()
    print((' ' in tiw.ip))
