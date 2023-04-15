def square_divide():
    try:
        a = float(input("Enter a number a: "))
        b = float(input("Enter a number b: "))
        if b == 0:
            raise ZeroDivisionError("Can't division by zero")
        result = (a ** 2) / b
        return result
    except ValueError:
        print("Error: Only numbers!")
print(square_divide())
