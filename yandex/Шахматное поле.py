import tkinter


window = tkinter.Tk()
canvas = tkinter.Canvas(window, bg='white', height=600, width=600)
start = (50, 50)
start_1 = start
for i in range(1, 9):
    for j in range(1, 9):
        canvas.create_line(start[0], start[1], start[0] + 50, start[1], fill='black')
        canvas.create_line(start[0] + 50, start[1], start[0] + 50, start[1] + 50, fill='black')
        canvas.create_line(start[0] + 50, start[1] + 50, start[0], start[1] + 50, fill='black')
        canvas.create_line(start[0], start[1] + 50, start[0], start[1], fill='black')
        if i < 4:
            if i % 2:
                if j % 2:
                    canvas.create_oval(start, (start[0] + 50, start[1] + 50), fill='red')
            else:
                if not j % 2:
                    canvas.create_oval(start, (start[0] + 50, start[1] + 50), fill='red')
        elif i > 5:
            if i % 2:
                if j % 2:
                    canvas.create_oval(start, (start[0] + 50, start[1] + 50), fill='blue')
            else:
                if not j % 2:
                    canvas.create_oval(start, (start[0] + 50, start[1] + 50), fill='blue')
        start = (start[0] + 50, start[1])
    start = (start_1[0], start_1[1] + 50 * i)
canvas.pack()
window.mainloop()
