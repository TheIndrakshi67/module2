
from tkinter import*
from datetime import date

root=Tk()
root.title('Getting started with Widgets')
root.geometry('400x300')

lbl=Label(text="Heyy!", fg="white", bg="#dbc7b4", height=1,width=300)
name_lbl=Label(text="Full Name", bg="#dac5e6")
name_entry=Entry()

def display():
    name=name_entry.get()
    global message
    message="Welcome to the Aplication! \nToday's date is: "
    greet="Hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box=Text(height=3)
btn=Button(text="Begin", command=display, bg="#fc0324", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()