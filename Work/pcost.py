# Manipulate the Data/portfolio.csv CSV file
# Compute the cost of all the stocks

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).strip().split(',')
    total_cost = 0
    for line in f:
        stock = line.strip().split(',')
        shares = int(stock[1])
        share_cost = float(stock[2])
        total_cost = total_cost + shares * share_cost
print('Total cost', total_cost)
