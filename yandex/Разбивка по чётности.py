class OddEvenSeparator:
    def __init__(self):
        self.odd_number = []
        self.even_number = []

    def add_number(self, number):
        self.odd_number.append(number) if number % 2 else self.even_number.append(number)

    def odd(self):
        return self.odd_number[:]

    def even(self):
        return self.even_number[:]
