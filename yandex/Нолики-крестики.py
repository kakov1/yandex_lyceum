length = int(input())
list_ = [input() for i in range(length)]
answer = ''
for i in list_:
    count = 1
    for j in range(1, len(i)):
        if i[j] != '.':
            if i[j] == i[j - 1]:
                count += 1
            else:
                count = 1
        if count == 3:
            answer = i[j - 1]
            break
if answer == '':
    for i in range(length):
        count = 1
        for j in range(1, length):
            if list_[j][i] != '.':
                if list_[j][i] == list_[j - 1][i]:
                    count += 1
                else:
                    count = 1
            if count == 3:
                answer = list_[j - 1][i]
                break
print(answer if answer != '' else '-')
