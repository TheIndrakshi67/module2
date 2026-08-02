import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("Letter Writing Application")
root.geometry("400x450")

txt = tk.Text(root, width=45, height=20)
txt.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

def open_file():
    path = filedialog.askopenfilename()
    if path:
        root.title(path)
        f = open(path, "r")
        content = f.read()
        f.close()
        txt.delete("1.0", tk.END)
        txt.insert("1.0", content)

def save_file():
    path = filedialog.asksaveasfilename()
    if path:
        root.title(path)
        content = txt.get("1.0", tk.END)
        f = open(path, "w")
        f.write(content)
        f.close()

btn_open = tk.Button(root, text="Open File", command=open_file)
btn_open.grid(row=1, column=0, pady=10)

btn_save = tk.Button(root, text="Save File", command=save_file)
btn_save.grid(row=1, column=1, pady=10)

root.mainloop()
