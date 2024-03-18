n = int(input())
check = True
for i in range(2, n):
    check = True
    for j in range(2, n - 1):
        if i % j == 0 and j != i:
            check = False
            break
    if check:
        print(i)
