# Definition of a stock object for portfolio computations

class Stock:

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = int(shares)
        self.price = float(price)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f'{self.name:<10s} {self.shares:>10d} {self.price:>10.2f} {self.cost:>10.2f}'

# Example of using inheritance


class MyStock(Stock):

    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    # example of overriding a method using the original method via 'super'
    @property
    def cost(self):
        return self.factor * super().cost()


class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    # Other useful functions for a container
    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares


if __name__ == '__main__':

    from pprint import pprint

    import fileparse
    portdicts = fileparse.parse_csv('Data/portfolio.csv')
    pprint(portdicts)

    # portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    portfolio = [Stock(**d) for d in portdicts]
    for s in portfolio:
        print(s)

    print('Showing inheritance...')
    s = MyStock('GOOG', 100, 490.1, 1.1)
    print(s)
    s.sell(25)
    print(s)
    s.panic()
    print(s)

    print(f's is instance of MyStock {isinstance(s, MyStock)}')
    print(f's is instance of Stock {isinstance(s, Stock)}')
