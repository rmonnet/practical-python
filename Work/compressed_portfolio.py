# Manipulate the Data/portfolio.csv CSV file

import gzip

with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    headers = next(f).upper().strip()
    print(headers)
    for line in f:
        stats = line.strip()
        print(stats)
