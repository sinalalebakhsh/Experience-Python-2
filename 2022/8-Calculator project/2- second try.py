import tkinter as tk

window = tk.Tk()

lbl_numbers = tk.Label(
    master=window ,
    text='12345678901234567892123456789' ,
)
lbl_numbers.grid(row=0 , column=0 , columnspan=4 , padx=(30 , 20) , pady=(20 , 20))

btn_number7 = tk.Button(
    master=window ,
    text='7',
    height=3 ,
)
btn_number7.grid(row=1 , column=0 , sticky='ewns' )

btn_number8 = tk.Button(
    master=window ,
    text='8',
    height=3 ,
)
btn_number8.grid(row=1 , column=1 , sticky='ewns' )

btn_number9 = tk.Button(
    master=window ,
    text='9',
    height=3 ,
)
btn_number9.grid(row=1 , column=2 , sticky='ewns' )

btn_number_plus = tk.Button(
    master=window ,
    text='+',
    height=3 ,
)
btn_number_plus.grid(row=1 , column=3 , sticky='ewns' )

btn_number_4 = tk.Button(
    master=window ,
    text='4',
    height=3 ,
)
btn_number_4.grid(row=2 , column=0 , sticky='ewns' )

btn_number_5 = tk.Button(
    master=window ,
    text='5',
    height=3 ,
)
btn_number_5.grid(row=2 , column=1 , sticky='ewns' )

btn_number_6 = tk.Button(
    master=window ,
    text='6',
    height=3 ,
)
btn_number_6.grid(row=2 , column=2 , sticky='ewns' )

btn_number_subtraction = tk.Button(
    master=window ,
    text='-',
    height=3 ,
)
btn_number_subtraction.grid(row=2 , column=3 , sticky='ewns' )


window.mainloop()
