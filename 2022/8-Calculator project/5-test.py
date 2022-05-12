import tkinter as tk

from setuptools import Command

window = tk.Tk()

lbl_numbers_and_operator = tk.Label(
    master=window ,
    width=25 ,
)
lbl_numbers_and_operator.grid(row=0 , column=0 , columnspan=4 , padx=(30 , 20) , pady=(20 , 20))

list_of_memory = []

def show_number(number):
    lbl_numbers_and_operator['text'] += str(number)
    with open('memory.txt' , 'a') as memory:
        memory.write(str(number))


btn_number7 = tk.Button(
    master=window ,
    text='7',
    height=3 ,
    command= lambda:show_number(7)  ,
)
btn_number7.grid(row=1 , column=0 , sticky='ewns' )

btn_mark_plus = tk.Button(
    master=window ,
    text='+',
    height=3 ,
)
btn_mark_plus.grid(row=1 , column=3 , sticky='ewns' )

btn_equal_sign = tk.Button(
    master=window ,
    text='=',
    height=3 ,
)
btn_equal_sign.grid(row=5 , column=0 , sticky='ewns' , columnspan=4 )


window.mainloop()