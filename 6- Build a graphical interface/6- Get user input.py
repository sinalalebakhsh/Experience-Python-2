from cgitb import text
import tkinter as tk

window =  tk.Tk()

text_sina = tk.Label(
    master=window , 
    text='سینا لاله بخش' ,
)



text_sina_Eng = tk.Label(
    master=window , 
    text='SINA LALEBAKHSH' , 
)

user_input = tk.Entry(master=window)

text_sina.pack()
text_sina_Eng.pack()
user_input.pack()

window.mainloop()
