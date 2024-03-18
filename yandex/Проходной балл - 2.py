def check(k, pupils):
    return len(list(filter(lambda x: x, map(lambda x: int(x) >= k, pupils))))


data = input().split()
n, k = data[0], int(data[1])
pupils = data[2:]
print(check(k, pupils))
