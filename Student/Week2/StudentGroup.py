class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        if not self.size:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            last = self.data.pop()
            self.size -= 1
            return last

    def is_empty(self):
        if not self.data:
            return True
        else:
            return False

    def get_stack_top(self):
        if not self.size:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            last = self.data.pop()
            self.data.append(last)
            return last

    def get_size(self):
        return self.size

    def print_stack(self):
        print(self.data)

STUDENT = ArrayStack()
STUDENT_GROUP = list()

for _ in range(int(input())):
    STUDENT_GROUP.append(ArrayStack())

for _ in range(int(input())):
    STUDENT.push(input())

def main():
    """main function"""
    while STUDENT.get_size():
        for student_sub in STUDENT_GROUP:
            if STUDENT.get_size():
                student_sub.push(STUDENT.pop())

    for index, student_name in enumerate(STUDENT_GROUP):
        print(f"Group {index + 1}:", end=" ")
        print(*student_name.data, sep=", ")

main()
