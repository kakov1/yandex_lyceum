letters = list('AБВГДЕЁЖЗИЙКЛМНОРПСТУФХЦЧШЩЪЫЬЭЮЯ')


def who_are_you_and_hello():
    while True:
        name = input()
        if len(name.split()) == 1 and name[0] in letters and \
                not set(letters).intersection(set(list(name[1:]))) and name.isalpha():
            print('Привет,', name + '!')
            break
