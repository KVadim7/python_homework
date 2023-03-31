import random

base_string = input('Введіть базову строку: ')

for i in range(1, 6):
    result_string = ''
    indexes = ''
    while True:
        random_index = random.randint(0, len(base_string) - 1)
        if str(random_index) not in indexes:
            indexes = indexes + str(random_index)
            result_string = result_string + base_string[random_index]
        if len(indexes) == len(base_string):
            break

    print(result_string)
