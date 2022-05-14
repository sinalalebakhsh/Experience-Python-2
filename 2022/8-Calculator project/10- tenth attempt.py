import tkinter as tk
from functions_project import clear_1
clear_1()
from functions_project import duplicate_checker


window = tk.Tk()
clear_1()
flag_1 = 0
number_value = None
finall_list = ''
flag_for_check_operator = 0

lbl_numbers_and_operator = tk.Label(
    master=window ,
    width=25 ,
)
lbl_numbers_and_operator.grid(row=0 , column=0 , columnspan=4 , padx=(30 , 20) , pady=(20 , 20))

def lbl_numbers_and_operator_func(input_):
    lbl_numbers_and_operator['text'] += input_

def show_number(number):
    with open('Memory_in_one_line.txt' , 'a') as memory_in_one_line:
        memory_in_one_line.write(str(number))
    global flag_1
    if flag_1 != 0:
        lbl_numbers_and_operator['text'] = ''
        flag_1 = 0  
    lbl_numbers_and_operator_func(number)
    with open('memory.txt' , 'a') as memory:
        memory.write(str(number))

def read_memory_in_one_line():
    with open('memory_in_one_line.txt' , 'r') as memory_in_one_line:
        return memory_in_one_line.read()  

def plus_operator():
    try:
        duplicate_checker()
    except Exception:
        with open('Memory_in_one_line.txt' , 'a') as memory_in_one_line:
            memory_in_one_line.write('+')
        lbl_numbers_and_operator['text'] = read_memory_in_one_line()
    with open('memory.txt' , 'a') as memory:
        memory.write('\n+\n')

def minus_operator():
    duplicate_checker()
    with open('Memory_in_one_line.txt' , 'a') as memory_in_one_line:
        memory_in_one_line.write('-')
    lbl_numbers_and_operator['text'] = duplicate_checker()
    with open('memory.txt' , 'a') as memory:
        memory.write('\n-\n')

def equal_operator():
    global flag_1 
    flag_1 += 1
    with open('memory.txt' , 'r') as memory:
        get_memory = memory.read()
        memory_list = get_memory.split('\n')
    finall_number = 0
    while memory_list != []:
        try:
            if memory_list[1] == '+':
                finall_number = float(memory_list[0]) + float(memory_list[2])
                memory_list = memory_list[3:]
            elif memory_list[0] == '+':
                finall_number += float(memory_list[1])
                memory_list = memory_list[2:]
            elif memory_list[1] == '-':
                finall_number = float(memory_list[0]) - float(memory_list[2])
                memory_list = memory_list[3:]
            elif memory_list[0] == '-':
                finall_number -= float(memory_list[1])
                memory_list = memory_list[2:]
        except:
            memory_list = []
    lbl_numbers_and_operator['text'] = str(finall_number)
    clear_1()
    
btn_number7 = tk.Button(
    master=window ,
    text='7',
    height=3 ,
    command= lambda:show_number('7')  ,
)
btn_number7.grid(row=1 , column=0 , sticky='ewns' )

btn_mark_plus = tk.Button(
    master=window ,
    text='+',
    height=3 ,
    command=lambda:plus_operator() ,
)
btn_mark_plus.grid(row=1 , column=3 , sticky='ewns' )

btn_number8 = tk.Button(
    master=window ,
    text='8',
    height=3 ,
    command= lambda:show_number('8')  ,
)
btn_number8.grid(row=1 , column=1 , sticky='ewns' )

btn_number9 = tk.Button(
    master=window ,
    text='9',
    height=3 ,
    command= lambda:show_number('9')  ,
)
btn_number9.grid(row=1 , column=2 , sticky='ewns' )



btn_number_4 = tk.Button(
    master=window ,
    text='4',
    height=3 ,
    command= lambda:show_number('4')  ,
)
btn_number_4.grid(row=2 , column=0 , sticky='ewns' )

btn_number_5 = tk.Button(
    master=window ,
    text='5',
    height=3 ,
    command= lambda:show_number('5')  ,
)
btn_number_5.grid(row=2 , column=1 , sticky='ewns' )

btn_number_6 = tk.Button(
    master=window ,
    text='6',
    height=3 ,
    command= lambda:show_number('6')  ,
)
btn_number_6.grid(row=2 , column=2 , sticky='ewns' )

btn_minus_operator = tk.Button(
    master=window ,
    text='-',
    height=3 ,
    command= lambda:minus_operator(),
)
btn_minus_operator.grid(row=2 , column=3 , sticky='ewns' )

btn_number_1 = tk.Button(
    master=window ,
    text='1',
    height=3 ,
    command= lambda:show_number('1')  ,
)
btn_number_1.grid(row=3 , column=0 , sticky='ewns' )

btn_number_2 = tk.Button(
    master=window ,
    text='2',
    height=3 ,
    command= lambda:show_number('2')  ,
)
btn_number_2.grid(row=3 , column=1 , sticky='ewns' )

btn_number_3 = tk.Button(
    master=window ,
    text='3',
    height=3 ,
    command= lambda:show_number('3')  ,
)
btn_number_3.grid(row=3 , column=2 , sticky='ewns' )

btn_multiply_the_mark = tk.Button(
    master=window ,
    text='*',
    height=3 ,
)
btn_multiply_the_mark.grid(row=3 , column=3 , sticky='ewns' )

btn_decimal_sign = tk.Button(
    master=window ,
    text='.',
    height=3 ,
)
btn_decimal_sign.grid(row=4 , column=0 , sticky='ewns' )

btn_number_0 = tk.Button(
    master=window ,
    text='0',
    height=3 ,
    command= lambda:show_number('0')  ,
)
btn_number_0.grid(row=4 , column=1 , sticky='ewns' )

btn_clear = tk.Button(
    master=window ,
    text='C',
    height=3 ,
)
btn_clear.grid(row=4 , column=2 , sticky='ewns' )

btn_division_sign = tk.Button(
    master=window ,
    text='/',
    height=3 ,
)
btn_division_sign.grid(row=4 , column=3 , sticky='ewns' )

btn_equal_sign = tk.Button(
    master=window ,
    text='=',
    height=3 ,
    command= lambda:equal_operator() ,
)
btn_equal_sign.grid(row=5 , column=0 , sticky='ewns' , columnspan=4 )

window.mainloop()