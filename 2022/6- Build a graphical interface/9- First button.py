import tkinter as tk

window =  tk.Tk()

text_var = tk.StringVar()


text_sina = tk.Label(
    master=window , 
    textvariable=text_var ,
)

first_button = tk.Button(
    master=window ,
    text='Click here' ,

)


text_sina_Eng = tk.Label(
    master=window , 
    text='SINA LALEBAKHSH' , 
)

user_input = tk.Entry(
    master=window ,
    textvariable=text_var,
)

text_sina_Eng.pack(side=tk.LEFT)
user_input.pack(side=tk.LEFT)
first_button.pack(side=tk.LEFT)


window.mainloop()
