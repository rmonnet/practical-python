# follow the stock data generated in 'Data/stocklog.csv'

import os
import time


def follow(filename):

    f = open(filename)
    # move file pointer 0 bytes from end of file
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if len(line) > 0:
            yield line


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == '__main__':

    import report3
    portfolio = report3.read_portfolio('Data/portfolio.csv')
    stock_names = {s.name for s in portfolio}
    print(f'stock names to watch: {stock_names}')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
