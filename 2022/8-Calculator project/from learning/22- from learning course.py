import tkinter as tk

window = tk.Tk()

lbl_calc_result = tk.Label(
    master= window,
    text= '0',
    width= 30,
    height=3,
)
lbl_calc_result.grid(row=0, column=0 , columnspan=4)

def insert_number_in_calc_result(button_number):
    current = lbl_calc_result['text']
    if current == '0': 
        lbl_calc_result['text'] = button_number
    elif button_number == '=':
        lbl_calc_result['text'] = f'{eval(current)}'
    else:
        lbl_calc_result['text'] += button_number


calc_list = [
    {
        'text' : '7',
        'command' : lambda:insert_number_in_calc_result('7'),
    },
    {
        'text' : '8',
        'command' : lambda:insert_number_in_calc_result('8'),
    },
    {
        'text' : '9',
        'command' : lambda:insert_number_in_calc_result('9'),
    },
    {
        'text' : '+',
        'command' : lambda:insert_number_in_calc_result('+'),
    },
        {
        'text' : '4',
        'command' : lambda:insert_number_in_calc_result('4'),
    },
    {
        'text' : '5',
        'command' : lambda:insert_number_in_calc_result('5'),
    },
    {
        'text' : '6',
        'command' : lambda:insert_number_in_calc_result('6'),
    },
    {
        'text' : '-',
        'command' : lambda:insert_number_in_calc_result('-'),
    },
            {
        'text' : '1',
        'command' : lambda:insert_number_in_calc_result('1'),
    },
    {
        'text' : '2',
        'command' : lambda:insert_number_in_calc_result('2'),
    },
    {
        'text' : '3',
        'command' : lambda:insert_number_in_calc_result('3'),
    },
    {
        'text' : '*',
        'command' : lambda:insert_number_in_calc_result('*'),
    },
                {
        'text' : '.',
        'command' : lambda:insert_number_in_calc_result('.'),
    },
    {
        'text' : '0',
        'command' : lambda:insert_number_in_calc_result('0'),
    },
    {
        'text' : 'C',
        'command' : lambda:insert_number_in_calc_result('C'),
    },
    {
        'text' : '=',
        'command' : lambda:insert_number_in_calc_result('='),
    },
    
]

calc_key_objs = []

for calc_key_data in calc_list:
    btn = tk.Button(
        master= window,
        text=calc_key_data['text'],
        command=calc_key_data['command'],
        height=3,
    )
    calc_key_objs.append(btn)

for i, calc_key_obj in enumerate(calc_key_objs):
    calc_key_obj.grid(row=(i//4)+1, column=i%4, sticky='nsew')


# btn7 = tk.Button(
#     master= window,
#     text='7',
#     command= lambda: print('7'),
#     height=3,
# )
# btn7.grid(row=1 , column=0, sticky='ewsn')


window.mainloop()