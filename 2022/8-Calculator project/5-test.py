import tkinter as tk
window = tk.Tk()

lbl_numbers_and_operator = tk.Label(
    master=window ,
    width=25 ,
)
lbl_numbers_and_operator.grid(row=0 , column=0 , columnspan=4 , padx=(30 , 20) , pady=(20 , 20))

def show_number(number):
    lbl_numbers_and_operator['text'] += str(number)
    with open('memory.txt' , 'a') as memory:
        memory.write(str(number))
def plus_operator():
    lbl_numbers_and_operator['text'] += '+'
    with open('memory.txt' , 'a') as memory:
        memory.write('\n+\n')
def equal_operator():
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
        except:
            memory_list = []
    lbl_numbers_and_operator['text'] = finall_number

btn_number7 = tk.Button(
    master=window ,
    text='7',
    height=3 ,
    command= lambda:show_number(7)  ,
)
btn_number7.grid(row=1 , column=0 , sticky='ewns' )

btn_mark_plus = tk.Button(
    master=window ,
    text='+',
    height=3 ,
    command=lambda:plus_operator() ,
)
btn_mark_plus.grid(row=1 , column=3 , sticky='ewns' )

btn_equal_sign = tk.Button(
    master=window ,
    text='=',
    height=3 ,
    command= lambda:equal_operator() ,
)
btn_equal_sign.grid(row=5 , column=0 , sticky='ewns' , columnspan=4 )


window.mainloop()