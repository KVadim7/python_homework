import random

first_number = random.randint(0, 10)
second_number = random.randint(0, 15)



while True:
    print(f'What is: ', first_number, '*', second_number, '=')
    if first_number*second_number == int(input('Your answer: ')):
        print('Correct!')
        break
    else:
        print('Wrong!')
