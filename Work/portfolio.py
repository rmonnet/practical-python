# Manipulate the Data/portfolio.csv CSV file

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).upper().strip()
    print(headers)
    for line in f:
        stats = line.strip()
        print(stats)
