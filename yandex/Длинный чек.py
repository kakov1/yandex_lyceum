cheque, count = [], 1


def add_item(item_name, item_cost):
    global cheque
    cheque.append((item_name, item_cost))


def print_receipt():
    global cheque, count
    if len(cheque):
        total = 0
        print(f'Чек {count}. Всего предметов: {len(cheque)}')
        for i in cheque:
            print(f'{i[0]} - {i[1]}')
            total += i[1]
        print(f'Итого: {total}')
        print('-----')
        cheque = []
        count += 1
