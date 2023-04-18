def logger(func):
    def wrapper(*args):
        args_str = ", ".join(str(arg) for arg in args)
        print(f"{func.__name__} called with {args_str}")
        return func
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

add(4, 5)
square_all(4, 5, 2, 5, 2, 25, 3)
