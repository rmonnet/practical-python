# Read the data from a portfolio file and populate a list of tuples

import csv
import sys
from pprint import pprint


def read_portfolio(filename):
    """
    Read a file of portfolio data and return as a list of dictionaries.

    The keys to each stock dictionary are 'name', 'shares' and 'price'.
    """
    # Using zip to pair headers and values and build a dictionary
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for lineno, row in enumerate(rows, start=1):
            try:
                portfolio.append(dict(zip(headers, row)))
            except ValueError:
                print(f'Warning: skipped invalid entry {row} on line {lineno}')
    return portfolio


def read_prices(filename):
    """
    Read a file of stock prices and return as a dictionary of [name, price].
    """
    prices = []

    with open(filename, 'rt') as f:
        # the price database file has no headers
        rows = csv.reader(f)
        for row in rows:
            if len(row) < 2:
                continue
            try:
                prices.append(row)
            except ValueError:
                print(f'Warning: skipped invalid entry {row}')
    return dict(prices)


def portfolio_initial_cost(portfolio):
    """
    Compute the initial cost of a stock portfolio represented as a list
    of dictionary with keys 'name', 'shares' and 'price'.
    """
    total_cost = 0
    for stock in portfolio:
        total_cost += int(stock['shares']) * float(stock['price'])
    return total_cost


def portfolio_current_value(portfolio, prices):
    """
    Compute the current value of a stock protfolio using a database of current stock prices.

    The portfolio is a list of stock dictionaries with the keys being 'name', 'shares', and price'.
    The price database is a dictionary of stocks with k/v being 'name'/'price'.
    """
    total_value = 0
    for stock in portfolio:
        total_value += int(stock['shares']) * float(prices[stock['name']])
    return total_value


def make_report(portfolio, prices):
    """
    Produce a report on the portfolio as a list of tuples (name, shares, price, change).

    The price is the original price, the change is the different between the current and the
    original price.
    """
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = int(stock['shares'])
        price = float(prices[name])
        original_price = float(stock['price'])
        report.append((name, shares, price, price-original_price))
    return report


def print_report(report):
    """
    Print a tabulated version of the report.
    The table columns are Name, Shares, Price and Change.
    Each column is 10 characters wide.
    """
    print('Stock report:')
    print('      Name     Shares      Price     Change')
    print('---------- ---------- ---------- ----------')
    for name, shares, price, change in report:
        dollar_price = f'${price:0.2f}'
        print(
            f"{name:>10s} {shares:>10d} {dollar_price:>10s} {change:10.2f}")

# portfolio = read_portfolio_as_tuples('Data/portfolio.csv')
# print('Portfolio as tuple:')
# pprint(portfolio)


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)

    prices = read_prices(prices_filename)

    initial_cost = portfolio_initial_cost(portfolio)
    print(f'Initial cost : {initial_cost:12.2f}')

    current_value = portfolio_current_value(portfolio, prices)
    print(f'Current value: {current_value:12.2f}')

    print(f'Gain         : {current_value - initial_cost:12.2f}')

    report = make_report(portfolio, prices)
    print_report(report)


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

portfolio_report(filename, 'Data/prices.csv')
