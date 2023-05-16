import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.geometry("255x135")
window.title("Example")
label1 = tk.Label(window,text="A cuddly puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#A4F3FF")
label2 = tk.Label(window,text="Pochacco!")
dogphoto = PhotoImage(file="dog.png")
image = tk.Label(window, image=dogphoto)

image.grid(row = 1, column = 1, columnspan=3)
label2.grid(row = 1, column = 3, columnspan=1)
label1.grid(row = 2, column = 1, columnspan=3)

window.mainloop()