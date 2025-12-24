"""AlmostMean"""
class DataNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        current = self.head
        if current is None:
            print("This is an empty list.")
        else:
            while current is not None:
                if current.next is not None:
                    print(current.data, end=" -> ")
                else:
                    print(current.data)
                current = current.next

    def insert_last(self, data):
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.count += 1

    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_before(self, node, data):
        new_node = DataNode(data)
        current = self.head
        prev = None
        while current is not None:
            if current.data == node:
                if prev is None:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    prev.next = new_node
                    new_node.next = current
                self.count += 1
                return 0
            prev = current
            current = current.next
        else:
            print("Cannot insert, " + node + " does not exist.")

    def delete(self, data):
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                if self.head.data == data:
                    self.head = self.head.next
                elif current.next is not None:
                    prev.next = current.next
                    self.count -= 1
                else:
                    prev.next = None
                return 0
            current = current.next
            prev = current
        print("Cannot delete, " + data + " does not exist.")

STUDENT = SinglyLinkedList()
NUM = int(input())
SUM = 0

# Split tab from input
for _ in range(NUM):
    b_student = input().split('\t')
    STUDENT.insert_last(b_student)

# Sum score
CURRENT = STUDENT.head
while CURRENT is not None:
    i = 1
    for s_score in CURRENT.data:
        if i == 1:
            i += 1
            continue
        SUM += float(s_score)
        break
    CURRENT = CURRENT.next

# Calc mean
MEAN = SUM / NUM

# Find mean
ID = ""
ID_SCORE = 0

CURRENT = STUDENT.head
while CURRENT is not None:
    i = 1
    current_id = ""
    for id in CURRENT.data:
        if i == 1:
            current_id = id
            i += 1
        else:
            if ID_SCORE < float(id) <= MEAN:
                ID_SCORE = float(id)
                ID = current_id
            break
    CURRENT = CURRENT.next

print(ID + "\t" + str(ID_SCORE))
