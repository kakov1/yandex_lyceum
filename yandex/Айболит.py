from tkinter import *

tk = Tk()
canvas = Canvas(tk, height=400, width=450)
button = Button(canvas, bg='black')
button.place(x=50, y=50)
canvas.create_rectangle(350, 400, 400, 450)
canvas.pack()
tk.mainloop()
