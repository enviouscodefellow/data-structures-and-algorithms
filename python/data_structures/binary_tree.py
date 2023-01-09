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

