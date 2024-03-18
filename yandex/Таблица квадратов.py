def squared(a, b, k):
    source = a
    string = []
    for i in range(a, b + 1):
        if i % k:
            string.append(i ** 2)
        if int(str(i)[-1]) + 1 == int(str(source)[-1]) and not i % k:
            string = []


squared(11, 99, 10)