# Manipulate the Data/portfolio.csv CSV file
# Compute the cost of all the stocks

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


total_cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', total_cost)
