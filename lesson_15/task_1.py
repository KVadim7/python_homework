class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.name} {self.last_name} and I’m {self.age} years old")

my_name = Person("Carl", "Johnson", 26)

my_name.talk()
