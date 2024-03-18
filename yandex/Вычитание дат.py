from datetime import date


class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        return (date(2001, self.month, self.day) - date(2001, other.month, other.day)).days
