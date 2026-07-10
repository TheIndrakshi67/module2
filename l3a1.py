from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("the button was clicked.")

button=Button(window,text="Button")
button.bind("<Button-1>", handle_click)
button.pack()
window.mainloop()

