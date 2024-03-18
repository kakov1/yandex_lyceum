n = int(input())
count_1 = 0
for i in range(1, n + 1):
    count = 0
    previous = count_1
    while count < n:
        if count_1 == 0:
            count += i + previous
        else:
            count += i + previous - i
        count_1 += 1
    if count == n:
        print(i)
        break
