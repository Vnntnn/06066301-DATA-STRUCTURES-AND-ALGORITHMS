class ArrayStack:
    def __init__(self):
        self._size = 0
        self._data = list()

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
            self._data.append(input_data)
            self._size += 1

    def pop(self):
        if not self._size:
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            last = self._data.pop()
            self._size -= 1
            return last

    def is_empty(self):
        if not self._data:
            return True
        else:
            return False

    def get_stack_top(self):
        if not self._size:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            last = self._data.pop()
            self._data.append(last)
            return last

    def get_size(self):
        return self._size

    def print_stack(self):
        print(self._data)

def copy_stack(stack1, stack2):
    rev_stack = ArrayStack()

    while not stack2.is_empty():
        stack2.pop()

    while not stack1.is_empty():
        rev_stack.push(stack1.pop())

    while not rev_stack.is_empty():
        item = rev_stack.pop()
        stack1.push(item)
        stack2.push(item)

def print_status():
    """Print all stacks"""
    print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
    STACK1_.print_stack()
    print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
    STACK2_.print_stack()
    print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
    STACK3_.print_stack()
    print("This is stack 4 (%d): " % STACK4_.get_size(), end='')
    STACK4_.print_stack()
    print()

STACK1_ = ArrayStack()
STACK2_ = ArrayStack()

STACK3_ = ArrayStack()
STACK4_ = ArrayStack()

# เพิ่มข้อมูลใน stack1
for _ in range(int(input())):
    STACK1_.push(input())

# เพิ่มข้อมูลใน stack2
for _ in range(int(input())):
    STACK2_.push(input())

TEMP1_, TEMP2_, TEMP3_, TEMP4_ = id(STACK1_), id(STACK2_), id(STACK3_), id(STACK4_)

print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
print_status()

print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("A")
print_status()

print("Copy Stack 2 to Stack 1")
copy_stack(STACK2_, STACK1_)
STACK2_.push("B")
print_status()

print("Copy Stack 3 to Stack 2")
copy_stack(STACK3_, STACK2_)
STACK3_.push("C")
print("Copy Stack 1 to Stack 3")
copy_stack(STACK1_, STACK3_)
STACK1_.push("D")
print("Copy Stack 2 to Stack 4")
copy_stack(STACK2_, STACK4_)
STACK2_.push("E")
print_status()

print(TEMP1_ == id(STACK1_), TEMP2_ == id(STACK2_),
TEMP3_ == id(STACK3_), TEMP4_ == id(STACK4_))
