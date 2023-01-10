class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, new_value):
        if not self.head:
            raise TargetError("The list is empty.")
        if self.head.value == value:
            self.head = Node(new_value, self.head)
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = Node(new_value, current.next)
                return
            current = current.next
        raise TargetError(f"Value {value} not found in the list.")

    def insert_after(self, value, new_value):
        if not self.head:
            raise TargetError("The list is empty.")
        current = self.head
        while current:
            if current.value == value:
                current.next = Node(new_value, current.next)
                return
            current = current.next
        raise TargetError(f"Value {value} not found in the list.")

    def kth_from_end(self, k):
        if not self.head:
            return None
        if k < 0:
            raise TargetError(f"Input k: {k} should be greater than or equal to 0.")
        current = self.head
        length = 1
        while current.next:
            length += 1
            current = current.next
        if k >= length:
            raise TargetError(f"Input k: {k} should be less than length of list: {length}.")
        current = self.head
        for _ in range(length - k - 1):
            current = current.next
        return current.value

    def __str__(self):
        current = self.head
        values = []
        while current:
            values.append("{ "+str(current.value)+" }")
            current = current.next
        if values:
            return " -> ".join(values) + " -> NULL"
        else:
            return " -> ".join(values) + "NULL"


class TargetError(Exception):
    pass
