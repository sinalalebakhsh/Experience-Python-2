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

window.mainloop()
