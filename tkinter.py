import tkinter as tk
from tkinter import ttk, messagebox
import string
import random
import time

def check_password_strength(password):
    strength = 0
    criteria = [
        (len(password) >= 8, "Length >= 8"),
        (any(c.isdigit() for c in password), "Has Number"),
        (any(c in string.punctuation for c in password), "Has Symbol"),
    ]
    
    for condition, _ in criteria:
        if condition:
            strength += 1
    
    if strength == 0:
        return "😡 Weak", "red"
    elif strength == 1:
        return "😬 Medium", "orange"
    else:
        return "💪 Strong", "green"

def update_strength_meter(*args):
    password = entry.get()
    strength_text, color = check_password_strength(password)
    strength_label.config(text=strength_text, fg=color)
    strength_bar['value'] = len(password) * 10  

def generate_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    suggested_password = ''.join(random.choice(characters) for _ in range(12))
    entry.delete(0, tk.END)
    entry.insert(0, suggested_password)
    update_strength_meter()

def apply_theme(theme):
    if theme == "Cyberpunk":
        root.config(bg="#000000")
        strength_label.config(bg="#000000", fg="#FF00FF")
        entry.config(bg="#222222", fg="#FFFF00")
    elif theme == "Soft Pastel":
        root.config(bg="#D8BFD8")
        strength_label.config(bg="#D8BFD8", fg="#4169E1")
        entry.config(bg="#E6E6FA", fg="#4682B4")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", font=("Arial", 10))

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=10)
entry.bind("<KeyRelease>", update_strength_meter)

strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack()

strength_bar = ttk.Progressbar(root, length=200, mode='determinate')
strength_bar.pack(pady=5)

suggest_button = ttk.Button(root, text="Suggest Strong Password", command=generate_strong_password)
suggest_button.pack(pady=5)

theme_var = tk.StringVar(value="Cyberpunk")
theme_menu = ttk.Combobox(root, textvariable=theme_var, values=["Cyberpunk", "Soft Pastel"], state="readonly")
theme_menu.pack(pady=5)
theme_menu.bind("<<ComboboxSelected>>", lambda e: apply_theme(theme_var.get()))

apply_theme("Cyberpunk") 
root.mainloop()
