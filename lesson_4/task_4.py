my_name = 'vadim'
name_input = input('Enter your name: ')

while True:
    if name_input == my_name.upper():
        print('Good')
    elif name_input == my_name.capitalize():
        print('Ok')
    elif name_input == my_name:
        print('Super')
    else:
        print('Wrong')
    break
