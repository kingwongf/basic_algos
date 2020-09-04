
class toy:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
    @classmethod
    def car(cls, color, sides):
        if sides==4:
            v = 'swuare'
        elif sides ==3:
            v = 'triangle'
        return cls(color, v)
    @classmethod
    def ty(cls):
        return cls
    @staticmethod
    def action(name):
        return name
    def show(self):
        print(f"it's a {self.color} {self.shape}")

    def sth_self(self):
        return self

print(type(toy('red',3).sth_self()))

result = toy.car('red',3)
result.show()


print()
print(toy.action('crash'))

print(toy.ty())
print(toy)
print(toy.ty)
print(dir(toy.car('red',4)))