from itertools import product


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, rectangle):
        rectangle_1 = set(product(*[[i for i in range(self.x, self.x + self.w + 1)],
                                    [i for i in range(self.y, self.y + self.h + 1)]]))
        rectangle_2 = set(product(*[[i for i in range(rectangle.get_x(),
                                     rectangle.get_x() + rectangle.get_w() + 1)],
                                    [i for i in range(rectangle.get_y(),
                                     rectangle.get_y() + rectangle.get_h() + 1)]]))
        new = rectangle_1.intersection(rectangle_2)
        if rectangle_1.intersection(rectangle_2) and len(set(map(lambda x: x[0], new))) >= 2\
                and len(set(map(lambda x: x[1], new))) >= 2:
            new = sorted(new, key=lambda x: sum(x))
            return Rectangle(new[0][0], new[0][1], new[-1][0] - new[0][0],
                             new[-1][1] - new[0][1])
        else:
            return None

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h
