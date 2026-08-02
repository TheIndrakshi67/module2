import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Reading Planner")
root.geometry("300x200")

def open_planner():
    win = tk.Toplevel(root)
    win.title("Planner Window")
    win.geometry("300x250")
    
    lbl1 = tk.Label(win, text="Total Pages:")
    lbl1.pack(pady=5)
    ent1 = tk.Entry(win)
    ent1.pack(pady=5)
    
    lbl2 = tk.Label(win, text="Pages Per Day:")
    lbl2.pack(pady=5)
    ent2 = tk.Entry(win)
    ent2.pack(pady=5)
    
    lbl_res = tk.Label(win, text="")
    lbl_res.pack(pady=10)
    
    def calculate():
        try:
            total = int(ent1.get())
            per_day = int(ent2.get())
            days = total // per_day
            rem = total % per_day
            lbl_res.config(text="Days: " + str(days) + ", Leftover: " + str(rem))
        except:
            messagebox.showerror("Error", "Enter valid numbers")
            
    btn = tk.Button(win, text="Calculate", command=calculate)
    btn.pack(pady=5)

btn_open = tk.Button(root, text="Open Planner", command=open_planner)
btn_open.pack(pady=50)

root.mainloop()
