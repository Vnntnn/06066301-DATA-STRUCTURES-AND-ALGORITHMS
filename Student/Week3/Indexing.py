"""Indexing"""
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

MENU = SinglyLinkedList()

while (FOOD:= input()) != "Last":
    MENU.insert_last(FOOD)

def main():
    index = int(input())
    if index < 0:
        index = MENU.count + index
    if index < 0 or index >= MENU.count:
        return "Error"
    try:
        current = MENU.head
        for _ in range(index):
            current = current.next
        return current.data
    except AttributeError:
        return "Error"

print(main())
