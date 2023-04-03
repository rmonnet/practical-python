# Manipulate the Data/portfolio.csv CSV file
# Compute the cost of all the stocks
# Use the csv module

import csv

with open('Data/portfolio.csv', 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0
    for row in rows:
        shares = int(row[1])
        share_cost = float(row[2])
        total_cost = total_cost + shares * share_cost
print('Total cost', total_cost)
