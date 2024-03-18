WHITE = 1
BLACK = 2


class Figure:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def can_move(self, row, color):
        pass

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color

    @staticmethod
    def char():
        pass


class Rook(Figure):
    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        return True

    @staticmethod
    def char():
        return 'R'


class Pawn(Figure):
    def can_move(self, row, col):
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if self.col == col and \
                ((self.row == start_row and self.row + 2 * direction == row)
                 or self.row + direction == row):
            return True

        return False

    @staticmethod
    def char():
        return 'P'


class Knight(Figure):
    def can_move(self, row, col):
        if (row, col) in \
                [(self.row - 1, self.col + 2), (self.row + 1, self.col + 2),
                 (self.row - 1, self.col - 2), (self.row + 1, self.col - 2),
                 (self.row - 2, self.col - 1), (self.row - 2, self.col + 1),
                 (self.row + 2, self.col - 1), (self.row + 2, self.col + 1)]:
            return True
        return False

    @staticmethod
    def char():
        return 'N'


class Bishop(Figure):
    def can_move(self, row, col):
        if abs(row - self.row) == abs(col - self.col):
            return True
        return False

    @staticmethod
    def char():
        return 'B'


class Queen(Figure):
    def can_move(self, row, col):
        if (self.row == row or self.col == col or
                abs(row - self.row) == abs(col - self.col)):
            return True
        return False

    @staticmethod
    def char():
        return 'Q'


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        piece = self.field[row][col]
        if not correct_coords(row, col) or not correct_coords(row1, col1) \
                or (row == row1 and col == col1) or piece is None \
                or not piece.can_move(row1, col1) or piece.get_color() != self.color:
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if isinstance(self.field[i][j], (Pawn, Rook, Queen, Bishop, Knight)) and\
                        self.field[i][j].get_color() == color and\
                        self.field[i][j].can_move(row, col):
                    return True
