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

def remove_duplicate(in_str):
    checkStr = in_str

    checkStack = ArrayStack()
    resultStack = ArrayStack()
    for i in checkStr:
        if checkStack.is_empty():
            checkStack.push(i)
        elif i.lower() != checkStack.get_stack_top().lower():
            checkStack.push(i)
        else:
            print("Remove duplicate :", checkStack.pop().lower())
    
    while not checkStack.is_empty():
        resultStack.push(checkStack.pop())

    print("output of", in_str, ": ", end="")
    while not resultStack.is_empty():
        print(resultStack.pop(), end="")    

def main():
    remove_duplicate(input())

main()
