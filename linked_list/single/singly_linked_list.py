class SLLNode:
    """A class to represent a Singly-Linked List Node."""

    def __init__(self, value, next_node=None):
        """Initializes a Single-Linked List Node."""
        self.value = value
        self.next_node = next_node


class SinglyLinkedList:
    """A class to represent a Singly Linked List."""

    def __init__(self):
        """Initializes the Singly Linked List."""
        self.head = SLLNode(None)  # Sentinel head node simplifies all operations.
        self.tail = self.head
        self.length = 0

    def prepend(self, value):
        """Prepends a node to the Singly Linked List."""
        to_prepend = SLLNode(value, self.head.next_node)
        self.head.next_node = to_prepend
        if not self.length:  # Edge Case: Empty SLL
            self.tail = to_prepend

    def append(self, value):
        """Appends a node to the Singly Linked List."""
        to_append = SLLNode(value)
        self.tail.next_node = to_append
        self.tail = to_append
        self.length += 1

    def traverse(self):
        """Traverses & prints the nodes in the Singly Linked List."""
        cur_node = self.head.next_node

        while cur_node:
            print(f'{cur_node.value}', end=" -> ")
            cur_node = cur_node.next_node
