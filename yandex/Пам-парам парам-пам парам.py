
data = [[j for j in i if j in ['а', 'о', 'у', 'ы', 'и', 'е', 'я', 'ё', 'ю']]
        for i in input().split()]
print('Парам пам-пам' if len(list(filter(lambda x: len(data[0]) == len(x), data))) == len(data)
      else 'Пам парам')
