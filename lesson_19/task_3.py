class MyIterable:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        if step == 0:
            raise ValueError("Step cannot be zero")

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.end) or (self.step < 0 and self.current <= self.end):
            raise StopIteration
        result = self.current
        self.current += self.step
        return result

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(len(self)))]
        elif isinstance(index, int):
            if index < 0:
                index += len(self)
            if index >= len(self) or index < 0:
                raise IndexError("Index out of range")
            return self.start + index * self.step
        else:
            raise TypeError("Invalid index type")

    def __len__(self):
        return (self.end - self.start - 1) // self.step + 1


my_iterable = MyIterable(1, 11)

for i in my_iterable:
    print(i)

print(my_iterable[:])

print(my_iterable[2:6])

print(my_iterable[::-1])

print(f'Length: {len(my_iterable)}')
