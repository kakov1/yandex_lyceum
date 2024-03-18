WHITE = 1
BLACK = 2


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
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
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
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
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
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        direction = 1 if self.color == WHITE else -1
        if isinstance(self.field[row][col], Pawn) and\
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
    @staticmethod
    def char():
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row != row1 and col != col1:
            return False
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(r, col) is None):
                return False
        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn(Figure):
    @staticmethod
    def char():
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1:
            return True

        # ход на 2 клетки из начального положения
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
        return 'N'  # kNight, буква 'K' уже занята королём

    def can_move(self, board, row, col, row1, col1):
        return True  # Заглушка

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class King(Figure):
    @staticmethod
    def char():
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        return True  # Заглушка

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(self, board, row, col, row1, col1)


class Bishop(Figure):
    @staticmethod
    def char():
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        return True  # Заглушка

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
