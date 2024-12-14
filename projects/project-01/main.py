import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")

def copy_to_clipboard():
    password = entry_password.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

root = tk.Tk()
root.title("Password Generator")


label_length = tk.Label(root, text="Enter password length:")
label_length.grid(row=0, column=0, padx=5, pady=5)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=5, pady=5)

btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.grid(row=1, column=0, columnspan=2, pady=5)

label_password = tk.Label(root, text="Generated Password:")
label_password.grid(row=2, column=0, padx=5, pady=5)
entry_password = tk.Entry(root, width=25)
entry_password.grid(row=2, column=1, padx=5, pady=5)

btn_copy = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
btn_copy.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
