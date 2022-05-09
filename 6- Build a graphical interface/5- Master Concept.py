import tkinter as tk

window =  tk.Tk()

text_sina = tk.Label(
    master=window , 
    text='سینا لاله بخش' ,
)



text_sina_Eng = tk.Label(
    master=window , 
    text='SINA LALEBAKHSH' , 
)


text_sina.pack()
text_sina_Eng.pack()


window.mainloop()
