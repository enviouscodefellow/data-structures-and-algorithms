from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Implements BST
    """

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(value, node.right)

    def contains(self, value):
        if self.root is None:
            return False
        else:
            return self._contains(value, self.root)

    def _contains(self, value, node):
        if value == node.value:
            return True
        elif value < node.value and node.left is not None:
            return self._contains(value, node.left)
        elif value > node.value and node.right is not None:
            return self._contains(value, node.right)
        return False
