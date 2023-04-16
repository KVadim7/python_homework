def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

print(outer_function(10)(5))
