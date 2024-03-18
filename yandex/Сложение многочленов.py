class Polynomial:
    def __init__(self, coefficents):
        self.coefficents = coefficents

    def __call__(self, x):
        amount = self.coefficents[0]
        for i in range(1, len(self.coefficents)):
            amount += self.coefficents[i] * int(x) ** i
        return amount

    def __add__(self, other):
        terms = sorted([self.coefficents, other.coefficents], key=lambda x: len(x))
        result = terms[1][:]
        for i in range(len(terms[0])):
            result[i] += terms[0][i]
        return Polynomial(result)

