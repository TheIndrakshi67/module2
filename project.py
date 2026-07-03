from tkinter import *

def multiply_number():
    number1=int(box1.get())
    number2=int(box2.get())
    total=number1 * number2
    result_lbl.config(text="The product is: "+ str(total))
window=Tk()
window.title("Multiplication")
window.geometry("300x200")

lbl1=Label(window, text="Type Number 1: ")
lbl1.pack()
box1=Entry(window)
box1.pack()

lbl2=Label(window, text="Type number 2: ")
lbl2.pack()
box2=Entry(window)
box2.pack()

go_button=Button(window, text="Multiply", command=multiply_number)
go_button.pack()

result_lbl=Label(window,text="")
result_lbl.pack()

window.mainloop()