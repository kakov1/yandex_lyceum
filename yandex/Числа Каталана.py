from math import factorial


def catalan(n):
    return factorial(2 * n) // (factorial(n) * factorial(n + 1))
