def sum_squares():
    list_ = [i for i in range(10, 100)]
    print(sum(map(lambda x: x ** 2, filter(lambda x: not x % 9, list_))))


sum_squares()
