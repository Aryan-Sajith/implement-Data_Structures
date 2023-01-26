import unittest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    """Tests the Singly Linked List class."""

    def setUp(self):
        """Setup empty Singly Linked List."""
        self.sll = SinglyLinkedList()

    def tearDown(self):
        """Deletes Singly Linked List instance."""
        del self.sll

    def test_empty_SLL(self):
        """Tests whether newly initialized Singly Linked Lists works properly."""
        self.assertEqual(self.sll.head, self.sll.tail,
                         'Initial head and tail references not equal.')
        self.assertEqual(self.sll.length, 0, 'Initial length not equal to 0')

    def test_empty_SLL_prepend(self):
        """Tests whether prepending to an empty Singly Linked List works properly."""
        self.sll.prepend(1)
        self.assertEqual(self.sll.head.next.value, 1, 'Head reference not updated.')
        self.assertEqual(self.sll.tail.value, 1, 'Tail reference not updated.')
        self.assertEqual(self.sll.length, 1, 'Length not updated.')

    def test_non_empty_SLL_prepend(self):
        """Tests whether prepending to a non-empty Singly Linked List works properly."""
        self.sll.prepend(2)
        self.sll.prepend(1)
        self.assertEqual(self.sll.head.next.value, 1, 'Head reference not updated.')
        self.assertEqual(self.sll.tail.value, 2, 'Tail reference not updated.')
        self.assertEqual(self.sll.length, 2, 'Length not updated.')

    def test_SLL_append(self):
        """Tests whether appending to a Singly Linked List works properly."""
        self.sll.append(1)
        self.assertEqual(self.sll.tail.value, 1, 'Tail reference not updated.')
        self.assertEqual(self.sll.length, 1, 'Length not updated.')

    def test_successful_insert_after_value(self):
        """Tests whether successfully inserting after a value in the Singly Linked List works properly."""
        self.sll.append(1)
        self.sll.insert_after_value(1, 2)
        self.assertEqual(self.sll.head.next.value, 1, 'Head reference not updated.')
        self.assertEqual(self.sll.tail.value, 2, 'Tail reference not updated.')
        self.assertEqual(self.sll.length, 2, 'Length not updated.')

    def test_failed_insert_after_value(self):
        """Tests whether trying to insert after a non-existent value raises a ValueError."""
        with self.assertRaises(ValueError):
            self.sll.insert_after_value(1, 2)

    def test_delete_single_SLL_head(self):
        """Tests whether deleting the head node from a Singly Linked List with 1 node works properly."""
        self.sll.append(1)
        self.sll.delete_head()
        self.assertIsNone(self.sll.head.value, 'Head reference not updated.')
        self.assertIsNone(self.sll.tail.value, 'Tail reference not updated.')
        self.assertEqual(self.sll.length, 0, 'Length not updated.')

    def test_delete_non_single_SLL_head(self):
        """Tests whether deleting the head node from a Singly Linked List with >1 node works properly."""
        self.sll.append(2)
        self.sll.prepend(1)
        self.sll.prepend(0)
        self.sll.delete_head()
        self.assertEqual(self.sll.head.next.value, 1, 'Head reference not updated.')
        self.assertEqual(self.sll.tail.value, 2, 'Tail reference not updated.')
        self.assertEqual(self.sll.length, 2, 'Length not updated.')


if __name__ == '__main__':
    unittest.main()
