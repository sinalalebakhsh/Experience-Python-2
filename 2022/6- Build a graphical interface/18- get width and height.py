import tkinter as tk
from tkinter import E , W , S , N 

window =  tk.Tk()

show_title = tk.Label(
    master=window ,
    text='*** Wellcome here ***'
)
show_title.grid(row=0, column=0, columnspan=2)

show_name = tk.Label(
    master=window ,
    text='Enter your name: ' ,
)
write_name = tk.Entry(
    master=window ,
)
write_name.insert(0, 'here...')
show_name.grid(row=1 , column=0 , sticky=(W , ))
write_name.grid(row=1 , column=1)

question_mood = tk.Label(
    master=window ,
    text='What is your mood to day?  '
)
answer_mood = tk.Entry(
    master=window ,
)
answer_mood.insert(0, 'Goodly...')
question_mood.grid(row=2 , column=0 , sticky=(W , ))
answer_mood.grid(row=2 , column=1)


show_message = tk.Label(
    master=window ,
)

def get_and_show():
    show_message['text'] = 'Hi ' + write_name.get() + ' Your mood is ' + answer_mood.get() 


button_for_click = tk.Button(
    master=window ,
    text='***  Click here ... ***' ,
    command=get_and_show ,    
    height=3 ,
    bg='#00464a' , 
    fg='#fff',
)
button_for_click.grid(row=4 , column=0 , columnspan=2 , sticky=(E , W))
show_message.grid(row=5, column=0 , columnspan=2)


window.mainloop()
