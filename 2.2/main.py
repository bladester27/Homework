class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('sub_method from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        A.__init__(self)

    def sub_method(self, b):
        print('sub_method from class B:', b)
        A.sub_method(b, b + 1)


class X(B):
    def __init__(self):
        print('Initializing: class X')
        B.__init__(self)


    def sub_method(self, b):
        print('sub_method from class X:', b)
        B.sub_method(b, b + 1)


class Y(X):
    def __init__(self):
        print('Initializing: class Y')
        # super() с параметрами
        B.__init__(self)

    def sub_method(self, b):
        print('sub_method from class Y:', b)
        X.sub_method(b, b + 1)



x = X()
x.sub_method(1)
y = Y()
y.sub_method(5)