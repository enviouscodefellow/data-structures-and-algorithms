class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    """
    Implements a binary tree
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self, node=None):
        if node is None:
            node = self.root
        values = []
        if node:
            values.append(node.value)
        if node.left:
            values.extend(self.pre_order(node.left))
        if node.right:
            values.extend(self.pre_order(node.right))
        return values

    def in_order(self, node=None):
        if node is None:
            node = self.root
        values = []
        if node.left:
            values.extend(self.in_order(node.left))
        if node:
            values.append(node.value)
        if node.right:
            values.extend(self.in_order(node.right))
        return values

    def post_order(self, node=None):
        if node is None:
            node = self.root
        values = []
        if node.left:
            values.extend(self.post_order(node.left))
        if node.right:
            values.extend(self.post_order(node.right))
        if node:
            values.append(node.value)
        return values

    def find_maximum_value(self):
        if self.root is None:
            raise InvalidOperationError("Tree is empty.")
        return self._find_maximum_value(self.root)

    def _find_maximum_value(self, node):
        if node is None:
            return float("-inf")

        left_max = self._find_maximum_value(node.left)
        right_max = self._find_maximum_value(node.right)
        return max(node.value, left_max, right_max)


class InvalidOperationError(Exception):
    pass
