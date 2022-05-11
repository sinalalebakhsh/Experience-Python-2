from cgitb import text
import tkinter as tk
from unicodedata import name
window =  tk.Tk()

write_user_input = tk.Entry(
    master=window ,

)

show_user_input = tk.Label(
    master=window ,
)

def get_than_print():
    show_user_input['text'] = 'I like you ' + write_user_input.get()
    

tap_the_buttom = tk.Button(
    master=window ,
    text='*Click here*' ,
    command=get_than_print ,
)

show_write_your_name = tk.Label(
    master=window ,
    text='*** Enter you name ***'
)

show_write_your_name.pack()
write_user_input.pack()
tap_the_buttom.pack()
show_user_input.pack()

window.mainloop()
