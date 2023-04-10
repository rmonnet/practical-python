
import time


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__module__}.{func.__name__}: {end - start:0.3f}s')
        return res
    return wrapper


def logged(func):
    def wrapper(*args, **kwargs):
        print('>> Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@timed
def add(x, y):
    time.sleep(1)
    return x + y


@logged
def sub(x, y):
    return x - y


print('add(1,2) = ', add(1, 2))
print('sub(1,2) = ', sub(1, 2))
