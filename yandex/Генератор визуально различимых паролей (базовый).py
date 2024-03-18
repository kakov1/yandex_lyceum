from string import ascii_letters, digits
from random import choice


def main(n, m):
    passwords = []
    for i in range(n):
        password = ''
        for j in range(m):
            symbol = choice(ascii_letters + digits)
            while symbol in 'lI1oO0':
                symbol = choice(ascii_letters + digits)
            password += symbol
        while password in passwords:
            password = generate_password(m)
        passwords.append(password)
    return passwords


def generate_password(m):
    return ''.join(main(1, m))
