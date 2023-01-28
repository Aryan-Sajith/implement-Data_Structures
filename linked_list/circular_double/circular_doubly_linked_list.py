class CDLLNode:
    """A class to represent a node in a Circular Doubly Linked List(CDLL)."""

    def __init__(self, value, next=None, prev=None):
        """Initializes a CDLL node."""
        self.value = value
        self.next = next
        self.prev = prev


class CircularDoublyLinkedList:
    """A class to represent a Circular Doubly Linked List(CDLL)."""

    def __init__(self):
        """Initializes a CDLL."""
        # Placeholder sentinel nodes that simplify all algorithms.
        self.head = CDLLNode(None)
        self.tail = CDLLNode(None, self.head, self.head)
        self.head.next = self.tail
        self.head.prev = self.tail
        self.length = 0

    # Insertion
    """
        Time: O(1)
        Space: O(1)
    """
    def prepend(self):
        """Inserts a node to the front of the CDLL."""
    