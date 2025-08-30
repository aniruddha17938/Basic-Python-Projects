import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length should be at least 4")
            return

        characters = ""
        if use_upper.get():
            characters += string.ascii_uppercase
        if use_lower.get():
            characters += string.ascii_lowercase
        if use_digits.get():
            characters += string.digits
        if use_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Selection Error", "Please select at least one character set!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Input Error", "Enter a valid number for length!")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Window
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.config(bg="lightgray")

# Title
tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="lightgray").pack(pady=10)

# Password Length
tk.Label(root, text="Enter Password Length:", bg="lightgray").pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkbuttons for character sets
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=use_upper, bg="lightgray").pack()
tk.Checkbutton(root, text="Include Lowercase", variable=use_lower, bg="lightgray").pack()
tk.Checkbutton(root, text="Include Digits", variable=use_digits, bg="lightgray").pack()
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols, bg="lightgray").pack()

# Output Password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Courier", 12), justify="center").pack(pady=10)

# Buttons
tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="blue", fg="white").pack()

root.mainloop()
