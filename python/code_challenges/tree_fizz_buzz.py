import pytest
from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree
from data_structures.queue import Queue


def fizz_buzz_tree(tree):
    new_tree = tree.clone()
    values = tree.breadth_first()

    for i, value in enumerate(values):
        if value % 15 == 0:
            values[i] = "FizzBuzz"
        elif value % 3 == 0:
            values[i] = "Fizz"
        elif value % 5 == 0:
            values[i] = "Buzz"
        else:
            values[i] = str(value)

    queue = Queue()
    queue.enqueue(new_tree.root)

    i = 0
    while not queue.is_empty():
        node = queue.dequeue()
        node.value = values[i]
        i += 1
        for child in node.children:
            queue.enqueue(child)

    return new_tree
