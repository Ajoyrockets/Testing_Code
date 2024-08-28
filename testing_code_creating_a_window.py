import tkinter as tk
from tkinter import ttk

def button_one_press(button_one,button_two):
    button_one.destroy()
    button_two.destroy()
    label = tk.Label(root, text="you pressed button 1 ", font=("Helvetica", 16))
    label.pack(pady=20)
    main = ttk.Button(root, text = 'Main', command=lambda:button_one_press() )
    main.pack(ipadx=5, ipady=5, expand=True)


def button_two_press():
    button_one.destroy()
    button_two.destroy()
    label = tk.Label(root, text="you pressed button 2 ", font=("Helvetica", 16))
    label.pack(pady=20)
    main = ttk.Button(root, text = 'Main', command=lambda:button_one_press() )
    main.pack(ipadx=5, ipady=5, expand=True)

# Create the main window
root = tk.Tk()
root.geometry('500x350')
root.resizable(False, False)
root.title('Button Demo')

button_one = ttk.Button(root, text = 'Button_one', command=lambda:button_one_press() )
button_one.pack(ipadx=5, ipady=5, expand=True)

button_two = ttk.Button(root, text = 'Button_two', command=lambda:button_two_press() )
button_two.pack(ipadx=5, ipady=5, expand=True)

exit_button = ttk.Button(root, text = 'Quit', command=lambda: root.quit())
exit_button.pack(ipadx=5, ipady=5, expand=True)

# Create an "Exit" button
# if __name__ == "__main__":
#     main()

# Start the Tkinter event loop
root.mainloop()