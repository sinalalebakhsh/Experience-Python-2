from ast import Return
import tkinter as tk

window = tk.Tk()
window.title('SINANIS')
lbl_calc_result = tk.Label(
    master= window,
    text= '0',
    width= 30,
    height=3,
)
lbl_calc_result.grid(row=0, column=0 , columnspan=4)

def is_last_number_decimal(current):
    for char in current[::-1]:
        if char == '.':
            return True
        if char in ['+', '-' , '*']:
            return False
    return False 

def insert_number_in_calc_result(button_number):
    current = lbl_calc_result['text']
    if button_number == 'C':
        lbl_calc_result['text'] = '0'
    elif current == '0': 
        lbl_calc_result['text'] = button_number
    elif button_number == '=':
        if current[-1] in ['+', '-' , '*']:
            current = current[:-1]      
        result = f'{eval(current)}'
        lbl_calc_result['text'] = result 
    elif button_number == '.':
        if not is_last_number_decimal(current):
            lbl_calc_result['text'] += button_number
    elif button_number in ['+', '-' , '*'] and current[-1] in ['+', '-' , '*']:
        lbl_calc_result['text'] = current[:-1] + button_number
    else:
        lbl_calc_result['text'] += button_number

calc_list = [
    {
        'text' : '7',
        'command' : lambda:insert_number_in_calc_result('7'),
        'bg' : 'white' ,
    },
    {
        'text' : '8',
        'command' : lambda:insert_number_in_calc_result('8'),
        'bg' : 'white' ,
    },
    {
        'text' : '9',
        'command' : lambda:insert_number_in_calc_result('9'),
        'bg' : 'white' ,
    },
    {
        'text' : '+',
        'command' : lambda:insert_number_in_calc_result('+'),
        'bg' : 'white' ,
    },
        {
        'text' : '4',
        'command' : lambda:insert_number_in_calc_result('4'),
        'bg' : 'white' ,
    },
    {
        'text' : '5',
        'command' : lambda:insert_number_in_calc_result('5'),
        'bg' : 'white' ,
    },
    {
        'text' : '6',
        'command' : lambda:insert_number_in_calc_result('6'),
        'bg' : 'white' ,
    },
    {
        'text' : '-',
        'command' : lambda:insert_number_in_calc_result('-'),
        'bg' : 'white' ,
    },
            {
        'text' : '1',
        'command' : lambda:insert_number_in_calc_result('1'),
        'bg' : 'white' ,
    },
    {
        'text' : '2',
        'command' : lambda:insert_number_in_calc_result('2'),
        'bg' : 'white' ,
    },
    {
        'text' : '3',
        'command' : lambda:insert_number_in_calc_result('3'),
        'bg' : 'white' ,
    },
    {
        'text' : '*',
        'command' : lambda:insert_number_in_calc_result('*'),
        'bg' : 'white' ,
    },
                {
        'text' : '.',
        'command' : lambda:insert_number_in_calc_result('.'),
        'bg' : 'white' ,
    },
    {
        'text' : '0',
        'command' : lambda:insert_number_in_calc_result('0'),
        'bg' : 'white' ,
    },
    {
        'text' : 'C',
        'command' : lambda:insert_number_in_calc_result('C'),
        'bg' : '#f4004f' , 
    },
    {
        'text' : '=',
        'command' : lambda:insert_number_in_calc_result('='),
        'bg' : 'white' ,
    },
    
]

calc_key_objs = []

for calc_key_data in calc_list:
    btn = tk.Button(
        master= window,
        text=calc_key_data['text'],
        command=calc_key_data['command'],
        height=3,
        bg=calc_key_data['bg'],
    )
    calc_key_objs.append(btn)



for i, calc_key_obj in enumerate(calc_key_objs):
    calc_key_obj.grid(row=(i//4)+1, column=i%4, sticky='nsew')

window.mainloop()