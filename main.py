class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_students(self):
        return self.students


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.teacher = None

    def set_teacher(self, teacher):
        self.teacher = teacher

    def get_teacher(self):
        return self.teacher


class School:
    def __init__(self):
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher_to_student(self, teacher, student):
        if teacher in self.teachers and student in self.students:
            teacher.add_student(student)
            student.set_teacher(teacher)
        else:
            print("Teacher or student not found in the school.")

    def get_students_of_teacher(self, teacher):
        return teacher.get_students()


# Misol:
school = School()

teacher1 = Teacher("John Doe", "Math")
teacher2 = Teacher("Jane Doe", "Science")

student1 = Student("Alice", 10)
student2 = Student("Bob", 11)
student3 = Student("Charlie", 12)

school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

school.assign_teacher_to_student(teacher1, student1)
school.assign_teacher_to_student(teacher1, student2)
school.assign_teacher_to_student(teacher2, student3)

print("Teacher 1 students:")
for student in school.get_students_of_teacher(teacher1):
    print(student.name)

print("Teacher 2 students:")
for student in school.get_students_of_teacher(teacher2):
    print(student.name)
```

Bu kodda, `Teacher` va `Student` klasslari orasida munosabat bog'langan. `Teacher` klassi `add_student`, `remove_student` va `get_students` metodlariga ega bo'lib, shu klassdagi talabalar ro'yxatini saqlaydi. `Student` klassi `set_teacher` va `get_teacher` metodlariga ega bo'lib, shu klassdagi o'qituvchini saqlaydi. `School` klassi `add_teacher`, `add_student`, `assign_teacher_to_student` va `get_students_of_teacher` metodlariga ega bo'lib, maktabdagi o'qituvchilar va talabalar ro'yxatini saqlaydi.
