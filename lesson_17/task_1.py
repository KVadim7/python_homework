class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


def make_animal_talk(animal: Animal):
    return animal.talk()

dog = Dog()
cat = Cat()

make_animal_talk(dog)
make_animal_talk(cat)
