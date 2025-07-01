import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%A, %d %B %Y')
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)

# Create main window
root = tk.Tk()
root.title("✨ Aditya's Digital Clock")
root.geometry("600x300")
root.configure(bg='#1e1e1e')  # Dark theme background

# Time label
time_label = tk.Label(
    root,
    font=('DS-Digital', 70),
    fg='#39FF14',
    bg='#1e1e1e'
)
time_label.pack(pady=20)

# Date label
date_label = tk.Label(
    root,
    font=('Arial', 20),
    fg='lightgrey',
    bg="#1e1e1e"
)
date_label.pack()

# Add glow effect (optional with multiple labels)
shadow = tk.Label(root, font=('DS-Digital', 70), fg='#00FF00', bg='#1e1e1e')
shadow.place(x=3, y=3)

# Start updating time
update_time()

# Run the app
root.mainloop()
