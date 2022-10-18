class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self, full_name, age, is_married,):
        print(f"Fullname: {full_name} \n "
              f"Age: {age} \n "
              f"Is married: {is_married}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        isinstance(marks, dict)
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average(self):
        print(sum(self.marks) / i.marks)


class Teacher(Person):

    salary = 12000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def teacher_cash(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary / 100 * 5) * (self.experience - 3))
            return new_salary


teacher = Teacher("Марина", 30, "No", 5)
print(f'Fullname: {teacher.fullname} Age: {teacher.age} Married: {teacher.is_married} experience'
      f': {teacher.experience}')
print(teacher.teacher_cash())


def create_students():
    student1 = Student(fullname="Андрей", age=14, is_married="No", marks={
        "Физра": 2,
        "Математика": 3,
        "Русский": 5,
        "Биология": 5,
        "Английский": 4,
    })
    student2 = Student(fullname="Дмитрий", age=15, is_married="No", marks={
        "Русский": 4,
        "Биология": 3,
        "Физра": 5,
        "Английский": 4,
        "Математика": 5,
    })
    student3 = Student(fullname="Сергей", age=14, is_married="No", marks={
        "Биология": 5,
        "Физра": 5,
        "Математика": 5,
        "Английский": 5,
        "Русский": 5,
    })
    results = [student1, student2, student3]
    return results


students = create_students()
for i in students:
    list_1 = []
    for marks in i.marks.values():
        list_1.append(marks)
    print(f"Fullname: {i.fullname}\n"
          f"Age: {i.age}\n"
          f"Married: {i.is_married}\n"
          f"Average marks: {sum(list_1) / len(list_1)}\n")
