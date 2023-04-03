# Manipulate the Data/portfolio.csv CSV file
# Compute the cost of all the stocks

import sys


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f).strip().split(',')
        total_cost = 0
        for line in f:
            stock = line.strip().split(',')
            try:
                shares = int(stock[1])
                share_cost = float(stock[2])
                total_cost = total_cost + shares * share_cost
            except ValueError:
                print(f"Warning: skipping invalid entry '{line.strip()}'")
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

total_cost = portfolio_cost(filename)
print('Total cost', total_cost)
