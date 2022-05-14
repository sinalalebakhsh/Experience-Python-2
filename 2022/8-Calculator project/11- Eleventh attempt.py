import tkinter as tk

window = tk.Tk()

lbl_numbers_and_operator = tk.Label(
    master=window ,
    width=25 ,
)
lbl_numbers_and_operator.grid(row=0 , column=0 , columnspan=4 , padx=(30 , 20) , pady=(20 , 20))


def lbl_numbers_and_operator_func(input_):
    lbl_numbers_and_operator['text'] += input_

last_character_is_operator = 0

def show_number(number):
    lbl_numbers_and_operator_func(number)

last_char = ''
def get_last_mark_and_send_previous_operations(input_):
    global last_char
    last_char = lbl_numbers_and_operator['text'][:-1]
    last_char += str(input_)
    lbl_numbers_and_operator['text'] = last_char

def plus_operator():
    global last_character_is_operator 
    if last_character_is_operator == 1:
        get_last_mark_and_send_previous_operations('+')
    else:
        lbl_numbers_and_operator_func('+')
        last_character_is_operator = 1

def minus_operator():
    global last_character_is_operator 
    if last_character_is_operator == 1:
        get_last_mark_and_send_previous_operations('-')
    else:
        lbl_numbers_and_operator_func('-')   
        last_character_is_operator = 1



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

btn_minus_operator = tk.Button(
    master=window ,
    text='-',
    height=3 ,
    command= lambda:minus_operator(),
)
btn_minus_operator.grid(row=2 , column=3 , sticky='ewns' )

window.mainloop()

