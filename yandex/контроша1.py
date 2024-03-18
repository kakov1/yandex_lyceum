a, b, c, d = int(input()), int(input()), int(input()), int(input())
n = 2 ** a + 2 ** b - 2 ** c
number = list()
while True:
    number.append(n % 2)
    if n == 1:
        break
    n //= 2
number = str(int(''.join(list(map(str, reversed(number))))))
print(number.count(str(d)))
