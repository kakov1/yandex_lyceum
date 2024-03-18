class A:
    def __str__(self):
        return 'A.__str__ method'

    @staticmethod
    def hello():
        print('Hello')


class B:
    def __str__(self):
        return 'B.__str__ method'

    @staticmethod
    def good_evening():
        print('Good evening')


class C(A, B):
    pass


class D(B, A):
    pass
