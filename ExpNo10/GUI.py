import tkinter as tk

# Create main window
window = tk.Tk()

# Set window title
window.title("Simple GUI Window")

# Set window size
window.geometry("400x300")

# Add a label
label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Add a button
button = tk.Button(window, text="Click Me")
button.pack(pady=10)

# Run the application
window.mainloop()