import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Stationery Order Management App")
root.geometry("500x400")

is_usd = True

canvas = tk.Canvas(root, width=500, height=100, bg="lightblue")
canvas.pack(fill="x")
canvas.create_text(250, 50, text="Stationery Shop", font=("Arial", 20))

items = ["Notebook", "Pen", "Eraser", "Ruler"]
prices_inr = [80, 20, 10, 30]

entries = []

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

for i, item in enumerate(items):
    lbl_item = ttk.Label(frame, text=item, font=("Arial", 12))
    lbl_item.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    
    if is_usd:
        price = prices_inr[i] / 80
        currency = "$"
    else:
        price = prices_inr[i]
        currency = "₹"
    
    price_text = currency + str(price)
    lbl_price = ttk.Label(frame, text=price_text, font=("Arial", 12))
    lbl_price.grid(row=i, column=1, padx=10, pady=5)
    
    ent_qty = ttk.Entry(frame, width=5)
    ent_qty.grid(row=i, column=2, padx=10, pady=5)
    ent_qty.insert(0, "0")
    entries.append(ent_qty)

if is_usd:
    lbl_total = ttk.Label(root, text="Total: $0", font=("Arial", 14))
else:
    lbl_total = ttk.Label(root, text="Total: ₹0", font=("Arial", 14))
lbl_total.pack(pady=10)

def calculate_total():
    grand_total = 0
    for i, entry in enumerate(entries):
        val = entry.get()
        if val.isdigit():
            qty = int(val)
            if is_usd:
                item_price = prices_inr[i] / 80
            else:
                item_price = prices_inr[i]
            grand_total = grand_total + (qty * item_price)
            
    if is_usd:
        currency = "$"
    else:
        currency = "₹"
        
    final_text = "Total: " + currency + str(grand_total)
    lbl_total.config(text=final_text)

btn_calc = ttk.Button(root, text="Calculate Total", command=calculate_total)
btn_calc.pack(pady=5)

root.mainloop()
