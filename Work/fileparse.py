
import csv
from pprint import pprint
import logging

log = logging.getLogger(__name__)
print('>>>', __name__)


def parse_csv(filename, select=None, headers=None):
    """
    Parse a CSV file into a list of records
    """
    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        # read the headers
        if not headers:
            headers = next(rows)

        if select:
            indices = [(headers.index(name), cvt) for name, cvt in select]
            headers = [headers[index] for index, cvt in indices]
        else:
            indices = []

        records = []
        for row in rows:
            # skip rows with no data
            if not row:
                continue
            # if we selected a subset of column, filter the row down to this subset
            if indices:
                try:
                    row = [cvt(row[index]) for index, cvt in indices]
                    record = dict(zip(headers, row))
                except ValueError as error:
                    log.warning('Skipping invalid entry %s', row)
                    log.debug('Exception is %s', error)
            else:
                record = dict(zip(headers, row))

            records.append(record)

    return records


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)

    portfolio = parse_csv('Data/portfolio.csv',
                          select=[('name', str), ('shares', int), ('price', float)])
    print('Portfolio:')
    pprint(portfolio)

    prices = parse_csv('Data/prices.csv',
                       select=[('name', str), ('price', float)], headers=['name', 'price'])
    print('Prices:')
    pprint(prices)

    portfolio2 = parse_csv('Data/missing.csv',
                           select=[('name', str), ('shares', int), ('price', float)])
    print('Portfolio2:')
    pprint(portfolio2)
