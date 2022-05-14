import tkinter as tk

window = tk.Tk()

lbl_alarm_for_empty = tk.Label(
    master=window ,
)
lbl_alarm_for_empty.grid(row=0 , column=0 , columnspan=4 , padx=(30 , 20) )

lbl_numbers_and_operator = tk.Label(
    master=window ,
    width=25 ,
)
lbl_numbers_and_operator.grid(row=1 , column=0 , columnspan=4 , padx=(30 , 20) , pady=(20 , 20))

def show_number_on_the_lbl(number):
    if lbl_alarm_for_empty['text'] == 'epmty':
        lbl_alarm_for_empty['text'] = ''
    lbl_numbers_and_operator['text'] += str(number)

def equal_operator(): # =
    if lbl_numbers_and_operator['text'] == '' :
        lbl_alarm_for_empty['text'] = 'epmty'

def plus_operator(): # +
    if lbl_numbers_and_operator['text'] == '' :
        lbl_alarm_for_empty['text'] = 'epmty'

def minus_operator():  # -
    if lbl_numbers_and_operator['text'] == '' :
        lbl_alarm_for_empty['text'] = 'epmty'    

def multiply_operator(): # *
    if lbl_numbers_and_operator['text'] == '' :
        lbl_alarm_for_empty['text'] = 'epmty'


def divide_operator(): # /
    if lbl_numbers_and_operator['text'] == '' :
        lbl_alarm_for_empty['text'] = 'epmty'

def clear_command(): # Clear every thing
    lbl_alarm_for_empty['text'] = ''
    lbl_numbers_and_operator['text'] = ''

btn_equal_sign = tk.Button(
    master=window ,
    text='=',
    height=3 ,
    command= lambda:equal_operator() ,
)
btn_equal_sign.grid(row=6 , column=0 , sticky='ewns' , columnspan=4 )

btn_mark_plus = tk.Button(
    master=window ,
    text='+',
    height=3 ,
    command= lambda: plus_operator() ,
)
btn_mark_plus.grid(row=2 , column=3 , sticky='ewns' ) 

btn_minus_operator = tk.Button(
    master=window ,
    text='-',
    height=3 ,
    command= lambda: minus_operator() ,
)
btn_minus_operator.grid(row=3 , column=3 , sticky='ewns' )

btn_multiply_operator = tk.Button(
    master=window ,
    text='*',
    height=3 ,
    command= lambda: multiply_operator() ,
)
btn_multiply_operator.grid(row=4 , column=3 , sticky='ewns' )

btn_divide_operator = tk.Button(
    master=window ,
    text='/',
    height=3 ,
    command= lambda: divide_operator() ,
)
btn_divide_operator.grid(row=5 , column=3 , sticky='ewns' )

btn_clear_command = tk.Button(
    master=window ,
    text='C',
    height=3 ,
    command= lambda:clear_command() ,
    bg= '#f4004f' ,
    fg= 'white' , 
)
btn_clear_command.grid(row=5 , column=2 , sticky='ewns' )

btn_number7 = tk.Button(
    master=window ,
    text='7',
    height=3 ,
    command= lambda:show_number_on_the_lbl('7') ,
)
btn_number7.grid(row=2 , column=0 , sticky='ewns' )

btn_number8 = tk.Button(
    master=window ,
    text='8',
    height=3 ,
    command= lambda:show_number_on_the_lbl('8') ,
)
btn_number8.grid(row=2 , column=1 , sticky='ewns' )


btn_number9 = tk.Button(
    master=window ,
    text='9',
    height=3 ,
    command= lambda:show_number_on_the_lbl('9') ,
)
btn_number9.grid(row=2 , column=2 , sticky='ewns' )

btn_number4 = tk.Button(
    master=window ,
    text='4',
    height=3 ,
    command= lambda:show_number_on_the_lbl('4') ,
)
btn_number4.grid(row=3 , column=0 , sticky='ewns' )

btn_number5 = tk.Button(
    master=window ,
    text='5',
    height=3 ,
    command= lambda:show_number_on_the_lbl('5') ,
)
btn_number5.grid(row=3 , column=1 , sticky='ewns' )

btn_number6 = tk.Button(
    master=window ,
    text='6',
    height=3 ,
    command= lambda:show_number_on_the_lbl('6') ,
)
btn_number6.grid(row=3 , column=2 , sticky='ewns' )

btn_number1 = tk.Button(
    master=window ,
    text='1',
    height=3 ,
    command= lambda:show_number_on_the_lbl('1') ,
)
btn_number1.grid(row=4 , column=0 , sticky='ewns' )

btn_number2 = tk.Button(
    master=window ,
    text='2',
    height=3 ,
    command= lambda:show_number_on_the_lbl('2') ,
)
btn_number2.grid(row=4 , column=1 , sticky='ewns' )

btn_number3 = tk.Button(
    master=window ,
    text='3',
    height=3 ,
    command= lambda:show_number_on_the_lbl('3') ,
)
btn_number3.grid(row=4 , column=2 , sticky='ewns' )

btn_decimal_sign = tk.Button(
    master=window ,
    text='.',
    height=3 ,
    command= lambda:show_number_on_the_lbl('.') ,
)
btn_decimal_sign.grid(row=5 , column=0 , sticky='ewns' )

btn_number0 = tk.Button(
    master=window ,
    text='0',
    height=3 ,
    command= lambda:show_number_on_the_lbl('0') ,
)
btn_number0.grid(row=5 , column=1 , sticky='ewns' )

window.mainloop()