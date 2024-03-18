a = (1, 1)
print_ = a
b = int(input())
print(1)
for i in range(b - 1):
    a = tuple(print_)
    print(*a)
    print_ = [1, 1]
    for j in range(1, len(a)):
        print_.insert(j, a[j] + a[j - 1])
