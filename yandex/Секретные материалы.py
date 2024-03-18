def print_document(pages):
    for i in pages:
        if i[:8] == 'Секретно':
            print('Дальнейшие материалы засекречены')
            break
        elif i == pages[-1]:
            print(i)
            print('Напечатано без купюр')
        else:
            print(i)
