from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x200")
root.title("Alert")
def show_warning():
    messagebox.showwarning("Alert", "Stop! Virus Found.")
button=Button(root, text="Scan for Virus", command=show_warning)
button.place(x=40,y=60)

root.mainloop()