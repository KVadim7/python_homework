while True:
    number_phone = input('Enter number phone: ')
    if len(number_phone) == 10 and number_phone.isdigit() is True:
        print('Correct!')
        break
    if len(number_phone) != 10:
        print('10 symbols!')
    elif number_phone.isdigit() is not True:
        print('Only numbers!')
