class Person:
    def __init__(self, name, patronymic, surname, numbers):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.numbers = numbers

    def get_phone(self):
        return self.numbers['private'] if 'private' in self.numbers.keys() else None

    def get_name(self):
        return '{} {} {}'.format(self.surname, self.name, self.patronymic)

    def get_work_phone(self):
        return self.numbers['work'] if 'work' in self.numbers.keys() else None

    def get_sms_text(self):
        return 'Уважаемый {} {}! Примите участие в нашем беспроигрышном ' \
               'конкурсе для физических лиц'.format(self.name, self.patronymic)


class Company:
    def __init__(self, name, kind, numbers, *names):
        self.name = name
        self.type = kind
        self.numbers = numbers
        self.names = names

    def get_phone(self):
        numbers = list(map(lambda x: x.numbers['work'], filter(
            lambda y: 'work' in y.numbers, self.names)))
        return self.numbers['contact'] if 'contact' in self.numbers.keys() else numbers[0] \
            if len(numbers) >= 1 else None

    def get_name(self):
        return self.name

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! ' \
               f'Примите участие в нашем беспроигрышном конкурсе для {self.type}'


def send_sms(*args):
    for name in args:
        if name.get_phone():
            print(f'Отправлено СМС на номер {name.get_phone()} с текстом: '
                  f'{name.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {name.get_name()}')
