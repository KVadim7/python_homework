def count_lines(name):
    with open(name, 'r') as file:
        return len(file.readlines())
def count_chars(name):
    with open(name, 'r') as file:
        return len(file.read())
def test(name):
    print(f"Number of lines: {count_lines(name)}")
    print(f"Number of characters: {count_chars(name)}")
