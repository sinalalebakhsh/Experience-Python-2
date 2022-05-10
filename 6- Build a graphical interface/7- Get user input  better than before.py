from cgitb import text
import tkinter as tk

window =  tk.Tk()

text_var = tk.StringVar()


text_sina = tk.Label(
    master=window , 
    textvariable=text_var ,
)



text_sina_Eng = tk.Label(
    master=window , 
    text='SINA LALEBAKHSH' , 
)

user_input = tk.Entry(
    master=window ,
    textvariable=text_var,
)

user_input.pack()
text_sina.pack()
text_sina_Eng.pack()

window.mainloop()
