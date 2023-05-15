import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.geometry("300x150")
window.title("Example")
label1 = tk.Label(window,text="Text that does\nnothing is a label", bg="#2CCEF7")

label1.place(x=0,y=0)

window.mainloop()