class SLLNode:
    """A class to represent a Singly-Linked List Node."""

    def __init__(self, next_node=None, value=None):
        """Initializes a Single-Linked List Node."""
        self.next_node = next_node
        self.value = value


class SinglyLinkedList:
    """A class to represent a Singly Linked List."""

    def __init__(self):
        """Initializes the Single Linked List."""
        # Sentinel nodes simplify operations.
        self.tail = SLLNode()
        self.head = SLLNode(self.tail)
