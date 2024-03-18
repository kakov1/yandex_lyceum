dictionary = {i[0]: ' '.join(i[1:]) for i in [input().split() for j in range(int(input()))]}
for i in range(int(input())):
    guess = input()
    print(dictionary[guess] if guess in dictionary.keys() else 'Нет в словаре')
