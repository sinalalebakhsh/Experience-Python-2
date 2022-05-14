import tkinter as tk

window = tk.Tk()

lbl_numbers_and_operator = tk.Label(
    master=window ,
    width=25 ,
    text='123+123'
)
lbl_numbers_and_operator.grid(row=0 , column=0 , columnspan=4 , padx=(30 , 20) , pady=(20 , 20))

lbl_alarm_for_empty = tk.Label(
    master=window ,
    width= 25 ,
)
lbl_alarm_for_empty.grid(row=0 , column=0 , columnspan=4 , padx=(30 , 20) , pady=(20 , 20))

def lbl_numbers_and_operator_func(input_):
    lbl_numbers_and_operator['text'] += input_


last_char = ''
def get_last_mark_and_send_previous_operations(input_):
    global last_char
    last_char = lbl_numbers_and_operator['text'][:-1]
    last_char += str(input_)
    lbl_numbers_and_operator['text'] = last_char


first_char_list = ['0','1','2','3','4','5','6','7','8','9']
last_character_is_operator = 0
def plus_operator():
    global last_character_is_operator, first_char_list
    if lbl_numbers_and_operator['text'][0] in first_char_list:
        if last_character_is_operator == 1:
            get_last_mark_and_send_previous_operations('+')
            last_character_is_operator = 0
        else:
            lbl_numbers_and_operator_func('+')
            last_character_is_operator = 1
    else:
        lbl_alarm_for_empty['text'] = 'No number!'  


def minus_operator():
    global last_character_is_operator, first_char_list
    try:
        first_char_list = lbl_numbers_and_operator['text'][0]
        if last_character_is_operator == 1:
            get_last_mark_and_send_previous_operations('-')
            last_character_is_operator = 0
        else:
            lbl_numbers_and_operator_func('-')
            last_character_is_operator = 1
    except IndexError:
        lbl_alarm_for_empty['text'] = 'No number!' 


def equal_operator():
    pass


def show_number(number):
    if lbl_alarm_for_empty['text'] == 'No number!':
        lbl_alarm_for_empty['text'] = str(number)
    else:
        lbl_alarm_for_empty['text'] += str(number)
        

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


btn_equal_sign = tk.Button(
    master=window ,
    text='=',
    height=3 ,
    command= lambda:equal_operator() ,
)
btn_equal_sign.grid(row=5 , column=0 , sticky='ewns' , columnspan=4 )

window.mainloop()

