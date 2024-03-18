import pymorphy2

word = pymorphy2.MorphAnalyzer().parse(input())
if 'NOUN' in word[0].tag:
    word = word.normal_form.inflect({'gent', 'plur'})
    for i in word:
        printI
else:
    print('Не существительное')
