import ttkbootstrap as ttk
import tkinter as tk

def button_func():
    print("A button was pressed")

window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x600")

label = ttk.Label(master=window, text="This is a test")
label.pack()

text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="A button", command=button_func)
button.pack()

def button_ex():
    print("Hello")

# exercise
label_ex = ttk.Label(master=window, text=f"My label")
label_ex.pack()
buttonEx = ttk.Button(master=window, command=button_ex)
buttonEx.pack()

window.mainloop()