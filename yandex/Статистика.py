class Stat:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def all_result(self):
        return

    def result(self):
        return None if not len(self.numbers) else self.all_result()


class MinStat(Stat):
    def all_result(self):
        return min(self.numbers)


class MaxStat(Stat):
    def all_result(self):
        return max(self.numbers)


class AverageStat(Stat):
    def all_result(self):
        return sum(self.numbers) / len(self.numbers)
