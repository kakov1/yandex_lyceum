class Date:
    def __init__(self, year, month, day):
        self.year = str(year)
        self.month = str(month)
        self.day = str(day)

    def set_year(self, year):
        self.year = str(year)

    def set_month(self, month):
        self.month = str(month)

    def set_day(self, day):
        self.day = str(day)

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day


class EuropeanDate(Date):
    def format(self):
        return self.day.rjust(2, '0') + '.' + self.month.rjust(2, '0') + '.' + self.year


class AmericanDate(Date):
    def format(self):
        return self.month.rjust(2, '0') + '.' + self.day.rjust(2, '0') + '.' + self.year
