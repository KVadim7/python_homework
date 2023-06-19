def in_range(start, end, step=1):
    if step == 0:
        raise ValueError('Step cannot be zero')
    while (step > 0 and start < end) or (step < 0 and start > end):
        yield start
        start += step

for i in in_range(1, 10):
    print(i)
