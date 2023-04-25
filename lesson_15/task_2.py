class Dog:
    age_factor = 7
    def __init__(self, age_dog):
        self.age_dog = age_dog

    def human_age(self):
        return f"The dog’s age in human equivalent: {self.age_dog * self.age_factor} years old"

bulldog = Dog(5)
print(bulldog.human_age())
