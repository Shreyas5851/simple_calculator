import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        current = entry.get()
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear_entry():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Create the main window
root = tk.Tk()
root.title("Sophisticated Calculator")

# Entry widget for input and display
entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons
row = 1
col = 0
buttons = []

for text in button_texts:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 20))
    button.grid(row=row, column=col)
    buttons.append(button)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Bind button clicks
for i, text in enumerate(button_texts):
    if text == '=':
        buttons[i].config(command=calculate)
    elif text == 'C':
        buttons[i].config(command=clear)
    elif text == '⌫':
        buttons[i].config(command=clear_entry)
    else:
        buttons[i].config(command=lambda t=text: button_click(t))

# Additional buttons
clear_button = tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 20), command=clear)
clear_button.grid(row=5, column=0)

backspace_button = tk.Button(root, text="⌫", padx=20, pady=20, font=('Arial', 20), command=clear_entry)
backspace_button.grid(row=5, column=1)

# Start the main loop
root.mainloop()
