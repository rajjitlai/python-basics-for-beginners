import tkinter as tk
from tkinter import messagebox

import random
import string

import pyperclip


# generating password function
def generate_password():
    try:
        length = int(user_length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters")
        elif length > 30:
            messagebox.showerror("Error", "Password length cannot be more than 30 characters")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        gen_pass.delete(0, tk.END)
        gen_pass.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length!")


# copying the generated password
def copy_password():
    password = gen_pass.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")


# create the GUI
main_Window = tk.Tk()
main_Window.title("Password Generator")

# labels for entering password length
length_label = tk.Label(main_Window, text="Enter password length:")
length_label.grid(row=0, column=0, padx=5, pady=5)

# input box for the length of the password
user_length_entry = tk.Entry(main_Window)
user_length_entry.grid(row=0, column=1, padx=5, pady=5)

# buttons for generating password
btn = tk.Button(main_Window, text="Generate", command=generate_password)
btn.grid(row=1, column=0, columnspan=2, pady=5)

# labels for generated password
pass_label = tk.Label(main_Window, text="Generated password:")
pass_label.grid(row=2, column=0, padx=5, pady=5)

# generated password
gen_pass = tk.Entry(main_Window, width=25)
gen_pass.grid(row=2, column=1, padx=5, pady=5)

# buttons for copying password
btn2 = tk.Button(main_Window, text="Copy", command=copy_password)
btn2.grid(row=3, column=0, columnspan=2, pady=5)

main_Window.mainloop()
print("The Project ran with 0 errors")

# Try to implement a function which will save the generated password to a file with the time and date
