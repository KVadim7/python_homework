from functools import wraps

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if not isinstance(args[0], type_):
                print(f"Argument type must be {type_}")
                return False
            if len(args) > max_length:
                print(f"Argument length must not exceed {max_length} characters")
                return False
            for symbol in contains:
                if symbol not in args[0]:
                    print(f"Argument must contain '{symbol}'")
                    return False
            return func(*args)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('S@SH05'))
print(create_slogan.__name__)

assert create_slogan('johndoe05@gmail.com') is not False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
