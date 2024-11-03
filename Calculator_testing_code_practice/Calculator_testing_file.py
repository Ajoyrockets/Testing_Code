#Setup

import tkinter
def temp():
    window = tkinter.Tk()
    window.title("menu screen")
    window.geometry("500x450")
    window.configure(background="gray51")

    window.mainloop()

import tkinter as tk

# Function to handle button press
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to calculate result
def button_equal():
    try:
        global expression
        result = str(eval(expression))  # Evaluate the mathematical expression
        input_text.set(result)
        expression = result  # Save result for further calculations
    except:
        input_text.set("Error")
        expression = ""

# Function to clear the input
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Main program window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x500")

expression = ""
input_text = tk.StringVar()

# Input field
input_frame = tk.Frame(window)
input_frame.pack(expand=True, fill='both')

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), justify='right')
input_field.grid(row=0, column=0, ipady=10)  # 'ipady' for internal padding

# Buttons frame
buttons_frame = tk.Frame(window)
buttons_frame.pack(expand=True, fill='both')

# Create buttons using a loop for better layout
button_texts = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in button_texts:
    if text == "=":
        btn = tk.Button(buttons_frame, text=text, width=10, height=3, command=lambda: button_equal())
    elif text == "C":
        btn = tk.Button(buttons_frame, text=text, width=10, height=3, command=lambda: button_clear())
    else:
        btn = tk.Button(buttons_frame, text=text, width=10, height=3, command=lambda t=text: button_click(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()