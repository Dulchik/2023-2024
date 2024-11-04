import tkinter as tk

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=60)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_num, col_num = 1, 0

button_width, button_height = 10, 6

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, command=lambda b=button: entry.delete(0, tk.END), width=button_width, height=button_height).grid(row=row_num,column=col_num)
    elif button == '=':
        tk.Button(root, text=button, command=lambda b=button: calculate(), width=button_width, height=button_height).grid(row=row_num, column=col_num)
    else:
        tk.Button(root, text=button, command=lambda b=button: button_click(b), width=button_width, height=button_height).grid(row=row_num, column=col_num)

    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

def calculate():
    try:
        expresion = entry.get()
        result = eval(expresion)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root.mainloop()