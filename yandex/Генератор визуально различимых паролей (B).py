from random import choice
from string import ascii_uppercase, ascii_lowercase, digits


def main(n, m):
    passwords = []
    for i in range(n):
        password = ''
        for j in range(m):
            symbol = choice(ascii_uppercase + ascii_lowercase + digits)
            while symbol in 'lI1oO0':
                symbol = choice(ascii_uppercase + ascii_lowercase + digits)
            password += symbol
        while password in passwords or not\
                set(password).intersection(ascii_uppercase) or not \
                set(password).intersection(ascii_lowercase) or not\
                set(password).intersection(digits):
            password = generate_password(m)
        passwords.append(password)
    return passwords


def generate_password(m):
    return ''.join(main(1, m))
