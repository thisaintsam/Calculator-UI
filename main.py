import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("270x270")

# Create the text entry box
entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=4)

# Create the buttons
btn_1 = tk.Button(root, text="1", command=lambda: entry.insert("1"))
btn_2 = tk.Button(root, text="2", command=lambda: entry.insert("2"))
btn_3 = tk.Button(root, text="3", command=lambda: entry.insert("3"))
btn_4 = tk.Button(root, text="4", command=lambda: entry.insert("4"))
btn_5 = tk.Button(root, text="5", command=lambda: entry.insert("5"))
btn_6 = tk.Button(root, text="6", command=lambda: entry.insert("6"))
btn_7 = tk.Button(root, text="7", command=lambda: entry.insert("7"))
btn_8 = tk.Button(root, text="8", command=lambda: entry.insert("8"))
btn_9 = tk.Button(root, text="9", command=lambda: entry.insert("9"))
btn_0 = tk.Button(root, text="0", command=lambda: entry.insert("0"))

# Add the buttons to the grid
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)
btn_0.grid(row=4, column=0)

# Run the main loop
root.mainloop()