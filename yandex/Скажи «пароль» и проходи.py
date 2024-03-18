def ask_password():
    for i in range(3):
        password = input()
        if password == 'password':
            print('Пароль принят')
            break
        else:
            if i == 2:
                print('В доступе отказано')
