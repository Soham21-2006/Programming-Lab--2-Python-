import tkinter as tk

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function to clear screen
def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""
equation = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvariable=equation, font=("Arial", 18), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, command=equalpress).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text="C", width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4)

# Run app
root.mainloop()