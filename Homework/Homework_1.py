class person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married


    def introduce_myself(self):
        married_status = "married" if self.is_married else "not married"

        print(f"Name: {self.full_name}, Age: {self.age}, Status: {self.is_married}" )

class Student(person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_mark(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        return total_marks / num_subjects if num_subjects > 0 else 0

class Teacher(person):
    base_salary = 30000ed)
        self.experience = experience

    def calculate_salary(self):
        bonus_years = max(0, self.experience - 3)
        bonus = Teacher.base_salary * 0.05 * bonus_years
        return Teacher.base_salary + bonus



    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_marri)
teacher = Teacher("Alice Brown", 45, True, 10)
teacher.introduce_myself()
print(f"Experience: {teacher.experience} years")
print(f"Salary: {teacher.calculate_salary()}\n")


def create_students():
    student1 = Student("John Doe", 16, False, {"Math": 90, "English": 85, "Science": 88})
    student2 = Student("Jane Smith", 17, False, {"Math": 75, "English": 80, "Science": 78})
    student3 = Student("Tom Harris", 15, False, {"Math": 92, "English": 88, "Science": 95})
    return [student1, student2, student3]



students = create_students()
for student in students:
    student.introduce_myself()
    print("Marks:")
    for subject, mark in student.marks.items():
        print(f"  {subject}: {mark}")
    print(f"Average Mark: {student.average_mark()}\n")

