class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def can_move(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7 and (row, col) in \
                [(self.row - 1, self.col + 2), (self.row + 1, self.col + 2),
                 (self.row - 1, self.col - 2), (self.row + 1, self.col - 2),
                 (self.row - 2, self.col - 1), (self.row - 2, self.col + 1),
                 (self.row + 2, self.col - 1), (self.row + 2, self.col + 1)]:
            return True
        return False

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color

    @staticmethod
    def char():
        return 'N'
