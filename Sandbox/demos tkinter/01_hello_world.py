import tkinter as tk

def button_handler():
    n1 = float(input1.get())
    n2 = float(input2.get())
    result.set(n1 + n2)

root = tk.Tk()
root.geometry('400x300+200+200')
root.title('TkInter demo')

label1 = tk.Label(root, text='Number 1')
label1.grid(column=0, row=0)

input1 = tk.StringVar()
entry1 = tk.Entry(root, textvariable = input1)
entry1.grid(column=1, row=0)

label2 = tk.Label(root, text='Number 2')
label2.grid(column=0, row=1)

input2 = tk.StringVar()
entry2 = tk.Entry(root, textvariable=input2)
entry2.grid(column=1, row=1)

tk.Button(root, text="Add", command = button_handler).grid(column=1, row=2)

result_label = tk.Label(root, text='Result')
result_label.grid(column=0, row=3)

result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result)
result_entry.grid(column=1, row=3)

root.mainloop()
