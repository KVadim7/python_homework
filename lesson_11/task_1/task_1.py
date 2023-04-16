with open('mytext.txt', 'w') as f:
    f.write("Hello file world!\n")

with open('mytext.txt', 'r') as f:
    print(f.read())
