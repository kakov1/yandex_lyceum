def is_prime(n: int):
    dividers = list()
    for i in range(2, n):
        if not n % i:
            dividers.append(i)
            break
    return not bool(len(dividers))


def is_exponent_2(n):
    exponent = 0
    while True:
        if 2 ** exponent == n:
            return True
        elif 2 ** exponent > n:
            return False
        exponent += 1


def check_pin(pinCode):
    pincode = pinCode.split('-')
    if int(pincode[0]) != 1 and is_prime(int(pincode[0]))\
            and list(pincode[1]) == list(reversed(list(pincode[1])))\
            and is_exponent_2(int(pincode[2])):
        return 'Корректен'
    else:
        return 'Некорректен'
