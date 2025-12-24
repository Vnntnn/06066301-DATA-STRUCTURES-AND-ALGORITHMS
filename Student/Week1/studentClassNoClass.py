"""Student Class without using class method"""

LST = [[input() for _ in range(5)] for _ in range(3)]
CHECK = input()

for i in LST:

    if i[3] == str(CHECK):

        if i[1] == "Male":
            print(f"Mr {i[0]} ({i[2]}) ID: {i[3]} GPA {float(i[4]):.2f}")
            break

        elif i[1] == "Female":
            print(f"Miss {i[0]} ({i[2]}) ID: {i[3]} GPA {float(i[4]):.2f}")
            break

else:
    print("Student not found")
