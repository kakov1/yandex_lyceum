from math import sqrt


def roots_of_quadratic_equation(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return ['all']
            else:
                return ['']
        else:
            return [-c / b]
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return ''
        elif d == 0:
            return [-b / (2 * a)]
        else:
            return [(-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)]
