import tkinter as tk
from tkinter import messagebox
import random
import string

# Password generator that ensures strong passwords
def generate_passwords(lengths):
    passwords = []
    for length in lengths:
        while True:  # Keep generating until strong
            password = generate_base_password(length)
            if is_strong(password):
                passwords.append(password)
                break
    return passwords

# Basic random generation (lower → digit → uppercase)
def generate_base_password(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = ""
    for _ in range(length):
        next_letter = random.choice(alphabet)
        password += next_letter

    password = replace_with_number(password)
    password = replace_with_uppercase(password)
    return password

def replace_with_number(pword):
    pword = list(pword)
    for _ in range(random.randint(1, 2)):
        idx = random.randint(0, len(pword) // 2 - 1)
        pword[idx] = str(random.randint(0, 9))
    return "".join(pword)

def replace_with_uppercase(pword):
    pword = list(pword)
    for _ in range(random.randint(1, 2)):
        idx = random.randint(len(pword) // 2, len(pword) - 1)
        pword[idx] = pword[idx].upper()
    return "".join(pword)

# Check for strong password conditions
def is_strong(pword):
    has_upper = any(c.isupper() for c in pword)
    has_lower = any(c.islower() for c in pword)
    has_digit = any(c.isdigit() for c in pword)
    return has_upper and has_lower and has_digit

# GUI functionality
def generate():
    try:
        count = int(entry_count.get())
        if count <= 0:
            raise ValueError
    except:
        messagebox.showerror("Invalid Input", "Please enter a valid number of passwords.")
        return

    lengths = []
    for i in range(count):
        length_str = length_entries[i].get()
        try:
            length = int(length_str)
            if length < 3:
                length = 3  # Force minimum
        except:
            length = 3
        lengths.append(length)

    results = generate_passwords(lengths)
    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    for i, p in enumerate(results, start=1):
        output_box.insert(tk.END, f"Password #{i}: {p}\n")
    output_box.config(state="disabled")

def create_length_fields():
    global length_entries
    try:
        count = int(entry_count.get())
        if count <= 0:
            raise ValueError
    except:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    for widget in length_frame.winfo_children():
        widget.destroy()

    length_entries = []
    for i in range(count):
        tk.Label(length_frame, text=f"Length for Password #{i+1}:").pack()
        e = tk.Entry(length_frame)
        e.insert(0, "8")
        e.pack()
        length_entries.append(e)

# GUI setup
root = tk.Tk()
root.title("💪 Strong Password Generator")
root.geometry("400x500")

tk.Label(root, text="How many passwords to generate?").pack(pady=5)
entry_count = tk.Entry(root)
entry_count.pack()

tk.Button(root, text="Set Lengths", command=create_length_fields).pack(pady=5)

length_frame = tk.Frame(root)
length_frame.pack(pady=10)

tk.Button(root, text="Generate Strong Passwords", command=generate, bg="green", fg="white").pack(pady=10)

output_box = tk.Text(root, height=10, width=40, state="disabled")
output_box.pack(pady=10)

root.mainloop()
