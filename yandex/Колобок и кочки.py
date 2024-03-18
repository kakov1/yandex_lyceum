n = int(input())
jumps = [int(input()) for _ in range(n)]
words = [input() for _ in range(n)]
count = 0
word = []
check = 0
for i in jumps:
    check = 0
    for j in words[count]:
        if words[count].count(j) == i:
            if j in word:
                if len(word) == count:
                    word.append(j)
                    check += 1
            else:
                word.append(j)
                check += 1
    count += 1
    if check != 1:
        check = - 1
        break
if len(word) != len(words) or check == -1:
    print('нечленораздельно')
else:
    print(*word, sep='')
