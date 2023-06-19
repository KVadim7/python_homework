def with_index(iterable, start=0):
    for i in iterable:
        yield start, i
        start += 1


list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for index, item in with_index(list):
    print(index, item)
    