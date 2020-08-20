
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
    @staticmethod
    def action(name):
        return name
    def show(self):
        print(f"it's a {self.color} {self.shape}")

result = toy.car('red',3)
result.show()

print(toy.action('crash'))