# follow the stock data generated in 'Data/stocklog.csv'

import os
import time


def follow(filename):

    f = open(filename)
    # move file pointer 0 bytes from end of file
    # f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if len(line) > 0:
            yield line


def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line


if __name__ == '__main__':

    lines = follow('Data/stocklog.csv')
    ibm = filematch(lines, 'IBM')
    for line in ibm:
        print(line, end='')
