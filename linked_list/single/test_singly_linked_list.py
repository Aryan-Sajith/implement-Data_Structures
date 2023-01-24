import unittest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    """Tests the Singly Linked List class."""

    def setUp(self):
        """Sets up an empty singly linked list per test."""
        self.singly_linked_list = SinglyLinkedList()

    def tearDown(self):
        """Deletes the Singly Linked List instance per test."""
        del self.singly_linked_list


if __name__ == '__main__':
    unittest.main()
