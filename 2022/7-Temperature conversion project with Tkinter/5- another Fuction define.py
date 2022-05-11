import tkinter as tk
from tkinter import S , N

window = tk.Tk()

show_fahrenheit = tk.Label(
    master=window ,
    text='Fahrenheit:' ,
)
show_fahrenheit.grid(row=0 , column= 0 , padx=20 , pady=10 )

get_fahrenheit_heat = tk.Entry(
    master=window , 
    width=50 ,
)
get_fahrenheit_heat.grid(row=0, column=1 )

show_celsius = tk.Label(
    master=window ,
    text='Celsius' ,
)
show_celsius.grid(row=1 , column=0 , pady=(10 , 20) )

show_message_result = tk.Label(
    master=window ,
    text='Result...' , 
)
show_message_result.grid(row=1 , column=1 , pady=(10 , 20))

def get_num_calc_for_celsius():
    fahrenheit_input = get_fahrenheit_heat.get()
    try:
        fahrenheit_value = float(fahrenheit_input)
        #convert to Celsius
        show_message_result['text'] = (fahrenheit_value-32) * 5 / 9
    except ValueError:
        if fahrenheit_input != '':
            # if user input is not valid
            show_message_result['text'] = 'You should enter a number!!'
        else:
            # if user input is empty
            show_message_result['text'] = 'Your input is empty.'



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

window.title('INSTAGRAM: @Hackme.space')
window.mainloop()