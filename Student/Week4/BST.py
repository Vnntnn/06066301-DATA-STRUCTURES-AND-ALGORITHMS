"""Binary search tree"""
class BSTNode:
    """Lab 04.01"""
    def __init__(self, data: int):
        """Init node attributes"""
        self.__data = data
        self.__left = None
        self.__right = None

    def set_data(self, data):
        """Set data of BSTNode"""
        self.__data = data

    def set_left(self, left):
        """Set left child of BSTNode"""
        self.__left = left
    
    def set_right(self, right):
        """Set right child of BSTNode"""
        self.__right = right

    def get_data(self):
        """Retrieve data from node"""
        return self.__data
    
    def get_left(self):
        """Retrieve left child from node"""
        return self.__left
    
    def get_right(self):
        """Retrieve right child from node"""
        return self.__right


class BST:
    """Lab 04.02 - Lab 04.06"""
    def __init__(self):
        self.__root = None

    def set_root(self, root):
        self.__root = root
    
    def get_root(self):
        return self.__root

    def is_empty(self):
        return self.__root is None

    def insert(self, data):
        def insert_(node: BSTNode, data):
            if not node:
                return BSTNode(data)
            elif data < node.get_data():
                node.set_left(insert_(node.get_left(), data))
            else:
                node.set_right(insert_(node.get_right(), data))
            return node
        self.set_root(insert_(self.get_root(), data))

    def traverse(self):
        if self.is_empty():
            return print("This is an empty binary search tree.")

        current = self.get_root()

        # Preorder: root -> left -> right
        print("Preorder: ", end="")
        def preorder_(node: BSTNode):
            if node is not None:
                print("-> " + str(node.get_data()), end=" ")
                preorder_(node.get_left())
                preorder_(node.get_right())
        preorder_(current)
        print()

        # Inorder: left -> root -> right
        print("Inorder: ", end="")
        def inorder_(node: BSTNode):
            if node is not None:
                inorder_(node.get_left())
                print("-> " + str(node.get_data()), end=" ")
                inorder_(node.get_right())
        inorder_(current)
        print()

        # Postorder: left -> right -> root
        print("Postorder: ", end="")
        def postorder_(node: BSTNode):
            if node is not None:
                postorder_(node.get_left())
                postorder_(node.get_right())
                print("-> " + str(node.get_data()), end=" ")
        postorder_(current)
        print()

    def find_min(self):
        if self.is_empty():
            return None
        current = self.get_root()
        while current.get_left() is not None:
            current = current.get_left()
        return current.get_data()

    def find_max(self):
        if self.is_empty():
            return None
        current = self.get_root()
        while current.get_right() is not None:
            current = current.get_right()
        return current.get_data()

    def delete(self, data):
        if self.is_empty():
            return None

        current = self.root
        parent = None

        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        if current is None:
            print("Delete Error, %i is not found in Binary Search Tree." %data)
            return None

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        else:
            max_node_parent = current
            max_node = current.left
            while max_node.right:
                max_node_parent = max_node
                max_node = max_node.right

            current.data = max_node.data

            if max_node_parent.left == max_node:
                max_node_parent.left = max_node.left
            else:
                max_node_parent.right = max_node.left

        return data

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()
