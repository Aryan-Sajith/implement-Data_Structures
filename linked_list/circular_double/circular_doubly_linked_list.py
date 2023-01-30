import fastenum


class CDLLNode:
    """A class to represent a node in a Circular Doubly Linked List(CDLL)."""

    def __init__(self, value, next=None, prev=None):
        """Initializes a CDLL node."""
        self.value = value
        self.next = next
        self.prev = prev


class StartingPoint(fastenum.Enum):
    HEAD = 'head'
    TAIL = 'tail'


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
    def prepend(self, insert_value):
        """
        Inserts a node to the front of the CDLL.
        Time: O(1)
        Space: O(1)
        """
        to_prepend = CDLLNode(insert_value, self.head.next, self.head)
        self.head.next.prev = to_prepend
        self.head.next = to_prepend
        self.length += 1

    def append(self, insert_value):
        """
        Inserts a node to the end of the CDLL.
        Time: O(1)
        Space: O(1)
        """
        to_append = CDLLNode(insert_value, self.tail, self.tail.prev)
        self.tail.prev.next = to_append
        self.tail.prev = to_append
        self.length += 1

    def insert_before_value(self, target_value, insert_value, starting_point):
        """
        Attempts to insert a node with insert value before a node with target value.
        Time: O(N)
        Space: O(1)
        :raises ValueError: If invalid starting point or node with target value not found.
        :param target_value: The target value to insert before.
        :param insert_value: The value to insert.
        :param starting_point: Determines whether search for target value occurs from head or tail.
        Uses StartingPoint enum to validate starting point.
        """
        self._validate_starting_point(starting_point)

        if starting_point == StartingPoint.HEAD.value:
            target_node = self.search_from_head(target_value)
        else:
            target_node = self.search_from_tail(target_value)

        if target_node.value:
            to_insert = CDLLNode(insert_value, target_node, target_node.prev)
            target_node.prev.next = to_insert
            target_node.prev = to_insert
            self.length += 1
        else:
            raise ValueError('Node with target value not found.')

    def _validate_starting_point(self, starting_point):
        """
        Uses StartingPoint enum to validate starting point
        :raises ValueError: If invalid starting point.
        """
        if starting_point not in [e.value for e in StartingPoint]:
            raise ValueError('Invalid starting point.')

    # Search
    def search_from_head(self, target_value) -> CDLLNode:
        """
        Searches for a node with target value starting at head.
        :returns: CDLLNode with target value or None.
        Time: O(N)
        Space: O(1)
        """
        cur_node = self.head.next

        while cur_node.value is not None:
            if cur_node.value != target_value:
                cur_node = cur_node.next
            else:
                break

        return cur_node

    def search_from_tail(self, target_value) -> CDLLNode:
        """
        Searches for a node with target value starting at tail.
        :returns: CDLLNode with target value or None.
        Time: O(N)
        Space: O(1)
        """
        cur_node = self.tail.prev

        while cur_node.value is not None:
            if cur_node.value != target_value:
                cur_node = cur_node.prev
            else:
                break

        return cur_node
