import unittest
from singly_linked_list import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):
    """Tests the Singly Linked List class."""

    def setUp(self):
        """Setup empty Singly Linked List."""
        self.singly_linked_list = SinglyLinkedList()

    def tearDown(self):
        """Deletes Singly Linked List instance."""
        del self.singly_linked_list

    def test_empty_SLL(self):
        """Tests whether newly initialized Singly Linked Lists works properly."""
        self.assertEqual(self.singly_linked_list.head, self.singly_linked_list.tail,
                         'Initial head and tail references not equal.')
        self.assertEqual(self.singly_linked_list.length, 0, 'Initial length not equal to 0')

    def test_empty_SLL_prepend(self):
        """Tests whether prepending to an empty Singly Linked List works properly."""
        self.singly_linked_list.prepend(1)
        self.assertEqual(self.singly_linked_list.head.next_node.value, 1, 'Head reference not updated.')
        self.assertEqual(self.singly_linked_list.tail.value, 1, 'Tail reference not updated.')
        self.assertEqual(self.singly_linked_list.length, 1, 'Length not updated.')

    def test_non_empty_SLL_prepend(self):
        """Tests whether prepending to a non-empty Singly Linked List works properly."""
        self.singly_linked_list.prepend(2)
        self.singly_linked_list.prepend(1)
        self.assertEqual(self.singly_linked_list.head.next_node.value, 1, 'Head reference not updated.')
        self.assertEqual(self.singly_linked_list.tail.value, 2, 'Tail reference not updated.')
        self.assertEqual(self.singly_linked_list.length, 2, 'Length not updated.')

    def test_SLL_append(self):
        """Tests whether appending to an Singly Linked List works properly."""
        self.singly_linked_list.append(1)
        self.assertEqual(self.singly_linked_list.tail.value, 1, 'Tail reference not updated.')
        self.assertEqual(self.singly_linked_list.length, 1, 'Length not updated.')

    def test_successful_insert_after_value(self):
        """Tests whether successfully inserting after a value in the Singly Linked List works properly."""
        self.singly_linked_list.append(1)
        self.singly_linked_list.insert_after_value(1, 2)
        self.assertEqual(self.singly_linked_list.head.next_node.value, 1, 'Head reference not updated.')
        self.assertEqual(self.singly_linked_list.tail.value, 2, 'Tail reference not updated.')
        self.assertEqual(self.singly_linked_list.length, 2, 'Length not updated.')

    def test_failed_insert_after_value(self):
        """Tests whether trying to insert after a non-existent value raises a ValueError."""
        with self.assertRaises(ValueError):
            self.singly_linked_list.insert_after_value(1, 2)

    def test_delete_single_SLL_head(self):
        """Tests whether deleting the head node from a Singly Linked List with 1 node works properly."""
        self.singly_linked_list.append(1)
        self.singly_linked_list.delete_head()
        self.assertIsNone(self.singly_linked_list.head.value, 'Head reference not updated.')
        self.assertIsNone(self.singly_linked_list.tail.value, 'Tail reference not updated.')
        self.assertEqual(self.singly_linked_list.length, 0, 'Length not updated.')

    def test_delete_non_single_SLL_head(self):
        """Tests whether deleting the head node from a Singly Linked List with >1 node works properly."""
        self.singly_linked_list.append(2)
        self.singly_linked_list.prepend(1)
        self.singly_linked_list.prepend(0)
        self.singly_linked_list.delete_head()
        self.assertEqual(self.singly_linked_list.head.next_node.value, 1, 'Head reference not updated.')
        self.assertEqual(self.singly_linked_list.tail.value, 2, 'Tail reference not updated.')
        self.assertEqual(self.singly_linked_list.length, 2, 'Length not updated.')


if __name__ == '__main__':
    unittest.main()
