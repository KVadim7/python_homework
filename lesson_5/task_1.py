from random import randint


b = randint(1, 10)

while True:
    enter = int(input('Enter your number from 1 to 10: '))
    if enter == b:
        print(f'Congatulation! It was number {b}!')
        break
    else:
        print('Try again')
