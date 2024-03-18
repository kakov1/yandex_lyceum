class BoundingRectangle:
    def __init__(self):
        self.points = []
        self.width_ = 0
        self.height_ = 0
        self.bottom_y_ = 0
        self.top_y_ = 0
        self.left_x_ = 0
        self.right_x_ = 0

    def add_point(self, x, y):
        self.points += [(x, y)]
        end = ((max(map(lambda k: k[0], self.points)), max(map(lambda k: k[1], self.points))),
               (min(map(lambda k: k[0], self.points)), min(map(lambda k: k[1], self.points))))
        self.bottom_y_ = end[1][1]
        self.top_y_ = end[0][1]
        self.left_x_ = end[1][0]
        self.right_x_ = end[0][0]
        self.width_ = abs(end[0][0] - end[1][0])
        self.height_ = abs(end[1][1] - end[0][1])

    def width(self):
        return self.width_

    def height(self):
        return self.height_

    def bottom_y(self):
        return self.bottom_y_

    def top_y(self):
        return self.top_y_

    def left_x(self):
        return self.left_x_

    def right_x(self):
        return self.right_x_
