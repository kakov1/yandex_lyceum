list_ = [input().lower() for i in range(int(input()))]
list_new = []
check = [',', '.', '!', '?', ':', ';']
for i in list_:
    current = ''
    for j in i:
        if j not in check:
            current += j
    list_new.extend(current.split())
counts = []
all_words = sorted(list(set(list_new)))
check = []
list_ = []
for i in range(len(all_words)):
    list_.append((all_words[i], list_new.count(all_words[i])))
    counts.append(list_new.count(all_words[i]))
counts.sort(reverse=True)
check = []
for i in counts:
    for j in list_:
        if i in j and j[0] not in check:
            print(j[0].capitalize())
            check.append(j[0])
            break
