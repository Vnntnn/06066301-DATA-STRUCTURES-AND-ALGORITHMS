"""Tree Height"""
class Node:
    def __init__(self, data):
        """Constructor"""
        self.__data = data
        self.__left = None
        self.__right = None

    def getData(self):
        return self.__data
    
    def setData(self, data):
        self.__data = data

    def getLeft(self):
        return self.__left
    
    def setLeft(self, left):
        self.__left = left

    def getRight(self):
        return self.__right

    def setRight(self, right):
        self.__right = right

class BST:
    def __init__(self):
        """Constructor"""
        self.__root = None

    def getRoot(self):
        return self.__root

    def setRoot(self, root):
        self.__root = root

    def isEmpty(self):
        return self.__root is None

    def insert(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.setRoot(new_node)
            return
        current = self.getRoot()
        while True:
            if data < current.getData():
                if current.getLeft() is not None:
                    current = current.getLeft()
                else:
                    current.setLeft(new_node)
                    return
            else:
                if current.getRight() is not None:
                    current = current.getRight()
                else:
                    current.setRight(new_node)
                    return

    def isExist(self, data):
        current = self.getRoot()
        while current is not None:
            if data == current.getData():
                return True
            elif data < current.getData():
                current = current.getLeft()
            else:
                current = current.getRight()
        return False

    def treeHeight(self):
        def height(node):
            if node is None:
                return 0
            left_height = height(node.getLeft())
            right_height = height(node.getRight())
            return 1 + max(left_height, right_height)
        return height(self.getRoot())

def main():
    """main function"""
    bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            bst.insert(int(data))
        else:
            print("Invalid Condition")
    print(bst.treeHeight())

main()
