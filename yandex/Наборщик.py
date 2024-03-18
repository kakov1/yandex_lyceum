english = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
russian = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
letter = []
letter.extend(input())
for i in letter:
    count = 1
    if i in english:
        for j in english:
            if j == i:
                print((i, count))
                break
            count += 1
    else:
        for j in russian:
            if j == i:
                print((i, count))
                break
            count += 1
