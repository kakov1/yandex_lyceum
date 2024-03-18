class Summator:
    @staticmethod
    def transform(n):
        return n

    def sum(self, n):
        return sum([self.transform(i) for i in range(1, n + 1)])


class SquareSummator(Summator):
    @staticmethod
    def transform(n):
        return n ** 2


class CubeSummator(Summator):
    @staticmethod
    def transform(n):
        return n ** 3
