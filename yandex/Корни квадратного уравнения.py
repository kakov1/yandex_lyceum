from math import sqrt


def larger_root(p, q):
    d = p ** 2 - 4 * q
    return max((-p + sqrt(d)) / 2, (-p - sqrt(d)) / 2)


def smaller_root(p, q):
    d = p ** 2 - 4 * q
    return min((-p + sqrt(d)) / 2, (-p - sqrt(d)) / 2)


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def main():
    p = float(input())
    q = float(input())
    d = p ** 2 - 4 * q
    print(d)
    print(*sorted(((-p + sqrt(d)) / 2, (-p - sqrt(d)) / 2)))
