"""Find unique character from string using stack + greedy"""


class Stack:
    """stack object"""
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, data):
        self.data.append(data)
        self.size += 1

    def pop(self):
        if self.size <= 0:
            return False
        self.data.pop()
        self.size -= 1

    def get_stack_top(self):
        if self.size <= 0:
            return False
        top = self.data.pop()
        self.data.append(top)
        return top

    def is_empty(self):
        return True if not len(self.data) else False

class mewing:
    """sep char from str"""
    def __init__(self, texts):
        self.texts = texts
        self.data = Stack()

    def check(self):
        """Checking text methods"""
        for text in self.texts:
            if self.data.is_empty():
                self.data.push(text)

            
