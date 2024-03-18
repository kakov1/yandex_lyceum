class BigBell:
    def __init__(self):
        self.count = 0

    def sound(self):
        if not self.count % 2:
            print('ding')
        else:
            print('dong')
        self.count += 1
