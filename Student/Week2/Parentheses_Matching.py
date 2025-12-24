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

OPEN_PARENTHESES = ArrayStack()

def is_parentheses_matching(expression):
    check = True

    for i in expression:
        if i == "(":
            OPEN_PARENTHESES.push("(")
        if i == ")":
            if OPEN_PARENTHESES.pop() == None:
                check = False

    if not check or OPEN_PARENTHESES.get_size():
        print(f"Parentheses in {expression} are unmatched")
        print("False")
    else:
        print(f"Parentheses in {expression} are matched")
        print("True")

is_parentheses_matching(input())
