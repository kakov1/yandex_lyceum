from functools import reduce


class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.bottom = self.width * self.length
        self.all = sorted([self.length, self.width, self.height])
        self.volume = length * width * height

    def __add__(self, other):
        if check_biggest(self, other):
            return self.volume
        elif check_biggest(other, self):
            return other.volume
        else:
            if self.bottom > other.bottom:
                return self.bottom * (self.height + other.height)
            else:
                return other.bottom * (self.height + other.height)


def check_biggest(x, y):
    if x.volume > y.volume and x.all[0] > y.all[0] and\
            x.all[1] > y.all[1] and x.all[2] > y.all[2]:
        return True
    else:
        return False

print(Box(1, 1, 2) + Box(2, 2, 2))
