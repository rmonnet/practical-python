# use functions for reusable code

def sumcount(n):
    '''
    Returns the sum of the first n integers
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


print('sum of 1 to 3 = ', sumcount(3))
print('sum of 1 to 10 = ', sumcount(10))
