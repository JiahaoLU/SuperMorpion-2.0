import tkinter as tk
from tkinter import ttk

class Type_in_window():
    def __init__(self):
        self.root = tk.Tk()
        self.name = None
        self.ip = None

    def type_in(self):
        self.root.title("information ")
        self.root.geometry('300x300')

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
        self.name = username.get()
        self.ip = ip_adress.get()
        self.ip = self.ip.replace(' ','')
        self.root.destroy()

if __name__ == '__main__':
    tiw = Type_in_window()
    tiw.type_in()
    print((' ' in tiw.ip))
