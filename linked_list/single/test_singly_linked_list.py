import unittest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    """Tests the Singly Linked List class."""

    def setUp(self):
        """Sets up an empty Singly Linked List per test."""
        self.singly_linked_list = SinglyLinkedList()

    def tearDown(self):
        """Deletes the utilized Singly Linked List instance after each test."""
        del self.singly_linked_list


if __name__ == '__main__':
    unittest.main()
