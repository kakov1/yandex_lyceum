import tkinter


def show_key(event):
    label.config(text=event.keysym)
    label_1.config(text=event.char)
    label_2.config(text=event.keysym_num)
    label_3.config(text=event.keycode)


master = tkinter.Tk()
label = tkinter.Label(master, text="Hello world!")
label_1 = tkinter.Label(master, text="Hello world!")
label_2 = tkinter.Label(master, text="Hello world!")
label_3 = tkinter.Label(master, text="Hello world!")
label.pack()
label_1.pack()
label_2.pack()
label_3.pack()
master.bind("<KeyPress>", show_key)
master.mainloop()