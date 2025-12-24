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

def priority(op):
    """Priority operators"""
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    return 0

def infixtoPostfix(expression):
    """Convert infix expression to postfix."""
    operators = ArrayStack()
    postfix = []

    for i in expression:
        if i.isalnum():  # Operand
            postfix.append(i)

        elif i == "(":
            operators.push(i)

        elif i == ")":
            while not operators.is_empty() and operators.get_stack_top() != "(":
                postfix.append(operators.pop())
            operators.pop()  # Remove '('
        elif i in "+-*/":
            while (not operators.is_empty() and 
                    priority(i) <= priority(operators.get_stack_top())):
                postfix.append(operators.pop())
            operators.push(i)

    while not operators.is_empty():
        postfix.append(operators.pop())

    return "".join(postfix)

print(infixtoPostfix(input()))
