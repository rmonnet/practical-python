# How to define generators

def countdown(n):
    while n > 0:
        yield n
        n -= 1


for x in countdown(10):
    print(x, end=' ')
print()
