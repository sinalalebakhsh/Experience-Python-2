import tkinter as tk

window =  tk.Tk()

text_var = tk.StringVar()


text_sina = tk.Label(
    master=window , 
    textvariable=text_var ,
)



text_sina_Eng = tk.Label(
    master=window , 
    text='SINA LALEBAKHSH' , 
)

user_input = tk.Entry(
    master=window ,
    textvariable=text_var,
)

user_input.pack(side=tk.LEFT)
text_sina.pack(side=tk.BOTTOM)
text_sina_Eng.pack(side=tk.RIGHT)

window.mainloop()
