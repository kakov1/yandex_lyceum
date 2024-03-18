def choose_coffee(*args):
    answer = False
    for i in args:
        if i == 'Эспрессо':
            if ingredients[0] >= 1:
                ingredients[0] -= 1
                answer = True
                return 'Эспрессо'
        elif i == 'Капучино':
            if ingredients[0] >= 1 and ingredients[1] >= 3:
                ingredients[0] -= 1
                ingredients[1] -= 3
                answer = True
                return 'Капучино'
        elif i == 'Маккиато':
            if ingredients[0] >= 2 and ingredients[1] >= 1:
                ingredients[0] -= 2
                ingredients[1] -= 1
                answer = True
                return 'Маккиато'
        elif i == 'Кофе по-венски':
            if ingredients[0] >= 1 and ingredients[2] >= 2:
                ingredients[0] -= 1
                ingredients[2] -= 2
                answer = True
                return 'Кофе по-венски'
        elif i == 'Латте Маккиато':
            if ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[1] -= 2
                ingredients[2] -= 1
                answer = True
                return 'Латте Маккиато'
        elif i == 'Кон Панна':
            if ingredients[0] >= 1 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[2] -= 1
                answer = True
                return 'Кон Панна'
    if not answer:
        return 'К сожалению, не можем предложить Вам напиток'
