class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    student_list.sort(key=lambda x: x.cgpa, reverse=True)

# Test the function with different input lists of students
students1 = [
    Student('Alice', 'A001', 3.8),
    Student('Bob', 'B002', 3.5),
    Student('Charlie', 'C003', 4.0)
]

students2 = [
    Student('David', 'D004', 3.9),
    Student('Eve', 'E005', 3.7),
    Student('Frank', 'F006', 3.2)
]

sort_students(students1)
sort_students(students2)

# Print sorted student lists
for student in students1:
    print(f'{student.name} ({student.roll_number}): CGPA - {student.cgpa}')

for student in students2:
    print(f'{student.name} ({student.roll_number}): CGPA - {student.cgpa}')