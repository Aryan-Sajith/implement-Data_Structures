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
        self.head = SLLNode(None)   # Sentinel node-> Placeholder head that simplified algorithms.
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

    def insert_after_value(self, target_value, insert_value):
        """
        Attempts to insert node after target node in Singly Linked List.
        :raises ValueError: Node with target value not found for insertion.
        """
        target_node = self.find_node(target_value)

        if target_node.value:
            if target_node == self.tail:
                self.append(insert_value)
            else:
                to_insert = SLLNode(insert_value, target_node.next_node)
                target_node.next_node = to_insert
                self.length += 1
        else:
            raise ValueError("Node with target value not found for insertion.")

    # Deletion
    def delete_head(self):
        """Attempts to delete the first node in the Singly Linked List."""
        head = self.head.next_node
        if head:
            if head == self.tail:  # Edge Case: Deleting 1 node.
                self.tail = self.head
            self.head.next_node = head.next_node
            self.length -= 1

    def delete_tail(self):
        """Attempts to delete the last node in the Singly Linked List."""
        if self.tail.value:
            new_tail_node = self._find_node_before_target_value(self.tail.value)
            self.tail = new_tail_node
            self.tail.next_node = None
            self.length -= 1

    def delete_node_with_value(self, target_value):
        """
        Attempts to delete a node with a target value in the Singly Linked List.
        @:raises ValueError: Node with target value not found for deletion.
        """
        target_node = self.find_node(target_value)

        if target_node.value:
            if target_node == self.head.next_node:
                self.delete_head()
            elif target_node == self.tail:
                self.delete_tail()
            else:
                before_target_node = self._find_node_before_target_value(target_value)
                before_target_node.next_node = target_node.next_node
                self.length -= 1
        else:
            raise ValueError('Node with target value not found for deletion.')

    # Search
    def _find_node_before_target_value(self, target_value):
        """Attempts to find the node right before the last one in the Singly Linked List."""
        cur_node = self.head
        while cur_node.next_node.value != target_value:
            cur_node = cur_node.next_node
        return cur_node

    def find_node(self, target_value) -> SLLNode:
        """Attempts to find a node with the target value in Singly Linked List."""
        cur_node = self.head.next_node

        while cur_node:
            if cur_node.value == target_value:
                return cur_node
            else:
                cur_node = cur_node.next_node

        return SLLNode(None)

    # Traversal
    def traverse(self):
        """Traverses & prints the nodes in the Singly Linked List."""
        cur_node = self.head.next_node

        while cur_node:
            print(f'{cur_node.value}', end=" -> ")
            cur_node = cur_node.next_node
