class MinMaxWordFinder:
    def __init__(self):
        self.sentences = []

    def add_sentence(self, sentence):
        self.sentences += sentence.split()

    def shortest_words(self):
        return sorted(filter(lambda x: len(x) == len(
            sorted(self.sentences, key=lambda y: len(y))[0]), self.sentences))

    def longest_words(self):
        return sorted(set(filter(lambda x: len(x) == len(
            sorted(self.sentences, key=lambda y: len(y))[-1]), self.sentences)))

