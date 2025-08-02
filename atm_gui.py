import tkinter as tk

class ATMApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ATM PIN Entry")
        self.root.geometry("300x150")

        self.label = tk.Label(self.root, text="Enter your PIN", font=("Arial", 16))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, show="*", font=("Arial", 16))
        self.entry.pack()

        self.warning_window = None  # to track the warning popup window

    def show_warning(self):
        if self.warning_window is None or not self.warning_window.winfo_exists():
            self.warning_window = tk.Toplevel(self.root)
            self.warning_window.title("⚠ Security Alert")
            self.warning_window.geometry("250x100")
            label = tk.Label(self.warning_window, text="⚠ Shoulder surfing detected!", fg="red", font=("Arial", 12))
            label.pack(pady=20)
            self.warning_window.lift()

    def reset(self):
        if self.warning_window and self.warning_window.winfo_exists():
            self.warning_window.destroy()
