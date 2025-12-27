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
    s1 = ArrayStack()
    nstr = ""
    for char in in_str:
        if char != '(':
            nstr += char
        if char == ')':
            while not s1.is_empty():
                nstr += s1.pop()
        else:
            s1.push(char)
            continue
    pass
    
def main():
    rev_parentheses(input())

main()