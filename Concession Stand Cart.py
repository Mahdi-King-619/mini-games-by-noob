import tkinter as tk
from tkinter import simpledialog, messagebox
menu = {
    "Popcorn": 5.99,
    "50 Cent Chicken": 0.50,
    "Ice-cream": 1.99,
    "Coke": 0.99,
    "Pizza": 3.99,
    "Chocolate Cupcake": 2.09,
    "Chicken": 1.69,
    "Mini Burger": 2.51,
    "Medium Burger": 3.99,
    "Large Burger": 4.99,
    "Extra Large Burger": 5.99,
    "Nachos": 1.99,
    "Lemonade": 4.25,
    "Pretzels": 3.50,
    "Fries": 2.50,
    "Chips": 1.00
}
cart = {}
total = 0.0
def add_to_cart(item, price):
    global total
    qty = simpledialog.askinteger("Quantity", f"How many {item}?", minvalue=1, parent=root)
    if qty:
        cart[item] = cart.get(item, 0) + qty
        total += price * qty
        status_label.config(text=f"{item} x{qty} added! Current total: ${total:.2f}")
def checkout():
    if not cart:
        messagebox.showinfo("Cart Summary", "Your cart is empty!")
        return
    summary = "Your Cart:\n\n"
    for item, qty in cart.items():
        summary += f"{item} x{qty} = ${menu[item] * qty:.2f}\n"
    summary += f"\nTotal: ${total:.2f}"
    messagebox.showinfo("Cart Summary", summary)
    root.quit()
root = tk.Tk()
root.title("Concession Stand Cart")
root.geometry("1000x650")
root.resizable(width=False, height=False)
intro_text = (
    "Welcome to Concession Stand Cart!\n"
    "Click on an item, enter how many you want,\n"
    "and when finished click Quit to see your total."
)
intro_label = tk.Label(root, text=intro_text, wraplength=500, justify="left", fg="DarkGreen")
intro_label.pack(pady=10)
for item, price in menu.items():
    btn = tk.Button(root, text=f"{item}: ${price:.2f}", width=30, fg="green",
                    command=lambda i=item, p=price: add_to_cart(i, p))
    btn.pack(pady=2)
status_label = tk.Label(root, text="Cart: (empty)\nTotal: $0.00", fg="black")
status_label.pack(pady=10)
quit_btn = tk.Button(root, text="Quit", width=30, fg="red", command=checkout)
quit_btn.pack(pady=10)
root.mainloop()
