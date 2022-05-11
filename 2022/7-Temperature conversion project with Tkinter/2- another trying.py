import tkinter as tk
from tkinter import S , N

window = tk.Tk()

show_fahrenheit = tk.Label(
    master=window ,
    text='Fahrenheit:' ,
    height=3 ,
    width=10 , 
)
show_fahrenheit.grid(row=0 , column= 0)

get_fahrenheit_heat = tk.Entry(
    master=window , 
    width=50 ,
)
get_fahrenheit_heat.grid(row=0, column=1 )

show_celsius = tk.Label(
    master=window ,
    text='Celsius => ' ,
    height=3 ,
)
show_celsius.grid(row=1 , column=0)

show_message_result = tk.Label(
    master=window ,
)
show_message_result.grid(row=1 , column=1)

def get_num_calc_for_celsius():
    try:
        number = int(get_fahrenheit_heat.get())
        show_message_result['text'] = ( number - 32 ) * 5.9
    except ValueError:
        show_message_result['text'] = 'Wrong!! just write number.'


to_distance = tk.Label(
    master=window ,
    width=15 ,
)
to_distance.grid(row=0 , column=2)

button_to_calc = tk.Button(
    master=window ,
    text='Calculate' ,
    command=get_num_calc_for_celsius ,
)
button_to_calc.grid(row=0, column=2)

window.mainloop()
