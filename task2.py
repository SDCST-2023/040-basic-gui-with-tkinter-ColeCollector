import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.geometry("575x175")
window.title("T-Town Veterinary Dental Clinic Database")
dogphoto = PhotoImage(file="dog.png")
image = tk.Label(window, image=dogphoto)
button = tk.Button(window,text="Save Entry",relief=GROOVE)
button2 = tk.Button(window,text="Search by Name",relief=GROOVE)
arrow1 = tk.Button(window,text="< Previous",relief=GROOVE)
arrow2 = tk.Button(window,text="Next >",relief=GROOVE)

label1 = tk.Label(window,text="Client Database")
label3 = tk.Label(window,text="Name")
label4 = tk.Label(window,text="Type")
label5 = tk.Label(window,text="Breed")
label6 = tk.Label(window,text="Owner")
label7 = tk.Label(window,text="Birthdate")
entry1 = tk.Entry(window,width=15)
entry2 = tk.Entry(window,width=15)
entry3 = tk.Entry(window,width=15)
entry4 = tk.Entry(window,width=15)
entry5 = tk.Entry(window,width=15)
entry6 = tk.Entry(window,width=15)


image.place(x=0,y=0)
button.place(x=220,y=150)
button2.place(x=380,y=0)
label1.place(x=210,y=30)
label3.place(x=30,y=100)
label4.place(x=130,y=100)
label5.place(x=230,y=100)
label6.place(x=330,y=100)
label7.place(x=430,y=100)
arrow1.place(x=0,y=150)
arrow2.place(x=535,y=150)
entry1.place(x=480,y=0)
entry2.place(x=5,y=125)
entry3.place(x=105,y=125)
entry4.place(x=205,y=125)
entry5.place(x=305,y=125)
entry6.place(x=405,y=125)



window.mainloop()