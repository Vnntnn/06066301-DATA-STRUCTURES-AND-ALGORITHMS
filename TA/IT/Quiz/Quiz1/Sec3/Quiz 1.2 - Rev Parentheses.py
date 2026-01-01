class ArrayStack:
    def __init__(self):
        self.stack_data = []
        self.size = 0

    def push(self, data):
        self.stack_data.append(data)
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("Underflow!!")
        else:
            self.size -= 1
            return self.stack_data.pop()

    def get_stack_top(self):
        if self.size == 0:
            print("Underflow!!")
        else:
            return self.stack_data[-1]

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print(self.stack_data)
    
def rev_parentheses(in_str):
    stack = ArrayStack()

    for char in in_str:
        if char == ')':
            tempStack1 = ArrayStack()
            tempStack2 = ArrayStack()
            while not stack.is_empty() and stack.get_stack_top() != '(':
                tempStack1.push(stack.pop())
            if not stack.is_empty():
                stack.pop()
            while not tempStack1.is_empty():
                tempStack2.push(tempStack1.pop())
            while not tempStack2.is_empty():
                stack.push(tempStack2.pop())
        else:
            stack.push(char)

    result = ""
    while not stack.is_empty():
        result = stack.pop() + result
    print("output of ", in_str, " : ", result, sep="")


def main():
    rev_parentheses(input())

main()
