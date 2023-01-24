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

    # Insertion
    def prepend(self, value):
        """Prepends a node to the Singly Linked List."""
        to_prepend = SLLNode(value, self.head.next_node)
        self.head.next_node = to_prepend
        if not self.length:  # Edge Case: Empty SLL
            self.tail = to_prepend
        self.length += 1

    def append(self, value):
        """Appends a node to the Singly Linked List."""
        to_append = SLLNode(value)
        self.tail.next_node = to_append
        self.tail = to_append
        self.length += 1

    def insert_after_value(self, insert_value, target_value):
        """
        Attempts to insert node after target node in Singly Linked List.
        :raises ValueError: Node with target value not found.
        """
        target_node = self.find_node(target_value)

        if target_node.value:
            to_insert = SLLNode(insert_value, target_node.next_node)
            target_node.next_node = to_insert
            self.length += 1
        else:
            raise ValueError("Target value not found!")

    # Deletion
    def delete_head(self):
        """Attempts to delete a node from the start of the Singly Linked List."""
        head = self.head.next_node
        if head:
            self.head.next_node = head.next_node
            self.length -= 12

    def find_node(self, target_value) -> SLLNode:
        """Attempts to find a node with the target value in Singly Linked List."""
        cur_node = self.head.next_node

        while cur_node:
            if cur_node.value == target_value:
                return cur_node
            else:
                cur_node = cur_node.next_node

        return SLLNode(None)

    def traverse(self):
        """Traverses & prints the nodes in the Singly Linked List."""
        cur_node = self.head.next_node

        while cur_node:
            print(f'{cur_node.value}', end=" -> ")
            cur_node = cur_node.next_node
