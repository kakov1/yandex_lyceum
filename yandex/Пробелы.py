def space_game(text):
    print('Вы проиграли' if (len(text.split()) - 1) % 2 else 'Вы выиграли')
