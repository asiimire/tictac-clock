import clock
import tkinter
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Tic Tac")
canvas = tkinter.Canvas(root, width=400, height= 200)

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Roboto", 80), background="black", foreground="cyan")
label.pack(anchor="center")
time()

mainloop()