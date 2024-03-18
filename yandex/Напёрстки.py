a, check, count = [[input(), i] for i in range(int(input()))], [], 0
m = int(input())
for i in range(m):
    n = int(input())
    check = []
    c = tuple(a)
    a = []
    count = 0
    for j in range(n):
        num = int(input())
        check.append(num - 1)
    for k in range(len(check)):
        a.append([c[check[count]][0], k])
        count += 1
for i in a:
    print(i[0])
