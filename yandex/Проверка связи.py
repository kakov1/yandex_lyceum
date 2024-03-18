string, count = input().split(), 1
for i in string:
    print(string[:count].count(i), end=' ')
    count += 1
