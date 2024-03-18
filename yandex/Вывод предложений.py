class Paragraph:
    def __init__(self, integer):
        self.integer = integer
        self.paragraph = []

    def add_word(self, word):
        self.paragraph += [word]

    def end(self):
        current = ''
        for i in self.paragraph:
            if not len(current):
                current = i
            elif len(current + ' ' + i) <= self.integer:
                current += ' ' + i
            else:
                print(self.just(current))
                current = i
        print(self.just(current))
        self.paragraph = []

    def just(self, string):
        return string


class LeftParagraph(Paragraph):
    def just(self, string):
        return string.ljust(self.integer, ' ')


class RightParagraph(Paragraph):
    def just(self, string):
        return string.rjust(self.integer, ' ')
