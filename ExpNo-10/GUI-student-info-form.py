import tkinter as tk
from tkinter import messagebox

# Function to display entered data
def submit():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = entry_course.get()

    info = f"Name: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}"
    messagebox.showinfo("Student Information", info)

# Main window
root = tk.Tk()
root.title("Student Information Form")
root.geometry("400x350")

# Labels and Entries
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age").grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Gender").grid(row=2, column=0, padx=10, pady=10)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2)

tk.Label(root, text="Course").grid(row=3, column=0, padx=10, pady=10)
entry_course = tk.Entry(root)
entry_course.grid(row=3, column=1)

# Submit Button
tk.Button(root, text="Submit", command=submit).grid(row=4, column=0, columnspan=2, pady=20)

# Run application
root.mainloop()