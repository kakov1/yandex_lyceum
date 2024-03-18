import tkinter
import random


def color(r, g, b):
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, bg=f'#{r}{g}{b}', height=600, width=600)
    canvas.create_line((0, 0), (300, 200), (600, 600), (200, 300), (0, 0), fill='red')
    oval = canvas.create_oval((10, 10), (100, 100), fill='white')
    for i in range(0, 10, 2):
        canvas.create_oval((i, i), (i ** 2, i ** 2), fill='blue')

    def draw(event):
        check = 0
        if event.char == 'r':
            canvas.create_oval((100, 100), (300, 300), fill='red')
        if event.char == 'g':
            canvas.create_oval((100, 100), (300, 300), fill='green')
        if event.char == 'b':
            canvas.create_oval((100, 100), (300, 300), fill='blue')
        if event.keysym == 'Up':
            canvas.move(oval, 0, -50)
        if event.keysym == 'Right':
            canvas.move(oval, 50, 0)
        if event.keysym == 'Left':
            canvas.move(oval, -50, 0)
        if event.keysym == 'Down':
            canvas.move(oval, 0, 50)
        if canvas.coords(oval)[1] <= 0 or canvas.coords(oval)[0] <= 0:
            canvas.itemconfig(oval, fill=f'#{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}')
            canvas.move(oval, 100, 100)
        label.config(text=event.keysym)

    canvas.pack()
    label = tkinter.Label(window, text="Hello world!")
    label.pack()
    window.bind("<KeyPress>", draw)
    window.mainloop()


color(7, 5, 8)
