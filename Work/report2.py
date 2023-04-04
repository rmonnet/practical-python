#! /usr/bin/env python3

# Read the data from a portfolio file and populate a list of tuples
# Same as report but import the parse_csv function from fileparse module.

import csv
import sys
from pprint import pprint
from fileparse import parse_csv


def read_portfolio(filename):
    """
    Read a file of portfolio data and return as a list of dictionaries.

    The keys to each stock dictionary are 'name', 'shares' and 'price'.
    """
    return parse_csv(filename, select=[('name', str), ('shares', int), ('price', float)])


def read_prices(filename):
    """
    Read a file of stock prices and return as a dictionary of [name, price].
    """
    prices = parse_csv(filename, select=[
                       ('name', str), ('price', float)], headers=['name', 'price'])
    return {entry['name']: entry['price'] for entry in prices}


def portfolio_initial_cost(portfolio):
    """
    Compute the initial cost of a stock portfolio represented as a list
    of dictionary with keys 'name', 'shares' and 'price'.
    """
    total_cost = 0
    for stock in portfolio:
        total_cost += stock['shares'] * stock['price']
    return total_cost


def portfolio_current_value(portfolio, prices):
    """
    Compute the current value of a stock protfolio using a database of current stock prices.

    The portfolio is a list of stock dictionaries with the keys being 'name', 'shares', and price'.
    The price database is a dictionary of stocks with k/v being 'name'/'price'.
    """
    total_value = 0
    for stock in portfolio:
        total_value += stock['shares'] * prices[stock['name']]
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
        shares = stock['shares']
        price = prices[name]
        original_price = stock['price']
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


def main(cli_options=[]):

    if len(cli_options) == 3:
        portfolio = cli_options[1]
        prices = cli_options[2]
    else:
        portfolio = 'Data/portfolio.csv'
        prices = 'Data/prices.csv'

    portfolio_report(portfolio, prices)


if __name__ == '__main__':
    main(sys.argv)
