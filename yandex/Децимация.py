a = [input() for i in range(int(input()))]
b = int(input())
c = int(input())
for i in range(c):
    delete = []
    for j in range(len(a)):
        if not (j + 1) % b:
            delete.append(j)
    for j in range(len(delete)):
        del a[delete[j] - j]
for i in a:
    print(i)
