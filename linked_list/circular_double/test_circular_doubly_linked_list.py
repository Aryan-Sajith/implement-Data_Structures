import fastenum
import unittest

from circular_doubly_linked_list import CircularDoublyLinkedList


class Error(fastenum.Enum):
    """An enum class for commonly recurring error messages."""
    SENTINEL = 'Sentinel nodes not set up properly.'
    HEAD = 'Head reference not updated.'
    TAIL = 'Tail reference not updated.'
    INSERT = 'Insertion error.'
    DELETE = 'Deletion error.'
    SEARCH = 'Search error.'
    TRAVERSAL = 'Traversal error.'
    LENGTH = 'Length not updated.'


class TestCircularDoublyLinkedList(unittest.TestCase):
    """Tests the Circular Doubly Linked List Class(CDLL)."""

    def setUp(self):
        """Initializes an empty CDLL instance."""
        self.cdll = CircularDoublyLinkedList()

    def tearDown(self):
        """Deletes CDLL instance."""
        del self.cdll

    def test_empty_CDLL(self):
        """Tests whether a newly initialized CDLL works properly."""
        self.assertEqual(self.cdll.head.next, self.cdll.tail, Error.SENTINEL.value)
        self.assertEqual(self.cdll.head.prev, self.cdll.tail, Error.SENTINEL.value)
        self.assertEqual(self.cdll.tail.next, self.cdll.head, Error.SENTINEL.value)
        self.assertEqual(self.cdll.tail.prev, self.cdll.head, Error.SENTINEL.value)
        self.assertIsNone(self.cdll.head.value, Error.SENTINEL.value)
        self.assertIsNone(self.cdll.tail.value, Error.SENTINEL.value)
        self.assertEqual(self.cdll.length, 0, Error.LENGTH.value)

    def test_prepend_empty_CDLL(self):
        """Tests whether prepending to an empty CDLL works properly."""
        self.cdll.prepend(0)
        self.assertEqual(self.cdll.head.next.value, 0, Error.INSERT.value)
        self.assertEqual(self.cdll.tail.prev.value, 0, Error.INSERT.value)
        self.assertEqual(self.cdll.length, 1, Error.LENGTH.value)

    def test_prepend_non_empty_CDLL(self):
        """Tests whether prepending to a non-empty CDLL works properly."""
        self.cdll.prepend(1)
        self.cdll.prepend(0)
        self.assertEqual(self.cdll.head.next.value, 0, Error.INSERT.value)
        self.assertEqual(self.cdll.tail.prev.value, 1, Error.INSERT.value)
        self.assertEqual(self.cdll.length, 2, Error.LENGTH.value)

    def test_append_empty_CDLL(self):
        """Tests whether appending to end of an empty CDLL works properly."""
        self.cdll.append(0)
        self.assertEqual(self.cdll.head.next.value, 0, Error.INSERT.value)
        self.assertEqual(self.cdll.tail.prev.value, 0, Error.INSERT.value)
        self.assertEqual(self.cdll.length, 1, Error.LENGTH.value)

    def test_append_nonempty_CDLL(self):
        """Tests whether prepending to a non-empty CDLL works properly."""
        self.cdll.append(0)
        self.cdll.append(1)
        self.assertEqual(self.cdll.head.next.value, 0, Error.INSERT.value)
        self.assertEqual(self.cdll.tail.prev.value, 1, Error.INSERT.value)
        self.assertEqual(self.cdll.length, 2, Error.LENGTH.value)

    def test_insert_before_value_empty_CDLL(self):
        """Tests if inserting before a value in an empty CDLL raises a ValueError."""
        with self.assertRaises(ValueError):
            self.cdll.insert_before_value(1, 0, 'head')

    def test_insert_before_value_invalid_starting_point(self):
        """Tests if inserting before a value with an invalid starting point raises a ValueError."""
        self.cdll.append(1)
        with self.assertRaises(ValueError):
            self.cdll.insert_before_value(1, 0, 'nowhere')

    def test_insert_before_value_nonempty_CDLL(self):
        """Tests if inserting before a value works properly in a non-empty CDLL."""
        self.cdll.append(0)
        self.cdll.append(2)
        self.cdll.append(3)
        self.cdll.append(4)
        self.cdll.append(5)
        self.cdll.append(6)
        self.cdll.insert_before_value(2, 1, 'head')
        self.assertEqual(self.cdll.head.next.next.value, 1, Error.INSERT.value)
        self.assertEqual(self.cdll.tail.prev.prev.prev.prev.prev.prev.value, 1, Error.INSERT.value)
        self.assertEqual(self.cdll.length, 7, Error.LENGTH.value)

    def test_insert_after_value_empty_CDLL(self):
        """Tests if inserting after a value in an empty CDLL raises a ValueError."""
        with self.assertRaises(ValueError):
            self.cdll.insert_after_value(0, 1, 'head')

    def test_insert_after_value_invalid_starting_point(self):
        """Tests if inserting after a value with an invalid starting point raises a ValueError."""
        self.cdll.append(1)
        with self.assertRaises(ValueError):
            self.cdll.insert_after_value(1, 0, 'nowhere')

    def test_insert_after_value_nonempty_CDLL(self):
        """Tests if inserting before a value works properly in a non-empty CDLL."""
        self.cdll.append(0)
        self.cdll.append(2)
        self.cdll.append(3)
        self.cdll.append(4)
        self.cdll.append(5)
        self.cdll.append(6)
        self.cdll.insert_after_value(0, 1, 'head')
        self.assertEqual(self.cdll.head.next.next.value, 1, Error.INSERT.value)
        self.assertEqual(self.cdll.tail.prev.prev.prev.prev.prev.prev.value, 1, Error.INSERT.value)
        self.assertEqual(self.cdll.length, 7, Error.LENGTH.value)

    def test_delete_head_empty_CDLL(self):
        """Tests if trying to delete head from an empty CDLL raises an IndexError."""
        with self.assertRaises(IndexError):
            self.cdll.delete_head()
            
    def test_delete_head_non_empty_CDLL(self):
        """Tests if trying to delete head from a non-empty CDLL works properly."""
        self.cdll.append(0)
        self.cdll.append(1)
        self.cdll.delete_head()
        self.assertEqual(self.cdll.head.next.value, 1, Error.DELETE.value)
        self.assertEqual(self.cdll.tail.prev.value, 1, Error.DELETE.value)
        self.assertEqual(self.cdll.length, 1, Error.LENGTH.value)

    def test_starting_point_validation(self):
        """Tests if passing in invalid starting point raises a ValueError."""
        with self.assertRaises(ValueError):
            self.cdll._validate_starting_point('nowhere')

    def test_search_from_head(self):
        """Tests if searching from head works properly."""
        for i in range(4):
            self.cdll.append(i)
        self.assertEqual(self.cdll._find_target_node(2, 'head').value, 2, Error.SEARCH.value)

    def test_search_from_tail(self):
        """Tests if searching from tail works properly."""
        for i in range(4):
            self.cdll.append(i)
        self.assertEqual(self.cdll._find_target_node(3, 'tail').value, 3, Error.SEARCH.value)

    def test_traversal_invalid_starting_point(self):
        """Tests if traversal with an invalid starting point returns a ValueError."""
        for i in range(4):
            self.cdll.append(i)
        with self.assertRaises(ValueError):
            self.cdll.traverse('nowhere')

    def test_traversal_from_head(self):
        """Tests if traversing from the head works properly."""
        for i in range(4):
            self.cdll.append(i)
        self.assertEqual(self.cdll.traverse('head'), ' 0 -> 1 -> 2 -> 3 ->', Error.TRAVERSAL.value)

    def test_traversal_from_tail(self):
        """Tests if traversing from the tail works properly."""
        for i in range(4):
            self.cdll.append(i)
        self.assertEqual(self.cdll.traverse('tail'), '0 -> 1 -> 2 -> 3 -> ', Error.TRAVERSAL.value)


if __name__ == '__main__':
    unittest.main()
