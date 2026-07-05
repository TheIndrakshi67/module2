from datetime import date
from tkinter import *

root = Tk()
root.title("Age Calculator")
root.geometry("250x250")

def calculate():
    age = date.today().year - int(year_input.get())
    result.config(text=f"Age: {age} years old")
    
Label(root, text="Enter Birth Year:").pack(pady=10)
year_input = Entry(root)
year_input.pack()

Button(root, text="Calculate", command=calculate).pack(pady=15)

result = Label(root, text="", font=("Arial", 14))
result.pack()

root.mainloop()
