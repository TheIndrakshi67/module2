from tkinter import *

root=Tk()
root.title("Length converter")
root.geometry("250x200")
global cm
cm = 0.0

def convertinches():
    global cm
    inches=float(entry.get())
    cm=inches*2.54
    resultlbl["text"] = f"{inches} inches is {cm} cm"

lbl=Label(root,text="Enter length in inches: ")
lbl.place(x=30, y=20)

entry=Entry(root, width=10)
entry.place(x=30, y=40)
button=Button(root, text="Convert to cm", command=convertinches)
button.place(x=30, y=80)

resultlbl=Label(root, text="")
resultlbl.place(x=30, y =140)

root.mainloop() 
