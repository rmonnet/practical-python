# Read from a CSV file and extract fields names 'name', 'shares', and 'price'.
# At the same time convert the extracted fields to the types str, int and float.

import csv
from pprint import pprint

with open('Data/portfoliodate.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)
    # specify the field names and types for extraction/conversion
    select = ['name', 'shares', 'price']
    types = [str, int, float]
    indices = [headers.index(colname) for colname in select]
    portfolio = []
    for row in rows:
        portfolio.append({colname: totype(row[index])
                         for colname, index, totype in zip(select, indices, types)})

pprint(portfolio)
