class Base:
    def method(self):
        return 'Hello from Base'


class Child(Base):
    def method(self):
        return 'Hello from Child'


a = Base()
b = Child()
print(a.method())
print(b.method())
