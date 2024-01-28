import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    password_length = int(entry_length.get())
    generated_password = generate_password(password_length)
    label_result.config(text=f"Generated Password: {generated_password}")

root = tk.Tk()
root.title("Password Generator")


label_length = ttk.Label(root, text="Enter password length:")
label_length.grid(row=0, column=0)

entry_length = ttk.Entry(root)
entry_length.grid(row=0, column=1)

generate_button = ttk.Button(root, text="Generate Password", command=generate_button_clicked)
generate_button.grid(row=1, column=0)

label_result = ttk.Label(root, text="")
label_result.grid(row=2, column=0)

root.mainloop()
