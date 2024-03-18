def prime(number):
    dels = [1]
    for i in range(2, number + 1):
        if number % i == 0:
            dels.append(i)
    if number == 1:
        return ''
    elif len(dels) != 2:
        return 'Составное число'
    else:
        return 'Простое число'
