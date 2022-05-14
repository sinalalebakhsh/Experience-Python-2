import tkinter as tk

window = tk.Tk()

lbl_show_numbers_and_operator = tk.Label(
    master=window,
)
lbl_show_numbers_and_operator.pack()

lbl_show_numbers_and_operator['text'] = '123+'

print(lbl_show_numbers_and_operator)

window.mainloop()