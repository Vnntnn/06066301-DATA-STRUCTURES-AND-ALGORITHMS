class ArrayStack:
    def __init__(self, data = []):
        self._size = 0
        self._data = data

    def push(self, data):
        self._data = self._data + [data]
        self._size += 1

    def pop(self):
        if not self._size:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            last_item = self._data[-1]
            del self._data[-1]
            self._size -= 1
            return last_item

    def is_empty(self):
        if not self._size:
            return True
        return False

    def get_stack_top(self):
        if not self._size:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self._data[-1]

    def get_size(self):
        return self._size

    def print_stack(self):
        return print(self._data)

CLAW = ArrayStack()
BRACKET = ArrayStack()
PAREN = ArrayStack()

def main(spam):
    check = True

    for i in spam:
        if i == "[":
            CLAW.push("[")
        elif i == "]":
            if CLAW.pop() == None:
                check = False

        if i == "{":
            BRACKET.push("{")
        elif i == "}":
            if BRACKET.pop() == None:
                check = False

        if i == "(":
            PAREN.push("(")
        elif i == ")":
            if PAREN.pop() == None:
                check = False

    print("False" if not check or CLAW.get_size() or BRACKET.get_size() or PAREN.get_size() else "True")
main(input())
