
def filematch(filename, substr):
    with open(filename, 'tr') as f:
        for line in f:
            if substr in line:
                yield line


print('List all lines in the portfolio.csv:')
with open('Data/portfolio.csv', 'tr') as f:
    for line in f:
        print(line, end='')
print('\n')

print('List all lines in portfolio with IBM stock:')
for line in filematch('Data/portfolio.csv', 'IBM'):
    print(line, end='')
print()
