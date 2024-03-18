import random
import tkinter


def move_wrap(obj, move):
    canvas.move(obj, move[0], move[1])
    if canvas.coords(obj)[0] < 0:
        canvas.move(obj, step * N_X, 0)
    if canvas.coords(obj)[2] > step * N_X:
        canvas.move(obj, -step * N_X, 0)
    if canvas.coords(obj)[1] < 0:
        canvas.move(obj, 0, step * N_Y)
    if canvas.coords(obj)[3] > step * N_Y:
        canvas.move(obj, 0, -step * N_Y)


def do_nothing(x):
    pass


def check_move():
    if canvas.coords(player) == canvas.coords(exit):
        label.config(text="Победа!")
        master.bind("<KeyPress>", do_nothing)
    for f in fires:
        if canvas.coords(player) == canvas.coords(f):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)
    for e in enemies:
        if canvas.coords(player) == canvas.coords(e[0]):
            label.config(text="Ты проиграл!")
            master.bind("<KeyPress>", do_nothing)


def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, (0, -step))
    if event.keysym == 'Down':
        move_wrap(player, (0, step))
    if event.keysym == 'Right':
        move_wrap(player, (step, 0))
    if event.keysym == 'Left':
        move_wrap(player, (-step, 0))
    for enemy in enemies:
        direction = enemy[1]()  # вызвать функцию перемещения у "врага"
        move_wrap(enemy[0], direction)  # произвести  перемещение
    check_move()


def always_right():
    return (step, 0)


def random_move():
    return random.choice([(step, 0), (-step, 0), (0, step), (0, -step)])


def prepare_and_start():
    global player, exit, fires, enemies
    canvas.delete("all")
    player_pos = (random.randint(0, N_X - 1) * step,
                  random.randint(0, N_Y - 1) * step)
    player = canvas.create_image(player_pos, image=player_pic, anchor='nw')
    exit_pos = (random.randint(0, N_X - 1) * step,
                random.randint(0, N_Y - 1) * step)
    exit = canvas.create_image(exit_pos, image=exit_pic, anchor='nw')
    N_FIRES = 6 #Число клеток, заполненных огнем
    fires = []
    for i in range(N_FIRES):
        fire_pos = (random.randint(0, N_X - 1) * step,
                    random.randint(0, N_Y - 1) * step)
        fire = canvas.create_image(fire_pos, image=fire_pic, anchor='nw')
        fires.append(fire)
    N_ENEMIES = 4 #Число врагов
    enemies = []
    for i in range(N_ENEMIES):
        enemy_pos = (random.randint(0, N_X - 1) * step,
                     random.randint(0, N_Y - 1) * step)
        enemy = canvas.create_image(enemy_pos, image=enemy_pic, anchor='nw')
        enemies.append((enemy, random.choice([always_right, random_move])))
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)


master = tkinter.Tk()

step = 60
N_X = 10
N_Y = 10
player_pic = tkinter.PhotoImage(file="C:/Users/semen/Pictures/russia.gif")
exit_pic = tkinter.PhotoImage(file="images/tardis.gif")
fire_pic = tkinter.PhotoImage(file="images/fire.gif")
enemy_pic = tkinter.PhotoImage(file="images/dalek.gif")

canvas = tkinter.Canvas(master, bg='blue',
                        width=step * N_X, height=step * N_Y)
player_pos = (random.randint(0, N_X - 1) * step,
              random.randint(0, N_Y - 1) * step)
player = canvas.create_image(player_pos, image=player_pic, anchor='nw')
exit_pos = (random.randint(0, N_X - 1) * step,
            random.randint(0, N_Y - 1) * step)
exit = canvas.create_image(exit_pos, image=exit_pic, anchor='nw')
N_FIRES = 6  # Число клеток, заполненных огнем
fires = []
for i in range(N_FIRES):
    fire_pos = (random.randint(0, N_X - 1) * step,
                random.randint(0, N_Y - 1) * step)
    fire = canvas.create_image(fire_pos, image=fire_pic, anchor='nw')
    fires.append(fire)
N_ENEMIES = 4  # Число врагов
enemies = []
for i in range(N_ENEMIES):
    enemy_pos = (random.randint(0, N_X - 1) * step,
                 random.randint(0, N_Y - 1) * step)
    enemy = canvas.create_image(enemy_pos, image=enemy_pic, anchor='nw')
    enemies.append((enemy, random.choice([always_right, random_move])))

label = tkinter.Label(master, text="Найди выход!")
restart = tkinter.Button(master, text="Начать заново",
                         command=prepare_and_start)
restart.pack()
label.pack()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
