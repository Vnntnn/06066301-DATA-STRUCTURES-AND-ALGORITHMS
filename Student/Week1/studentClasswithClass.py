"""Student Class using class method"""
class student:
    def __init__(self, name, gender, age, id, gpa):
        self.name = name
        self.gender = gender
        self.age = age
        self.id = id
        self.gpa = gpa

STUDENT1 = student(input(), input(), input(), input(), input())
STUDENT2 = student(input(), input(), input(), input(), input())
STUDENT3 = student(input(), input(), input(), input(), input())
CHECK = input()

for i in [STUDENT1, STUDENT2, STUDENT3]:

    if i.id == str(CHECK):

        if i.gender == "Male":
            print(f"Mr {i.name} ({i.age}) ID: {i.id} GPA {float(i.gpa):.2f}")
            break

        elif i.gender == "Female":
            print(f"Miss {i.name} ({i.age}) ID: {i.id} GPA {float(i.gpa):.2f}")
            break

else:
    print("Student not found")
