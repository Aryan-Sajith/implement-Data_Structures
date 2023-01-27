class SLLNode:
    """A class to represent a Singly-Linked List Node."""

    def __init__(self, value, next=None):
        """Initializes a Single-Linked List Node."""
        self.value = value
        self.next = next


class SinglyLinkedList:
    """
    A class to represent a Singly Linked List.
    Time Complexities:
    Best: Insertion & Deletion at Head: O(1)
        Example: Customer Service Wait list.
    Worst: Random Insertion & Deletion & Search: O(N)
    """

    def __init__(self):
        """Initializes the SLL."""
        self.head = SLLNode(None)  # Sentinel node-> Placeholder head that simplified algorithms.
        self.tail = self.head
        self.length = 0

    # Insertion
    """
    Time: O(1)
    Space: O(1)
    """
    def prepend(self, value):
        """Prepends a node to the SLL."""
        to_prepend = SLLNode(value, self.head.next)
        self.head.next = to_prepend
        if not self.length:  # Edge Case: Empty SLL
            self.tail = to_prepend
        self.length += 1

    """
    Time: O(1)
    Space: O(1)
    """
    def append(self, value):
        """Appends a node to the SLL."""
        to_append = SLLNode(value)
        self.tail.next = to_append
        self.tail = to_append
        self.length += 1

    """
    Time: O(N)
    Space: O(1)
    """
    def insert_after_value(self, target_value, insert_value):
        """
        Attempts to insert node after target node in SLL.
        :raises ValueError: Node with target value not found for insertion.
        """
        target_node = self.find_node_with_value(target_value)

        if target_node.value:
            if target_node == self.tail:
                self.append(insert_value)
            else:
                to_insert = SLLNode(insert_value, target_node.next)
                target_node.next = to_insert
                self.length += 1
        else:
            raise ValueError("Node with target value not found for insertion.")

    # Deletion
    """
    Time: O(1)
    Space: O(1)
    """
    def delete_head(self):
        """Attempts to delete the first node in the SLL."""
        head = self.head.next
        if head:
            if head == self.tail:  # Edge Case: Deleting 1 node.
                self.tail = self.head
            self.head.next = head.next
            self.length -= 1

    """
    Time: O(N)
    Space: O(1)
    """
    def delete_tail(self):
        """Attempts to delete the last node in the SLL."""
        if self.tail.value:
            new_tail_node = self._find_node_before_target_value(self.tail.value)
            self.tail = new_tail_node
            self.tail.next = None
            self.length -= 1

    """
    Time: O(N)
    Space: O(1)
    """
    def delete_node_with_value(self, target_value):
        """
        Attempts to delete a node with a target value in the SLL.
        @:raises ValueError: Node with target value not found for deletion.
        """
        target_node = self.find_node_with_value(target_value)

        if target_node.value:
            if target_node == self.head.next:
                self.delete_head()
            elif target_node == self.tail:
                self.delete_tail()
            else:
                before_target_node = self._find_node_before_target_value(target_value)
                before_target_node.next = target_node.next
                self.length -= 1
        else:
            raise ValueError('Node with target value not found for deletion.')

    # Search
    """
    Time: O(N)
    Space: O(1)
    """
    def _find_node_before_target_value(self, target_value):
        """Attempts to find the node right before the last one in the SLL."""
        cur_node = self.head
        while cur_node.next.value != target_value:
            cur_node = cur_node.next
        return cur_node

    """
    Time: O(N)
    Space: O(1)
    """
    def find_node_with_value(self, target_value) -> SLLNode:
        """Attempts to find a node with the target value in SLL."""
        cur_node = self.head.next

        while cur_node:
            if cur_node.value == target_value:
                return cur_node
            else:
                cur_node = cur_node.next

        return SLLNode(None)

    # Traversal
    """
    Time: O(N)
    Space: O(1)
    """
    def traverse(self):
        """Traverses the nodes in the SLL"""
        traversal = ''
        cur_node = self.head.next

        while cur_node:
            traversal += f' {cur_node.value} ->'
            cur_node = cur_node.next

        return traversal
