import tkinter as tk
import pyautogui
import threading
import time

class AutoClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("AutoClicker")

        self.click_rate_label = tk.Label(master, text="Click Rate (clicks per second):")
        self.click_rate_label.pack()

        self.click_rate_entry = tk.Entry(master)
        self.click_rate_entry.pack()

        self.start_button = tk.Button(master, text="Start AutoClicker", command=self.start_autoclicker)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop AutoClicker", command=self.stop_autoclicker, state=tk.DISABLED)
        self.stop_button.pack()

        self.is_running = False
        self.click_rate = 0

    def start_autoclicker(self):
        try:
            self.click_rate = float(self.click_rate_entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input for click rate.")
            return

        if self.click_rate <= 0:
            tk.messagebox.showerror("Error", "Click rate must be greater than zero.")
            return

        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Start a new thread for autoclicking
        click_thread = threading.Thread(target=self.autoclick_thread)
        click_thread.start()

    def stop_autoclicker(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def autoclick_thread(self):
        while self.is_running:
            pyautogui.click()
            time.sleep(self.click_rate)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x100")
    app = AutoClickerApp(root)
    root.mainloop()
