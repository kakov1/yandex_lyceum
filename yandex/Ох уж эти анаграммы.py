data = [input().lower() for i in range(int(input()))]
data = sorted(list(map(lambda x: (sorted(list(set(x))), x), data)), key=lambda x: x[0])
print(data)
prev = data[0]
string = [data[0][1]]
all_ = []
for i in data:
    if prev[0] == i[0] and i[1].lower() not in string:
        string.append(i[1])
    else:
        if len(string) > 1:
            all_.append(string)
        string = []
    prev = i
print(*sorted(all_, key=lambda x: x[0]), sep='\n')
