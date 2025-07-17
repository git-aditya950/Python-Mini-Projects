import tkinter as tk
from tkinter import messagebox
import re

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = errors.count(False)

    if score == 5:
        return "Strong 💪", "green"
    elif 3 <= score < 5:
        return "Medium ⚠️", "orange"
    else:
        return "Weak ❌", "red"

def on_check():
    password = entry.get()
    strength, color = check_strength(password)
    result_label.config(text=f"Strength: {strength}", fg=color)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="Enter your password:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
entry = tk.Entry(root, width=30, show="*", font=("Arial", 14))
entry.pack()

tk.Button(root, text="Check Strength", command=on_check, font=("Arial", 12), bg="blue", fg="white").pack(pady=20)
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
result_label.pack()

root.mainloop()
