class Table:
    def __init__(self, rows, cols):
        self.table = [[0 for __ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        return self.table[row][col] if 0 <= row < self.rows and 0 <= col < self.cols else None

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols
