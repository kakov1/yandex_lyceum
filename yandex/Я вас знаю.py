count, name = 0, ''


def polite_input(question):
    global count, name
    if count == 0:
        print('Как вас зовут?')
        name = input()
    print(f'{name}, {question}')
    count += 1
    return input()
