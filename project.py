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

def subtract_number():
    n01=int(boxx1.get())
    n02=int(boxx2.get())
    ttotal=n01 - n02
    resultlbl.config(text="The difference is: "+ str(ttotal))
window=Tk()
window.title("Subtraction")
window.geometry("300x200")

labl1=Label(window, text="Type Number 1: ")
labl1.pack()
boxx1=Entry(window)
boxx1.pack()

labl2=Label(window, text="Type number 2: ")
labl2.pack()
boxx2=Entry(window)
boxx2.pack()

gobutton=Button(window, text="Subtract", command=subtract_number)
gobutton.pack()

resultlbl=Label(window,text="")
resultlbl.pack()


def calculate_bmi():
    weight=float(bmi_box1.get())
    height=float(bmi_box2.get())
    bmi_total=weight / (height * height)
    bmi_result_lbl.config(text="The BMI index is: "+ str(round(bmi_total, 2)))
window=Tk()
window.title("BMI Calculator")
window.geometry("300x200")

bmi_lbl1=Label(window, text="Enter Weight (kg): ")
bmi_lbl1.pack()
bmi_box1=Entry(window)
bmi_box1.pack()

bmi_lbl2=Label(window, text="Enter Height (meters): ")
bmi_lbl2.pack()
bmi_box2=Entry(window)
bmi_box2.pack()

bmi_button=Button(window, text="Calculate BMI", command=calculate_bmi)
bmi_button.pack()

bmi_result_lbl=Label(window,text="")
bmi_result_lbl.pack()


window.mainloop()
