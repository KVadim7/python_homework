def make_operation(operator, *args):
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        result = args[0] - sum(args[1:])
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
    print(result)
