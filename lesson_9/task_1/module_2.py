from module_1 import pythagorean_theorem
def text_theorem(a, b):
    print(f'Якщо перший катет дорівнює: {a}, а другий {b}. Тоді третій катет буде дорівнювати: {int(pythagorean_theorem(a, b))}')
#Sorry for my example
print(text_theorem(10, 15))
