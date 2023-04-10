
def typedproperty(name, expected_type):

    private_name = '_' + name

    @property
    def prop(self):
        # print('>>> in getter')
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        # print('>>> in setter')
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop


def String(name): return typedproperty(name, str)
def Integer(name): return typedproperty(name, int)
def Float(name): return typedproperty(name, float)


class Stock:

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f'{self.name:<10s} {self.shares:>10d} {self.price:>10.2f} {self.cost:>10.2f}'


if __name__ == '__main__':

    s = Stock('IBM', 10, 9.99)
    print(s.name)
