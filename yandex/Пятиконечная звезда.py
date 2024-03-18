import tkinter


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=600, width=600)
p1 = (425, 300),
p2 = (450, 200)
p3 = (475, 300)
p4 = (600, 300)
p5 = (500, 350)
p6 = (500, 450)
p7 = (450, 350)
p8 = (400, 450)
p9 = (400, 350)
p10 = (300, 300)
canvas.create_line(p1, p2, p2, p3, p3, p4, p4, p5, p5, p6, p6, p7, p7, p8, p8, p9, p9, p10, p10, p1, fill='red')
canvas.pack()
master.mainloop()
