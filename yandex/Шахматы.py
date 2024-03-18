from tkinter import *
from PIL import ImageTk, Image
from functools import partial

WHITE = 1
BLACK = 2
row, col = -1, -1


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), King(WHITE),
            Queen(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), King(BLACK),
            Queen(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела.'''
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        if isinstance(piece, Rook) or isinstance(piece, King):
            self.field[row1][col1].check = False
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        direction = 1 if self.color == WHITE else -1
        if isinstance(self.field[row][col], Pawn) and \
                correct_coords(row1, col1) and (not self.field[row1][col1] and
                                                (row + direction == row1 and col == col1)) or \
                (row + direction == row1 and self.field[row1][col1] and
                 self.field[row1][col1].get_color() != self.color and
                 (col + 1 == col1 or col - 1 == col1)):
            self.move_piece(row, col, row1, col1)
            if char == 'Q':
                self.field[row1][col1] = Queen(opponent(self.color))
            elif char == 'R':
                self.field[row1][col1] = Rook(opponent(self.color))
            elif char == 'B':
                self.field[row1][col1] = Bishop(opponent(self.color))
            else:
                self.field[row1][col1] = Knight(opponent(self.color))
            return True
        else:
            return False

    def castling0(self):
        if self.color == WHITE:
            if isinstance(self.field[0][0], Rook) and isinstance(self.field[0][3], King) and \
                    not any(self.field[0][1:3]):
                if self.field[0][0].check and self.field[0][3].check:
                    self.field[0][2] = self.field[0][0]
                    self.field[0][0] = None
                    self.field[0][1] = self.field[0][3]
                    self.field[0][3] = None
                    self.color = opponent(self.color)
                    return True
        else:
            if isinstance(self.field[7][0], Rook) and isinstance(self.field[7][3], King) and \
                    not any(self.field[7][1:3]):
                if self.field[7][0].check and self.field[7][3].check:
                    self.field[7][2] = self.field[7][0]
                    self.field[7][0] = None
                    self.field[7][1] = self.field[7][3]
                    self.field[7][3] = None
                    self.color = opponent(self.color)
                    return True
        return False

    def castling7(self):
        if isinstance(self.field[0][7], Rook) and isinstance(self.field[0][3], King) and \
                not any(self.field[0][4:7]):
            if self.color == WHITE:
                if self.field[0][3].check and self.field[0][7].check:
                    self.field[0][5] = self.field[0][3]
                    self.field[0][3] = None
                    self.field[0][4] = self.field[0][7]
                    self.field[0][7] = None
                    self.color = opponent(self.color)
                    return True
        else:
            if isinstance(self.field[7][7], Rook) and isinstance(self.field[7][3], King) and \
                    not any(self.field[7][4:7]):
                if self.field[7][3].check and self.field[7][7].check:
                    self.field[7][5] = self.field[7][3]
                    self.field[7][3] = None
                    self.field[7][4] = self.field[7][7]
                    self.field[7][7] = None
                    self.color = opponent(self.color)
                    return True
        return False

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if isinstance(self.field[i][j], (Pawn, Rook, Queen, Bishop, Knight)) and \
                        self.field[i][j].get_color() == color and \
                        self.field[i][j].can_move(row, col):
                    return True


class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    @staticmethod
    def char():
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        pass

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Rook(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.check = True

    @staticmethod
    def char():
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        if row != row1 and col != col1:
            return False
        if not straight(board, row, col, row1, col1, 'erect'):
            return False
        if not straight(board, row, col, row1, col1, 'horizontal'):
            return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn(Figure):
    @staticmethod
    def char():
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        if col != col1:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if row + direction == row1:
            return True
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Knight(Figure):
    @staticmethod
    def char():
        return 'N'

    def can_move(self, board, row, col, row1, col1):
        if board.field[row1][col1] and \
                board.field[row1][col1].get_color() == board.field[row][col].get_color():
            return False
        if (row1, col1) in \
                [(row - 1, col + 2), (row + 1, col + 2),
                 (row - 1, col - 2), (row + 1, col - 2),
                 (row - 2, col - 1), (row - 2, col + 1),
                 (row + 2, col - 1), (row + 2, col + 1)]:
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class King(Figure):
    def __init__(self, color):
        super().__init__(color)
        self.check = True

    @staticmethod
    def char():
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        if board.is_under_attack(row1, col1, opponent(self.color)):
            return False
        if board.field[row1][col1] and \
                board.field[row1][col1].get_color() == board.field[row][col].get_color():
            return False
        if (row == row1 and abs(col - col1) == 1) or (col == col1 and abs(row - row1) == 1)\
                or (abs(row - row1) == abs(col - col1) == 1):
            return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class Bishop(Figure):
    @staticmethod
    def char():
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        if board.field[row1][col1] and \
                board.field[row1][col1].get_color() == board.field[row][col].get_color():
            return False
        elif abs(row - row1) == abs(col - col1):
            return diagonal(board, row, col, row1, col1)
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class Queen(Figure):
    @staticmethod
    def char():
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        if board.field[row1][col1] and \
                board.field[row1][col1].get_color() == board.field[row][col].get_color():
            return False
        elif row == row1:
            return straight(board, row, col, row1, col1, 'horizontal')
        elif col == col1:
            return straight(board, row, col, row1, col1, 'erect')
        elif abs(row - row1) == abs(col - col1):
            return diagonal(board, row, col, row1, col1)
        else:
            return False

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


def diagonal(board, row, col, row1, col1):
    part = board.field[min([row, row1]) + 1:max([row, row1])]
    for i in range(len(part)):
        part[i] = part[i][min([col, col1]) + 1:max([col, col1])]
    for i in range(len(part)):
        if col < col1:
            if (row > row1 and list(reversed(part))[i][i]) \
                    or (row < row1 and part[i][i]):
                return False
        else:
            if (row < row1 and list(reversed(part))[i][i]) \
                    or (row > row1 and part[i][i]):
                return False
    return True


def straight(board, row, col, row1, col1, direction):
    if direction == 'erect':
        part = list(zip(*board.field))[col][min([row, row1]) + 1:max([row, row1])]
    else:
        part = board.field[row][min([col, col1]) + 1:max([col, col1])]
    for i in part:
        if i:
            return False
    return True


def main():
    global button_
    board = Board()
    tk = Tk()
    tk.title('Шахматы')
    canvas = Canvas(tk, height=450, width=550, highlightthickness=0)
    image = ImageTk.PhotoImage(Image.open('board.png'))
    canvas.create_image(0, 0, anchor=NW, image=image)
    letters = 'abcdefgh'
    for i in range(7, -1, -1):
        canvas.create_text(8 * 50 + 25, i * 50 + 25, text=8 - i, fill="black", font="Verdana 25")
        canvas.create_text(i * 50 + 25, 425, text=letters[i], fill="black", font="Verdana 25")
    images = []
    for i in range(8):
        string = []
        for j in range(8):
            color = '#ffcc99' if (i % 2 and j % 2) or (not i % 2 and not j % 2) else '#b57335'
            if board.field[i][j]:
                img = PhotoImage(file=board.cell(i, j) + '.png').subsample(2, 2)
            else:
                img = PhotoImage(file=color + '.png')
            string.append(img)
        images.append(string)
    buttons = []
    for i in range(8):
        for j in range(8):
            buttons.append(list())
            color = '#ffcc99' if (i % 2 and j % 2) or (not i % 2 and not j % 2) else '#b57335'
            buttons[i].append(Button(canvas, image=images[i][j], highlightthickness=0,
                              bd=0, bg=color, activebackground=color))
            buttons[i][j].place(x=j * 50, y=i * 50)
            if board.field[i][j]:
                action = partial(figure_click, i, j)
            else:
                action = partial(cell_click, board, i, j, buttons)
            buttons[i][j].configure(command=action)
    canvas.pack()
    tk.mainloop()


def figure_click(x, y):
    global row, col
    if row != -1 and col != -1:
        print('Фигуру вы уже выбрали, выберите клетку в которую хотите походить')
    else:
        row, col = x, y
    print(row, col)


def cell_click(board, x1, y1, buttons):
    global row, col
    x, y = row, col
    if row == -1 and col == -1:
        print('Сначала выберите фигуру, которой хотите сделать ход')
    elif board.move_piece(x, y, x1, y1):
        color = '#ffcc99' if (x % 2 and y % 2) or (not x % 2 and not y % 2) else '#b57335'
        color1 = '#ffcc99' if (x1 % 2 and y1 % 2) or (not x1 % 2 and not y1 % 2) else '#b57335'
        buttons[x][y].configure(bg=color1, activebackground=color1)
        buttons[x][y].place_configure(relx=y1 * 50, rely=x1 * 50)
        buttons[x1][y1].configure(bg=color, activebackground=color)
        buttons[x1][y1].place_configure(relx=y * 50, rely=x * 50)
        buttons[x][y], buttons[x1][y1] = buttons[x1][y1], buttons[x][y]
        print('ok')
        row, col = -1, -1
    else:
        print('Неверный ход')


if __name__ == '__main__':
    main()
