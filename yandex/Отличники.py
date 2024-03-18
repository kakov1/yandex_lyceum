data = [[input() for i in range(int(input()))] for j in range(int(input()))]
count = 0
for elem in data:
    if any(map(lambda x: x[-1] == '5', elem)):
        count += 1
print('ДА' if count == len(data) else 'НЕТ')
