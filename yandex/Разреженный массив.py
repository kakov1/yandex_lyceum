class SparseArray:
    def __init__(self):
        self.dict = dict()

    def __setitem__(self, index, value):
        self.dict[str(index)] = value

    def __getitem__(self, index):
        return self.dict[str(index)] if str(index) in self.dict.keys() else 0
