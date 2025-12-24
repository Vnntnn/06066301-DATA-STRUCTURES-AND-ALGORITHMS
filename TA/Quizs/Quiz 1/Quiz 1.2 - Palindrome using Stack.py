"""

Average solution this quiz time: 5 - 10 mins
Time: 14:50 - 15:00 (Bangkok timezone)

"""

class ArrayStack:
    def __init__(self):
        self.stack_data = []
        self.size = 0

    def push(self, data: str) -> None:
        self.stack_data.append(data)
        self.size += 1

    def pop(self) -> str:
        if self.size == 0:
            print("Underflow!!")
        else:
            self.size -= 1
            return self.stack_data.pop()

    def get_stack_top(self) -> str:
        if self.size == 0:
            print("Underflow!!")
        else:
            return self.stack_data[-1]

    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def print_stack(self) -> None:
        if self.is_empty():
            print("Stack is empty.")
        else:
            print(self.stack_data)

def is_palindrome(in_str: str) -> None:
    cleaned_str: str = in_str.replace(" ", "").lower()
    stack: ArrayStack = ArrayStack()

    for char in cleaned_str:
        stack.push(char)
    
    for char in cleaned_str:
        if char != stack.pop():
            print(in_str, "is not a palindrome.")
            return

    print(in_str, "is a palindrome.")
    
def main():
    for _ in range(int(input())):
        is_palindrome(input())

main()