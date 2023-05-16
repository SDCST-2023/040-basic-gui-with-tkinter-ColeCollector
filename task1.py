import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.geometry("420x30")
entry1 = tk.Entry(window,width=17)
entry2 = tk.Entry(window,width=17)
entry3 = tk.Entry(window,width=30)
label1 = tk.Label(window,text="x")
label2 = tk.Button(window,text="=",relief=GROOVE)

entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
label2.pack(side=LEFT)
entry3.pack(side=LEFT)

def click(e):
    n1 = int(entry1.get())
    n2 = int(entry2.get())
    sum = n1 * n2
    entry3.delete(0,tk.END)
    entry3.insert(0,sum)

label2.bind("<Button-1>",click)
window.mainloop()

