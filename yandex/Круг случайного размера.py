import tkinter
import random


def draw(event):
    canvas.create_oval((random.randint(1, 600), random.randint(1, 600)),
                       (random.randint(1, 600), random.randint(1, 600)), fill='red')
    return


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
canvas.pack()
master.bind("<KeyPress>", draw)
master.mainloop()
