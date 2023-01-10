import pytest
from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("Cannot dequeue from an empty queue.")
        value = self.front.value
        self.front = self.front.next
        return value

    def peek(self):
        if not self.front:
            raise InvalidOperationError("Cannot peek at an empty queue.")
        return self.front.value

    def is_empty(self):
        return self.front is None

# class InvalidOperationError(Exception):
#     pass
