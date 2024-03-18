class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass

    def info(self):
        return ''

    def describe(self):
        print(self.name, self.info())


class Person(User):
    def __init__(self, name, birthday):
        super(Person, self).__init__(name)
        self.birthday = birthday

    def info(self):
        return f'Дата рождения: {self.birthday}'

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, description):
        super(Community, self).__init__(name)
        self.description = description

    def info(self):
        return f'Описание: {self.description}'
