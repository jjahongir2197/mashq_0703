class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)

    def get_info(self):
        return f"{self.name} | O'rtacha: {self.average()}"


class Teacher(Person):
    def give_mark(self, student, mark):
        student.add_mark(mark)
        print(f"{student.name} ga {mark} qo'yildi.")


class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_students(self):
        print("\nTalabalar:")
        for s in self.students:
            print(s.get_info())


def run_school():
    school = School()

    s1 = Student("Ali")
    s2 = Student("Vali")

    t1 = Teacher("Karim")

    school.add_student(s1)
    school.add_student(s2)
    school.add_teacher(t1)

    t1.give_mark(s1, 5)
    t1.give_mark(s1, 4)

    t1.give_mark(s2, 3)
    t1.give_mark(s2, 5)

    school.show_students()


run_school()
