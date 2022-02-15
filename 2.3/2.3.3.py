class Temp:
    def __init__(self, value, var):
        self.value = value
        self.var = var

    @property
    def conv(self):
        if self.var == 'F':
            return str(round(((self.value - 32) / 1.8), 2)) + 'C'
        elif self.var == 'C':
            return str(round(((self.value * 1.8) + 32), 2)) + 'F'

    def set_temp_C(self, arg):
        self.value = arg
        self.var = 'C'

    def set_temp_F(self, arg):
        self.value = arg
        self.var = 'F'

    def get_temp(self):
        return str(self.value) + str(self.var)

    def get_temp_C(self):
        if self.var == 'C':
            return str(self.value) + 'C'
        else:
            return self.conv

    def get_temp_F(self):
        if self.var == 'F':
            return str(self.value) + 'F'
        else:
            return self.conv


a = Temp(100, 'F')
print(a.get_temp())
print(a.conv)
a.set_temp_F(120)
print(a.get_temp())
print(a.get_temp_F())
print(a.get_temp_C())
a.set_temp_C(100)
print(a.get_temp())
print(a.get_temp_C())
print(a.get_temp_F())
