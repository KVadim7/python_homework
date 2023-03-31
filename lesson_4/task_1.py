new_string = input('Please, enter string: ')

if len(new_string) < 2:
    None
if len(new_string) >= 2:
    print(new_string[:2] + new_string[-2:])
