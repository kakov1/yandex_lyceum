data = list(map(int, input().split()))
commands = [input() for i in range(int(input()))]
for i in commands:
    if i == 'make_negative':
        for j in range(len(data)):
            if data[j] > 0:
                data[j] *= -1
    elif i == 'square':
        data = list(map(lambda x: x ** 2, data))
    elif i == 'strange_command':
        for j in range(len(data)):
            if not data[j] % 5:
                data[j] += 1
print(*data)
