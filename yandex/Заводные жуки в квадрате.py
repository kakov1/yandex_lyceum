length = float(input())
speed = float(input())
count = 0
while length - speed > 0.01:
    length = ((length - speed) ** 2 + speed ** 2) ** 0.5
    count += 1
print(count)
