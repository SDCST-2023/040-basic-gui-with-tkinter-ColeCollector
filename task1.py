import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.geometry("305x100")
entry1 = tk.Entry(window,width=10)
entry2 = tk.Entry(window,width=10)
entry3 = tk.Entry(window,width=15)
label1 = tk.Label(window,text="x")
label2 = tk.Label(window,text="=",relief=GROOVE)

entry1.grid(row = 1, column = 1, columnspan=3)
entry2.grid(row = 1, column = 5, columnspan=3)
entry3.grid(row = 1, column = 12, columnspan=3)
label1.grid(row = 1, column = 4, columnspan=1)
label2.grid(row = 1, column = 10, columnspan=1)

window.mainloop()

