import tkinter as tk

window =  tk.Tk()

text_var = tk.StringVar()

def print_user_input():
    print(f'I Like you')

first_button = tk.Button(
    master=window ,
    text='Click here' ,
    command=print_user_input ,
)


write_your_name = tk.Label(
    master=window , 
    text='Write your name:' , 
)

user_input = tk.Entry(
    master=window ,
    textvariable=text_var,
)

write_your_name.pack(side=tk.LEFT)
user_input.pack(side=tk.LEFT)
first_button.pack(side=tk.LEFT)

window.mainloop()
