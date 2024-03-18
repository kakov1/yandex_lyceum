def equation(a, b):
    left = float(b.split(';')[0]) - float(a.split(';')[0])
    right = float(b.split(';')[1]) - float(a.split(';')[1])
    if left == 0:
        k = 0
    else:
        k = right / left
    b = float(a.split(';')[1]) - k * float(a.split(';')[0])
    if k == 0:
        print(b)
    else:
        print(k, b)
