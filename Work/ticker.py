
from follow import follow
from tableformat import create_formatter
import csv


def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows


def select_columns(rows, indices):
    # use a list comprehension like generator
    return ([row[index] for index in indices] for row in rows)


def convert_types(rows, types):
    # use a list comprehension like generator
    return ([cvt(val) for cvt, val in zip(types, row)] for row in rows)


def make_dicts(rows, headers):
    # use a list comprehension like generator
    return (dict(zip(headers, row)) for row in rows)


def filter_symbols(rows, names):
    # use a list comprehension like generator
    return (row for row in rows if row['name'] in names)


def stock_names(filename):
    with open(filename, 'rt') as f:
        headers = next(f)
        rows = csv.reader(f)
        return {stock[0] for stock in rows}


def print_stocks(rows, colnames, fmt):
    formatter = create_formatter(fmt)
    cap_colnames = [colname.capitalize() for colname in colnames]
    formatter.headings(cap_colnames)
    for row in rows:
        fields = [str(row[key]) for key in colnames]
        formatter.row(fields)


def ticker(portfile, logfile, fmt):
    colnames = ['name', 'price', 'change']
    names = stock_names(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, colnames)
    rows = filter_symbols(rows, names)
    print_stocks(rows, colnames, 'txt')


if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', create_formatter('txt'))
