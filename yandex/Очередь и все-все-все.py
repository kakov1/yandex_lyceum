class Queue:
    def __init__(self, *args):
        self.queue = list(args)

    def __add__(self, other):
        return Queue(*(self.queue + other.queue))

    def __iadd__(self, other):
        self.queue += other.queue
        return self

    def __eq__(self, other):
        return self.queue == other.queue

    def __rshift__(self, other):
        return Queue(*self.queue[other:]) if other < len(self.queue) else Queue()

    def __str__(self):
        string = ' -> '.join(map(str, self.queue))
        return f'[{string}]'

    def __next__(self):
        return Queue(*self.queue[1:])

    def append(self, *args):
        self.queue += args

    def copy(self):
        return Queue(*self.queue)

    def pop(self):
        pop = self.queue.pop(0) if len(self.queue) else None
        return pop

    def extend(self, queue):
        self.queue += queue.queue

    def next(self):
        return Queue(*self.queue[1:])
