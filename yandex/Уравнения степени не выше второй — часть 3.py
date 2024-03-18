from math import sqrt


def solve(*coefficients):
    if len(coefficients) > 3 or len(coefficients) == 0:
        return None
    elif len(coefficients) == 3:
        if coefficients[0] == 0:
            if coefficients[1] == 0:
                if coefficients[2] == 0:
                    return ['all']
                else:
                    return ['']
            else:
                return [-coefficients[2] / coefficients[1]]
        else:
            d = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
            if d < 0:
                return ''
            elif d == 0:
                return [-coefficients[1] / (2 * coefficients[0])]
            else:
                return [(-coefficients[1] + sqrt(d)) / (2 * coefficients[0]),
                        (-coefficients[1] - sqrt(d)) / (2 * coefficients[0])]
    elif len(coefficients) == 2:
        return [-coefficients[1] / coefficients[0]]
    else:
        if coefficients[0] == 0:
            return ['all']
        else:
            return []


print(*solve(map(int, input().split())))
