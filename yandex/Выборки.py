class Selector:
    def __init__(self, nums_list):
        self.nums_list = nums_list[:]

    def get_odds(self):
        return list(filter(lambda x: x % 2, self.nums_list))

    def get_evens(self):
        return list(filter(lambda x: not x % 2, self.nums_list))
