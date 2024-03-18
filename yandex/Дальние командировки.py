n = int(input())
check = [9 * 10 ** 0, 18 * 10 ** 1, 27 * 10 ** 2, 36 * 10 ** 3, 45 * 10 ** 4,
         54 * 10 ** 5, 63 * 10 ** 6, 72 * 10 ** 7, 81 * 10 ** 8, 90 * 10 ** 9]
for i in check:
    if sum(check[:check.index(i)]) >= n:
        count = check.index(i)
        check[count - 1] = n - sum(check[:count - 1])
        check = check[:count]
        for j in check:
            check[check.index(j)] = j // (check.index(j) + 1)
        print(sum(check))
        break
