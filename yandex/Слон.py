class Bishop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def can_move(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7 and \
                abs(row - self.row) == abs(col - self.col):
            return True
        return False

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color

    @staticmethod
    def char():
        return 'B'
