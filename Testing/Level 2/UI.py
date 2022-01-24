import tkinter as tk

def sendKeys(keys): #This functions allows the sending of data to the other .py file
    return keys

KEYS = ["w","a","s","d"] #Make this cuztomisable
window = tk.Tk()
window.mainloop()

tk.Label(text="Control Menu")
tk.pack()
Button1 = tk.Entry()
Button1.pack()
Button1TRUE = Button1.get()


'''
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

#diff

master = Tk()

variable = StringVar(master)
variable.set("one") # default value

w = OptionMenu(master, variable, "one", "two", "three")
w.pack()

mainloop()
'''
#Learn Dropdown window