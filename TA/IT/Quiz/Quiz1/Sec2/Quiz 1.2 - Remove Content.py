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

def remove_content(in_str):
    cleanStr = in_str.replace(' ', '')

    checkArr = ArrayStack()
    resultArr = ArrayStack()
    parenArr = ArrayStack()

    for char in cleanStr:
        if char == '(':
            parenArr.push(char)
            continue
        
        if char == ')' and not parenArr.is_empty():
            parenArr.pop()
            continue
        elif char == ')' and parenArr.is_empty():
            while not checkArr.is_empty():
                checkArr.pop()
            continue

        if parenArr.is_empty():
            checkArr.push(char)

    print(f"output of {in_str} : ", end="")
    while not checkArr.is_empty():
        resultArr.push(checkArr.pop())
    while not resultArr.is_empty():
        print(resultArr.pop(), end="")
    
def main():
    remove_content(input())

main()
