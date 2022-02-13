class A:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def check(arg1, arg2):
        return arg1 + arg2


class B(A):
    def check(arg1, arg2):
        print(arg1 - arg2)


class C(B):
    def check(arg1, arg2):
        print(arg1 * arg2)


A.check(10, 15)
B.check(10, 15)
C.check(10, 15)
