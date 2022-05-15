import tkinter as tk

window = tk.Tk()

lbl_calc_result = tk.Label(
    master= window,
    text= '0',
    width= 30,
    height=3,
)
lbl_calc_result.grid(row=0, column=0 , columnspan=4)

last_operator_index = -1
last_dot_index = -1
def insert_number_in_calc_result(button_number):
    global last_operator_index , last_dot_index
    current = lbl_calc_result['text']

    if button_number in ['+', '-' , '*']:
        last_operator_index = len(current)

    if button_number == 'C':
        lbl_calc_result['text'] = '0'
        last_operator_index, last_dot_index = -1,-1
    elif current == '0': 
        lbl_calc_result['text'] = button_number
    elif button_number == '=':
        lbl_calc_result['text'] = f'{eval(current)}'
        last_operator_index = -1
        if '.' in lbl_calc_result['text']:
            last_dot_index = len(lbl_calc_result['text'])
    else:
        if button_number == '.':
            if last_dot_index > last_operator_index:
                pass
            elif current[-1] == '.':
                pass
            else:
                lbl_calc_result['text'] += button_number
                last_dot_index = len(current)

        elif button_number in ['+', '-' , '*']:
            if current[-1] in ['+', '-' , '*']:
                lbl_calc_result['text'] = current[:-1] + button_number
            else:
                lbl_calc_result['text'] += button_number
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