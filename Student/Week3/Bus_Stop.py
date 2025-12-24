"""Bus stop"""
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

    def get_node_at(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current

def main(p, n):
    """main function"""
    bus_stops = SinglyLinkedList()
    counter = 0
    while counter < n + 1:
        bus_stops.insert_last(SinglyLinkedList())
        counter += 1

    counter = 0
    while counter < n:
        line = input()
        new_line = DataNode()
        current = new_line
        # split input
        for char in line:
            if char == " ":
                current.next = DataNode()
                current = current.next
            else:
                if current.data is None:
                    current.data = char
                else:
                    current.data += char
        stop = int(new_line.data)
        current_stop = bus_stops.get_node_at(stop).data
        current = new_line.next
        while current is not None:
            current_stop.insert_last(int(current.data))
            current = current.next
        counter += 1

    passengers = SinglyLinkedList()
    total_dropped = 0

    stop = 1
    while stop <= n:
        current = passengers.head
        prev = None
        while current is not None:
            if current.data == stop:
                total_dropped += 1
                if prev is None:
                    passengers.head = current.next
                else:
                    prev.next = current.next
                passengers.count -= 1
                current = prev.next if prev else passengers.head
            else:
                prev = current
                current = current.next

        current_stop = bus_stops.get_node_at(stop).data
        current = current_stop.head
        while current is not None and passengers.count < p:
            if current.data > stop:
                passengers.insert_last(current.data)
            current = current.next
        stop += 1

    print(total_dropped)

main(int(input()), int(input()))
