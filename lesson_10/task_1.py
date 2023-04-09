def oops():
    raise IndexError("Oops! It's IndexError")
def catch_error():
    try:
        oops()
    except IndexError as e:
        print(f"Caught an error: {e}")
print(catch_error())

"""
Якщо замінити помилку IndexError на KeyError, то наша функція не обробить нашу помилку 
і програма завершиться з необробленою помилкою KeyError
"""
