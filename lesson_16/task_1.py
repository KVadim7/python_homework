class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, name, age, gender, year, stipend):
        super().__init__(name, age, gender)
        self.year = year
        self.stipend = stipend

    def study(self):
        if self.year == 1:
            return f'I am studying for the {self.year}st year'
        if self.year == 2:
            return f'I am studying for the {self.year}nd year'
        if self.year == 3:
            return f'I am studying for the {self.year}rd year'
        else:
            return f'I am studying for the {self.year}th year'


class Teacher(Person):
    def __init__(self, name, age, gender, salary, subject):
        super().__init__(name, age, gender)
        self.salary = salary
        self.subject = subject

    def teach(self):
        return f'I teach {self.subject}'

student_1 = Student('Max', 19, 'male', 4, 1500)
teacher_1 = Teacher('Anna', 45, 'female', 10000, 'biology')

print(student_1.study())
print(teacher_1.teach())
