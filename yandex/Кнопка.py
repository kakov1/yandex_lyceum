class Button:
    def __init__(self):
        self.button = 0

    def click(self):
        self.button += 1

    def click_count(self):
        return self.button

    def reset(self):
        self.button = 0
