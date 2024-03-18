k, m, a, b = int(input()), int(input()), int(input()), int(input())
list_ = [i for i in range(a, b + 1)]
print(len(list(filter(lambda x: x % m, list_))) - len(list(filter(lambda x: x % k, list_))))
