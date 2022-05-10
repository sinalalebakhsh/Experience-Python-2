# from tkinter import *
import tkinter as tk


window =  tk.Tk()

show_name = tk.Label(
    master=window ,
    text='Enter your name: ' ,
)
write_name = tk.Entry(
    master=window ,
)
write_name.insert(0, 'Exp: sina lalebakhsh ...')
show_name.grid(row=0 , column=0)
write_name.grid(row=0 , column=1)

question_mood = tk.Label(
    master=window ,
    text='What is your mood to day?  '
)
answer_mood = tk.Entry(
    master=window ,
)
answer_mood.insert(0, 'Good , Bad , Normally')
question_mood.grid(row=1 , column=0)
answer_mood.grid(row=1 , column=1)


show_message = tk.Label(
    master=window ,
)

def get_and_show():
    show_message['text'] = 'Hi ' + write_name.get() + ' Your mood is ' + answer_mood.get() 


button_for_click = tk.Button(
    master=window ,
    text='***  Click here ... ***' ,
    command=get_and_show ,
)
show_message.grid(row=2, column=1)
button_for_click.grid(row=2 , column=0)


window.mainloop()
