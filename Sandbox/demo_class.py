
class Temp(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

t = Temp('Peter')


print(t)
print(str(t))
print(repr(t))