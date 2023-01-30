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
    def prepend(self, value):
        """
        Inserts a node to the front of the CDLL.
        Time: O(1)
        Space: O(1)
        """
        to_prepend = CDLLNode(value, self.head.next, self.head)
        self.head.next.prev = to_prepend
        self.head.next = to_prepend
        self.length += 1

    def append(self, value):
        """
        Inserts a node to the end of the CDLL.
        Time: O(1)
        Space: O(1)
        """
        to_append = CDLLNode(value, self.tail, self.tail.prev)
        self.tail.prev.next = to_append
        self.tail.prev = to_append
        self.length += 1