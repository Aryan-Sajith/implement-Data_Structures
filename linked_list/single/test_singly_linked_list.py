import fastenum
import unittest

from singly_linked_list import SinglyLinkedList


class Error(fastenum.Enum):
    """An enum class for commonly recurring error messages."""
    HEAD = 'Head reference not updated.'
    TAIL = 'Tail reference not updated.'
    LENGTH = 'Length not updated.'


class TestSinglyLinkedList(unittest.TestCase):
    """Tests the Singly Linked List(SLL) class."""

    def setUp(self):
        """Setup empty SLL."""
        self.sll = SinglyLinkedList()

    def tearDown(self):
        """Deletes SLL instance."""
        del self.sll

    def test_empty_SLL(self):
        """Tests whether newly initialized SLLs works properly."""
        self.assertEqual(self.sll.head, self.sll.tail, f'{Error.HEAD.value} & {Error.TAIL.value}')
        self.assertEqual(self.sll.length, 0, Error.TAIL.value)

    def test_empty_SLL_prepend(self):
        """Tests whether prepending to an empty SLL works properly."""
        self.sll.prepend(1)
        self.assertEqual(self.sll.head.next.value, 1, Error.HEAD.value)
        self.assertEqual(self.sll.tail.value, 1, Error.TAIL.value)
        self.assertEqual(self.sll.length, 1, Error.LENGTH.value)

    def test_non_empty_SLL_prepend(self):
        """Tests whether prepending to a non-empty SLL works properly."""
        self.sll.prepend(2)
        self.sll.prepend(1)
        self.assertEqual(self.sll.head.next.value, 1, Error.HEAD.value)
        self.assertEqual(self.sll.tail.value, 2, Error.TAIL.value)
        self.assertEqual(self.sll.length, 2, Error.LENGTH.value)

    def test_SLL_append(self):
        """Tests whether appending to a SLL works properly."""
        self.sll.append(1)
        self.assertEqual(self.sll.tail.value, 1, Error.TAIL.value)
        self.assertEqual(self.sll.length, 1, Error.LENGTH.value)

    def test_successful_insert_after_value(self):
        """Tests whether successfully inserting after a value in the SLL works properly."""
        self.sll.append(1)
        self.sll.insert_after_value(1, 2)
        self.assertEqual(self.sll.head.next.value, 1, Error.HEAD.value)
        self.assertEqual(self.sll.tail.value, 2, Error.TAIL.value)
        self.assertEqual(self.sll.length, 2, Error.LENGTH.value)

    def test_failed_insert_after_value(self):
        """Tests whether trying to insert after a non-existent value raises a ValueError."""
        with self.assertRaises(ValueError):
            self.sll.insert_after_value(1, 2)

    def test_delete_single_SLL_head(self):
        """Tests whether deleting the head node from a SLL with 1 node works properly."""
        self.sll.append(1)
        self.sll.delete_head()
        self.assertIsNone(self.sll.head.value, Error.HEAD.value)
        self.assertIsNone(self.sll.tail.value, Error.TAIL.value)
        self.assertEqual(self.sll.length, 0, Error.LENGTH.value)

    def test_delete_non_single_SLL_head(self):
        """Tests whether deleting the head node from a SLL with >1 node works properly."""
        self.sll.append(2)
        self.sll.prepend(1)
        self.sll.prepend(0)
        self.sll.delete_head()
        self.assertEqual(self.sll.head.next.value, 1, Error.HEAD.value)
        self.assertEqual(self.sll.tail.value, 2, Error.TAIL.value)
        self.assertEqual(self.sll.length, 2, Error.LENGTH.value)

    def test_delete_singly_SLL_tail(self):
        """Tests whether deleting the tail node from a SLL with 1 node works properly."""
        self.sll.append(1)
        self.sll.delete_tail()
        self.assertIsNone(self.sll.head.value, Error.HEAD.value)
        self.assertIsNone(self.sll.tail.value, Error.TAIL.value)
        self.assertEqual(self.sll.length, 0, Error.LENGTH.value)

    def test_delete_non_single_SLL_tail(self):
        """Tests whether deleting the head node from a SLL with >1 node works properly."""
        self.sll.append(2)
        self.sll.prepend(1)
        self.sll.prepend(0)
        self.sll.delete_tail()
        self.assertEqual(self.sll.head.next.value, 0, Error.HEAD.value)
        self.assertEqual(self.sll.tail.value, 1, Error.TAIL.value)
        self.assertEqual(self.sll.length, 2, Error.LENGTH.value)

    def test_successful_delete_node_with_value(self):
        """Tests whether successfully deleting a node based on value works properly."""
        self.sll.append(0)
        self.sll.append(1)
        self.sll.append(2)
        self.sll.delete_node_with_value(1)
        self.assertEqual(self.sll.head.next.value, 0, Error.HEAD.value)
        self.assertEqual(self.sll.tail.value, 2, Error.TAIL.value)
        self.assertEqual(self.sll.length, 2, Error.LENGTH.value)

    def test_failed_delete_node_with_value(self):
        """Tests whether trying to delete a non-existent value raises a ValueError."""
        with self.assertRaises(ValueError):
            self.sll.delete_node_with_value(1)

    def test_find_node_before_target_value(self):
        """Tests whether finding the node before target value works properly."""
        self.sll.append(2)
        self.sll.prepend(1)
        self.assertEqual(self.sll._find_node_before_target_value(2), self.sll.head.next, 'Finding the node before '
                                                                                         'a target value failed.')

    def test_successful_find_node_with_value(self):
        """Tests whether successfully finding a node with a value works properly."""
        self.sll.append(2)
        self.assertEqual(self.sll.find_node_with_value(2), self.sll.tail, 'Failed to successfully find a node with'
                                                                          'target value when it actually exists.')

    def test_failed_find_node_with_value(self):
        """Tests whether failing to find a node with value returns a node with value None."""
        self.assertIsNone(self.sll.find_node_with_value(0).value, 'Found a node with target value when it does not'
                                                                  'actually exist.')

    def test_traversal(self):
        """Tests whether traversing the SLL works properly."""
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)
        self.sll.append(4)
        self.assertEqual(self.sll.traverse(), ' 1 -> 2 -> 3 -> 4 ->')


if __name__ == '__main__':
    unittest.main()
