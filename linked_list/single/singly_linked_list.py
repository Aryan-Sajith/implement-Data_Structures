class SLLNode:
    """A class to represent a Singly-Linked List Node."""

    def __init__(self, value=None, next_node=None):
        """Initializes a Single-Linked List Node."""
        self.value = value
        self.next_node = next_node


class SinglyLinkedList:
    """A class to represent a Singly Linked List."""

    def __init__(self):
        """Initializes the Single Linked List."""
        # Sentinel nodes simplify operations.
        self.tail = SLLNode()
        self.head = SLLNode(next_node=self.tail)
